# Lenkai Christian School — website build brief

Slogan: **Empowering minds, transforming lives** (hero eyebrow + footer on every page)
Domain: **lenkaichristianschool.org**, bought at **Truehost** (live site will be `www.lenkaichristianschool.org`)
Platform: **Google Sites**, staff-editable
Audience: parents and donors, split at the top of the homepage

## Deliverables

- **Design preview** — https://claude.ai/code/artifact/e78984c8-e941-4f92-b347-2141f2d6f300
- **Build kit** (incl. IT-admin walkthrough + Truehost DNS) — https://claude.ai/code/artifact/80fe6cdb-8081-4d20-aecd-438e38677d66
- **shuka-divider.png** (2400×36) — thin stripe band for the top of each page

## Design system

| | |
|---|---|
| Primary | `#1E3A73` shuka indigo |
| Deep band | `#12224A` |
| Accent | `#E29A0F` marigold (use `#8A5B00` for accent *text* on light grounds — contrast) |
| Secondary | `#B0472C` clay — rescue-centre thread only |
| Light band | `#EDF1F8` · Ground `#FCFCFD` · Text `#17223A` |
| Display type | Newsreader (fallback Lora) |
| Body type | Archivo (fallback Work Sans) |
| Layout | Normal 1280px, Comfortable density, top nav |

Cultural grounding: colours keyed to Maasai beadwork/shuka meanings — red bravery/unity, blue sky/rain, white peace, orange-yellow hospitality. Shuka stripe used only as a thin 7px band. "Karibu" opens the Contact page.

## Structure

Home · About · Admissions · Rescue Centre · Our Team · Contact · Give (7 pages)

## School facts confirmed by Dan (Aug 2026)

- **~300 pupils total**, day and boarding
- **117 boarders: 65 girls, 52 boys** — boarding is co-educational, not girls-only
- **Co-educational throughout**, Pre-Primary to Senior School, in class and boarding
- Rescue programme remains girls-only (distinct from general boarding)
- Homepage figures band reads: 5 · 300 · 117 · 500+

## Academic structure — 2026/27 plan (confirmed by Dan)

Lenkai runs the full ladder on one campus:
- Pre-Primary PP1–PP2
- Grade 1–6 (KPSEA at Grade 6)
- Junior School Grade 7–9 (KJSEA at Grade 9) — confirmed
- Senior School Grade 10 (first national cohort Jan 2026; Grade 11 in 2027) — pathways (STEM / Social Sciences / Arts & Sports Science) still to confirm
- 8-4-4 phase-out: Form 3 & Form 4 — Form 4 sits KCSE Nov 2026, Form 3 in 2027 (the country's last KCSE)

Rescue narrative: a rescued girl can now stay at Lenkai from arrival to finishing Senior School; Give card is "Carry her through Senior School".

## Other verified facts

- Kimana, Kajiado County. Coordinates 2°48'06.0"S 37°32'03.2"E = −2.801667, 37.534222
- Phone +254 725 501 002. Old email lenkaischool@yahoo.com → move to info@lenkaichristianschool.org
- Founded and led by Rev. John Parit and Dorcus Parit; opened with 5 pupils
- Rescue centre for girls fleeing FGM and forced marriage; works alongside Hope Beyond Foundation, 500+ girls rescued in Kajiado
- 2019: ICT lab worth ~KSh 6M donated by an American family — two labs plus two offices
- Mission, vision and Proverbs 22:6 philosophy carried verbatim from the old site ("conductive" corrected to "conducive")
- 12 teaching + 6 support staff in the archived records — predates the Junior/Senior expansion; current staff list still needed
- The three photos on the old Weebly site are **genuine**, not stock — all from one bake-sale event

## Platform corrections

- **No "show page as button" in Sites nav.** Give must be a Button component in each page banner instead.
- Sites cannot serve an apex domain; HTTPS is provisioned by Sites (no SSL purchase from Truehost needed).

## Four launch blockers

1. Photographs — nine shots needed (list in the build kit §04)
2. Fees — day and boarding, per term, per level
3. Payment details — M-Pesa Paybill/Till, bank account, SWIFT
4. Child protection policy and safeguarding lead

## Future considerations (non-blocking — build kit §09)

- **US tax-deductible giving:** what plans does Lenkai have to let a US person make a deductible donation supporting a child through the year? Options to evaluate: a "friends of" / fiscal-sponsorship fund (e.g. Chapel & York US Foundation, a 501(c)(3) that receives gifts for member orgs abroad; also Myriad USA, CAF America, GlobalGiving) — or, possibly free, designated gifts through an existing US partner such as Just One Africa / the Hope Beyond network. Answer feeds the Give page's "From outside Kenya" block.

## DNS — all in the Truehost zone editor

Client area → Domains → Manage DNS → Edit DNS Zone (pencil). Nameservers stay ns1.cloudoon.com / ns2.cloudoon.net / ns3.cloudoon.org. (If on hosting nameservers instead: cPanel → Zone Editor.)

| Purpose | Type | Host | Value | Priority |
|---|---|---|---|---|
| Website | CNAME | `www` | `ghs.googlehosted.com.` | — |
| Email in | MX | `@` | `smtp.google.com` | 1 |
| Email out | TXT | `@` | `v=spf1 include:_spf.google.com ~all` | — |
| Verification | TXT | `@` | google-site-verification=… (from Search Console) | — |

Bare domain 301 → www via Truehost URL forwarding (support ticket if not in panel; fallback redirect.pizza or Cloudflare). Add DKIM + DMARC once mail flows.
