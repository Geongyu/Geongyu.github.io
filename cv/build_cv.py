# -*- coding: utf-8 -*-
"""Render Geongyu Lee's CV to PDF in three languages.

    python3 build_cv.py [outdir]

Produces Geongyu_Lee_CV_{EN,KO,JA}.pdf using WeasyPrint + cv.css.
"""
import sys
import pathlib
from weasyprint import HTML, CSS

from content import EDITIONS, PUBS, SCHOLAR

HERE = pathlib.Path(__file__).resolve().parent


def render_html(d):
    p = []
    a = p.append
    a(f'<html lang="{d["lang"]}"><head><meta charset="utf-8">'
      f'<title>Geongyu Lee — CV ({d["lang"].upper()})</title></head><body>')

    # masthead
    a('<div class="masthead">')
    a(f'<div class="name">{d["name"]}<span class="native">{d["native"]}</span></div>')
    a(f'<div class="role">{d["role"]}</div>')
    a('<div class="contact">' + "".join(f"<span>{c}</span>" for c in d["contact"]) + "</div>")
    a("</div>")

    a(f'<p class="summary">{d["summary"]}</p>')

    # publications
    a("<section>")
    a(f'<h2>{d["h_pubs"]}<span class="scholar"><a href="{SCHOLAR}">{d["scholar_note"]}</a></span></h2>')
    for i, (title, venue, extra) in enumerate(PUBS, 1):
        x = f' <span class="x">{extra}</span>' if extra else ""
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
        a(f'<div class="item"><div class="h"><span class="when">{when}</span>{title}</div>'
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
    a(f'<p class="talks">{d["talks"]}</p>')
    a("</section>")

    a("</body></html>")
    return "\n".join(p)


def main():
    outdir = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE
    outdir.mkdir(parents=True, exist_ok=True)
    css = CSS(filename=str(HERE / "cv.css"))
    for code, d in EDITIONS.items():
        html = render_html(d)
        (HERE / f"preview_{code}.html").write_text(html, encoding="utf-8")
        out = outdir / f"Geongyu_Lee_CV_{code}.pdf"
        HTML(string=html, base_url=str(HERE)).write_pdf(str(out), stylesheets=[css])
        print("wrote", out)


if __name__ == "__main__":
    main()
