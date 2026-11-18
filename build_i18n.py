#!/usr/bin/env python3
"""
Generate /ko/index.html, /ja/index.html and /bio/index.html from the root index.html.

Variants: elements marked data-variant="general" appear on the root, /ko/ and /ja/ pages;
elements marked data-variant="bio" appear only on /bio/ (English, noindex, shared by link).
Inside a data-bio-sort container, children with data-bio-order="n" are reordered on /bio/;
data-bio-open adds `open` to a <details> on /bio/. The root page hides bio elements with CSS.

index.html (English) is the single source of truth: every element that carries
data-ko="..." / data-ja="..." attributes gets its inner HTML swapped for the
translation, the <head> metadata is localised, and the data-* attributes are
stripped from the output so each language page is a clean, indexable document.

Usage:  python3 build_i18n.py        (run from the repository root, then commit ko/ and ja/)
"""
import html, os, re, sys, datetime
TODAY = datetime.date.today().isoformat()

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "https://geongyu.github.io"
SRC = os.path.join(ROOT, "index.html")

META = {
    "ko": {
        "lang": "ko", "locale": "ko_KR", "dir": "ko",
        "title": "이건규 · 머신러닝 리서처",
        "description": "멀티모달 학습, 모델 해석, 신뢰성 평가를 연구하는 머신러닝 리서처 이건규의 포트폴리오입니다. 문제 설정부터 모델 구현, 실험 설계, 논문 작성까지 직접 합니다.",
        "og_title": "이건규 · 머신러닝 리서처",
        "og_description": "멀티모달 학습, 모델 해석, 신뢰성 평가를 연구하는 머신러닝 리서처 이건규의 포트폴리오입니다. 문제 설정부터 모델 구현, 실험 설계, 논문 작성까지 직접 합니다.",
        "image_alt": "이건규 · 머신러닝 리서처 · Multimodal Learning · Interpretability · Reliable ML",
        "ld_description": "멀티모달 학습, 모델 해석, 신뢰성 평가를 연구하는 머신러닝 리서처 이건규의 포트폴리오입니다. 문제 설정부터 모델 구현, 실험 설계, 논문 작성까지 직접 합니다.",
        "cv": "/assets/Geongyu_Lee_CV_KO.pdf",
    },
    "ja": {
        "lang": "ja", "locale": "ja_JP", "dir": "ja",
        "title": "イ・ゴンギュ · 機械学習リサーチャー",
        "description": "マルチモーダル学習、解釈可能性、信頼性評価に取り組む機械学習リサーチャー、イ・ゴンギュのポートフォリオです。研究課題の設定からモデル開発、実験設計、論文執筆まで取り組みます。",
        "og_title": "イ・ゴンギュ · 機械学習リサーチャー",
        "og_description": "マルチモーダル学習、解釈可能性、信頼性評価に取り組む機械学習リサーチャー、イ・ゴンギュのポートフォリオです。研究課題の設定からモデル開発、実験設計、論文執筆まで取り組みます。",
        "image_alt": "イ・ゴンギュ · 機械学習リサーチャー · Multimodal Learning · Interpretability · Reliable ML",
        "ld_description": "マルチモーダル学習、解釈可能性、信頼性評価に取り組む機械学習リサーチャー、イ・ゴンギュのポートフォリオです。研究課題の設定からモデル開発、実験設計、論文執筆まで取り組みます。",
        "cv": "/assets/Geongyu_Lee_CV_JA.pdf",
    },
}

TAG_OPEN = re.compile(r"<([a-zA-Z][a-zA-Z0-9]*)")
ATTR = re.compile(r'\s+([^\s=/>]+)(?:="([^"]*)")?')
VOID = {"br", "img", "meta", "link", "input", "hr", "source"}


def parse_start_tag(s, i):
    """s[i] == '<'. Returns (tag, attrs(list of (name, value|None)), end_index_after_'>')."""
    m = TAG_OPEN.match(s, i)
    tag = m.group(1)
    j = m.end()
    attrs = []
    while True:
        m = ATTR.match(s, j)
        if not m:
            break
        attrs.append((m.group(1), m.group(2)))
        j = m.end()
    m = re.compile(r"\s*/?>").match(s, j)
    if not m:
        raise ValueError(f"unterminated tag at {i}: {s[i:i+80]!r}")
    return tag, attrs, m.end()


def find_matching_end(s, tag, start):
    """Find index of the matching </tag> for a start tag whose content begins at `start`."""
    depth = 1
    open_re = re.compile(rf"<{tag}(?=[\s>/])", re.I)
    close_re = re.compile(rf"</{tag}\s*>", re.I)
    pos = start
    while True:
        mo = open_re.search(s, pos)
        mc = close_re.search(s, pos)
        if not mc:
            raise ValueError(f"no closing </{tag}> after {start}")
        if mo and mo.start() < mc.start():
            depth += 1
            pos = mo.end()
        else:
            depth -= 1
            if depth == 0:
                return mc.start(), mc.end()
            pos = mc.end()


