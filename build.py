#!/usr/bin/env python3
"""Generates the 4 pages so header/footer stay identical. Run: python3 build.py"""

# ---- EDIT THESE ----
MARIA_DISPLAY = "(224) 413-1620"
MARIA_TEL = "+12244131620"
VICTOR_DISPLAY = "(224) 637-7971"
VICTOR_TEL = "+12246377971"
EMAIL = "info@example.com"  # TODO: replace with the real business email
# --------------------

# Images are hosted on Higgsfield for now. To self-host, save them into assets/ and change these values to "assets/name.jpg"
IMG_BASE = "https://d8j0ntlcm91z4.cloudfront.net/user_3Gy0O1oJK9nZCQd6ZidORNJu8qM/"
IMG = {
    "hero": "hf_20261017_224734_cab937fd-9fd4-4245-bd66-3b08febd8044.png",
    "install": "hf_20261017_224733_52c04477-a54c-4cf7-95b7-3fb10510652d.png",
    "repair": "hf_20261017_224733_8e12d792-cb5d-4a95-bab0-8cf3d3c41c6f.png",
    "winter": "hf_20261017_224734_baeb9b04-0b1c-424c-b356-33c40e5199c3.png",
    "backyard": "hf_20261017_224732_81fea884-f100-4eeb-8efb-dbd53540cead.png",
    "drip": "hf_20261017_224733_5c8c31fb-71a1-4232-8ace-ff255b1fae7c.png",
    "valves": "hf_20261017_224733_5125b516-0277-4df1-b4f6-b8455aec5f2f.png",
    "sunset": "hf_20261017_224732_8a25df22-9ee4-4938-b3b7-dede5e513336.png",
}
def img(k):
    v = IMG[k]
    return v if v.startswith("assets/") else IMG_BASE + v

SITE = "VC Irrigation"

def drop_svg():
    return '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M12 2s6 6.6 6 11a6 6 0 0 1-12 0c0-4.4 6-11 6-11z"/></svg>'

def head(title, desc, page):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="assets/logo.png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="index.html" aria-label="{SITE} home">
      <img src="assets/logo.png" alt="{SITE} logo" onerror="this.style.display='none';this.nextElementSibling.style.display='inline-flex'">
      <span class="wordmark" style="display:none">{drop_svg()} VC Irrigation</span>
    </a>
    <button class="menu-btn" aria-label="Menu" aria-expanded="false" onclick="var n=document.getElementById('nav');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o)">Menu</button>
    <nav id="nav">
      <a href="index.html"{' class="on"' if page=='home' else ''}>Home</a>
      <a href="services.html"{' class="on"' if page=='services' else ''}>Services</a>
      <a href="faq.html"{' class="on"' if page=='faq' else ''}>FAQ</a>
      <a href="contact.html" class="cta"{' aria-current="page"' if page=='contact' else ''}>Free Estimate</a>
    </nav>
  </div>
</header>
<main>
'''

FOOT = f'''</main>
<footer class="site-footer">
  <div class="wrap cols">
    <div>
      <strong>{SITE}</strong>
      <p>Sprinkler installation, service and repair across the Chicagoland area. Family owned.</p>
    </div>
    <div>
      <strong>Pages</strong>
      <p><a href="index.html">Home</a><br><a href="services.html">Services</a><br><a href="faq.html">FAQ</a><br><a href="contact.html">Contact</a></p>
    </div>
    <div>
      <strong>Contact</strong>
      <p><a href="tel:{MARIA_TEL}">{MARIA_DISPLAY}</a><br><a href="tel:{VICTOR_TEL}">{VICTOR_DISPLAY}</a></p>
    </div>
  </div>
  <div class="wrap small">&copy; <span id="yr"></span> {SITE}. All rights reserved.</div>
