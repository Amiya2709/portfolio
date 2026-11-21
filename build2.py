from build import page, E, ico, stack, tool

# ---------- UAE CONCEPTS ----------
css_c = '''
.concept{border:2px solid var(--ink);border-radius:26px;overflow:hidden;box-shadow:8px 8px 0 var(--ink);margin-bottom:56px;background:var(--card)}
.concept .top{display:grid;grid-template-columns:1.2fr .8fr;gap:0}
.concept .txt{padding:40px}
.concept .txt h2{font-size:clamp(40px,5.5vw,76px);margin:12px 0 16px}
.concept .ins{font-size:20px;max-width:40ch}
.concept .stage{display:grid;place-items:center;padding:36px;border-left:2px solid var(--ink);min-height:520px;position:relative;overflow:hidden}
.mock{width:250px;aspect-ratio:9/16;border-radius:28px;border:6px solid var(--ink);background:#111;position:relative;overflow:hidden;box-shadow:6px 6px 0 var(--ink)}
.hooks{display:grid;grid-template-columns:repeat(3,1fr);border-top:2px solid var(--ink)}
.hooks div{padding:22px 26px;border-right:2px solid var(--ink);font-family:var(--display);font-weight:800;font-size:21px;line-height:1.15;letter-spacing:-.01em}
.hooks div:last-child{border-right:0}
.hooks span{display:block;font-family:var(--mono);font-weight:500;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--soft);margin-bottom:8px}
.tl{padding:22px 26px;border-top:2px solid var(--ink)}
.tl .bar{display:flex;height:44px;border:2px solid var(--ink);border-radius:12px;overflow:hidden;position:relative;margin-top:10px}
.tl .bar div{display:flex;align-items:center;padding:0 10px;font-size:13px;font-weight:600;border-right:2px solid var(--ink);white-space:nowrap;overflow:hidden}
.tl .bar div:last-child{border-right:0}
.tl .bar i{position:absolute;top:-2px;bottom:-2px;width:3px;background:var(--tomato);left:0;animation:play var(--d) linear infinite}
@keyframes play{to{left:100%}}
/* two climates */
.temp{position:absolute;inset:0;animation:climate 6s ease-in-out infinite;display:grid;place-items:center}
@keyframes climate{0%,40%{background:#FF8A3D}50%,90%{background:#9ED8FF}100%{background:#FF8A3D}}
.deg{font-family:var(--display);font-weight:800;font-size:68px;color:#16121F;text-align:center;line-height:.9}
.deg small{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.1em;margin-top:10px}
.cap{position:absolute;left:12px;right:12px;bottom:18px;background:#fff;color:#16121F;border-radius:10px;padding:8px 10px;font-weight:700;font-size:14px;line-height:1.2;text-align:center}
/* chat */
.chat{position:absolute;inset:0;background:#ECE5DD;padding:42px 10px 10px;display:flex;flex-direction:column;gap:6px;font-size:12px}
.chat .hd{position:absolute;top:0;left:0;right:0;background:#16121F;color:#fff;padding:10px;font-weight:700;font-size:12px;display:flex;justify-content:space-between}
.chat .hd b{background:var(--tomato);border-radius:999px;padding:0 8px;font-variant-numeric:tabular-nums}
.chat p{background:#fff;border-radius:10px;padding:6px 9px;max-width:85%;opacity:0;transform:translateY(8px);animation:pop 9s infinite}
.chat p.me{align-self:flex-end;background:#DCF8C6}
.chat p strong{display:block;font-size:10px;color:var(--cobalt)}
@keyframes pop{0%{opacity:0;transform:translateY(8px)}6%,85%{opacity:1;transform:none}100%{opacity:0}}
/* countdown */
.dusk{position:absolute;inset:0;background:linear-gradient(#2B1B5C,#E9775A 70%,#F7C873);display:grid;place-items:center}
.clock{font-family:var(--display);font-weight:800;font-size:64px;color:#fff;font-variant-numeric:tabular-nums;text-align:center;line-height:1}
.clock small{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.1em;margin-top:8px}
@media (max-width:980px){.concept .top{grid-template-columns:1fr}.concept .stage{border-left:0;border-top:2px solid var(--ink);min-height:480px}.hooks{grid-template-columns:1fr}.hooks div{border-right:0;border-bottom:2px solid var(--ink)}}
'''
def tl(parts, total, color):
    segs = ''.join(f'<div style="width:{w/total*100:.1f}%;background:{c}">{E(t)}</div>' for t, w, c in parts)
    return f'<div class="tl"><span class="mono">Structure · {total} seconds</span><div class="bar" style="--d:{total}s">{segs}<i></i></div></div>'