def localise_body(s, lang):
    """Every translatable element carries data-ko first (then data-ja), so anchor on data-ko
    and pick the requested language from the parsed attribute list."""
    key = f"data-{lang}"
    out, pos, n = [], 0, 0
    while True:
        k = s.find('data-ko="', pos)
        if k == -1:
            out.append(s[pos:])
            break
        lt = s.rfind("<", 0, k)
        tag, attrs, after = parse_start_tag(s, lt)
        names = [a for a, _ in attrs]
        if "data-ko" not in names:  # false positive (inside text); skip
            out.append(s[pos:k + 1]); pos = k + 1
            continue
        tr = dict(attrs).get(key)
        kept = [(a, v) for a, v in attrs if a not in ("data-ko", "data-ja")]
        new_tag = "<" + tag + "".join(f' {a}="{v}"' if v is not None else f" {a}" for a, v in kept) + ">"
        if tag.lower() in VOID or tr is None:
            out.append(s[pos:lt] + new_tag); pos = after
        else:
            cs, ce = find_matching_end(s, tag, after)
            out.append(s[pos:lt] + new_tag + html.unescape(tr) + s[cs:ce])
            pos = ce
        n += 1
    return "".join(out), n


# ---------- site variants: general (root, ko, ja) vs bio (/bio/, English only) ----------
VARIANT = re.compile(r'<([a-zA-Z][a-zA-Z0-9]*)(?=[^>]*\sdata-variant="(general|bio)")')


def apply_variant(s, keep):
    """Drop every element whose data-variant is not `keep`; strip the attribute from the rest."""
    out, pos = [], 0
    while True:
        m = VARIANT.search(s, pos)
        if not m:
            out.append(s[pos:]); break
        tag, var = m.group(1), m.group(2)
        _, _, after = parse_start_tag(s, m.start())
        if var == keep:
            out.append(s[pos:m.start()] + s[m.start():after].replace(f' data-variant="{var}"', ""))
            pos = after
        else:
            if tag.lower() in VOID:
                end = after
            else:
                _, end = find_matching_end(s, tag, after)
            out.append(s[pos:m.start()]); pos = end
    return "".join(out)


def bio_sort(s):
    """Inside each data-bio-sort container, reorder the children that carry data-bio-order."""
    pos = 0
    while True:
        k = s.find(" data-bio-sort", pos)
        if k == -1:
            return s
        lt = s.rfind("<", 0, k)
        tag, _, after = parse_start_tag(s, lt)
        cs, _ = find_matching_end(s, tag, after)
        inner = s[after:cs]
        items = []
        for m in re.finditer(r'<([a-zA-Z]+)[^>]*\sdata-bio-order="(\d+)"', inner):
            if items and m.start() < items[-1][1]:
                continue  # nested
            t, _, a2 = parse_start_tag(inner, m.start())
            _, e2 = find_matching_end(inner, t, a2)
            items.append((m.start(), e2, int(m.group(2))))
        ordered = sorted(items, key=lambda x: x[2])
        new, p0 = [], 0
        for (st, en, _), (ost, oen, _) in zip(items, ordered):
            new.append(inner[p0:st] + inner[ost:oen]); p0 = en
        new.append(inner[p0:])
        s = s[:after] + "".join(new) + s[cs:]
        pos = after


def strip_variant_marks(s, bio=False):
    s = s.replace('[data-variant="bio"] { display: none !important; }\n', "")
    if bio:
        s = s.replace(" data-bio-open", " open")
    s = s.replace(" data-bio-open", "").replace(" data-bio-sort", "")
    return re.sub(r'\sdata-bio-order="\d+"', "", s)


BIO = {
    "title": "Geongyu Lee · Medical &amp; Bio AI Researcher",
    "description": "Medical and bio AI researcher working on computational pathology, multi-omics and precision oncology: models that link H&amp;E pathology with proteomics and RNA, validated across sites.",
}


