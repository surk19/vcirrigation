#!/usr/bin/env python3
"""Generates the 4 pages so header/footer stay identical. Run: python3 build.py"""

# ---- EDIT THESE ----
MARIA_DISPLAY = "(224) 413-1620"
MARIA_TEL = "+12244131620"
VICTOR_DISPLAY = "(224) 637-7971"
VICTOR_TEL = "+12246377971"
EMAIL = "info@example.com"  # TODO: replace with the real business email
# --------------------

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
      <p>Maria: <a href="tel:{MARIA_TEL}">{MARIA_DISPLAY}</a><br>Victor: <a href="tel:{VICTOR_TEL}">{VICTOR_DISPLAY}</a></p>
    </div>
  </div>
  <div class="wrap small">&copy; <span id="yr"></span> {SITE}. All rights reserved.</div>
</footer>
<script src="site.js"></script>
</body>
</html>
'''

def yard_svg():
    return '''<svg class="hero-art" viewBox="0 0 600 380" role="img" aria-label="Lawn sprinkler watering a green yard">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfeaf7"/><stop offset="1" stop-color="#eef8fc"/></linearGradient>
    <linearGradient id="grass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5fb15a"/><stop offset="1" stop-color="#2f8a3e"/></linearGradient>
  </defs>
  <rect width="600" height="380" fill="url(#sky)"/>
  <circle cx="500" cy="70" r="34" fill="#ffe28a"/>
  <path d="M0 230 Q150 190 300 225 T600 215 V380 H0z" fill="url(#grass)"/>
  <g fill="none" stroke="#3aa0d8" stroke-width="3" stroke-linecap="round" opacity=".85">
    <path d="M300 250 Q240 150 160 215"/><path d="M300 250 Q270 130 215 205"/>
    <path d="M300 250 Q300 120 300 200"/><path d="M300 250 Q330 130 385 205"/><path d="M300 250 Q360 150 440 215"/>
  </g>
  <g fill="#3aa0d8" opacity=".8"><circle cx="160" cy="218" r="4"/><circle cx="215" cy="208" r="4"/><circle cx="300" cy="203" r="4"/><circle cx="385" cy="208" r="4"/><circle cx="440" cy="218" r="4"/></g>
  <rect x="294" y="248" width="12" height="22" rx="3" fill="#33414a"/>
  <rect x="289" y="266" width="22" height="8" rx="3" fill="#1f2a30"/>
  <g transform="translate(60 150)"><rect x="0" y="40" width="90" height="70" fill="#e9dfd0"/><path d="M-8 44 L45 0 L98 44z" fill="#b5533c"/><rect x="36" y="68" width="18" height="42" fill="#7a5a3a"/></g>
</svg>'''

# ---------------- HOME ----------------
home = head(f"{SITE} | Sprinkler Installation, Service & Repair in Chicagoland",
            "Family-owned sprinkler system installation, service, repair and fall winterization serving the Chicagoland area. Free estimates.", "home") + f'''
<section class="notice">
  <div class="wrap">Winterization season is here. We are booking sprinkler blowouts from mid-October through early November. <a href="contact.html">Schedule a blowout</a></div>
</section>

<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="eyebrow">Chicagoland sprinkler specialists</p>
      <h1>A greener lawn, without the guesswork.</h1>
      <p class="lead">{SITE} installs, services and repairs sprinkler systems for homeowners across the Chicago area. Honest advice, fair pricing and work we stand behind.</p>
      <p class="btns"><a class="btn primary" href="contact.html">Get a free estimate</a> <a class="btn" href="tel:{MARIA_TEL}">Call Maria</a> <a class="btn" href="tel:{VICTOR_TEL}">Call Victor</a></p>
    </div>
    {yard_svg()}
  </div>
</section>

<section class="band">
  <div class="wrap trio">
    <div><h3>Family owned</h3><p>You deal directly with the people doing the work, not a call center.</p></div>
    <div><h3>Straight answers</h3><p>We tell you what your system needs and what it does not.</p></div>
    <div><h3>Built to last</h3><p>Proper zoning, quality parts and clean installs for your yard and water pressure.</p></div>
  </div>
</section>

<section class="wrap section">
  <h2>What we do</h2>
  <div class="cards">
    <article class="card"><h3>New system installation</h3><p>Custom layout designed around your lawn, beds and water pressure.</p></article>
    <article class="card"><h3>Service and repair</h3><p>Broken heads, leaks, stuck valves and timer problems fixed fast.</p></article>
    <article class="card"><h3>Spring startup</h3><p>We wake your system up, check every zone and adjust coverage.</p></article>
    <article class="card"><h3>Fall winterization</h3><p>Compressed air blowout to clear the lines before freezing weather.</p></article>
  </div>
  <p class="center"><a class="btn" href="services.html">See all services</a></p>
</section>

<section class="band alt">
  <div class="wrap">
    <h2>How it works</h2>
    <ol class="steps">
      <li><strong>Tell us about your yard.</strong> Call or send the quick form.</li>
      <li><strong>Free estimate.</strong> We look at the property and give you a clear price.</li>
      <li><strong>We get it done.</strong> Scheduled work, tidy site, and a walkthrough when we finish.</li>
    </ol>
  </div>
</section>