</footer>
<script src="site.js"></script>
</body>
</html>
'''


def tick():
    return '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

def hero_bg(k):
    return f'style="background-image:linear-gradient(90deg,rgba(10,40,30,.78),rgba(10,40,30,.35)),url({img(k)})"'

def banner(k, h, p):
    return f'<section class="banner" {hero_bg(k)}><div class="wrap"><h1>{h}</h1><p class="lead">{p}</p></div></section>'

# ---------------- HOME ----------------
def card(k, t, d):
    return f'<article class="card"><div class="ph" style="background-image:url({img(k)})"></div><div class="cb"><h3>{t}</h3><p>{d}</p></div></article>'

home = head(f"{SITE} | Sprinkler Installation, Service & Repair in Chicagoland",
            "Family-owned sprinkler system installation, service, repair and fall winterization serving the Chicagoland area. Free estimates.", "home") + f"""
<section class="notice"><div class="wrap">Winterization season is here. We are booking sprinkler blowouts from mid-October through early November. <a href="contact.html">Schedule yours</a></div></section>

<section class="hero" {hero_bg('hero')}>
  <div class="wrap">
    <p class="eyebrow">Chicagoland sprinkler specialists</p>
    <h1>A greener lawn, without the guesswork.</h1>
    <p class="lead">{SITE} installs, services and repairs sprinkler systems for homeowners across the Chicago area. Honest advice, fair pricing and work we stand behind.</p>
    <p class="btns"><a class="btn primary" href="contact.html">Get a free estimate</a> <a class="btn ghost" href="tel:{MARIA_TEL}">Call us</a></p>
  </div>
</section>

<section class="trust">
  <div class="wrap trio">
    <div>{tick()}<h3>Family owned</h3><p>You deal with the people doing the work, not a call center.</p></div>
    <div>{tick()}<h3>Straight answers</h3><p>We tell you what your system needs, and what it does not.</p></div>
    <div>{tick()}<h3>Built to last</h3><p>Proper zoning, quality parts and clean installs.</p></div>
  </div>
</section>

<section class="wrap section">
  <p class="eyebrow">What we do</p>
  <h2>Everything your sprinkler system needs</h2>
  <div class="cards">
    {card('install','New system installation','Custom layout designed around your lawn, beds and water pressure.')}
    {card('repair','Service and repair','Broken heads, leaks, stuck valves and timer problems fixed fast.')}
    {card('backyard','Spring startup','We wake your system up, check every zone and adjust coverage.')}
    {card('winter','Fall winterization','Compressed air blowout to clear the lines before freezing weather.')}
  </div>
  <p class="center"><a class="btn" href="services.html">See all services</a></p>
</section>

<section class="split">
  <div class="wrap split-grid">
    <img src="{img('drip')}" alt="Drip irrigation running through a garden bed" loading="lazy">
    <div>
      <p class="eyebrow">Beyond the lawn</p>
      <h2>Gardens and beds need water too</h2>
      <p>We can add drip zones for flower beds and gardens, set up smart controllers and rain sensors, and expand an older system when your landscaping changes.</p>
      <ul class="ticks"><li>Drip zones for beds and gardens</li><li>Smart controllers and rain sensors</li><li>Extra zones for new landscaping</li></ul>
    </div>
  </div>
</section>

<section class="wrap section">
  <p class="eyebrow">Simple process</p>
  <h2>How it works</h2>
  <ol class="steps">
    <li><span>1</span><div><strong>Tell us about your yard</strong><p>Call, text or send the quick form.</p></div></li>
    <li><span>2</span><div><strong>Free estimate</strong><p>We look at the property and give you a clear price.</p></div></li>
    <li><span>3</span><div><strong>We get it done</strong><p>Scheduled work, tidy site, and a walkthrough when we finish.</p></div></li>
  </ol>
</section>

<section class="wrap section" id="work" hidden>
  <p class="eyebrow">Our work</p><h2>Recent projects</h2>
  <div class="gallery" id="gallery"></div>
</section>

<section class="cta-band" style="background-image:linear-gradient(135deg,rgba(20,70,45,.88),rgba(20,87,127,.85)),url({img('sunset')})">
  <div class="wrap"><h2>Ready for a system that just works?</h2><p>Tell us about your property and we will get back to you.</p><a class="btn light" href="contact.html">Request a free estimate</a></div>
</section>
""" + FOOT

# ---------------- SERVICES ----------------
def svc(k, title, body, items, flip=False):
    li = "".join(f"<li>{i}</li>" for i in items)
    return f'<article class="svc{" flip" if flip else ""}"><img src="{img(k)}" alt="{title}" loading="lazy"><div><h2>{title}</h2><p>{body}</p><ul class="ticks">{li}</ul></div></article>'

services = head(f"Services | {SITE}",
                "Sprinkler installation, repair, spring startup and fall winterization across Chicagoland.", "services") + f"""
{banner('install','Our services','Everything your sprinkler system needs, from the first trench to the last blowout.')}
<section class="wrap section services">
{svc('install','New system installation','We design the system around your yard instead of forcing a template onto it.',['Layout and zone design for lawn and planting beds','Head and nozzle selection for even coverage','Controller setup and a walkthrough on how to use it','Clean install with the lawn restored'])}
{svc('repair','Service and repair','Something not working right? We find the cause and fix it properly.',['Broken or misaligned heads and nozzles','Leaks, low pressure and zones that will not turn on','Valve and wiring troubleshooting','Timer and controller replacement'],True)}
{svc('backyard','Spring startup','A quick check in spring catches small problems before they cost you a dry summer.',['Turn the system on and test every zone','Look for leaks and damaged heads','Adjust spray patterns and program the schedule'])}
{svc('winter','Fall winterization','In our climate the frost goes deeper than the pipes. Water left inside can freeze and crack lines, valves and heads.',['Compressed air blowout of every zone','Shut down and drain the system','Controller set to rain mode for winter','Best done before temperatures stay below freezing'],True)}
{svc('drip','Upgrades and add-ons','Make an older system more efficient.',['Smart controllers and rain sensors','Drip zones for gardens and beds','Adding zones for new landscaping'])}
</section>
<section class="cta-band" style="background-image:linear-gradient(135deg,rgba(20,70,45,.88),rgba(20,87,127,.85)),url({img('sunset')})"><div class="wrap"><h2>Not sure what you need?</h2><p>Describe the problem and we will point you in the right direction.</p><a class="btn light" href="contact.html">Contact us</a></div></section>
""" + FOOT

# ---------------- FAQ ----------------
groups = [
 ("Winterization", [
  ("When should I winterize my sprinkler system?", "Before temperatures stay below freezing. In the Chicago area that is usually mid-October through early November. Ground temperature drops slower than air temperature, so there is a window, but do not wait for the first hard freeze."),
  ("What is a sprinkler blowout?", "We connect an air compressor to your system and push the water out of the pipes, valves and heads, one zone at a time. It protects everything from freeze damage."),
  ("How long does it take?", "Usually a short visit. Most homes take well under an hour, depending on how many zones you have."),
  ("Do I need to be home?", "Usually not, as long as we can reach the controller and shutoff. We will confirm access when we schedule."),
  ("What happens if I skip it?", "Water can freeze and expand inside the system, cracking pipes, valves and heads. You often find out in spring when the repair bill shows up."),
 ]),
 ("Estimates and service", [
  ("Do you offer free estimates?", "Yes. Contact us and we will set up a time to look at your property."),
  ("What areas do you serve?", "The Chicagoland area. Send us your town and we will confirm we can get to you."),
  ("My sprinkler head is broken or a zone will not turn on. Can you fix it?", "Yes. Repair is a big part of what we do. Tell us what you are seeing when you contact us."),
  ("Do I need a backflow test?", "Many towns require backflow preventer testing on irrigation systems. Requirements vary by municipality, so check with your village or ask us when you book."),
 ]),
 ("New installation", [
  ("How long does an installation take?", "Most residential systems take a few days depending on yard size and layout. We will give you a clear timeline with your estimate."),
 ]),
]
fq = ""
n = 0
for g, items in groups:
    fq += f'<h2 class="gh">{g}</h2>'
    for q, a in items:
        n += 1
        fq += f'<details{" open" if n==1 else ""}><summary><span class="q">{q}</span></summary><div class="ans"><p>{a}</p></div></details>'
faq = head(f"FAQ | {SITE}", "Answers about sprinkler winterization, repair, installation and estimates in Chicagoland.", "faq") + f"""
{banner('winter','Frequently asked questions','Quick answers to what homeowners ask us most.')}
<section class="wrap section faq-grid">
  <div class="faqs">{fq}</div>
  <aside class="side">
    <img src="{img('winter')}" alt="Frost covered sprinkler head" loading="lazy">
    <h3>Still have a question?</h3>
    <p>Call or text us, or send a quick message and we will get back to you.</p>
    <p><a class="btn primary" href="contact.html">Ask us</a></p>
    <p><a href="tel:{MARIA_TEL}">Call us</a></p>
  </aside>
</section>
""" + FOOT

# ---------------- CONTACT ----------------
contact = head(f"Contact | {SITE}", "Request a free sprinkler estimate or schedule winterization with VC Irrigation.", "contact") + f"""
{banner('backyard','Get a free estimate','Call, text, or send the form and we will get back to you.')}
<section class="wrap section contact-grid">
  <form id="contact-form" class="form">
    <label>Name<input name="name" required autocomplete="name"></label>
    <label>Phone<input name="phone" type="tel" required autocomplete="tel"></label>
    <label>Email<input name="email" type="email" autocomplete="email"></label>
    <label>Town or ZIP<input name="town" required></label>
    <label>What do you need?
      <select name="service">
        <option>Free estimate (new system)</option>
        <option>Repair</option>
        <option>Fall winterization</option>
        <option>Spring startup</option>
        <option>Something else</option>
      </select>
    </label>
    <label>Details<textarea name="msg" rows="5"></textarea></label>
    <button class="btn primary" type="submit">Send request</button>
    <p class="muted small">This opens your email app with the message filled in.</p>
  </form>
  <aside class="info">
    <h2>Reach us directly</h2>
    <p><strong>Call or text</strong><br><a href="tel:{MARIA_TEL}">{MARIA_DISPLAY}</a><br><a href="tel:{VICTOR_TEL}">{VICTOR_DISPLAY}</a></p>
    <p><strong>Service area</strong><br>Chicagoland</p>
    <p><strong>Winterization</strong><br>Booking now through early November.</p>
  </aside>
</section>
""" + FOOT

for name, html in [("index", home), ("services", services), ("faq", faq), ("contact", contact)]:
    open(f"/home/claude/vc-irrigation/{name}.html", "w").write(html)

# JS
open("/home/claude/vc-irrigation/site.js", "w").write(f'''document.getElementById("yr").textContent = new Date().getFullYear();