def build_bio(src):
    s = apply_variant(src, "bio")
    s = bio_sort(s)
    s = strip_variant_marks(s, bio=True)
    s = re.sub(r'\sdata-(?:ko|ja)="[^"]*"', "", s)
    s = re.sub(r"<title>.*?</title>", f"<title>{BIO['title']}</title>", s, count=1)
    for pat in (r'<meta name="description" content="[^"]*">', r'<meta property="og:description" content="[^"]*">', r'<meta name="twitter:description" content="[^"]*">'):
        s = re.sub(pat, lambda m: re.sub(r'content="[^"]*"', f'content="{BIO["description"]}"', m.group(0)), s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{BIO["title"]}">', s, count=1)
    s = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{BIO["title"]}">', s, count=1)
    s = s.replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex, nofollow">')
    s = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{SITE}/bio/">', s, count=1)
    s = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">\n', "", s)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{SITE}/bio/">', s, count=1)
    s = re.sub(r'\s*<nav class="langsw".*?</nav>', "", s, count=1, flags=re.S)
    assert "data-variant=" not in s and "data-ko=" not in s
    return s


def localise_head(s, m):
    def sub1(pat, repl, s):
        new, k = re.subn(pat, repl, s, count=1)
        assert k == 1, pat
        return new

    def sub_opt(pat, repl, s):
        """Like sub1, but the target may be absent (e.g. a hidden / removed element)."""
        return re.subn(pat, lambda _m: repl, s, count=1)[0]
    s = sub1(r'<html lang="en">', f'<html lang="{m["lang"]}">', s)
    s = sub1(r"<title>.*?</title>", f"<title>{m['title']}</title>", s)
    s = sub1(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{m["description"]}">', s)
    s = sub1(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{SITE}/{m["dir"]}/">', s)
    s = sub1(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{SITE}/{m["dir"]}/">', s)
    s = sub1(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{m["og_title"]}">', s)
    s = sub1(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{m["og_description"]}">', s)
    s = sub1(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{m["og_title"]}">', s)
    s = sub1(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{m["og_description"]}">', s)
    # og:locale — swap primary with this language, keep the others as alternates
    locales = {"en_US", "ko_KR", "ja_JP"}
    alt = "\n".join(f'<meta property="og:locale:alternate" content="{l}">' for l in sorted(locales - {m["locale"]}))
    s = sub1(r'<meta property="og:locale" content="en_US">\n<meta property="og:locale:alternate" content="ko_KR">\n<meta property="og:locale:alternate" content="ja_JP">',
             f'<meta property="og:locale" content="{m["locale"]}">\n{alt}', s)
    # share-image alt text (optional tags); og:image URLs (incl. any ?v= cache-buster) are left untouched
    s = sub_opt(r'<meta property="og:image:alt" content="[^"]*">', f'<meta property="og:image:alt" content="{m["image_alt"]}">', s)
    s = sub_opt(r'<meta name="twitter:image:alt" content="[^"]*">', f'<meta name="twitter:image:alt" content="{m["image_alt"]}">', s)
    # JSON-LD url and (optional) description
    s = sub1(r'"url": "https://geongyu.github.io/"', f'"url": "{SITE}/{m["dir"]}/"', s)
    s = sub_opt(r'"description": "[^"]*"', f'"description": "{m["ld_description"]}"', s)
    # language switcher active state
    s = sub1(r'<a class="langopt is-active" href="/" hreflang="en" lang="en" aria-current="page">EN</a>',
             '<a class="langopt" href="/" hreflang="en" lang="en">EN</a>', s)
    s = sub1(rf'<a class="langopt" href="/{m["dir"]}/" hreflang="{m["lang"]}" lang="{m["lang"]}">',
             f'<a class="langopt is-active" href="/{m["dir"]}/" hreflang="{m["lang"]}" lang="{m["lang"]}" aria-current="page">', s)
    # CV download (optional: the chip is currently hidden and may be removed entirely)
    s = sub_opt(r'href="/assets/Geongyu_Lee_CV_EN\.pdf"', f'href="{m["cv"]}"', s)
    return s


def main():
    src = open(SRC, encoding="utf-8").read()
    # stamp today's date into the footer (index.html is rewritten so EN/KO/JA always agree)
    stamped = re.sub(r'(최종 업데이트 |最終更新 |LAST UPDATED )(?:\{\{DATE\}\}|\d{4}-\d{2}-\d{2})', lambda m: m.group(1) + TODAY, src)
    if stamped != src:
        src = stamped
        with open(SRC, "w", encoding="utf-8") as f:
            f.write(src)
        print(f"index.html  ← footer date stamped {TODAY}")
    # keep sitemap <lastmod> in step with the footer date
    upd = re.search(r"LAST UPDATED (\d{4}-\d{2}-\d{2})", src)
    smap = os.path.join(ROOT, "sitemap.xml")
    if upd and os.path.exists(smap):
        xml = open(smap, encoding="utf-8", newline="").read()
        new_xml = re.sub(r"<lastmod>\d{4}-\d{2}-\d{2}</lastmod>", f"<lastmod>{upd.group(1)}</lastmod>", xml)
        if new_xml != xml:
            with open(smap, "w", encoding="utf-8", newline="") as f:
                f.write(new_xml)
            print(f"sitemap.xml ← lastmod {upd.group(1)}")
    general = strip_variant_marks(apply_variant(src, "general"))
    for lang, m in META.items():
        body, n = localise_body(general, lang)
        page = localise_head(body, m)
        assert "data-ko=" not in page and "data-ja=" not in page, "leftover data-* attributes"
        assert 'src="assets/' not in page and 'href="assets/' not in page, "relative asset path"
        d = os.path.join(ROOT, m["dir"]); os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)
        print(f"{m['dir']}/index.html  ← {n} elements localised, {len(page):,} bytes")
    bio = build_bio(src)
    os.makedirs(os.path.join(ROOT, "bio"), exist_ok=True)
    with open(os.path.join(ROOT, "bio", "index.html"), "w", encoding="utf-8") as f:
        f.write(bio)
    print(f"bio/index.html  ← biomedical variant (English, noindex), {len(bio):,} bytes")


if __name__ == "__main__":
    sys.exit(main())
