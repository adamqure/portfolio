#!/usr/bin/env python3
"""Builds site/*.html from one shared header/footer so every page stays identical.
Run:  python3 build.py
Placeholders to replace before submitting are wrapped in class="todo" (dashed teal outline)."""
from pathlib import Path

SITE = Path(__file__).parent / "site"
NAME = "Adam Ure"
TITLE = "Software Engineer for Connected Devices"

EMAIL = "adamqure@icloud.com"
CITY = "Atlanta, GA"
FORM_ENDPOINT = "https://formspree.io/f/mrpprqoz"
BOOKING_URL = "https://cal.com/adamure/30min"

# One profile description, reused on the About page and (shortened) on the resume,
# LinkedIn and Upwork, as the rubric requires. Paste-ready copies live in profile.md.
PROFILE = [
    "I help hardware teams ship software that pairs reliably, syncs accurately and updates safely. I got into software because I love building things people depend on, and connected devices are where that matters most: when an app talks to hardware, &ldquo;it works on my machine&rdquo; isn&rsquo;t good enough.",
    "Over the past six years I&rsquo;ve led mobile and platform work for connected products, from consumer devices to a regulated medical device platform. I co-invented a patented multi-tier Bluetooth security framework for mobile-to-device communication, led compliance-critical features for a regulated medical device platform, and built a localization and audit pipeline that cut verification time by about 99.8%. Today I&rsquo;m the founding engineer at Snifr, building a Wi-Fi-connected e-nose for gut health tracking that&rsquo;s now in beta.",
    "I build quality in rather than bolting it on afterward: test-driven development, clean architecture and CI/CD quality gates that let teams ship on a cadence they can plan around. I hold an M.S. in Software Development and a B.S. in Computer Science, and I mentor engineers who want to grow. Away from the keyboard I&rsquo;m a dad of three, a singer and a lifelong student of Mandarin.",
]
PROFILE_SHORT = ("Software engineer for connected devices. I help hardware teams ship software that pairs reliably, "
                 "syncs accurately and updates safely. Patented Bluetooth security co-inventor with six years leading "
                 "mobile and platform work for consumer and regulated medical devices, built on TDD, clean "
                 "architecture and predictable delivery.")

PAGES = [("index.html", "Home"), ("about.html", "About"),
         ("portfolio.html", "Portfolio"), ("contact.html", "Contact")]

LOGO = """<svg viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="10" fill="#102b44"/>
<rect x="0.5" y="0.5" width="39" height="39" rx="9.5" fill="none" stroke="#15c2a3" stroke-opacity=".5"/>
<text x="20" y="26" text-anchor="middle" font-family="Poppins, sans-serif" font-weight="700" font-size="15" fill="#15c2a3">AU</text></svg>"""

LINKEDIN = """<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="9" width="4" height="12" rx="1"/><circle cx="5" cy="5" r="2.2"/>
<path d="M10 9h3.8v1.8C14.5 9.6 15.9 8.7 18 8.7c3 0 4 2 4 5V21h-4v-6.5c0-1.6-.5-2.6-1.9-2.6-1.5 0-2.1 1.1-2.1 2.6V21h-4z"/></svg>"""

SOCIAL = [
    ("GitHub", "https://github.com/adamqure", '<img src="https://cdn.simpleicons.org/github/8ea6bd" alt="" width="20" height="20">', False),
    ("LinkedIn", "https://www.linkedin.com/in/adamqure", LINKEDIN, False),
    ("Upwork", "https://www.upwork.com/freelancers/~015585d132264ee962", '<img src="https://cdn.simpleicons.org/upwork/8ea6bd" alt="" width="20" height="20">', False),
]


def header(active):
    links = "\n".join(
        f'        <li><a href="{f}"{" aria-current=\"page\"" if label == active else ""}>{label}</a></li>'
        for f, label in PAGES)
    return f"""  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="index.html">{LOGO}<span>{NAME}</span></a>
      <nav aria-label="Main"><ul class="nav">
{links}
      </ul></nav>
    </div>
  </header>"""


