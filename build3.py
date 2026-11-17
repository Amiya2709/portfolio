from build import page, E, ico, stack
from icons import svg as isvg

css = '''
.anat{display:grid;grid-template-columns:minmax(0,1fr) 280px;gap:40px;align-items:center}
.tbar{display:flex;height:64px;border:2px solid var(--ink);border-radius:12px;overflow:hidden;position:relative;background:var(--card);box-shadow:5px 5px 0 var(--ink)}
.tbar button{all:unset;cursor:pointer;display:flex;flex-direction:column;justify-content:center;padding:0 10px;border-right:2px solid var(--ink);font-weight:700;font-size:14px;line-height:1.1;overflow:hidden;white-space:nowrap}
.tbar button:last-of-type{border-right:0}
.tbar button small{font-family:var(--mono);font-size:10px;font-weight:400;opacity:.7;margin-top:3px}
.tbar button[aria-pressed="true"]{box-shadow:inset 0 -6px 0 var(--ink)}
.tbar i{position:absolute;top:0;bottom:0;width:3px;background:var(--tomato);left:0;pointer-events:none}
.beatbox{margin-top:26px;display:grid;grid-template-columns:auto 1fr;gap:6px 18px;align-items:baseline}
.beatbox .k{font-family:var(--mono);font-size:11px;text-transform:uppercase;color:var(--soft)}
.beatbox .v{font-size:19px}
.mock{width:260px;aspect-ratio:9/16;border-radius:30px;border:6px solid var(--ink);background:#1b1b1b;position:relative;overflow:hidden;box-shadow:6px 6px 0 var(--ink);margin:0 auto}
.mock .scr{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:flex-end;padding:18px;transition:background .4s}
.mock .tag{position:absolute;top:16px;left:16px}
.mock .say{background:#fff;color:var(--ink);border-radius:12px;padding:12px 14px;font-weight:700;font-size:16px;line-height:1.25}
.mock .face{position:absolute;top:34%;left:50%;width:96px;height:96px;margin-left:-48px;border-radius:50%;background:rgba(255,255,255,.25);border:3px solid rgba(255,255,255,.6)}
.mock .face::after{content:"";position:absolute;left:-30px;right:-30px;top:105px;height:120px;border-radius:60px 60px 0 0;background:rgba(255,255,255,.25)}
.rules{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.rule{background:var(--card);border:2px solid var(--ink);border-radius:14px;padding:18px;box-shadow:4px 4px 0 var(--ink)}
.rule b{display:block;font-family:var(--display);font-stretch:112%;font-size:20px;line-height:1.05;letter-spacing:-.02em;margin:8px 0 6px}
.rule p{font-size:15px;color:var(--soft)}
.flip{perspective:1000px;cursor:pointer;min-height:220px;border:0;background:none;text-align:left;font:inherit;color:inherit;padding:0}
.flip .in2{position:relative;width:100%;height:100%;min-height:220px;transition:transform .6s;transform-style:preserve-3d}
.flip.on .in2{transform:rotateY(180deg)}
.flip .f,.flip .b{position:absolute;inset:0;border:2px solid var(--ink);border-radius:16px;padding:20px;backface-visibility:hidden;box-shadow:5px 5px 0 var(--ink);display:flex;flex-direction:column}
.flip .f q{font-family:var(--display);font-stretch:108%;font-weight:800;font-size:20px;line-height:1.12;letter-spacing:-.015em;margin-top:12px;quotes:"“" "”"}
.flip .f em{margin-top:auto;font-style:normal;font-family:var(--mono);font-size:10.5px;text-transform:uppercase}
.flip .b{transform:rotateY(180deg);background:var(--ink);color:var(--bg)}
.flip .b h3{font-size:22px;margin-bottom:10px;color:var(--lime)}
.chat{display:flex;flex-direction:column;gap:12px;max-width:560px}
.bub{align-self:flex-start;background:var(--card);border:2px solid var(--ink);border-radius:18px 18px 18px 4px;padding:12px 16px;font-size:18px;box-shadow:3px 3px 0 var(--ink);max-width:90%}
.bub small{display:block;font-family:var(--mono);font-size:10px;text-transform:uppercase;color:var(--soft);margin-bottom:4px}
.bub:nth-child(2){align-self:center;background:var(--sun)}
.bub:nth-child(3){align-self:flex-end;background:var(--lime);border-radius:18px 18px 4px 18px}
.bub mark{background:var(--tomato);color:#fff;padding:0 4px;border-radius:3px}
.toggle{display:inline-flex;border:2px solid var(--ink);border-radius:10px;overflow:hidden;background:var(--card)}
.toggle button{all:unset;cursor:pointer;padding:8px 16px;font-weight:700;font-size:14px}
.toggle button[aria-pressed="true"]{background:var(--ink);color:var(--bg)}
.fb{margin-top:16px;display:grid;gap:10px}
.fb div{background:var(--card);border:2px solid var(--ink);border-radius:12px;padding:14px 16px;font-size:18px;font-weight:600}
.arc{display:flex;align-items:center;gap:0}
.arc .node{flex:1;text-align:center}
.arc .node b{display:block;font-family:var(--display);font-stretch:112%;font-size:22px}
.arc .ln{flex:0 0 40px;height:2px;background:repeating-linear-gradient(90deg,var(--ink) 0 6px,transparent 6px 11px);background-size:22px 2px;animation:flow 1s linear infinite}
.proof{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.proof div{border:2px solid var(--ink);border-radius:14px;padding:18px;background:var(--card)}
.proof b{font-family:var(--display);font-stretch:112%;font-size:20px;display:block;margin-bottom:6px}
.proof p{font-size:15px;color:var(--soft)}
.proof span{display:inline-block;margin-top:10px}
.funnel{display:grid;gap:10px}
.funnel .tier{margin:0 auto;display:grid;grid-template-columns:170px 1fr 1fr;gap:16px;align-items:center;border:2px solid var(--ink);border-radius:14px;padding:16px 20px;box-shadow:4px 4px 0 var(--ink)}
.funnel .tier b{font-family:var(--display);font-stretch:112%;font-size:19px;line-height:1.05}
.funnel .tier i{font-style:normal;color:var(--soft);font-size:15px}
.funnel .tier q{font-weight:700;font-size:16px}
.adset{display:grid;gap:10px}
.adset .row{display:grid;grid-template-columns:70px 1.1fr 2fr 1fr;gap:8px;align-items:stretch}
.adset .row > *{border:2px solid var(--ink);border-radius:10px;padding:10px 12px;font-weight:700;font-size:14px;display:flex;align-items:center}
.adset .row .id{font-family:var(--mono);font-weight:500;justify-content:center;background:var(--ink);color:var(--bg)}
.adset .row .h{background:var(--sun)}
.adset .row:nth-child(2) .h{background:var(--pink)}
.adset .row:nth-child(3) .h{background:var(--mint)}
.adset .row .bd{background:var(--card);color:var(--soft)}
.adset .row .ct{background:var(--lilac)}
.stamp{border:3px double var(--ink);border-radius:12px;padding:18px;background:var(--card);transform:rotate(var(--r,0deg))}
.stamp b{font-family:var(--display);font-stretch:118%;font-size:19px;text-transform:uppercase;display:block;margin-bottom:6px;letter-spacing:-.01em}
.stamp p{font-size:15px;color:var(--soft)}
.dash{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.metric{background:var(--card);border:2px solid var(--ink);border-radius:14px;padding:18px;position:relative;overflow:hidden}
.metric b{font-family:var(--display);font-stretch:112%;font-size:21px;display:block}
.metric p{font-size:14.5px;color:var(--soft);margin-top:6px}
.metric .meter{height:8px;border:1.5px solid var(--ink);border-radius:99px;margin-top:14px;overflow:hidden}
.metric .meter i{display:block;height:100%;background:var(--cobalt);width:0;transition:width 1.4s cubic-bezier(.2,.7,.2,1)}
.metric.in .meter i{width:var(--w)}
.diag{margin-top:22px;border:2px solid var(--ink);border-radius:16px;background:var(--ink);color:var(--bg);padding:22px}
.diag .toggle{background:transparent;border-color:var(--bg)}
.diag .toggle button{color:var(--bg)}
.diag .toggle button[aria-pressed="true"]{background:var(--lime);color:var(--ink)}
.diag p{font-size:20px;margin-top:16px;max-width:60ch}
.plat{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.plat > div{border:2px solid var(--ink);border-radius:14px;padding:16px;background:var(--card)}
.plat b{display:block;font-weight:800;margin:8px 0 4px}
.plat p{font-size:14.5px;color:var(--soft)}
@media (max-width:980px){.anat{grid-template-columns:minmax(0,1fr)}.rules,.plat{grid-template-columns:repeat(2,1fr)}.proof,.dash{grid-template-columns:repeat(2,1fr)}.funnel .tier{grid-template-columns:1fr;width:100%!important}.tbar button small{display:none}}
@media (max-width:600px){.rules,.plat,.proof,.dash{grid-template-columns:1fr}.arc{flex-direction:column}.arc .ln{width:2px;height:24px;flex:0 0 24px}.adset .row{grid-template-columns:50px 1fr}.adset .row .bd,.adset .row .ct{grid-column:2}}
'''

