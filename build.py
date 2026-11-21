import html
from icons import svg as _isvg, name as _iname
E = html.escape
OUT = '/home/claude/site/'

FONTS = '<link rel="preload" href="fonts/archivo-latin-wdth-normal.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="fonts/schibsted-grotesk-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>'
NAV = [('index.html', 'Home'), ('work.html', 'Work'), ('ugc.html', 'UGC playbook'), ('playbook.html', 'How I run a team'), ('about.html', 'About')]

def ico(k): return f'<span class="ico" title="{E(_iname(k))}">{_isvg(k)}</span>'
def stack(keys): return '<div class="stack">' + ''.join(ico(k) for k in keys) + '</div>'
def tool(k): return f'<div class="tool">{ico(k)}<span>{E(_iname(k))}</span></div>'

import hashlib
def _v(p): return hashlib.md5(open(OUT + p, 'rb').read()).hexdigest()[:8]

def page(fn, title, body, extra_css=''):
    nav = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == fn or (fn.startswith("work-") and h == "work.html") else ""}>{t}</a>' for h, t in NAV)
    doc = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="Amirthashree Vijayakumar: creative and marketing operations for UGC ads. 40+ campaigns, 11 brands, based in Dubai.">
{FONTS}<link rel="stylesheet" href="css/site.css?v={_v("css/site.css")}">{f"<style>{extra_css}</style>" if extra_css else ""}</head>
<body>
<header class="nav"><div class="wrap"><a class="logo" href="index.html"><i>AV</i>Amirthashree<em>Open to work · Dubai</em></a><nav aria-label="Main">{nav}</nav></div></header>
<main>{body}</main>
<footer class="foot"><div class="wrap"><div class="row">
<h2>Got a team<br>that needs this?</h2>
<p>+971 50 807 0510<br>amirthashreevijayakumar@gmail.com<br><a href="https://www.linkedin.com/in/amirthashree-vijayakumar">linkedin.com/in/amirthashree-vijayakumar</a><br><a href="resume.pdf">Download my resume (PDF)</a></p>
</div><small>Ads shown were produced by the VideoForce (Cipio.ai) team for its clients, 2025–2026, where I led creative operations: casting, briefs, scripts, compliance, editor direction and delivery.</small></div></footer>
<script src="js/site.js?v={_v("js/site.js")}"></script></body></html>'''
    open(OUT + fn, 'w').write(doc)

def ph(clip, title, sub='', cls=''):
    return f'<figure class="ph {cls}"><div class="frame"><video muted loop playsinline preload="none" poster="v/{clip}.jpg" src="v/{clip}.mp4"></video><button class="snd" type="button" tabindex="-1">Sound off</button></div><figcaption><b>{E(title)}</b><span>{E(sub)}</span></figcaption></figure>'

CASES = [
 dict(stack=['monday','frameio','drive','claude','instagram','tiktok'], fn='work-alcon.html', color='var(--cobalt)', ink='#fff', tag='Pharma · Eye care', name='Alcon',
  title='Compliant ads that sound like people', hook='Most compliant ads sound like a label read out loud. Ours sounded like friends talking about their eyes.',
  pills=['Pataday', 'Systane', 'Opti-Free', 'Clear Care', 'Precision1', 'MAP approvals', 'Veeva codes'],
  hero='pataday-onedrop',
  beats=[('The brief', 'A monthly flow of UGC ads for four eye-care lines. Every claim cleared by medical, legal and regulatory. Every creator with signed consent.'),
         ('The idea', 'Two voices in one ad. Everyday users talk about the moment of relief; eye doctors give the expert reason why.'),
         ('The moves', 'Rewrote each creator\'s own story into a compliant script. Made a standalone verbal disclosure a default ask. Never let the product sit beside a "problem" line.'),
         ('What changed', 'Legal feedback became standing rules, so the same rejection never had to be learned twice. Status updates went from hours of copying to seconds.')],
  clips=[('pataday-onedrop', 'Pataday · Mashup', 'Three creators, one approved body'), ('systane-pocket', 'Systane · UGC', 'An everyday dry-eye moment'), ('pataday-versus', 'Pataday · Comparison', 'Product kept away from the problem'), ('precision1-walmart', 'Precision1 · Walmart', 'In-store B-roll by script beat'), ('pataday-comfort', 'Pataday · Why Pataday', 'Amazon PDP version')],
  wide=('clearcare-doctor', 'Clear Care · Eye-doctor film', 'The expert voice, in a MAP-approved script.')),
 dict(stack=['monday','docs','slack','drive','tiktok','instagram'], fn='work-autotrader.html', color='var(--tomato)', ink='#fff', tag='Automotive · Cox Automotive', name='Autotrader & KBB',
  title="Don't argue with the doubt. Cast it.", hook='People hesitate before buying a car online. So we built the ads out of that hesitation.',
  pills=['Autotrader', 'Kelley Blue Book', '10 personas', '11 angles', '6 brief rounds', 'Weekly syncs'],
  hero='autotrader-really',
  beats=[('The brief', 'UGC ads for buying a car fully online, a decision that makes people nervous.'),
         ('The idea', 'Cast against the cliché. Instead of "busy mom", ten specific buyer types and eleven angles that start from doubt.'),
         ('The moves', 'The confession hook: "I closed the tab three times." A reverse-chronology opening that starts with keys in hand. Three ad sets mapped to transparency, education and ease.'),
         ('What changed', 'A full month delivered on target and a persona library the team reused for later briefs.')],
  clips=[('autotrader-really', 'Autotrader · Buy online', '15-second delivery cut'), ('cox-sellmycar', 'KBB · Sell my car', '"How much is my car actually worth?"'), ('cox-buyonline', 'Autotrader · Buy online', 'Hook variation'), ('cox-mashup', 'Autotrader · Mashup', 'Lines from several real buyers'), ('kbb-15', 'KBB · For all your car its', 'Brand spot')]),
 dict(stack=['monday','drive','gmail','instagram','tiktok'], fn='work-buildabear.html', color='var(--sun)', ink='var(--ink)', tag='Retail · Gifting', name='Build-A-Bear',
  title='The fix that stops the mistake twice', hook='When licensed toys showed up in our shots, the easy move was blaming creators. The real gap was ours.',
  pills=['Up to 18 ads a month', 'Easter', 'Halloween', 'Adoption stories', 'Banned-brand list'],
  hero='bab-goldenegg',
  beats=[('The brief', 'High monthly volume, every holiday landing on its date, every bear on brand.'),
         ('The miss', 'Disney, Marvel and Pokémon products appeared in content. We had told creators what to feature, never what to avoid.'),
         ('The fix', 'Owned it, then proposed four steps: a banned list from the client, sent to the store when a shoot is booked, given to creators, and added to our review check.'),
         ('Also', 'Turned a Halloween brief into "phone time vs Halloween prep": a kid scrolls past the decorations, a parent turns it into a Workshop trip.')],
  clips=[('bab-goldenegg', 'Golden Egg · Easter', 'Three hooks'), ('bab-adoption', 'Adoption story', 'Gifting'), ('bab-promisepet', 'Promise a pet', 'Family moment')]),
 dict(stack=['monday','sheets','drive','frameio','meta','instagram'], fn='work-tireagent.html', color='var(--mint)', ink='var(--ink)', tag='E-commerce · Tyres', name='Tire Agent',
  title='One shoot. A month of ads.', hook='Single-creator ads wear out fast. So we treated footage like building blocks.',
  pills=['142 ads', '31 ad sets', 'Spanish-language sets', 'Editing guidelines'],
  hero='tireagent-womans',
  beats=[('The brief', 'A set number of fresh ads every month from a limited pool of creator footage.'),
         ('The idea', 'Mashups: the strongest lines from several real customers in one ad. Keep the body and call to action fixed, swap the hook, and every set becomes a clean test.'),
         ('The moves', 'Themed sets of three, a hook for each. Spanish versions with their own editing guide. Brand rules turned into editing guidelines so every editor cut the same way.'),
         ('What changed', '142 ads across 31 ad sets from January to November, tracked in one master log.')],
  clips=[('tireagent-womans', 'Hook test', 'Same body, new opening'), ('tireagent-hook1', 'Hook 1', 'Fear of old tyres'), ('tireagent-hook2', 'Hook 2', 'Quick story'), ('tireagent-paylater', 'Pay later', 'Mashup of real customers')]),
]

def case_page(c, nxt):
    beats = ''.join(f'<div class="beat rv"><div class="n">0{i+1}</div><div><h3>{E(t)}</h3><p>{E(p)}</p></div></div>' for i, (t, p) in enumerate(c['beats']))
    pills = ''.join(f'<span class="pill">{E(p)}</span>' for p in c['pills'])
    clips = ''.join(ph(a, b, s, ('tilt-l' if i % 3 == 0 else 'tilt-r' if i % 3 == 2 else '')) for i, (a, b, s) in enumerate(c['clips']))
    wide = ''
    if c.get('wide'):
        w = c['wide']
        wide = f'<section><div class="wrap grid widecase"><div class="ph"><div class="frame" style="aspect-ratio:16/9;border-radius:18px"><video muted loop playsinline preload="none" poster="v/{w[0]}.jpg" src="v/{w[0]}.mp4"></video><button class="snd" type="button" tabindex="-1">Sound off</button></div></div><div><p class="mono">Featured · 16:9</p><h3 class="mid" style="margin-top:10px">{E(w[1])}</h3><p class="lede">{E(w[2])}</p></div></div></section>'
    body = f'''