def footer():
    items = "\n".join(
        f'        <li><a href="{url}" aria-label="{label}" title="{label}"'
        f'{" class=\"todo\"" if todo else ""} target="_blank" rel="noopener noreferrer">{icon}</a></li>'
        for label, url, icon, todo in SOCIAL)
    return f"""  <footer class="site-footer" id="footer">
    <div class="wrap">
      <p class="muted" style="margin:0">&copy; 2026 {NAME} &middot; {TITLE}</p>
      <ul class="social">
{items}
      </ul>
    </div>
  </footer>"""


def page(filename, label, description, body):
    title = f"{NAME} | {TITLE}" if label == "Home" else f"{label} | {NAME}"
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="icon" href="images/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&family=Lato:wght@400;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css?v=4">
</head>
<body>
{header(label)}
  <main>
{body}
  </main>
{footer()}
</body>
</html>
"""
    (SITE / filename).write_text(html)


HERO_ART = """<svg class="hero-art" viewBox="0 0 400 400" role="img" aria-label="A phone connected wirelessly to a smartwatch and a sensor">
  <g fill="none" stroke="#15c2a3" stroke-width="3" stroke-linecap="round" opacity=".55">
    <path d="M208 150q40-30 80-10"/><path d="M215 170q30-18 60-6"/>
    <path d="M208 250q40 30 80 10"/><path d="M215 230q30 18 60 6"/>
  </g>
  <rect x="80" y="70" width="140" height="260" rx="26" fill="#102b44" stroke="#8ea6bd" stroke-opacity=".5" stroke-width="2"/>
  <rect x="128" y="84" width="44" height="8" rx="4" fill="#0b1f33"/>
  <rect x="100" y="112" width="100" height="14" rx="5" fill="#8ea6bd" opacity=".35"/>
  <rect x="100" y="138" width="70" height="10" rx="5" fill="#8ea6bd" opacity=".25"/>
  <rect x="100" y="166" width="100" height="70" rx="10" fill="#0b1f33"/>
  <polyline points="108,220 125,205 140,212 158,186 175,198 192,178" fill="none" stroke="#15c2a3" stroke-width="3" stroke-linejoin="round"/>
  <rect x="100" y="250" width="100" height="34" rx="10" fill="#15c2a3"/>
  <text x="150" y="272" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="12" fill="#0b1f33">PAIRED ✓</text>
  <g transform="translate(300 110)">
    <rect x="-14" y="-52" width="28" height="22" rx="6" fill="#102b44"/><rect x="-14" y="30" width="28" height="22" rx="6" fill="#102b44"/>
    <rect x="-34" y="-34" width="68" height="68" rx="18" fill="#102b44" stroke="#8ea6bd" stroke-opacity=".5" stroke-width="2"/>
    <circle r="18" fill="none" stroke="#15c2a3" stroke-width="4" stroke-dasharray="80 120" transform="rotate(-90)"/>
  </g>
  <g transform="translate(305 285)">
    <circle r="36" fill="#102b44" stroke="#8ea6bd" stroke-opacity=".5" stroke-width="2"/>
    <circle r="10" fill="#15c2a3"/><circle r="20" fill="none" stroke="#15c2a3" stroke-opacity=".4" stroke-width="2"/>
  </g>
</svg>"""

SERVICES = [
    ("01 / CONNECT", "Device connectivity", "Bluetooth LE pairing, background sync and offline-first data that holds up in the real world, not just on the bench."),
    ("02 / VERIFY", "Test-driven development", "Simulated devices and automated tests so you find protocol and sync bugs before your customers do."),
    ("03 / SHIP", "Architecture &amp; delivery", "Release pipelines that keep app, firmware and cloud versions compatible, on a cadence you can plan around."),
    ("04 / GROW", "Technical mentorship", "Coaching for engineers and teams who want to build quality in, rather than bolting it on afterward."),
]

home = f"""    <section class="hero">
      <div class="wrap">
        <div>
          <span class="eyebrow">{NAME} &middot; {TITLE}</span>
          <h1>Ship quality.<br><span class="accent">Predictably.</span></h1>
          <p class="lead">I help hardware teams ship software that pairs reliably, syncs accurately and updates safely, from wearables to medical devices, with a release cadence you can plan around.</p>
          <div class="btn-row">
            <a class="btn btn-primary" href="contact.html">Start a project</a>
            <a class="btn btn-ghost" href="portfolio.html">See my work</a>
          </div>
        </div>
        {HERO_ART}
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        <span class="eyebrow">How I help</span>
        <h2>From first pairing to field updates</h2>
        <div class="grid grid-4" style="margin-top:2rem">