def hooks(h):
    return '<div class="hooks">' + ''.join(f'<div><span>Hook {i+1}</span>{E(x)}</div>' for i, x in enumerate(h)) + '</div>'

concepts = f'''
<section style="padding-bottom:30px"><div class="wrap"><span class="sticker" style="background:var(--pink)">Spec work · not commissioned</span>
<h1 class="big" style="margin-top:22px">Three ideas<br>for the UAE.</h1>
<p class="lede">Original concepts to show how I'd think about this market. Each starts from a local truth, then tests three hooks.</p></div></section>
<section style="padding-top:20px"><div class="wrap">

<article class="concept rv"><div class="top"><div class="txt"><p class="mono">01 · Eyewear &amp; optics · Magrabi Optical</p><h2>Two Climates</h2>
<p class="ins">In the UAE your eyes go from 45°C sun to 19°C air-conditioning many times a day. Most people never connect that to dry, tired eyes.</p>
<p style="margin-top:18px;color:var(--soft)">Four everyday UAE lives (office worker, student, school-run parent, delivery rider) each show their two-climate day, then an optometrist explains why it matters. Filmed in Arabic and English.</p><p class="mono" style="margin:20px 0 10px;opacity:.7">Built for</p>{stack(['instagram','tiktok','youtube'])}</div>
<div class="stage" style="background:#FFE6D1"><div class="mock"><div class="temp"><div class="deg" data-temp>46°C<small>OUTSIDE</small></div></div><div class="cap">“My eyes live in two countries every day.”</div></div></div></div>
{hooks(["A phone weather screen at 46°C, then a pan to the office thermostat at 19°C.", "“I thought it was screen time. It was the AC.”", "Optometrist to camera: “If you live in the UAE, here’s what your eyes are dealing with.”"])}
{tl([("Hook",3,"#FFD23F"),("Four lives, quick cuts",12,"#FFE6D1"),("Optometrist",9,"#9ED8FF"),("Book a test",6,"#7BE0C3")],30,"")}
</article>

<article class="concept rv"><div class="top"><div class="txt"><p class="mono">02 · Food delivery · talabat</p><h2>Six Nationalities, One Order</h2>
<p class="ins">In UAE flatshares, choosing dinner means negotiating across six cuisines, and the group chat is where the drama happens.</p>
<p style="margin-top:18px;color:var(--soft)">Real flatmates film the chaos as screen recordings of the group chat cut with reactions, ending with everyone getting their own dish in one order. Fixed ending, swappable hooks, built for Reels and TikTok.</p><p class="mono" style="margin:20px 0 10px;opacity:.7">Built for</p>{stack(['instagram','tiktok'])}</div>
<div class="stage" style="background:#FFF1B8"><div class="mock"><div class="chat"><div class="hd"><span>Flat 1204 🍽️</span><b data-unread>47</b></div>
<p style="animation-delay:0s"><strong>Priya</strong>biryani or I riot</p>
<p class="me" style="animation-delay:.9s">sushi pls 🙏</p>
<p style="animation-delay:1.8s"><strong>Omar</strong>shawarma. final answer.</p>
<p style="animation-delay:2.7s"><strong>Lucía</strong>tacos???</p>
<p style="animation-delay:3.6s"><strong>Wei</strong>dumplings or nothing</p>
<p class="me" style="animation-delay:4.5s">ok I’m ordering everything</p></div></div></div></div>
{hooks(["“There are six nationalities in this flat and one talabat order.”", "A group-chat screen recording: 47 unread messages, all about dinner.", "“POV: you’re the one who has to place the order.”"])}
{tl([("Hook",3,"#FFD23F"),("Chat chaos + reactions",9,"#FFF1B8"),("Every dish revealed",5,"#FF8AD8"),("CTA",3,"#7BE0C3")],20,"")}
</article>

<article class="concept rv"><div class="top"><div class="txt"><p class="mono">03 · Rides · Careem · Ramadan</p><h2>The Last 11 Minutes</h2>
<p class="ins">During Ramadan, the minutes before iftar are the most time-sensitive of the day. Getting home to family in time matters.</p>
<p style="margin-top:18px;color:var(--soft)">A real-time countdown series: creators film their journey to iftar with a running clock on screen, ending at the family table. Warm and respectful, built around the moment rather than the ride, with a cultural review before filming.</p><p class="mono" style="margin:20px 0 10px;opacity:.7">Built for</p>{stack(['tiktok','instagram','youtube'])}</div>
<div class="stage" style="background:#E9E1FF"><div class="mock"><div class="dusk"><div class="clock"><span data-clock>11:00</span><small>UNTIL IFTAR</small></div></div><div class="cap">“Iftar in 11 minutes. I’m still in Business Bay.”</div></div></div></div>
{hooks(["A clock on screen: “Iftar in 11 minutes. I’m still in Business Bay.”", "“My mother doesn’t wait. Neither does iftar.”", "A silent shot of an empty chair at the table, timer running."])}
{tl([("Countdown hook",4,"#FFD23F"),("The journey",16,"#E9E1FF"),("Arrival & iftar",7,"#F7C873"),("Sign-off",3,"#7BE0C3")],30,"")}
</article>
</div></section>
<script>
(function(){{
 var r=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches; if(r) return;
 var t=document.querySelector('[data-temp]'), hot=true;
 setInterval(function(){{ hot=!hot; t.innerHTML=(hot?'46°C':'19°C')+'<small>'+(hot?'OUTSIDE':'OFFICE AC')+'</small>'; }},3000);
 var u=document.querySelector('[data-unread]'), n=47;
 setInterval(function(){{ n=n>=99?47:n+1; u.textContent=n; }},700);
 var c=document.querySelector('[data-clock]'), s=660;
 setInterval(function(){{ s=s<=0?660:s-7; var m=Math.floor(s/60), x=s%60; c.textContent=m+':'+(x<10?'0':'')+x; }},120);
}})();
</script>'''


