# lenkaichristianschool.org

The website of Lenkai Christian School, Kimana, Kajiado County, Kenya. A hand-built static site: plain HTML and one stylesheet, no framework, about 140 KB for all six pages. It replaced the plan to build on Google Sites (see `docs/build-brief-2026-08.md` for the original brief and design system).

## Layout

- `src/pages/*.html`: one file per page. Each starts with a header comment (title, description, path, nav key); the rest is the page body.
- `src/styles.css`: the whole design system (shuka indigo, marigold, clay; Newsreader and Archivo).
- `build.py`: wraps each page in the shared header, footer and phone action bar, and writes `public/`. The phone number, WhatsApp link and email are set once at the top of this file.
- `public/`: the built site (not committed). GitHub Actions runs `build.py` on every push to `main` and deploys `public/` to GitHub Pages; see `.github/workflows/pages.yml`.

## Build and preview

```
python3 build.py
python3 -m http.server 8732 --directory public
```

## Approved content

The school's earlier site, lenkaischool.weebly.com, is the approved source. Everything on it is carried over here, and nothing new may contradict it; `docs/content-audit.md` maps each item to its place on this site and lists what is new and still needs the school's sign-off. Our Team is left out until the school has an up-to-date staff list.

## Still to come from the school

- Photographs (shot list in the build brief). Until then, drawn panels stand in for photos. Rescued girls' faces are never published without written guardian consent.
- Fee structure, M-Pesa and bank details. Admissions and Give currently ask people to call, WhatsApp or email.
- Founding year, and the current enrolment (the site says 300; a Hope Beyond page reportedly says 500+).
- A school address on the new domain, if wanted. The site uses lenkaischool@yahoo.com, as the approved site does.