""" + "\n".join(f"""          <div class="card"><span class="icon">{n}</span><h3>{t}</h3><p class="muted" style="margin:0">{d}</p></div>"""
                 for n, t, d in SERVICES) + """
        </div>
      </div>
    </section>"""

about = f"""    <section class="section">
      <div class="wrap about-grid">
        <img class="portrait" src="images/portrait.jpg" alt="Portrait of {NAME}" width="640" height="800">
        <div>
          <span class="eyebrow">About</span>
          <h1 style="font-size:clamp(2rem,4vw,3rem)">{NAME}</h1>
          <p class="muted" style="font:600 1.1rem var(--font-display)">{TITLE}</p>
          <div>
""" + "\n".join(f"            <p>{p}</p>" for p in PROFILE) + f"""
          </div>
          <ul class="tags" style="margin:1.5rem 0">
            <li>Bluetooth LE</li><li>Device sync</li><li>OTA updates</li><li>TDD</li><li>Software architecture</li><li>CI/CD</li><li>Regulated software</li><li>Mentorship</li>
          </ul>
          <div class="btn-row">
            <a class="btn btn-primary" href="#resume">View my resume</a>
            <a class="btn btn-ghost" href="contact.html">Get in touch</a>
          </div>
        </div>
      </div>
    </section>
    <section class="section" id="resume" style="padding-top:0">
      <div class="wrap">
        <span class="eyebrow">Resume</span>
        <h2>Experience, education &amp; skills</h2>
        <a href="resume.pdf" target="_blank"><img class="resume-img" src="images/resume.png?v=2" alt="{NAME} resume: About me, core strengths, experience, education and certifications" width="1632" height="2112"></a>
        <p class="muted" style="margin-top:1rem"><a href="resume.pdf" target="_blank">Download the resume (PDF)</a></p>
      </div>
    </section>"""


def tile(x, y, w, label, accent=False):
    fill, fg = ("#15c2a3", "#0b1f33") if accent else ("#0b1f33", "#eaf1f8")
    return (f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="10" fill="{fill}" stroke="#8ea6bd" stroke-opacity=".4"/>'
            f'<text x="{x + w / 2}" y="{y + 27}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="13" fill="{fg}">{label}</text>')


def visual(caption, body):
    return (f'<svg viewBox="0 0 400 300" role="img" aria-label="{caption}"><rect width="400" height="300" fill="#102b44"/>'
            f'<g stroke="#15c2a3" stroke-width="2" stroke-dasharray="5 5" opacity=".7">{body[0]}</g>{body[1]}</svg>')


VIS_MONOVO = visual("Diagram: a phone talks to a device through three security tiers", (
    '<line x1="200" y1="84" x2="200" y2="216"/>',
    tile(130, 40, 140, "Mobile app") + tile(60, 112, 280, "Tier 1 · Pairing &amp; identity") +
    tile(60, 160, 280, "Tier 2 · Encrypted session", True) + tile(60, 208, 280, "Tier 3 · Command auth") +
    '<text x="200" y="285" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="12" fill="#8ea6bd">U.S. PATENT · BLUETOOTH SECURITY</text>'))

VIS_NEVRO = visual("Diagram: translated strings flow through an automated audit pipeline into a verified release", (
    '<line x1="110" y1="150" x2="150" y2="150"/><line x1="250" y1="150" x2="290" y2="150"/>',
    tile(20, 128, 90, "Strings") + tile(150, 128, 100, "Audit", True) + tile(290, 128, 90, "Release") +
    '<text x="200" y="70" text-anchor="middle" font-family="Poppins, sans-serif" font-weight="700" font-size="44" fill="#15c2a3">~99.8%</text>'
    '<text x="200" y="98" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="12" fill="#8ea6bd">LESS VERIFICATION TIME</text>'
    '<text x="200" y="225" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="12" fill="#8ea6bd">REGULATED MEDICAL DEVICE PLATFORM</text>'))

VIS_MYIA = visual("Diagram: iOS, Android and Flutter apps unified on one platform connecting patients and care teams", (
    '<line x1="80" y1="84" x2="200" y2="140"/><line x1="200" y1="84" x2="200" y2="140"/><line x1="320" y1="84" x2="200" y2="140"/><line x1="200" y1="184" x2="200" y2="216"/>',
    tile(30, 40, 100, "iOS") + tile(150, 40, 100, "Android") + tile(270, 40, 100, "Flutter") +
    tile(90, 140, 220, "Unified platform", True) + tile(90, 216, 220, "Patients ⇄ care team")))

VIS_SNIFR = visual("Diagram: an e-nose sensor pairs with the app, which turns readings into AI insights and a weekly FloraScore report", (
    '<line x1="200" y1="84" x2="200" y2="128"/><line x1="200" y1="172" x2="200" y2="216"/>',
    tile(110, 40, 180, "E-nose sensor") + tile(110, 128, 180, "Paired app", True) + tile(110, 216, 180, "AI · FloraScore™") +
    '<text x="200" y="288" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="12" fill="#8ea6bd">WI-FI CONNECTED · IN BETA</text>'))

PROJECTS = [
    dict(name="A Wi-Fi e-nose for gut health tracking", org="Snifr", visual=VIS_SNIFR,
         shots=[("snifr-1.jpg", "Snifr app: FloraScore and weekly trend"), ("snifr-2.jpg", "Snifr app: consistency and duration analysis")],
         link="https://www.snifr.ai", link_label="Visit snifr.ai",
         goal="Help people managing IBS, food sensitivities or elimination diets stop guessing about their gut health, with real answers they can bring to a doctor.",
         role="Founding Engineer. I own the software that connects the e-nose to its users, from bringing the sensor online over Wi-Fi to the app and the AI insights built on its data.",
         approach="A Wi-Fi-connected electronic-nose sensor captures bowel readings and sends them to the app, which turns them into daily AI insights and a weekly FloraScore™ report with specific, science-backed tips, so users can see how diet and lifestyle changes play out over weeks and months.",
         deliverables="A Wi-Fi-connected e-nose and companion app, daily AI insights and weekly FloraScore™ reports, now in beta.",
         skills=["Wi-Fi device connectivity", "Sensor data", "AI integration", "Privacy &amp; security"],
         tools=["Kotlin Multiplatform", "AWS", "Python (ML)", "Server-side Swift"],
         date="Ongoing Project"),
    dict(name="Securing mobile-to-device Bluetooth", org="Monovo", visual=VIS_MONOVO,
         shots=[("monovo-2.jpg", "Monovo app: blood pressure monitor connection status"), ("monovo-3.jpg", "Monovo app: guided measurement help")],
         link="https://apps.apple.com/us/app/monovo/id1508030721", link_label="View on the App Store",
         goal="Give patients a remote vitals-monitoring app that connects securely and reliably to at-home devices such as a blood pressure monitor, on both iOS and Android.",
         role="Mobile Experience Architect. I built the iOS app from scratch, set mobile strategy across iOS and Android, co-invented the Bluetooth security framework with the hardware engineers, and later led the backend and web teams too.",
         approach="Designed security into the device link from the start: a multi-tier framework that layers protection on mobile-to-device communication. Established UI patterns, testing practices and engineering standards so both platforms stayed consistent as the product grew.",
         deliverables="Production iOS app, cross-platform mobile architecture, patented multi-tier Bluetooth security framework (U.S. Patent No. 12,652,273), and end-to-end systems across mobile, backend and web.",
         skills=["Bluetooth LE", "Device security", "Mobile architecture", "Team leadership"],
         tools=["Swift", "iOS", "Android", "Backend &amp; web"],
         date="November 2021"),
    dict(name="Compliance-critical features for a medical device", org="Nevro", visual=VIS_NEVRO,
         link="https://www.nevro.com", link_label="Visit nevro.com",
         goal="Ship compliance-critical mobile features for a regulated medical device platform, predictably and without compromising quality.",
         role="Engineering Team Lead and execution lead. I coordinated priorities and dependencies with product, QA and regulatory teams, and served as independent reviewer on firmware projects across the device and software boundary.",
         approach="Treated verification as an engineering problem: I architected a multilingual localization and audit pipeline that automated what had been manual checks, while keeping every release within medical device controls.",
         deliverables="Compliance-critical mobile releases, a localization and audit pipeline that reduced verification time by about 99.8%, and firmware design reviews.",
         skills=["Regulated software", "Verification automation", "Firmware review", "Release planning"],
         tools=["Swift", "SwiftUI", "CI/CD", "Medical device controls"],
         date="May 2025"),
    dict(name="Unifying a remote-care platform", org="Myia Health", visual=VIS_MYIA,
         link="https://myiahealth02.squarespace.com", link_label="Visit Myia Health",
         goal="Bring separate iOS, Android and Flutter apps onto one reliable platform for remote patient care.",
         role="Lead Mobile Developer. I architected the unified mobile platform, defined engineering standards and mentored the team.",
         approach="Introduced shared architecture patterns, clean architecture and SOLID principles, plus CI/CD and test-driven workflows that made each release safer than the last.",
         deliverables="A unified cross-platform mobile architecture, telemedicine platform components, and team workflows that reduced post-release defects by about 15%.",
         skills=["Cross-platform architecture", "TDD", "Telemedicine", "Mentorship"],
         tools=["iOS", "Android", "Flutter", "CI/CD"],
         date="January 2023"),
]


def project(p):
    tags = lambda xs: '<ul class="tags">' + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
    rows = [("Goal", p["goal"]), ("My contribution", p["role"]), ("How we got there", p["approach"]),
            ("Deliverables", p["deliverables"]), ("Skills", tags(p["skills"])), ("Tools", tags(p["tools"])),
            ("Completed", p["date"])]
    facts = "\n".join(f"            <dt>{k}</dt><dd>{v}</dd>" for k, v in rows)
    shots = p.get("shots", [])
    shots_html = ('          <div class="shots">' + "".join(
        f'<img src="images/projects/{f}" alt="{alt}" loading="lazy" width="450" height="800">' for f, alt in shots)
        + "</div>\n") if shots else ""
    return f"""      <article class="project{" todo" if p.get("todo") else ""}" id="{p["org"].lower().replace(" ", "-")}">
        <div class="project-media">
{shots_html}          <div class="project-visual">{p["visual"]}</div>
        </div>
        <div>
          <span class="eyebrow">{p["org"]}</span>
          <h2>{p["name"]}</h2>
          <dl class="facts">
{facts}
          </dl>
          <a class="btn btn-ghost" href="{p["link"]}" target="_blank" rel="noopener noreferrer">{p["link_label"]}</a>
        </div>
      </article>"""


portfolio = f"""    <section class="section">
      <div class="wrap">
        <span class="eyebrow">Portfolio</span>
        <h1 style="font-size:clamp(2rem,4vw,3rem)">Selected work</h1>
        <p class="lead" style="margin-bottom:3rem">Software for connected devices: secure pairing, reliable data and safe releases, built and tested to ship predictably.</p>