# ---------- PLAYBOOK ----------
css_p = '''
.strip{display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x mandatory;padding:10px 4px 26px}
.stage2{flex:0 0 270px;margin:0 8px;scroll-snap-align:start;border:2px solid var(--ink);border-radius:20px;padding:22px;background:var(--card);box-shadow:5px 5px 0 var(--ink);min-height:230px}
.stage2 .n{font-family:var(--display);font-stretch:125%;font-weight:800;font-size:56px;line-height:.85;-webkit-text-stroke:1.5px var(--ink);color:transparent}
.stage2.node{border-radius:16px;box-shadow:5px 5px 0 var(--ink)}
.rulec{display:flex;flex-direction:column;background:var(--card);border:2px solid var(--ink);border-radius:16px;padding:20px;box-shadow:5px 5px 0 var(--ink)}
.rulec:nth-child(4n+1){background:var(--lime)}.rulec:nth-child(4n+3){background:var(--lilac)}
.rulec h3{font-size:21px;margin:10px 0 8px;line-height:1.05}
.rulec p{font-size:15px;color:var(--ink);opacity:.8}
.check label{display:flex;gap:12px;align-items:flex-start;padding:10px 4px;border-top:1.5px dashed rgba(18,18,18,.25);cursor:pointer;font-weight:600;font-size:16px}
.check input{appearance:none;width:22px;height:22px;flex:none;border:2px solid var(--ink);border-radius:6px;background:var(--card);display:grid;place-items:center;margin-top:1px;cursor:pointer}
.check input:checked{background:#3DDC84}
.check input:checked::after{content:"✓";font-weight:800;font-size:14px}
.check input:checked+span{text-decoration:line-through;opacity:.55}
.pbar{height:10px;border:2px solid var(--ink);border-radius:99px;overflow:hidden;margin-bottom:8px}
.pbar i{display:block;height:100%;width:0;background:#3DDC84;transition:width .3s}
.stage2 h3{font-size:24px;margin:14px 0 8px}
.stage2 p{font-size:15px;color:var(--soft)}
.flip{perspective:1000px;cursor:pointer;min-height:230px;border:0;background:none;text-align:left;font:inherit;color:inherit;padding:0}
.flip .in2{position:relative;width:100%;height:100%;min-height:230px;transition:transform .6s;transform-style:preserve-3d}
.flip.on .in2{transform:rotateY(180deg)}
.flip .f,.flip .b{position:absolute;inset:0;border:2px solid var(--ink);border-radius:20px;padding:22px;backface-visibility:hidden;box-shadow:5px 5px 0 var(--ink);display:flex;flex-direction:column}
.flip .f h3{font-size:26px;margin-top:10px}
.flip .f em{margin-top:auto;font-style:normal;font-family:var(--mono);font-size:10.5px;text-transform:uppercase}
.flip .f h3{font-size:22px}
.flip .b{transform:rotateY(180deg);background:var(--ink);color:var(--bg)}
.flip .b p{font-size:15px}
.flip .b small{margin-top:auto;font-family:var(--mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;opacity:.7}
'''
stages = [("Plan", "Monthly targets per client. Tracker, calendar and info page set up before anything else."),
 ("Cast", "Personas and life situations, not just age and gender. A vetted roster of proven creators."),
 ("Brief", "Objective, must-say claims, don’t-say list, filming specs, example scripts."),
 ("Script", "Mashup sets: fixed body and CTA, three hooks on top, so every set is a test."),
 ("Clear", "Claims, approval codes and creator consent sorted before a single frame is shot."),
 ("Check", "Footage reviewed against the brief: hook in the first seconds, claims said right."),
 ("Edit", "Brand rules turned into editing guidelines, so the first cut is close to right."),
 ("Review", "One feedback list per ad. Client status tracked apart from internal status."),
 ("Track", "Delivered vs committed, every client, every month, with reasons for anything late."),
 ("Hand over", "SOPs per team and recorded walkthroughs, so nothing depends on one person.")]
