#!/usr/bin/env python3
"""Build the Lenkai Christian School site into public/.

Each page in src/pages/ starts with a header comment:

    <!--
    title: About
    description: One sentence for search results and link previews.
    path: /about/
    nav: about
    -->

Everything after the comment is the page body. build.py wraps it in the
shared header and footer and writes public/<path>/index.html.
Pages listed in DRAFTS are built to public/_drafts/ and left out of the
nav and the sitemap.

Usage: python3 build.py
"""
import html
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "src"
OUT = ROOT / "public"
SITE_URL = "https://www.lenkaichristianschool.org"
PHONE = "+254 725 501 002"
PHONE_HREF = "tel:+254725501002"
EMAIL = "info@lenkaichristianschool.org"
# WhatsApp goes to the same number. It is a personal phone that the old
# Weebly site already publishes; swap all three lines when the school
# gets a dedicated line.
WA_HREF = "https://wa.me/254725501002?text=" + "Habari%2C%20I%27m%20writing%20from%20the%20Lenkai%20Christian%20School%20website."

ICON_PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
ICON_WA = '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a.9.9 0 0 0-.7.3 2.8 2.8 0 0 0-.9 2.1 4.9 4.9 0 0 0 1 2.6 11.2 11.2 0 0 0 4.3 3.8c1.6.7 2.2.7 3 .6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.2-.3-.3-.5-.4z"/></svg>'

NAV = [
    ("home", "Home", "/"),
    ("about", "About", "/about/"),
    ("admissions", "Admissions", "/admissions/"),
    ("rescue", "Rescue Centre", "/rescue-centre/"),
    ("team", "Our Team", "/our-team/"),
    ("contact", "Contact", "/contact/"),
]
DRAFTS = {"team"}  # built, but not linked or listed until the staff roll is confirmed


def parse(page: Path):
    text = page.read_text()
    m = re.match(r"\s*<!--(.*?)-->\s*", text, re.S)
    if not m:
        raise SystemExit(f"{page}: missing header comment")
    meta = {}
    for line in m.group(1).strip().splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    return meta, text[m.end():]


def nav_html(current: str) -> str:
    items = []
    for key, label, href in NAV:
        if key in DRAFTS:
            continue
        cur = ' aria-current="page"' if key == current else ""
        items.append(f'<a href="{href}"{cur}>{label}</a>')
    give_cur = ' aria-current="page"' if current == "give" else ""
    items.append(f'<a href="/give/" class="give"{give_cur}>Give</a>')
    return "\n      ".join(items)


def footer_links(keys):
    out = []
    for label, href in keys:
        out.append(f'<li><a href="{href}">{label}</a></li>')
    return "\n          ".join(out)


def render(meta, body):
    title = meta["title"]
    full_title = "Lenkai Christian School" if meta["nav"] == "home" else f"{title} · Lenkai Christian School"
    desc = html.escape(meta["description"], quote=True)
    url = SITE_URL + meta["path"]
    for k, v in {"PHONE": PHONE, "PHONE_HREF": PHONE_HREF, "EMAIL": EMAIL, "WA_HREF": WA_HREF,
                 "ICON_PHONE": ICON_PHONE, "ICON_WA": ICON_WA}.items():
        body = body.replace("{{" + k + "}}", v)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Lenkai Christian School">
<meta property="og:title" content="{html.escape(full_title, quote=True)}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta name="theme-color" content="#12224A">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&family=Archivo:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="shuka" aria-hidden="true"></div>
<header class="topbar">
  <div class="topbar__inner">
    <a class="brand" href="/">
      <span class="crest" aria-hidden="true">L</span>
      <span>
        <span class="brand__name">Lenkai Christian School</span>
        <span class="brand__place">Kimana &middot; Kajiado County</span>
      </span>
    </a>
    <button class="navtoggle" type="button" id="navtoggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      {nav_html(meta["nav"])}
    </nav>
  </div>
</header>

<main id="main">
{body.strip()}
</main>

<div class="shuka" aria-hidden="true"></div>
<footer class="footer">
  <div class="frame">
    <div class="footer__grid">
      <div>
        <h2 class="footer__h">Lenkai Christian School</h2>
        <p class="footer__slogan">Empowering minds &middot; Transforming lives</p>
        <p class="footer__motto">&ldquo;Train up a child in the way she should go, and when she is old she will not depart from it.&rdquo; <span class="footer__cite">Proverbs 22:6</span></p>
      </div>
      <div>
        <h2 class="footer__h">For parents</h2>
        <ul>
          {footer_links([("Admissions", "/admissions/"), ("Curriculum", "/about/#curriculum"), ("Visit the school", "/contact/")])}
        </ul>
      </div>
      <div>
        <h2 class="footer__h">For supporters</h2>
        <ul>
          {footer_links([("Rescue centre", "/rescue-centre/"), ("Ways to give", "/give/"), ("Our leadership", "/about/#leadership")])}
        </ul>
      </div>
      <div>
        <h2 class="footer__h">Contact</h2>
        <ul>
          <li><a href="{PHONE_HREF}">{PHONE}</a></li>
          <li><a href="{WA_HREF}">WhatsApp us</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Kimana, Kajiado County, Kenya</li>
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <span>&copy; {date.today().year} Lenkai Christian School &middot; Kimana, Kajiado County, Kenya</span>
      <span>lenkaichristianschool.org</span>
    </div>
  </div>
</footer>
<nav class="actionbar" aria-label="Quick contact">
  <a class="ab-call" href="{PHONE_HREF}">{ICON_PHONE}Call</a>
  <a class="ab-wa" href="{WA_HREF}">{ICON_WA}WhatsApp</a>
  <a class="ab-give" href="/give/">Give</a>
</nav>
<script>
(function(){{
  var nav = document.getElementById('nav'), t = document.getElementById('navtoggle');
  t.addEventListener('click', function(){{
    var open = nav.classList.toggle('is-open');
    t.setAttribute('aria-expanded', open ? 'true' : 'false');
  }});
}})();
</script>
</body>
</html>
"""


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    for f in ["styles.css", "favicon.svg"]:
        shutil.copy(SRC / f, OUT / "assets" / f)
    if (SRC / "img").exists():
        shutil.copytree(SRC / "img", OUT / "assets" / "img")

    urls = []
    for page in sorted((SRC / "pages").glob("*.html")):
        meta, body = parse(page)
        path = meta["path"]
        if meta["nav"] in DRAFTS:
            path = "/_drafts" + path
        dest = OUT / path.strip("/") / "index.html" if path != "/" else OUT / "index.html"
        if meta["nav"] == "404":
            dest = OUT / "404.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(render(meta, body))
        if meta["nav"] not in DRAFTS and meta["nav"] != "404":
            urls.append(SITE_URL + meta["path"])
        print("built", dest.relative_to(ROOT))

    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
        + "</urlset>\n"
    )
    (OUT / "robots.txt").write_text(f"User-agent: *\nDisallow: /_drafts/\nSitemap: {SITE_URL}/sitemap.xml\n")


if __name__ == "__main__":
    main()