<div style="background:{c["color"]};color:{c["ink"]};border-bottom:2px solid var(--ink)"><div class="wrap chero">
 <div><p class="mono">{E(c["tag"])}</p><h1 class="big" style="margin-top:14px">{E(c["title"])}</h1><p style="margin-top:20px">{pills}</p><p class="mono" style="margin:18px 0 10px;opacity:.75">Built &amp; run with</p>{stack(c["stack"])}</div>
 <div style="max-width:300px;justify-self:center">{ph(c["hero"], c["name"], "Tap for sound", "tilt-r")}</div>
</div></div>
<section><div class="wrap"><p class="quote rv">“{E(c["hook"])}”</p></div></section>
<section style="padding-top:0"><div class="wrap">{beats}</div></section>
<section style="padding-top:0"><div class="wrap"><div class="kicker"><span class="dot"></span><span class="mono">The ads</span><span class="hand">tap any phone for sound</span></div>
<div class="grid clipgrid" style="--n:{min(5, len(c["clips"]))}">{clips}</div></div></section>
{wide}
<div class="wrap next"><a class="btn ghost" href="work.html">← All work</a><a class="btn" href="{nxt[0]}">Next: {E(nxt[1])} →</a></div>'''
    page(c['fn'], f'{c["name"]} · Amirthashree Vijayakumar', body)

# ---------- HOME ----------
rail = ['pataday-onedrop', 'capriottis-blt', 'tireagent-womans', 'bab-goldenegg', 'cox-sellmycar', 'systane-pocket', 'elcarwash-beforeafter', 'vf-everyday', 'botanic-spa', 'inshape-goals', 'autotrader-really', 'bab-adoption']
rail_html = ''.join(ph(c, '', '') for c in rail)
PIPE = [('docs', 'Brief'), ('instagram', 'Cast'), ('notion', 'Script'), ('gmail', 'Clear'), ('frameio', 'Edit'), ('monday', 'Track'), ('tiktok', 'Live')]
pipe = '<div class="pipe" data-pipe>' + '<i class="ln"></i>'.join(f'<div class="st"><span class="ic">{_isvg(k)}</span>{E(t)}</div>' for k, t in PIPE) + '</div>'
WALL = ['monday', 'claude', 'mcp', 'notion', 'airtable', 'asana', 'slack', 'sheets', 'drive', 'tableau', 'instagram', 'tiktok', 'linkedin', 'youtube', 'meta', 'frameio', 'excel', 'ppt']
wall = ''.join(f'<span>{ico(k)}{E(_iname(k))}</span>' for k in WALL)
home = f'''
<section style="padding:70px 0 40px;position:relative"><div class="wrap" style="position:relative">
 <span class="sticker">Creative ops · UGC · Automation</span>
 <h1 class="big" style="margin-top:26px;max-width:13ch">I make ads people <span data-rotate="stop scrolling for|watch twice|actually buy from|send to a friend" style="color:var(--tomato);transition:opacity .2s;white-space:nowrap">stop scrolling for</span><span style="white-space:nowrap">.</span></h1>
 <p class="lede">And I run the machine behind them: briefs, creators, approvals, editors, and the boards and AI agents that keep 40+ campaigns on time.</p>
 <p style="margin-top:30px;display:flex;gap:14px;flex-wrap:wrap"><a class="btn" href="work.html">See the work →</a><a class="btn ghost" href="ugc.html">Steal my playbook</a></p>
 <div class="badge" style="right:28px;top:10px" aria-hidden="true">Available now · in Dubai ·</div>