lessons = [("Lock legal before sourcing", "Tell creators up front if a script is word-for-word. Finding out after the shoot costs weeks and goodwill.", "A Costco reshoot"),
 ("Brief for the edit", "Split talking lines from silent B-roll, add a safe-zone guide and example videos.", "Creators mixing lines and actions"),
 ("Record the disclosure anyway", "Ask every regulated-brand creator for a standalone disclosure sentence, even if nobody asked yet.", "A Contact Lens legal issue"),
 ("Keep both versions", "Deliver with and without a disputed element until Legal settles the rule.", "The #ad debate"),
 ("Ask what to avoid", "Get a banned list as well as an approved list, and send it to the store and the creator.", "Build-A-Bear licensed toys"),
 ("Keep the product off the problem", "Hooks about old or wrong habits should show the problem object, never the brand.", "An Opti-Free compliance flag"),
 ("Scout creators’ own feeds", "Licensing a creator’s existing clips for a small fee beats a reshoot.", "A Systane eye-doctor ad"),
 ("One source of truth per stage", "Portal for content, one log for ads, one thread per brand for feedback.", "Feedback scattered across email and Frame.io"),
 ("Checklist before the client", "Claims, disclosures, legal lines, repeated footage, spelling, pauses.", "Typos clients kept catching"),
 ("Turn gaps into defaults", "When a brief is missing details, propose a default for each instead of sending questions.", "A Walmart brief with seven gaps"),
 ("Audit against the contract", "Compare delivered ads with what was promised every month.", "A forgotten Opti-Free campaign")]
