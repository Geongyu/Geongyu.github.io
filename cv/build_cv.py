# -*- coding: utf-8 -*-
"""Render Geongyu Lee's CV to PDF in three languages.

    python -B cv/build_cv.py [outdir]

Produces Geongyu_Lee_CV_{EN,KO,JA}.pdf from content.py + cv.css.

Engines, in order:
  1. WeasyPrint, when it can be imported.
  2. Headless Chrome / Edge (--print-to-pdf). Set CHROME=<path> to pick a binary.

The rendered HTML for each edition (cv_<CODE>.html, with cv.css inlined) is written
to a scratch directory outside the repo: $CV_WORKDIR if set, otherwise ../cvqa next
to the repo root. Open those files in a browser to preview.
"""
import os
import re
import sys
import html
import shutil
import pathlib
import subprocess

from content import EDITIONS, PUBS, SCHOLAR

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
WORKDIR = pathlib.Path(os.environ.get("CV_WORKDIR") or REPO.parent / "cvqa")

# Same families as the portfolio site. IBM Plex Sans KR / JP load from Google Fonts here;
# IBM Plex Sans (Latin) is declared with @font-face in cv.css, along with local fallbacks.
FONTS_URL = ("https://fonts.googleapis.com/css2"
             "?family=IBM+Plex+Sans+KR:wght@400;700"
             "&amp;family=IBM+Plex+Sans+JP:wght@400;700"
             "&amp;display=block")

CHROME_CANDIDATES = [
    r"C:/Program Files/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
    r"C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
    r"C:/Program Files/Microsoft/Edge/Application/msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]


def contact_html(c):
    """A contact entry is either plain text or a (label, url) tuple."""
    if isinstance(c, (tuple, list)):
        label, url = c
        return f'<span><a href="{html.escape(url)}">{label}</a></span>'
    return f"<span>{c}</span>"


def text_width(s):
    """Rough width of a fragment in Latin-character units (CJK counts double; tags and
    entities are dropped). Only used to decide whether a fragment may be kept unbroken."""
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"&[a-zA-Z]+;|&#\d+;", "x", s)
    return sum(2 if ord(ch) > 0x2E80 else 1 for ch in s)


def meta_html(meta, lead_dot=True, short=40, whole=64):
    """Render ' · '-separated meta. A short meta (venue · format · role) is kept on one line,
    so it either follows the title or moves under it as a unit. A longer one is split into
    segments: each dot is glued to the segment after it, so no line ends on a dangling '·',
    and short segments stay unbroken, which stops Chrome from breaking 'Co-author' at the
    hyphen."""
    if text_width(meta) < whole:
        lead = "·&nbsp;" if lead_dot else ""
        return f'<span class="nw">{lead}{meta}</span>'
    out = []
    for i, seg in enumerate(meta.split(" · ")):
        dot = "·&nbsp;" if (lead_dot or i) else ""
        if text_width(seg) < short:
            out.append(f'<span class="nw">{dot}{seg}</span>')
        else:
            out.append(f"{dot}{seg}")
    return " ".join(out)