BEATS = [("Hook", "0–3s", "Stop the scroll and promise a payoff", "“I was drinking two litres a day and still had headaches.”", "#F2E3B8"),
         ("Problem", "3–8s", "Make the viewer recognise themselves", "“Turns out I was forgetting to drink until 4pm.”", "#F2D9E2"),
         ("Solution", "8–14s", "Introduce the product as the fix", "“This bottle has time markers, so I actually pace it.”", "#D3E8DE"),
         ("Demo", "14–20s", "Show it working, don’t just say it", "Close-up of the markers, a refill, a real moment of use.", "#DDD8F5"),
         ("Proof", "20–25s", "Make the claim believable", "“My whole office has one now.”", "#E3EE9E"),
         ("CTA", "25–30s", "Tell them exactly what to do next", "“Link’s below. Use code X for 15% off.”", "#F6CFC4")]
SECS = [3, 5, 6, 6, 5, 5]

HOOKS = [("Confession", "I almost didn’t buy this. Three times.", "Admits a relatable mistake or doubt."),
         ("Problem callout", "If your eyes feel like sandpaper by 3pm, watch this.", "Names the viewer’s pain directly."),
         ("POV", "POV: you’re the one who has to order dinner for six people.", "Puts the viewer inside a scene."),
         ("Result first", "Keys in hand. Here’s how I got here without visiting a dealer.", "Opens with the outcome, then rewinds."),
         ("Bold claim", "This replaced three products in my bathroom.", "A surprising statement that begs proof."),
         ("Question", "Why does nobody tell you this about contact lenses?", "Asks something they can’t ignore."),
         ("Expert intro", "As an optometrist, this is what I’d tell my own family.", "Authority speaks first."),
         ("Pattern interrupt", "[product dropped into water · sudden cut to silence]", "An unexpected visual or sound."),
         ("List", "3 things I wish I knew before buying tyres online.", "Promises a quick, structured payoff.")]