STAGE_TOOLS = [['monday','sheets'],['instagram','tiktok'],['docs','notion'],['docs','claude'],['veeva','gmail'],['frameio'],['frameio','photoshop'],['frameio','slack'],['monday','ga4'],['notion','claude']]
RULES = [("The brief carries the rules", "Every brief template has the hook rules, a don’t-say list, filming specs and example scripts. Creators get the playbook without having to read it.", ['docs','notion']),
 ("Three hooks or it isn’t a set", "Scripts come back as 1A, 1B, 1C on a fixed body and CTA. Every set is a test.", ['docs']),
 ("Nothing reaches the client unchecked", "Every cut passes the pre-flight checklist below before it leaves the team.", ['frameio']),
 ("Claims stay as approved", "No code, no consent, no posting. The registry is linked to the ad tracker, so a gap shows up straight away.", ['veeva','monday']),
 ("Status lives on the board", "Not in DMs. Client status is tracked apart from internal status, so everyone sees the same truth.", ['monday','slack']),
 ("Refresh before it fades", "New hooks, new creators and new angles every month, before results drop.", ['sheets','tiktok']),
 ("Fridays are for fixing", "The creative team’s protected admin day, to clean up systems instead of firefighting.", ['monday']),
 ("Write it down", "SOPs and recorded walkthroughs, so nothing depends on one person, including me.", ['notion','claude'])]
CHECK = ["The hook works in 3 seconds, with the sound off", "The target viewer will think “that’s me”", "The problem is specific, not generic", "The product is shown working, not just mentioned", "Benefits are stated, not just features", "There’s a reason to believe: a peer, an expert or a number", "One clear CTA that fits the funnel stage", "It sounds like a real person, not a brand", "Captions on, format right for the platform", "All claims approved, consent signed", "At least three hooks ready to test"]
pb = """<section style="padding-bottom:20px"><div class="wrap"><span class="sticker" style="background:var(--card)">How I run a team</span>
<h1 class="big" style="margin-top:22px">Good taste doesn’t scale.<br><span style="color:var(--tomato)">Systems do.</span></h1><p class="lede">Ten stages every campaign moved through, the house rules that turned my playbook into team habit, and eleven lessons I paid for the hard way.</p></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="kicker"><span class="dot"></span><span class="mono">10 stages · who uses what</span><span class="hand">scroll sideways</span></div><div class="strip">"""
pb += ''.join(f'<div class="stage2 node"><div class="n">{i+1:02d}</div><h3>{E(t)}</h3><p>{E(d)}</p><div style="margin-top:14px">{stack(STAGE_TOOLS[i])}</div></div>' for i, (t, d) in enumerate(stages))
pb += """</div></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="kicker"><span class="dot" style="background:var(--lime)"></span><span class="mono">House rules</span><span class="hand">how the playbook becomes habit</span></div>
<h2 class="mid" style="margin-bottom:30px;max-width:18ch">A playbook only works if the team runs it without me.</h2><div class="grid g4">"""
pb += ''.join(f'<div class="rulec rv"><span class="mono">Rule {i+1:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p><div style="margin-top:auto;padding-top:14px">{stack(k)}</div></div>' for i, (t, d, k) in enumerate(RULES))
pb += """</div></div></section>
<section id="preflight" style="padding-top:10px"><div class="wrap"><div class="grid g2" style="gap:40px;align-items:start">
<div><div class="kicker"><span class="dot" style="background:var(--sun)"></span><span class="mono">Pre-flight check</span></div><h2 class="mid">Nothing ships until this says “ready”.</h2><p class="lede">Eleven questions every ad answers before a client sees it. Try it: tick them off.</p><p style="margin-top:20px"><a class="btn ghost" href="ugc.html">Why each one matters →</a></p></div>
<div class="check node" data-check><div style="display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:12px"><span class="mono">Ad 1A · review</span><span class="chip wip" data-progress>0 / 11</span></div><div class="pbar"><i data-bar></i></div>"""
pb += ''.join(f'<label><input type="checkbox"><span>{E(c)}</span></label>' for c in CHECK)
pb += """</div></div></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="kicker"><span class="dot" style="background:var(--pink)"></span><span class="mono">11 lessons</span><span class="hand">tap a card to flip it</span></div><div class="grid g4">"""
cols = ['var(--sun)', 'var(--pink)', 'var(--mint)', 'var(--card)']
pb += ''.join(f'<button class="flip" type="button" aria-pressed="false"><div class="in2"><div class="f" style="background:{cols[i%4]}"><span class="mono">Lesson {i+1:02d}</span><h3>{E(t)}</h3><em>tap →</em></div><div class="b"><p>{E(d)}</p><small>Learned from: {E(w)}</small></div></div></button>' for i, (t, d, w) in enumerate(lessons))
pb += '</div></div></section>'
page('playbook.html', 'How I run a team · Amirthashree Vijayakumar', pb, css_p)