// Gallery: list your project photos here (put files in assets/). Empty slots show a placeholder.
var PHOTOS = [
  // {{ src: "assets/project1.jpg", alt: "New front yard sprinkler install" }},
];
(function () {{
  var g = document.getElementById("gallery");
  if (!g || !PHOTOS.length) return;
  document.getElementById("work").hidden = false;
  var n = PHOTOS.length;
  for (var i = 0; i < n; i++) {{
    var d = document.createElement("div");
    d.className = "shot";
    if (PHOTOS[i]) {{
      var im = document.createElement("img");
      im.src = PHOTOS[i].src; im.alt = PHOTOS[i].alt || "Sprinkler project"; im.loading = "lazy";
      d.appendChild(im);
    }} else {{
      d.className += " empty"; d.textContent = "Project photo";
    }}
    g.appendChild(d);
  }}
}})();

var f = document.getElementById("contact-form");
if (f) f.addEventListener("submit", function (e) {{
  e.preventDefault();
  var v = function (k) {{ return f.elements[k].value; }};
  var body = "Name: " + v("name") + "\\nPhone: " + v("phone") + "\\nEmail: " + v("email") +
             "\\nTown/ZIP: " + v("town") + "\\nService: " + v("service") + "\\n\\n" + v("msg");
  location.href = "mailto:{EMAIL}?subject=" + encodeURIComponent("Estimate request: " + v("service")) +
                  "&body=" + encodeURIComponent(body);
}});
''')

open("/home/claude/vc-irrigation/style.css", "w").write('''
:root{--green:#2f8a3e;--green-d:#1f6a2d;--blue:#1d78b5;--blue-d:#14577f;--ink:#1c2a33;--muted:#5a6b76;--bg:#fff;--soft:#f2f8f3;--line:#dbe6dd}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font:17px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--ink);background:var(--bg)}
img{max-width:100%}
a{color:var(--blue)}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
.section{padding:56px 20px}
.narrow{max-width:780px}
.center{text-align:center}
.muted{color:var(--muted)}
.small{font-size:14px}
h1,h2,h3{line-height:1.2;margin:0 0 .5em}
h1{font-size:clamp(2rem,5vw,3.2rem)}
h2{font-size:clamp(1.5rem,3vw,2rem)}
.lead{font-size:1.15rem;color:var(--muted);max-width:620px}
.eyebrow{color:var(--green-d);font-weight:700;text-transform:uppercase;letter-spacing:.08em;font-size:.8rem;margin:0 0 .6em}

.site-header{position:sticky;top:0;z-index:10;background:#fff;border-bottom:1px solid var(--line)}
.bar{display:flex;align-items:center;justify-content:space-between;min-height:68px;gap:16px}
.brand{display:flex;align-items:center;text-decoration:none;color:var(--ink)}
.brand img{height:58px;width:auto}
.wordmark{align-items:center;gap:6px;font-weight:800;font-size:1.3rem;color:var(--blue-d)}
nav{display:flex;gap:6px;align-items:center}
nav a{padding:8px 12px;border-radius:8px;text-decoration:none;color:var(--ink);font-weight:600}
nav a:hover,nav a.on{background:var(--soft)}
nav a.cta{background:var(--green);color:#fff}
nav a.cta:hover{background:var(--green-d)}
.menu-btn{display:none;background:none;border:1px solid var(--line);border-radius:8px;padding:8px 14px;font:inherit;font-weight:600}
@media(max-width:760px){
  .menu-btn{display:block}
  nav{display:none;position:absolute;left:0;right:0;top:100%;background:#fff;border-bottom:1px solid var(--line);flex-direction:column;align-items:stretch;padding:10px 20px}
  nav.open{display:flex}
}

.notice{background:var(--blue-d);color:#fff;text-align:center;padding:10px 0;font-size:.95rem}
.notice a{color:#fff;font-weight:700}

.hero{background:linear-gradient(180deg,#eef8fc,#fff);padding:56px 0 40px}
.hero-grid{display:grid;grid-template-columns:1.1fr 1fr;gap:32px;align-items:center}
.hero-art{width:100%;height:auto;border-radius:18px;box-shadow:0 10px 30px rgba(20,87,127,.15)}
@media(max-width:820px){.hero-grid{grid-template-columns:1fr}}
.btns{display:flex;gap:12px;flex-wrap:wrap;margin-top:24px}
.btn{display:inline-block;padding:12px 22px;border-radius:10px;border:2px solid var(--blue);color:var(--blue-d);font-weight:700;text-decoration:none;background:#fff;cursor:pointer;font-size:1rem}
.btn:hover{background:var(--soft)}
.btn.primary{background:var(--green);border-color:var(--green);color:#fff}
.btn.primary:hover{background:var(--green-d)}
.btn.light{background:#fff;border-color:#fff;color:var(--green-d)}

.band{background:var(--soft);padding:36px 0}
.band.alt{background:#fff;padding:56px 0}
.trio{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
@media(max-width:760px){.trio{grid-template-columns:1fr}}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:18px;margin:20px 0 28px}
.card{border:1px solid var(--line);border-radius:14px;padding:22px;background:#fff}
.card h3{color:var(--green-d)}
.steps{padding-left:1.2em;display:grid;gap:12px;max-width:700px}

.gallery{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px;margin-top:20px}
.shot{aspect-ratio:4/3;border-radius:12px;overflow:hidden;background:var(--soft)}
.shot img{width:100%;height:100%;object-fit:cover;display:block}
.shot.empty{display:flex;align-items:center;justify-content:center;border:2px dashed var(--line);color:var(--muted);font-size:.9rem}

.cta-band{background:linear-gradient(135deg,var(--green-d),var(--blue-d));color:#fff;text-align:center;padding:56px 0}
.cta-band p{opacity:.9}

.page-title{background:var(--soft);padding:44px 0 36px}
.page-title .lead{margin:0}
.services{display:grid;gap:22px}
.svc{border:1px solid var(--line);border-radius:14px;padding:26px}
.svc h2{color:var(--green-d);font-size:1.4rem}
.ticks{list-style:none;padding:0;margin:12px 0 0}
.ticks li{padding-left:26px;position:relative;margin:6px 0}
.ticks li:before{content:"";position:absolute;left:0;top:.55em;width:14px;height:8px;border-left:3px solid var(--green);border-bottom:3px solid var(--green);transform:rotate(-45deg) translateY(-50%)}

details{border:1px solid var(--line);border-radius:12px;padding:0 18px;margin:12px 0;background:#fff}
summary{cursor:pointer;font-weight:700;padding:16px 0;list-style:none}
summary::-webkit-details-marker{display:none}
summary:after{content:"+";float:right;color:var(--green-d);font-size:1.3rem}
details[open] summary:after{content:"\\2212"}
details p{margin:0 0 16px;color:var(--muted)}

.contact-grid{display:grid;grid-template-columns:1.4fr 1fr;gap:36px;align-items:start}
@media(max-width:820px){.contact-grid{grid-template-columns:1fr}}
.form{display:grid;gap:14px}
.form label{display:grid;gap:6px;font-weight:600;font-size:.95rem}
.form input,.form select,.form textarea{font:inherit;padding:11px 12px;border:1px solid #b9c9bd;border-radius:9px;background:#fff}
.form input:focus,.form select:focus,.form textarea:focus{outline:3px solid #bfe3c5;border-color:var(--green)}
.info{background:var(--soft);border-radius:14px;padding:24px}

.site-footer{background:#14262e;color:#cfdce2;padding:40px 0 20px;margin-top:0}
.site-footer a{color:#fff}
.cols{display:grid;grid-template-columns:2fr 1fr 1fr;gap:24px}
@media(max-width:760px){.cols{grid-template-columns:1fr}}
.site-footer .small{margin-top:24px;opacity:.7}

/* ---- v2: imagery ---- */
.hero,.banner,.cta-band{background-size:cover;background-position:center}
.hero{padding:120px 0 110px;color:#fff}
.hero h1{max-width:680px;text-shadow:0 2px 14px rgba(0,0,0,.35)}
.hero .lead{color:#eaf3ee;max-width:560px}
.hero .eyebrow,.banner .eyebrow{color:#a9e3b3}
.banner{padding:80px 0 70px;color:#fff}
.banner .lead{color:#eaf3ee;margin:0}
.btn.ghost{background:rgba(255,255,255,.12);border-color:#fff;color:#fff}
.btn.ghost:hover{background:rgba(255,255,255,.25)}
.btn{transition:transform .15s,box-shadow .15s}
.btn:hover{transform:translateY(-1px);box-shadow:0 6px 16px rgba(0,0,0,.12)}
.trust{background:#fff;border-bottom:1px solid var(--line);padding:30px 0}
.trust .trio>div{display:grid;grid-template-columns:auto 1fr;column-gap:12px}
.trust svg{grid-row:span 2;color:#fff;background:var(--green);border-radius:50%;padding:7px;width:38px;height:38px}
.trust h3{margin:0;font-size:1.05rem}
.trust p{margin:0;color:var(--muted);font-size:.95rem}
.card{padding:0;overflow:hidden;box-shadow:0 2px 10px rgba(20,60,40,.06);transition:transform .2s,box-shadow .2s}
.card:hover{transform:translateY(-4px);box-shadow:0 12px 26px rgba(20,60,40,.14)}
.card .ph{aspect-ratio:3/2;background-size:cover;background-position:center}
.card .cb{padding:18px 20px 22px}
.card .cb p{margin:0;color:var(--muted);font-size:.97rem}
.split{background:var(--soft);padding:64px 0}
.split-grid{display:grid;grid-template-columns:1fr 1fr;gap:44px;align-items:center}
.split-grid img{width:100%;border-radius:18px;box-shadow:0 14px 34px rgba(20,60,40,.2);aspect-ratio:3/2;object-fit:cover}
@media(max-width:820px){.split-grid{grid-template-columns:1fr}}
.steps{list-style:none;padding:0;max-width:none;grid-template-columns:repeat(3,1fr);gap:20px}
.steps li{display:flex;gap:14px;align-items:flex-start;border:1px solid var(--line);border-radius:14px;padding:20px;background:#fff}
.steps li>span{flex:none;width:38px;height:38px;border-radius:50%;background:var(--green);color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center}
.steps p{margin:4px 0 0;color:var(--muted)}
@media(max-width:820px){.steps{grid-template-columns:1fr}}
.cta-band{padding:76px 0}
.eyebrow{margin-bottom:.4em}
.services{display:grid;gap:56px}
.svc{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;border:none;padding:0}
.svc img{width:100%;border-radius:18px;aspect-ratio:3/2;object-fit:cover;box-shadow:0 12px 30px rgba(20,60,40,.18)}
.svc.flip img{order:2}
@media(max-width:820px){.svc{grid-template-columns:1fr;gap:20px}.svc.flip img{order:0}}
.faq-grid{display:grid;grid-template-columns:1.6fr 1fr;gap:40px;align-items:start}
@media(max-width:900px){.faq-grid{grid-template-columns:1fr}}
.gh{font-size:1.15rem;color:var(--green-d);margin:30px 0 4px;text-transform:uppercase;letter-spacing:.06em}
.gh:first-child{margin-top:0}
details{border:1px solid var(--line);border-left:4px solid var(--line);border-radius:12px;padding:0 20px;margin:12px 0;background:#fff;box-shadow:0 1px 6px rgba(20,60,40,.05);transition:border-color .2s,box-shadow .2s}
details[open]{border-left-color:var(--green);box-shadow:0 8px 22px rgba(20,60,40,.1)}
summary{padding:18px 0}
summary:after{content:"+";width:30px;height:30px;border-radius:50%;background:var(--soft);display:inline-flex;align-items:center;justify-content:center;float:right;margin-left:12px;color:var(--green-d);font-size:1.3rem;line-height:1}
details[open] summary:after{content:"\2212";background:var(--green);color:#fff}
.ans p{margin:0 0 18px;color:var(--muted)}
.side{position:sticky;top:90px;background:var(--soft);border-radius:18px;padding:22px;border:1px solid var(--line)}
.side img{width:100%;border-radius:12px;aspect-ratio:3/2;object-fit:cover;margin-bottom:14px}
.side h3{margin-bottom:6px}
''')
print("built")