""" + "\n".join(project(p) for p in PROJECTS) + """
      </div>
    </section>"""

contact = f"""    <section class="section" id="contact">
      <div class="wrap contact-grid">
        <div>
          <span class="eyebrow">Contact</span>
          <h1 style="font-size:clamp(2rem,4vw,3rem)">Let&rsquo;s build something that connects</h1>
          <p class="lead">Tell me about your device, your timeline and what&rsquo;s getting in the way of shipping. I&rsquo;ll reply within two business days.</p>
          <p><span class="eyebrow" style="margin-bottom:.4rem">Email</span>
            <a href="mailto:{EMAIL}" style="font:600 1.25rem var(--font-display)">{EMAIL}</a></p>
          <div class="booking">
            <span class="eyebrow" style="margin-bottom:.4rem">Book a call</span>
            <p class="muted" style="margin:0 0 1rem">Prefer to talk it through? Grab a free 30-minute intro call.</p>
            <a class="btn btn-primary" href="{BOOKING_URL}" target="_blank" rel="noopener noreferrer">Book a 30-min call</a>
          </div>
        </div>
        <form class="card" action="{FORM_ENDPOINT}" method="POST">
          <input type="hidden" name="_subject" value="New inquiry from adamure.com">
          <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
          <label>Name <input type="text" name="name" autocomplete="name" required></label>
          <label>Email <input type="email" name="email" autocomplete="email" required></label>
          <label>Message <textarea name="message" required></textarea></label>
          <button class="btn btn-primary" type="submit">Send message</button>
        </form>
      </div>
    </section>"""


# ---------- Resume (resume/resume.html -> site/resume.pdf) ----------
EXPERIENCE = [
    ("Snifr", "Founding Engineer", "October 2025 – Present", [
        "Build the software for a Wi-Fi-connected e-nose for gut health tracking, now in beta: device connectivity, apps, backend and AI insights.",
        "Ship cross-platform apps with Kotlin Multiplatform on an AWS backend, with server-side Swift services and Python machine learning."]),
    ("Stable Kernel", "Principal Software Engineer", "June 2025 – Present", [
        "Lead technical direction for a greenfield native platform in Swift and SwiftUI, owning architecture, execution and quality standards.",
        "Defined clean architecture patterns, CI/CD quality gates and automated testing strategies that improved delivery consistency and onboarding.",
        "Guide engineers through architectural decisions, tradeoffs and delivery planning; partner with product, design and backend teams."]),
    ("Nevro Corp", "Engineering Team Lead", "January 2023 – May 2025", [
        "Led delivery of compliance-critical mobile features for a regulated medical device platform, shipping releases predictably and at quality.",
        "Architected a multilingual localization and audit pipeline that reduced verification time by ~99.8%.",
        "Served as independent reviewer on firmware projects, ensuring regulatory adherence across the device and software boundary.",
        "Acted as execution lead, coordinating priorities and dependencies with product, QA and regulatory stakeholders."]),
    ("Myia Health", "Lead Mobile Developer", "March 2022 – January 2023", [
        "Architected and unified iOS, Android and Flutter platforms for remote patient care, with consistent patterns for reliability and scale.",
        "Defined CI/CD and TDD workflows that reduced post-release defects by ~15%.",
        "Delivered telemedicine platform components and mentored engineers in clean architecture and SOLID principles."]),
    ("Nike Valiant Labs", "Lead iOS Developer", "November 2021 – March 2022", [
        "Architected workout and run-tracking features with modular, high-performance UIKit components.",
        "Designed the GraphQL data layer with backend engineers, covering schema design, query optimization and error handling."]),
    ("Monovo", "Mobile Experience Architect", "March 2020 – November 2021", [
        "Co-invented a multi-tier Bluetooth cybersecurity framework securing mobile-to-device communication (U.S. Patent No. 12,652,273).",
        "Built the iOS app from scratch and set mobile architecture across iOS and Android; expanded scope to lead backend and web teams."]),
]
STRENGTHS = [
    ("Device connectivity &amp; security", "Bluetooth LE, Wi-Fi devices, secure device communication, sync and firmware-boundary reviews"),
    ("Regulated software", "Compliance-critical delivery under medical device controls"),
    ("Platforms", "Swift, SwiftUI, UIKit, Kotlin Multiplatform, Android, Flutter, REST, GraphQL, server-side Swift (Vapor) and Python on AWS"),
    ("Engineering quality", "TDD, clean architecture, TCA, CI/CD quality gates, predictable releases"),
    ("Leadership", "Technical direction, cross-functional execution and mentorship"),
    ("AI-accelerated delivery", "Claude Certified Architect – Foundations"),
]


def build_resume():
    exp = "\n".join(f"""  <div class="job"><div class="job-head"><h3>{org} <span>— {role}</span></h3><time>{when}</time></div>
    <ul>{"".join(f"<li>{b}</li>" for b in bullets)}</ul></div>""" for org, role, when, bullets in EXPERIENCE)
    strengths = "".join(f"<li><b>{k}:</b> {v}</li>" for k, v in STRENGTHS)
    html = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>{NAME} – Resume</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&family=Lato:wght@400;700&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>
@page {{ size: Letter; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font: 9.1pt/1.36 Lato, sans-serif; color: #0b1f33; }}
header {{ background: #0b1f33; color: #eaf1f8; padding: 0.34in 0.55in 0.26in; display: flex; justify-content: space-between; align-items: flex-end; }}
header h1 {{ font: 700 26pt/1 Poppins, sans-serif; margin: 0 0 6px; letter-spacing: -0.02em; }}
header p {{ margin: 0; font: 600 11pt Poppins, sans-serif; color: #15c2a3; }}
.contact {{ text-align: right; font: 8.4pt/1.6 "JetBrains Mono", monospace; color: #8ea6bd; }}
.contact a {{ color: #eaf1f8; text-decoration: none; }}
main {{ padding: 0.18in 0.55in 0; }}
h2 {{ font: 500 8.5pt "JetBrains Mono", monospace; letter-spacing: 0.14em; text-transform: uppercase; color: #0e8a74; margin: 9px 0 4px; padding-bottom: 3px; border-bottom: 1.5px solid #15c2a3; }}
h3 {{ font: 600 10pt Poppins, sans-serif; margin: 0; }}
h3 span {{ font-weight: 400; font-family: Lato, sans-serif; }}
.job {{ margin-bottom: 4px; break-inside: avoid; }}
.job-head {{ display: flex; justify-content: space-between; align-items: baseline; }}
time {{ font: 8pt "JetBrains Mono", monospace; color: #475b6e; }}
ul {{ margin: 2px 0 0; padding-left: 15px; }} li {{ margin: 1px 0; }}
.strengths {{ columns: 2; column-gap: 0.3in; list-style: none; padding: 0; }} .strengths li {{ break-inside: avoid; margin-bottom: 3px; }}
p.summary {{ margin: 0; }}
.edu div {{ display: flex; justify-content: space-between; }}
</style></head><body>
<header><div><h1>{NAME}</h1><p>{TITLE}</p></div>
<div class="contact"><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="https://adamure.com">adamure.com</a><br>
<a href="https://www.linkedin.com/in/adamqure">linkedin.com/in/adamqure</a><br>{CITY}</div></header>
<main>
<h2>About me</h2><p class="summary">{PROFILE_SHORT}</p>
<h2>Core strengths</h2><ul class="strengths">{strengths}</ul>
<h2>Experience</h2>
{exp}
<h2>Education &amp; certifications</h2>
<div class="edu"><div><span><b>Maryville University</b> — M.S. Software Development</span><time>December 2023</time></div>
<div><span><b>Brigham Young University</b> — B.S. Computer Science</span><time>April 2020</time></div>
<div><span><b>Anthropic</b> — Claude Certified Architect – Foundations</span><time></time></div></div>
</main></body></html>"""
    out = Path(__file__).parent / "resume"
    out.mkdir(exist_ok=True)
    (out / "resume.html").write_text(html)
    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    import subprocess
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--virtual-time-budget=5000", f"--print-to-pdf={SITE / 'resume.pdf'}",
                    (out / "resume.html").as_uri()], check=True, capture_output=True)
    subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=816,1056",
                    "--force-device-scale-factor=2", "--virtual-time-budget=5000",
                    f"--screenshot={SITE / 'images' / 'resume.png'}", (out / "resume.html").as_uri()],
                   check=True, capture_output=True)


FAVICON = LOGO.replace(' aria-hidden="true"', ' xmlns="http://www.w3.org/2000/svg"')

if __name__ == "__main__":
    (SITE / "images").mkdir(parents=True, exist_ok=True)
    (SITE / "images" / "favicon.svg").write_text(FAVICON)
    (SITE / "CNAME").write_text("adamure.com\n")
    page("index.html", "Home", f"{NAME}, {TITLE}. I help hardware teams ship software that pairs reliably, syncs accurately and updates safely.", home)
    page("about.html", "About", f"About {NAME}, {TITLE}.", about)
    page("portfolio.html", "Portfolio", f"Connected-device projects by {NAME}.", portfolio)
    page("contact.html", "Contact", f"Contact {NAME} about your connected-device project.", contact)
    build_resume()
    print("Built:", ", ".join(f for f, _ in PAGES))