HCOL = ['var(--sun)', 'var(--pink)', 'var(--mint)', 'var(--lilac)', 'var(--lime)', 'var(--card)', 'var(--sun)', 'var(--pink)', 'var(--mint)']

def sec(kick, title, dot='var(--tomato)', note=''):
    n = f'<span class="hand">{E(note)}</span>' if note else ''
    return f'<div class="kicker"><span class="dot" style="background:{dot}"></span><span class="mono">{E(kick)}</span>{n}</div><h2 class="mid" style="margin-bottom:30px;max-width:20ch">{title}</h2>'

segs = ''.join(f'<button type="button" data-beat="{i}" style="width:{s/30*100:.2f}%;background:{c}" aria-pressed="{str(i==0).lower()}">{E(n)}<small>{E(t)}</small></button>' for i, ((n, t, j, x, c), s) in enumerate(zip(BEATS, SECS)))
beats_js = '[' + ','.join('{n:%r,t:%r,j:%r,x:%r,c:%r}' % (n, t, j, x, c) for n, t, j, x, c in BEATS) + ']'

body = f'''
<section style="padding-bottom:20px"><div class="wrap"><span class="sticker" style="background:var(--lime)">Playbook · generic examples only</span>
<h1 class="big" style="margin-top:22px">How a UGC ad<br>actually works.</h1>
<p class="lede">What I used every day writing, casting and directing ads for 11+ brands. One rule sits under all of it:</p>
<p class="quote rv" style="margin-top:28px;max-width:900px">If a line sounds like a brand wrote it, rewrite it.</p></div></section>

<section><div class="wrap">{sec("01 · Anatomy", "Six beats. Thirty seconds. Same order every time.", "var(--sun)", "click a beat")}
<div class="anat"><div>
 <div class="tbar" data-anat>{segs}<i data-head></i></div>
 <div class="beatbox"><span class="k">Beat</span><span class="v" style="font-family:var(--display);font-stretch:118%;font-weight:800;font-size:30px" data-bn>Hook</span>
 <span class="k">Job</span><span class="v" data-bj>Stop the scroll and promise a payoff</span>
 <span class="k">Time</span><span class="v mono" style="font-size:13px" data-bt>0–3s</span></div>
</div>
<div class="mock" aria-hidden="true"><div class="scr" data-scr style="background:#F2E3B8"><span class="chip tag" data-bc>Hook · 0–3s</span><div class="face"></div><div class="say" data-bx>“I was drinking two litres a day and still had headaches.”</div></div></div>
</div></div></section>

<section style="padding-top:20px"><div class="wrap">{sec("02 · Hooks", "The first three seconds decide everything else.", "var(--tomato)")}
<div class="rules">
 <div class="rule rv"><span class="chip ok">Rule 1</span><b>Say it and show it</b><p>The first line works with the sound off. On-screen text repeats the hook.</p></div>
 <div class="rule rv"><span class="chip ok">Rule 2</span><b>Faces beat logos</b><p>Open on a person, never a product shot.</p></div>
 <div class="rule rv"><span class="chip ok">Rule 3</span><b>One idea per hook</b><p>Needs a second sentence to make sense? Too complicated.</p></div>
 <div class="rule rv"><span class="chip ok">Rule 4</span><b>Always write three</b><p>The hook is the cheapest part to change and moves results most.</p></div>
</div>
<div class="kicker" style="margin-top:40px"><span class="mono">9 hook types I reach for</span><span class="hand">tap a card to see how it works</span></div>
<div class="grid g3">{"".join(f'<button class="flip" type="button" aria-pressed="false"><div class="in2"><div class="f" style="background:{HCOL[i]}"><span class="mono">{i+1:02d} · {E(t)}</span><q>{E(x)}</q><em>flip →</em></div><div class="b"><h3>{E(t)}</h3><p>{E(h)}</p></div></div></button>' for i, (t, x, h) in enumerate(HOOKS))}</div>
</div></section>

<section style="padding-top:20px"><div class="wrap">{sec("03 · The script", "Problem. Agitate. Solve.", "var(--lime)", "specificity wins")}
<div class="grid g2" style="align-items:start;gap:40px">
 <div class="chat">
  <div class="bub rv"><small>Problem</small>“My eyes get so dry at work.”</div>
  <div class="bub rv"><small>Agitate</small>“By <mark>4pm</mark> I’m blinking constantly and <mark>can’t focus on my screen</mark>.”</div>
  <div class="bub rv"><small>Solve</small>“Now I keep these drops on my desk, and two drops gets me through the afternoon.”</div>
 </div>
 <div data-tabs><span class="mono">Viewers buy the result, not the spec</span><br><br>
  <div class="toggle"><button type="button" data-tab="f" aria-pressed="false">Feature</button><button type="button" data-tab="b" aria-pressed="true">What the creator says</button></div>
  <div class="fb" data-pane="f" hidden><div>Preservative-free formula</div><div>Online checkout</div><div>Time markers on a bottle</div></div>
  <div class="fb" data-pane="b"><div style="background:var(--lime)">“Gentle enough that I use it every day.”</div><div style="background:var(--lime)">“I bought my car from my sofa on a Sunday.”</div><div style="background:var(--lime)">“I finally drink enough without thinking about it.”</div></div>
 </div>
</div>
<div class="kicker" style="margin-top:50px"><span class="mono">The emotional version · great for lifestyle &amp; beauty</span></div>
<div class="arc rv"><div class="node"><span class="mono">Before</span><b>The struggle</b></div><i class="ln"></i><div class="node" style="background:var(--sun)"><span class="mono">Turning point</span><b>Finding it</b></div><i class="ln"></i><div class="node" style="background:var(--lime)"><span class="mono">After</span><b>Life now</b></div></div>
<p class="lede" style="max-width:60ch">The demo is where people decide whether to believe you. It has to look unpolished and real, never a studio shot dropped into a phone video.</p>
</div></section>

<section style="padding-top:20px"><div class="wrap">{sec("04 · Proof", "“Why should I believe you?”", "var(--cobalt)", "peer + expert is the strongest combo")}
<div class="proof">
 <div class="rv"><b>Peer proof</b><p>A relatable person, their own experience.</p><span class="chip">Everyday products</span></div>
 <div class="rv" style="background:var(--lilac)"><b>Expert authority</b><p>A doctor or pro explains why it works.</p><span class="chip">Health &amp; pharma</span></div>
 <div class="rv"><b>Crowd proof</b><p>“Everyone in my office uses one.”</p><span class="chip">Momentum</span></div>
 <div class="rv"><b>Numbers</b><p>Ratings, reviews, units sold.</p><span class="chip">Late-funnel doubt</span></div>
 <div class="rv"><b>Before &amp; after</b><p>A visible result over time.</p><span class="chip">Beauty · fitness</span></div>
 <div class="rv"><b>Reviews on screen</b><p>Real review text as an overlay.</p><span class="chip">Retargeting</span></div>
</div>
<p style="margin-top:20px;display:flex;gap:10px;flex-wrap:wrap"><span class="chip stop">Every claim true &amp; supportable</span><span class="chip stop">Real experts only</span><span class="chip stop">Signed consent before it runs</span></p>
</div></section>

<section style="padding-top:20px"><div class="wrap">{sec("05 · Calls to action", "Match the ask to where they are.", "var(--pink)")}
<div class="funnel">
 <div class="tier rv" style="width:100%;background:var(--sun)"><b>Awareness<br><span class="mono">cold</span></b><i>“I’ve never heard of this.”</i><q>Follow for more tips like this.</q></div>
 <div class="tier rv" style="width:90%;background:var(--pink)"><b>Consideration</b><i>“Is this right for me?”</i><q>See if it works with your lenses. Link below.</q></div>
 <div class="tier rv" style="width:80%;background:var(--lime)"><b>Conversion<br><span class="mono">warm</span></b><i>“I’m nearly ready.”</i><q>Use code X for 15% off. This week only.</q></div>
 <div class="tier rv" style="width:70%;background:var(--lilac)"><b>Regulated</b><i>“Should I ask someone?”</i><q>Ask your eye doctor.</q></div>
</div>
<p style="margin-top:24px;display:flex;gap:10px;flex-wrap:wrap"><span class="chip">One action only</span><span class="chip">Said + shown + points at the button</span><span class="chip">“I’ll leave the link below” &gt; “Visit our website”</span><span class="chip">A reason to act now</span><span class="chip">Fixed across hook tests</span></p>
</div></section>

<section style="padding-top:20px"><div class="wrap">{sec("06 · Strategy beyond the script", "Build in sets. Test the hook. Refresh before it fades.", "var(--mint)")}
<div class="grid g2" style="gap:40px;align-items:start">
 <div><span class="mono">An ad set = one body, one CTA, three hooks</span>
 <div class="adset rv" style="margin-top:14px">
  <div class="row"><span class="id">1A</span><span class="h">Confession hook</span><span class="bd">Same body</span><span class="ct">Same CTA</span></div>
  <div class="row"><span class="id">1B</span><span class="h">POV hook</span><span class="bd">Same body</span><span class="ct">Same CTA</span></div>
  <div class="row"><span class="id">1C</span><span class="h">Expert hook</span><span class="bd">Same body</span><span class="ct">Same CTA</span></div>
 </div><p style="margin-top:12px;color:var(--soft)">Only the hook changes, so the results tell you which opening works.</p></div>
 <div class="grid" style="gap:14px">
  <div class="node rv"><div class="hd"><span class="chip wip">Casting</span></div><b>Cast the situation, not the demographic.</b><p style="color:var(--soft)">Not “woman, 30s”. “A nurse on night shifts who’s never had time to compare options.”</p></div>
  <div class="node rv"><div class="hd"><span class="chip rev">Objections</span></div><b>Say the doubt out loud first.</b><p style="color:var(--soft)">“I thought buying a car online would be risky, until I saw there’s a return window.”</p></div>
  <div class="node rv"><div class="hd"><span class="chip ok">Mashups</span></div><b>Best lines from several creators, one ad.</b><p style="color:var(--soft)">One shoot powers many ads, and every voice is extra proof.</p></div>
 </div>
</div>
<div class="kicker" style="margin-top:46px"><span class="mono">Where it runs changes how it’s cut</span></div>
<div class="plat">
 <div class="rv"><div class="stack">{ico("tiktok")}{ico("instagram")}</div><b>Feeds</b><p>9:16, fast cuts, captions on, native and unpolished.</p></div>
 <div class="rv"><div class="stack">{ico("youtube")}{ico("meta")}</div><b>Sound off</b><p>Every ad works silent, with burned-in captions.</p></div>
 <div class="rv"><div class="stack"><span class="chip">PDP</span></div><b>Product pages</b><p>Calmer, explanatory, answers buyer questions.</p></div>
 <div class="rv"><div class="stack"><span class="chip">EN</span><span class="chip">ES</span><span class="chip">AR</span></div><b>Languages</b><p>Re-cast or re-edit per language. Not just subtitles.</p></div>
</div>
</div></section>

<section style="padding-top:20px"><div class="wrap">{sec("07 · Regulated categories", "Make approved claims sound human.", "var(--tomato)", "pharma & health")}
<div class="grid g3">
 <div class="stamp rv" style="--r:-1deg"><b>Claims as approved</b><p>Creators rephrase around a claim. The claim itself never changes.</p></div>
 <div class="stamp rv" style="--r:1deg;background:var(--lime)"><b>Experience, not promises</b><p>“It helped my eyes feel less dry” ✓ &nbsp; “It cures dry eye” ✗</p></div>
 <div class="stamp rv" style="--r:-.5deg"><b>Review before filming</b><p>Medical, legal and regulatory see the script first. Fixing a script beats a reshoot.</p></div>
 <div class="stamp rv" style="--r:.8deg"><b>Traceable</b><p>Every approved asset gets a reference code. Every script change is logged.</p><div style="margin-top:10px">{stack(["veeva","monday"])}</div></div>
 <div class="stamp rv" style="--r:-1deg;background:var(--sun)"><b>Consent first</b><p>Everyone on screen signs before the ad runs.</p></div>
</div></div></section>

<section style="padding-top:20px"><div class="wrap">{sec("08 · Metrics that matter", "Read them together, not one at a time.", "var(--cobalt)")}
<div class="dash">
 <div class="metric rv" style="--w:82%"><span class="mono">Reflects: the hook</span><b>Hook rate</b><p>Share who watch past 3 seconds.</p><div class="meter"><i></i></div></div>
 <div class="metric rv" style="--w:64%"><span class="mono">Reflects: problem, solution, pacing</span><b>Hold rate</b><p>How long people keep watching.</p><div class="meter"><i></i></div></div>
 <div class="metric rv" style="--w:52%"><span class="mono">Reflects: relatability</span><b>Engagement</b><p>Likes, comments, shares, saves.</p><div class="meter"><i></i></div></div>
 <div class="metric rv" style="--w:38%"><span class="mono">Reflects: the CTA &amp; offer</span><b>Click-through</b><p>Share who click the link.</p><div class="meter"><i></i></div></div>
 <div class="metric rv" style="--w:30%"><span class="mono">Reflects: offer + landing page</span><b>Conversion</b><p>Share who buy or sign up.</p><div class="meter"><i></i></div></div>
 <div class="metric rv" style="--w:46%"><span class="mono">Reflects: everything</span><b>Cost per acquisition</b><p>What each customer costs.</p><div class="meter"><i></i></div></div>
</div>
<div class="diag" data-tabs><span class="mono" style="color:var(--lime)">Diagnose it</span><br><br>
 <div class="toggle"><button type="button" data-tab="a" aria-pressed="true">High hook rate, low CTR</button><button type="button" data-tab="b" aria-pressed="false">Low hook rate</button></div>
 <p data-pane="a">The opening works. The rest of the ad doesn’t convince. Fix the body, the proof or the offer.</p>
 <p data-pane="b" hidden>The rest of the ad never gets a chance. Test new hooks before touching anything else.</p>
</div>
<p class="mono" style="margin-top:12px;opacity:.6">Meters are illustrative, not real campaign data.</p>
</div></section>

<section style="padding-top:0"><div class="wrap"><a class="tile rv" href="playbook.html#preflight" style="background:var(--ink);color:var(--bg);min-height:0;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap"><div><span class="mono" style="color:var(--lime)">Next</span><h3 style="margin-top:8px">How my team follows all of this, every single ad →</h3></div></a></div></section>
<script>
(function(){{
 var B={beats_js}, segs=[0,3,8,14,20,25,30];
 var bar=document.querySelector('[data-anat]'), head=document.querySelector('[data-head]'), btns=bar.querySelectorAll('button');
 var q=function(s){{return document.querySelector(s);}};
 var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches, cur=-1, t=0, manual=false;
 function show(i){{ if(i===cur) return; cur=i; var b=B[i];
  q('[data-bn]').textContent=b.n; q('[data-bj]').textContent=b.j; q('[data-bt]').textContent=b.t; q('[data-bx]').textContent=b.x;
  q('[data-bc]').textContent=b.n+' · '+b.t; q('[data-scr]').style.background=b.c;
  [].forEach.call(btns,function(x,k){{x.setAttribute('aria-pressed',k===i);}}); }}
 [].forEach.call(btns,function(x,k){{ x.addEventListener('click',function(){{ t=segs[k]; manual=true; show(k); head.style.left=(t/30*100)+'%'; setTimeout(function(){{manual=false;}},4000); }}); }});
 show(0); if(reduce) return;
 setInterval(function(){{ if(manual) return; t=(t+0.1)%30; head.style.left=(t/30*100)+'%'; for(var k=0;k<6;k++) if(t>=segs[k]&&t<segs[k+1]) show(k); }},100);
 var ms=document.querySelectorAll('.metric'); if('IntersectionObserver' in window){{ var o=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting)e.target.classList.add('in');}});}}); [].forEach.call(ms,function(m){{o.observe(m);}}); }}
}})();
</script>'''
page('ugc.html', 'UGC playbook · Amirthashree Vijayakumar', body, css)
print('ugc ok')