def render_html(d, inline_css=None):
    p = []
    a = p.append
    head_css = f"<style>\n{inline_css}\n</style>" if inline_css else ""
    a(f'<!doctype html>\n<html lang="{d["lang"]}"><head><meta charset="utf-8">'
      f'<title>Geongyu Lee · CV ({d["lang"].upper()})</title>'
      '<link rel="preconnect" href="https://fonts.googleapis.com">'
      '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
      f'<link rel="stylesheet" href="{FONTS_URL}">'
      f'{head_css}</head><body>')

    # masthead
    a('<div class="masthead">')
    a(f'<div class="name">{d["name"]}<span class="native">{d["native"]}</span></div>')
    a(f'<div class="role">{d["role"]}</div>')
    a('<div class="contact">' + "".join(contact_html(c) for c in d["contact"]) + "</div>")
    a("</div>")

    a(f'<p class="summary">{d["summary"]}</p>')

    # publications
    a("<section>")
    scholar = html.escape(d.get("scholar", SCHOLAR))
    a(f'<h2><span>{d["h_pubs"]}</span><span class="scholar"><a href="{scholar}">{d["scholar_note"]}</a></span></h2>')
    for i, (title, venue, extra) in enumerate(PUBS, 1):
        extra = extra[d["lang"]] if isinstance(extra, dict) else extra
        # a short extra stays on one line; a long one breaks only between segments
        if not extra:
            x = ""
        elif text_width(extra) < 60:
            x = f' <span class="x nw">{extra}</span>'
        else:
            x = f' <span class="x">{meta_html(extra, lead_dot=False)}</span>'
        a(f'<div class="pub"><div class="n">{i}</div><div class="body">'
          f'<span class="t">{title}</span> <span class="v">{venue}</span>{x}</div></div>')
    a("</section>")

    # experience
    a("<section>")
    a(f'<h2>{d["h_exp"]}</h2>')
    for co, when, sub, bullets in d["jobs"]:
        a('<div class="job">')
        a(f'<div class="job-h"><span class="co">{co}</span><span class="when">{when}</span></div>')
        a(f'<div class="sub">{sub}</div>')
        a("<ul>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>")
        a("</div>")
    a("</section>")

    # projects
    a("<section>")
    a(f'<h2>{d["h_proj"]}</h2>')
    for title, org, desc in d["projects"]:
        a(f'<div class="item"><div class="h">{title} <span class="org">· {org}</span></div>'
          f'<div class="d">{desc}</div></div>')
    a("</section>")

    # education
    a("<section>")
    a(f'<h2>{d["h_edu"]}</h2>')
    for title, when, desc in d["education"]:
        a(f'<div class="item"><div class="h edu"><span>{title}</span><span class="when">{when}</span></div>'
          f'<div class="d">{desc}</div></div>')
    a("</section>")

    # skills
    a("<section>")
    a(f'<h2>{d["h_skills"]}</h2>')
    for k, v in d["skills"]:
        a(f'<div class="skill"><div class="k">{k}</div><div class="v">{v}</div></div>')
    a("</section>")

    # awards
    a("<section>")
    a(f'<h2>{d["h_awards"]}</h2>')
    for title, meta in d["awards"]:
        a(f'<div class="award"><div class="h">{title}</div><div class="m">{meta}</div></div>')
    a("</section>")

    # talks
    a("<section>")
    a(f'<h2>{d["h_talks"]}</h2>')
    for title, meta in d["talks"]:
        a(f'<div class="li">{title} <span class="m">{meta_html(meta)}</span></div>')
    a("</section>")

    # community & service
    a("<section>")
    a(f'<h2>{d["h_service"]}</h2>')
    for title, meta in d["service"]:
        a(f'<div class="li">{title} <span class="m">{meta_html(meta)}</span></div>')
    a("</section>")

    a("</body></html>")
    return "\n".join(p)


def find_chrome():
    env = os.environ.get("CHROME")
    if env:
        return env
    for c in CHROME_CANDIDATES:
        if pathlib.Path(c).is_file():
            return c
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
                 "chrome", "msedge", "microsoft-edge"):
        hit = shutil.which(name)
        if hit:
            return hit
    return None


def chrome_pdf(chrome, html_path, out):
    """Print an HTML file to PDF with headless Chrome (virtual time lets web fonts load)."""
    out = out.resolve()
    if out.exists():
        out.unlink()
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-extensions",
        f"--user-data-dir={WORKDIR / '.chrome-profile'}",
        "--no-pdf-header-footer",
        f"--print-to-pdf={out}",
        "--virtual-time-budget=10000",
        html_path.resolve().as_uri(),
    ]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if not out.is_file() or out.stat().st_size == 0:
        raise RuntimeError(f"Chrome did not write {out} (exit {r.returncode}):\n{r.stderr[-2000:]}")
    warn_if_fallback_fonts(out)


def warn_if_fallback_fonts(pdf):
    """If PyMuPDF is around, warn when the web fonts did not make it into the PDF."""
    try:
        import pymupdf
    except ImportError:
        return
    with pymupdf.open(pdf) as doc:
        names = {f[3].split("+")[-1] for page in doc for f in page.get_fonts()}
    if not any(n.startswith("IBMPlexSans") for n in names) or "" in names:
        print(f"  warning: {pdf.name} embeds {sorted(names)}; the web fonts may not have "
              "loaded (offline?) or a Type 3 fallback font was used")


def main():
    outdir = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE
    outdir.mkdir(parents=True, exist_ok=True)
    WORKDIR.mkdir(parents=True, exist_ok=True)
    css_text = (HERE / "cv.css").read_text(encoding="utf-8")

    try:
        from weasyprint import HTML
    except Exception:  # not installed, or GTK/Pango missing (common on Windows)
        HTML = None

    chrome = None
    if HTML is None:
        chrome = find_chrome()
        if not chrome:
            sys.exit("Neither WeasyPrint nor Chrome/Edge found. Install one, or set CHROME=<path>.")
        print("engine: headless", pathlib.Path(chrome).name)
    else:
        print("engine: WeasyPrint")

    for code, d in EDITIONS.items():
        out = outdir / f"Geongyu_Lee_CV_{code}.pdf"
        html_path = WORKDIR / f"cv_{code}.html"
        html = render_html(d, inline_css=css_text)
        html_path.write_text(html, encoding="utf-8")
        if HTML is not None:
            HTML(string=html, base_url=str(HERE)).write_pdf(str(out))
        else:
            chrome_pdf(chrome, html_path, out)
        print("wrote", out)


if __name__ == "__main__":
    main()