# ---------- ABOUT ----------
css_a = '''
.path{display:flex;gap:0;flex-wrap:wrap;margin-top:34px}
.path div{flex:1 1 200px;border:2px solid var(--ink);margin:-1px;padding:20px;background:var(--card)}
.path div b{display:block;font-family:var(--display);font-stretch:112%;font-size:20px;letter-spacing:-.02em;line-height:1.1;margin:6px 0 4px}
.path div span{color:var(--soft);font-size:15px}
.receipt{background:var(--card);border:2px dashed var(--ink);border-radius:6px;padding:22px;font-size:15px;position:relative}
.receipt h3{font-size:22px;margin:6px 0 12px}
.receipt dl{display:grid;grid-template-columns:70px 1fr;gap:6px 10px}
.receipt dt{font-family:var(--mono);font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--soft);padding-top:3px}
.cloud{display:flex;flex-wrap:wrap;gap:10px}
.cloud span{border:2px solid var(--ink);border-radius:8px;padding:8px 14px;font-weight:600;background:var(--card)}
.cloud span:nth-child(3n){background:var(--sun);transform:rotate(-2deg)}
.job{display:grid;grid-template-columns:320px 1fr;border:2px solid var(--ink);border-radius:18px;overflow:hidden;background:var(--card);box-shadow:6px 6px 0 var(--ink)}
.job .side{padding:24px;border-right:2px solid var(--ink);display:flex;flex-direction:column}
.job .side h3{font-size:24px;margin:10px 0 6px}
.job ul{padding:22px 26px 22px 44px;display:grid;gap:8px;align-content:center}
.job li{font-size:16px}
.job li::marker{color:var(--tomato)}
.tgroup{display:grid;grid-template-columns:220px 1fr;gap:18px;align-items:start;padding:18px 0;border-top:2px solid var(--ink)}
.tgroup h3{font-size:19px;display:inline-block;padding:8px 12px;border:2px solid var(--ink);border-radius:8px;justify-self:start}
@media (max-width:800px){.job,.tgroup{grid-template-columns:1fr}.job .side{border-right:0;border-bottom:2px solid var(--ink)}}
.cloud span:nth-child(4n){background:var(--pink);transform:rotate(2deg)}
'''
receipts = [("The banned list", "Licensed toys appeared in Build-A-Bear shoots.", "Owned the miss and proposed a banned-brand list for every retail shoot."),
 ("Protected Fridays", "Constant pings left no time to fix systems.", "Made Fridays the creative team’s admin day."),
 ("Line by line", "A creator found word-for-word scripts robotic.", "Walked her through it line by line on a call. She agreed to reshoot the next day."),
 ("The forgotten campaign", "An agreed Opti-Free campaign had quietly never started.", "Traced it with timestamped call notes and raised it with my lead."),
 ("Nothing depends on me", "Account know-how lived in my head.", "Wrote SOPs for 8 accounts and recorded three walkthroughs before leaving.")]