</div></section>
<div class="marquee" aria-hidden="true"><div class="track">{"".join(f"<span>{w}</span>" for w in ["40+ campaigns","11 brands at once","Intern to full-time in a year","Pharma-compliant","20 linked boards","Every campaign on schedule"]*2)}</div></div>
<div class="cliprail" aria-label="A reel of ads"><div class="track">{rail_html}{rail_html}</div></div>

<section style="padding-top:30px"><div class="wrap">
 <div class="kicker"><span class="dot" style="background:var(--lime)"></span><span class="mono">How an ad moves through my desk</span><span class="hand">every stage has an owner, a tool and a check</span></div>
 <div class="node rv" style="padding:26px 22px">{pipe}</div>
 <div class="grid g2" style="margin-top:34px;align-items:stretch">
  <div class="console rv"><div class="bar"><i></i><i></i><i></i><span style="margin-left:8px">agent log · sample run</span></div><div class="body" data-console></div></div>
  <div class="card rv" style="display:flex;flex-direction:column;justify-content:center;background:var(--lilac)">
   <span class="mono">Ops + AI, not ops vs AI</span>
   <h3 style="font-size:clamp(26px,2.8vw,36px)">I connect Claude to the team’s tools so the busywork runs itself.</h3>
   <p style="color:var(--ink)">Trackers, status updates and SOP drafts come from the real boards, and a human checks every one before it’s shared.</p>
   <div style="margin-top:18px">{stack(['claude','mcp','monday','drive','notion','slack'])}</div>
  </div>
 </div>