<section class="wrap section">
  <h2>Recent work</h2>
  <p class="muted">Real projects from around Chicagoland.</p>
  <div class="gallery" id="gallery"></div>
</section>

<section class="cta-band">
  <div class="wrap">
    <h2>Ready for a system that just works?</h2>
    <p>Tell us about your property and we will get back to you.</p>
    <a class="btn light" href="contact.html">Request a free estimate</a>
  </div>
</section>
''' + FOOT

# ---------------- SERVICES ----------------
def svc(title, body, items):
    li = "".join(f"<li>{i}</li>" for i in items)
    return f'<article class="svc"><h2>{title}</h2><p>{body}</p><ul class="ticks">{li}</ul></article>'

services = head(f"Services | {SITE}",
                "Sprinkler installation, repair, spring startup and fall winterization across Chicagoland.", "services") + f'''
<section class="page-title"><div class="wrap"><h1>Our services</h1><p class="lead">Everything your sprinkler system needs, from the first trench to the last blowout.</p></div></section>
<section class="wrap section services">
{svc("New system installation", "We design the system around your yard instead of forcing a template onto it.", ["Layout and zone design for lawn and planting beds", "Head and nozzle selection for even coverage", "Controller setup and a walkthrough on how to use it", "Clean install with the lawn restored"])}
{svc("Service and repair", "Something not working right? We find the cause and fix it properly.", ["Broken or misaligned heads and nozzles", "Leaks, low pressure and zones that will not turn on", "Valve and wiring troubleshooting", "Timer and controller replacement"])}
{svc("Spring startup", "A quick check in spring catches small problems before they cost you a dry summer.", ["Turn the system on and test every zone", "Look for leaks and damaged heads", "Adjust spray patterns and program the schedule"])}
{svc("Fall winterization", "In our climate the frost goes deeper than the pipes. Water left inside can freeze and crack lines, valves and heads.", ["Compressed air blowout of every zone", "Shut down and drain the system", "Controller set to rain mode for winter", "Best done before temperatures stay below freezing"])}
{svc("Upgrades and add-ons", "Make an older system more efficient.", ["Smart controllers and rain sensors", "Drip zones for gardens and beds", "Adding zones for new landscaping"])}
</section>
<section class="cta-band"><div class="wrap"><h2>Not sure what you need?</h2><p>Describe the problem and we will point you in the right direction.</p><a class="btn light" href="contact.html">Contact us</a></div></section>
''' + FOOT

# ---------------- FAQ ----------------
faqs = [
 ("When should I winterize my sprinkler system?", "Before temperatures stay below freezing. In the Chicago area that usually means October through early November, but ground temperature drops slower than air temperature, so there is a window. Do not wait for the first hard freeze."),
 ("What is a sprinkler blowout?", "We connect an air compressor to your system and push the water out of the pipes, valves and heads, one zone at a time. It protects everything from freeze damage."),
 ("How long does winterization take?", "Usually a short visit. Most homes take well under an hour, depending on how many zones you have."),
 ("Do I need to be home?", "Usually not, as long as we can reach the controller and shutoff. We will confirm access when we schedule."),
 ("What happens if I skip winterization?", "Water can freeze and expand inside the system, cracking pipes, valves and sprinkler heads. You often find out in spring when the repair bill shows up."),
 ("Do you offer free estimates?", "Yes. Contact us and we will set up a time to look at your property."),
 ("What areas do you serve?", "The Chicagoland area. Reach out with your town and we will confirm we can get to you."),
 ("How long does a new installation take?", "Most residential systems take a few days depending on yard size and layout. We will give you a clear timeline with your estimate."),
 ("My sprinkler head is broken or a zone will not turn on. Can you fix it?", "Yes. Repair is a big part of what we do. Tell us what you are seeing when you contact us."),
 ("Do I need a backflow test?", "Many towns require backflow preventer testing on irrigation systems. Requirements vary by municipality, so check with your village or ask us when you book."),
]
fq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)
faq = head(f"FAQ | {SITE}", "Answers about sprinkler winterization, repair, installation and estimates in Chicagoland.", "faq") + f'''
<section class="page-title"><div class="wrap"><h1>Frequently asked questions</h1><p class="lead">Quick answers to what homeowners ask us most.</p></div></section>
<section class="wrap section narrow">
{fq}
<p class="center muted">Do not see your question? <a href="contact.html">Ask us</a>.</p>
</section>
''' + FOOT

# ---------------- CONTACT ----------------
contact = head(f"Contact | {SITE}", "Request a free sprinkler estimate or schedule winterization with VC Irrigation.", "contact") + f'''
<section class="page-title"><div class="wrap"><h1>Get a free estimate</h1><p class="lead">Call, email, or send the form and we will get back to you.</p></div></section>
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
    <p><strong>Call or text</strong><br>Maria: <a href="tel:{MARIA_TEL}">{MARIA_DISPLAY}</a><br>Victor: <a href="tel:{VICTOR_TEL}">{VICTOR_DISPLAY}</a></p>
    <p><strong>Service area</strong><br>Chicagoland</p>
  </aside>
</section>
''' + FOOT

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
  if (!g) return;
  var n = Math.max(PHOTOS.length, 6);
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
''')
print("built")