about = '''<section><div class="wrap"><span class="sticker" style="background:var(--mint)">About</span>
<h1 class="big" style="margin-top:22px">Hi, I’m<br>Amirthashree.</h1>
<p class="lede">I sit between the creative idea and the finished ad. I started as an intern at a UGC agency, was rarely the most senior person in the room, and learned that you don’t need a title to lead. You need to notice what’s slipping, and care enough to fix it.</p>
<p style="margin-top:28px"><a class="btn" href="resume.pdf">Download resume (PDF)</a></p>
<div class="path rv">
 <div><span class="mono">2018–2020</span><b>MA, Mass Communication</b><span>Women’s Christian College, India</span></div>
 <div><span class="mono">2022–2024</span><b>Content &amp; social</b><span>DIVO, then Indo Overseas Films, India</span></div>
 <div><span class="mono">2024–2025</span><b>MS, Marketing &amp; Analytics</b><span>Hult, San Francisco</span></div>
 <div style="background:var(--sun)"><span class="mono">2025–2026</span><b>Creative Operations</b><span>Cipio.ai (VideoForce.ai), intern to full-time</span></div>
 <div style="background:var(--pink)"><span class="mono">Now</span><b>Dubai</b><span>Ready for the next team</span></div>
</div></div></section>
<section style="padding-top:10px"><div class="wrap"><div class="kicker"><span class="dot"></span><span class="mono">Receipts</span><span class="hand">how I lead, in real moments</span></div><div class="grid g3">'''
about += ''.join(f'<div class="receipt rv"><span class="mono">#{i+1:03d}</span><h3>{E(t)}</h3><dl><dt>Problem</dt><dd>{E(p)}</dd><dt>Move</dt><dd>{E(m)}</dd></dl></div>' for i, (t, p, m) in enumerate(receipts))
about += """<div class="receipt rv" style="background:var(--ink);color:var(--bg);border-style:solid"><span class="mono">Total</span><h3>40+ campaigns, 11 brands, every one on schedule.</h3></div></div></div></section>"""
JOBS = [("May 2025 – Oct 2026", "Creative Operations Manager", "Cipio.ai (VideoForce.ai) · USA", "var(--lime)",
  ["Promoted from intern to full-time within a year; the creative and ops focal point for 40+ campaigns across 11+ brands, including Alcon, Cox Automotive (Autotrader), Tire Agent and Vanity Fair.",
   "Led a 3-person in-house creative team and coordinated agencies, editors, creators and production partners from brief to delivery. Every campaign on schedule.",
   "Designed 20 linked Monday.com boards, including a master tracker of delivered vs committed work for every client, every month.",
   "Ran pharma approval workflows (Veeva codes, MAP approval, creator consent) with registries tying every ad to its status.",
   "Turned brand standards into editing guidelines, briefs and templates; wrote handover SOPs for 8 accounts.",
   "Used GA4 insights to refine creative: 15% engagement lift, 28% better retention on TikTok and Instagram, 18% higher CTR on UGC concepts."],
  ['monday','veeva','claude','ga4','tiktok','instagram']),
 ("Mar 2023 – Feb 2024", "Digital & Social Media Manager", "Indo Overseas Films · India", "var(--sun)",
  ["Owned the content and campaign calendar across 8+ platforms. 0% launch delays.",
   "Developed key messaging for 12 content categories, lifting brand recognition 20%.",
   "Read audience behaviour and platform trends: 30% uplift in audience relevance, 22% engagement growth, 35% higher view-completion from per-platform edits."],
  ['instagram','youtube','facebook','linkedin','sprout']),
 ("Mar 2022 – Feb 2023", "Assistant Social Media Content Producer", "DIVO · India", "var(--pink)",
  ["Partnered with editors, executive producers, talent and brand partners on briefs, scripts and ad integrations for 20+ campaigns. 28% higher engagement.",
   "Coordinated design, video and talent teams on assets and schedules at 95% execution accuracy.",
   "Built KPI dashboards that gave stakeholders real-time campaign visibility."],
  ['youtube','instagram','tableau','excel'])]
