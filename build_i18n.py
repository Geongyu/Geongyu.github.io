#!/usr/bin/env python3
"""
Generate /ko/index.html and /ja/index.html from the root index.html.

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
        "title": "이건규 | 머신러닝 리서처 · 의료 AI · 디지털 병리",
        "description": "머신러닝 리서처 이건규(Geongyu Lee)의 포트폴리오입니다. 병리 슬라이드로 분자 정보를, 프로테오믹스로 약물 반응을 예측하는 머신러닝 모델을 연구합니다. 새로운 병원의 데이터나 학습에 없던 약물에서도 예측이 유효한지 검증하는 데 집중합니다.",
        "og_title": "이건규 · 머신러닝 리서처 (의료 AI · 디지털 병리)",
        "og_description": "병리 슬라이드로 분자 정보를, 프로테오믹스로 약물 반응을 예측하는 머신러닝 모델을 연구합니다. 새로운 병원의 데이터나 학습에 없던 약물에서도 예측이 유효한지 검증하는 데 집중합니다.",
        "image_alt": "이건규(Geongyu Lee) 소개 카드 · 머신러닝 리서처(서울) · 크로스모달 학습, 신뢰할 수 있는 예측, Computational Pathology × 멀티오믹스",
        "ld_description": "병리 슬라이드로 분자 정보를 예측하는 모델을 연구하는 머신러닝 리서처입니다. 현 직장에서는 프로테오믹스로 약물 반응을 예측하는 모델도 개발합니다. 새로운 병원의 데이터나 학습에 없던 약물에서도 예측이 유효한지 검증하는 데 집중합니다.",
        "cv": "/assets/Geongyu_Lee_CV_KO.pdf",
    },
    "ja": {
        "lang": "ja", "locale": "ja_JP", "dir": "ja",
        "title": "イ・ゴンギュ | 機械学習リサーチャー・医療AI・デジタル病理",
        "description": "機械学習リサーチャー、イ・ゴンギュ(Geongyu Lee)のポートフォリオです。病理画像から分子情報を、プロテオミクスから薬剤応答を予測する機械学習モデルを研究しています。学習データに含まれない施設や薬剤でも予測が有効かどうかの検証に力を入れています。",
        "og_title": "イ・ゴンギュ · 機械学習リサーチャー(医療AI・デジタル病理)",
        "og_description": "病理画像から分子情報を、プロテオミクスから薬剤応答を予測する機械学習モデルを研究しています。学習データに含まれない施設や薬剤でも予測が有効かどうかの検証に力を入れています。",
        "image_alt": "イ・ゴンギュ(Geongyu Lee)の共有カード。ソウルの機械学習リサーチャー · クロスモーダル学習、信頼できる予測、Computational Pathology × マルチオミクス。",
        "ld_description": "病理画像から分子情報を予測するモデルを研究し、現職ではプロテオミクスから薬剤応答を予測するモデルも開発している機械学習リサーチャーです。学習データに含まれない施設や薬剤でも予測が有効かどうかの検証に力を入れています。",
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
    for lang, m in META.items():
        body, n = localise_body(src, lang)
        page = localise_head(body, m)
        assert "data-ko=" not in page and "data-ja=" not in page, "leftover data-* attributes"
        assert 'src="assets/' not in page and 'href="assets/' not in page, "relative asset path"
        d = os.path.join(ROOT, m["dir"]); os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)
        print(f"{m['dir']}/index.html  ← {n} elements localised, {len(page):,} bytes")


if __name__ == "__main__":
    sys.exit(main())