</div></section>

<section style="padding-top:10px"><div class="wrap">
 <div class="stats rv">
  <div><strong data-count="40" data-suffix="+">40+</strong><span>campaigns delivered</span></div>
  <div><strong data-count="11" data-suffix="+">11+</strong><span>brands at the same time</span></div>
  <div><strong data-count="20">20</strong><span>linked Monday.com boards I built</span></div>
  <div><strong data-count="8">8</strong><span>accounts handed over with SOPs</span></div>
 </div></div></section>

<div class="kicker wrap" style="margin-bottom:12px"><span class="dot" style="background:var(--cobalt)"></span><span class="mono">The stack I’m comfy in</span><span class="hand">see all of it on the About page</span></div>
<div class="logowall" aria-label="Tools I use"><div class="track">{wall}{wall}</div></div>

<section><div class="wrap">
 <div class="kicker"><span class="dot"></span><span class="mono">Pick a rabbit hole</span><span class="hand">start anywhere</span></div>
 <div class="grid g3">
  <a class="tile rv" href="work-alcon.html" style="background:var(--cobalt);color:#fff"><span class="mono">Pharma</span><h3>Compliant ads that sound like people</h3><p>Alcon eye care</p><span class="arrow">→</span></a>
  <a class="tile rv" href="work-autotrader.html" style="background:var(--tomato);color:#fff"><span class="mono">Automotive</span><h3>Cast the doubt</h3><p>Autotrader &amp; Kelley Blue Book</p><span class="arrow">→</span></a>
  <a class="tile rv" href="work-buildabear.html" style="background:var(--sun)"><span class="mono">Retail</span><h3>The fix that stops a mistake twice</h3><p>Build-A-Bear</p><span class="arrow">→</span></a>
  <a class="tile rv" href="work-tireagent.html" style="background:var(--mint)"><span class="mono">E-commerce</span><h3>One shoot, a month of ads</h3><p>Tire Agent</p><span class="arrow">→</span></a>
  <a class="tile rv" href="ugc.html" style="background:var(--lime)"><span class="mono">Playbook</span><h3>How a UGC ad actually works</h3><p>Hooks, proof, CTAs, metrics</p><span class="arrow">→</span></a>
  <a class="tile rv" href="playbook.html" style="background:var(--ink);color:var(--bg)"><span class="mono">Team</span><h3>How I run a creative team</h3><p>10 stages, house rules, 11 lessons</p><span class="arrow">→</span></a>
 </div>
</div></section>
<section style="padding-top:0"><div class="wrap"><p class="quote rv">“Creative work rarely falls apart because people run out of ideas. It falls apart when nobody can see what’s going on.”</p></div></section>'''
page('index.html', 'Amirthashree Vijayakumar · Creative Operations', home)

# ---------- WORK INDEX ----------
work = '''
<section style="padding-bottom:30px"><div class="wrap"><span class="sticker" style="background:var(--mint)">Selected work</span><h1 class="big" style="margin-top:22px">Four brands.<br>Four problems.</h1><p class="lede">Each one is a short story: the brief, the idea, what I did, what changed. Tap any phone for sound.</p></div></section>
<section style="padding-top:20px"><div class="wrap grid g2">'''
for c in CASES:
    work += f'<a class="tile rv" href="{c["fn"]}" style="background:{c["color"]};color:{c["ink"]};display:grid;grid-template-columns:1fr 150px;gap:20px;align-items:center"><div><span class="mono">{E(c["tag"])}</span><h3>{E(c["title"])}</h3><p>{E(c["name"])}</p></div><div class="ph tilt-r"><div class="frame" style="box-shadow:none"><video muted loop playsinline preload="none" poster="v/{c["hero"]}.jpg" src="v/{c["hero"]}.mp4"></video></div></div></a>'
work += '</div></section>'
extra_work = ''
page('work.html', 'Work · Amirthashree Vijayakumar', work)

order = [(c['fn'], c['name']) for c in CASES]
for i, c in enumerate(CASES):
    case_page(c, order[(i + 1) % len(order)])
print('ok')