about += """<section style="padding-top:10px"><div class="wrap"><div class="kicker"><span class="dot" style="background:var(--lime)"></span><span class="mono">Experience</span><span class="hand">3+ years · India → USA → UAE</span></div><div class="grid" style="gap:22px">"""
for d, r, co, col, pts, st in JOBS:
    about += f'<article class="job rv"><div class="side" style="background:{col}"><span class="mono">{E(d)}</span><h3>{E(r)}</h3><p>{E(co)}</p><div style="margin-top:auto;padding-top:16px">{stack(st)}</div></div><ul>' + ''.join(f'<li>{E(p)}</li>' for p in pts) + '</ul></article>'
about += """</div>
<div class="grid g2" style="margin-top:22px">
 <div class="card rv"><span class="mono">Hult · Expedia Group Business Challenge</span><h3>Predictive-analytics content strategy for a global travel brand</h3><p>Personalised short-form video across TikTok, Instagram and LinkedIn: 22% more engagement, 30% less planning time.</p><div style="margin-top:14px">""" + stack(['tiktok','instagram','linkedin','tableau']) + """</div></div>
 <div class="card rv"><span class="mono">Education</span><h3 style="font-size:20px;line-height:1.25">MS Marketing &amp; Analytics, Hult International Business School, San Francisco · 2024–25</h3><p style="margin-top:8px">MBA Foundation, University Canada West · 2021<br>MA Mass Communication, Women’s Christian College · 2018–20</p></div>
</div></div></section>"""
GROUPS = [("Ops &amp; workflow", "var(--lime)", ['monday','airtable','asana','notion','slack','sheets','drive','gmail','excel']),
 ("AI &amp; agents", "var(--lilac)", ['claude','mcp','n8n']),
 ("Analytics &amp; listening", "var(--sun)", ['ga4','tableau','sprout','sprinklr','brandwatch']),
 ("Platforms", "var(--pink)", ['instagram','tiktok','linkedin','youtube','facebook','meta']),
 ("Creative &amp; review", "var(--mint)", ['photoshop','frameio','veeva','ppt','word'])]
about += """<section style="padding-top:10px"><div class="wrap"><div class="kicker"><span class="dot" style="background:var(--cobalt)"></span><span class="mono">Toolbox</span><span class="hand">apps, agents and software I’m comfy in</span></div>"""
for g, col, ks in GROUPS:
    about += f'<div class="tgroup rv"><h3 style="background:{col}">{g}</h3><div class="tools">' + ''.join(tool(k) for k in ks) + '</div></div>'
about += """<div class="cloud" style="margin-top:30px">""" + ''.join(f'<span>{E(x)}</span>' for x in ["Creative operations", "UGC strategy", "Hook writing", "Mashup ad sets", "Creator casting", "Pharma compliance", "Editor direction", "Marketing calendars", "KPI reporting", "SOPs & handovers", "Agency & freelancer management", "Competitor intelligence"]) + """</div></div></section>"""
page('about.html', 'About · Amirthashree Vijayakumar', about, css_a)
print('ok2')
