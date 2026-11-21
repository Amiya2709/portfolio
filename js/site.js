(function(){
  document.documentElement.classList.add('js');
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  // videos: play when visible, click toggles sound (one at a time)
  var vids = [].slice.call(document.querySelectorAll('video'));
  function label(v){ var b=v.parentNode.querySelector('.snd'); if(b) b.textContent = v.muted ? 'Sound off' : 'Sound on'; }
  if('IntersectionObserver' in window && !reduce){
    var io = new IntersectionObserver(function(es){ es.forEach(function(e){ var v=e.target;
      if(e.isIntersecting){ if(v.preload==='none') v.preload='auto'; var p=v.play(); if(p&&p.catch)p.catch(function(){}); } else v.pause(); }); },{threshold:.3});
    vids.forEach(function(v){ io.observe(v); });
  }
  function toggle(v){ vids.forEach(function(o){ if(o!==v){o.muted=true;label(o);} }); v.muted=!v.muted; label(v); var p=v.play(); if(p&&p.catch)p.catch(function(){}); }
  document.querySelectorAll('.frame').forEach(function(f){ var v=f.querySelector('video'); if(!v || f.closest('a')) return;
    f.setAttribute('tabindex','0');
    f.addEventListener('click',function(){toggle(v);});
    f.addEventListener('keydown',function(e){ if(e.key==='Enter'||e.key===' '){e.preventDefault();toggle(v);} }); });

  // reveal on scroll (content is visible at rest)
  if('IntersectionObserver' in window){
    var ro = new IntersectionObserver(function(es){ es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); ro.unobserve(e.target);} }); },{threshold:.12});
    document.querySelectorAll('.rv').forEach(function(el){ ro.observe(el); });
  } else document.querySelectorAll('.rv').forEach(function(el){ el.classList.add('in'); });

  // count-up numbers
  document.querySelectorAll('[data-count]').forEach(function(el){
    var end=+el.getAttribute('data-count'), suf=el.getAttribute('data-suffix')||'', pre=el.getAttribute('data-prefix')||'';
    if(reduce){ return; }
    var started=false;
    var o=new IntersectionObserver(function(es){ if(es[0].isIntersecting && !started){ started=true; var t0=performance.now();
      (function step(t){ var k=Math.min(1,(t-t0)/1100); el.textContent=pre+Math.round(end*(1-Math.pow(1-k,3)))+suf; if(k<1) requestAnimationFrame(step); })(t0); } });
    o.observe(el);
  });

  // rotating words
  document.querySelectorAll('[data-rotate]').forEach(function(el){
    var words=el.getAttribute('data-rotate').split('|'), i=0;
    if(reduce) return;
    setInterval(function(){ i=(i+1)%words.length; el.style.opacity=0; setTimeout(function(){ el.textContent=words[i]; el.style.opacity=1; },220); },2200);
  });

  // flip cards
  document.querySelectorAll('.flip').forEach(function(c){
    c.addEventListener('click',function(){ c.classList.toggle('on'); c.setAttribute('aria-pressed', c.classList.contains('on')); });
  });

  // pipeline: light up each stage in turn
  document.querySelectorAll('[data-pipe]').forEach(function(p){
    var st=p.querySelectorAll('.st'), i=0; if(!st.length) return;
    st[0].classList.add('on'); if(reduce) return;
    setInterval(function(){ st[i].classList.remove('on'); i=(i+1)%st.length; st[i].classList.add('on'); },1100);
  });

  // agent console: types a sample run
  document.querySelectorAll('[data-console]').forEach(function(box){
    var L=[['> ','pull delivered vs committed from monday.com, all clients'],['ok','every client checked · late items listed with reasons'],
           ['> ','how many veeva codes are left for systane?'],['ok','running low · new batch requested before it blocks a shoot'],
           ['> ','draft the tire agent handover SOP from drive + slack'],['ok','draft ready · checking it against the source first'],
           ['> ','summarise this week’s creator feedback from slack'],['ok','3 themes found · brief update drafted for review']];
    if(reduce){ box.innerHTML=L.map(function(l){return '<p>'+(l[0]==='ok'?'<span class="ok">✓ </span>':'<span class="tag">› </span>')+l[1]+'</p>';}).join(''); return; }
    var li=0, ci=0, cur;
    function next(){
      if(li>=L.length){ setTimeout(function(){ box.innerHTML=''; li=0; next(); },3500); return; }
      var l=L[li]; cur=document.createElement('p');
      cur.innerHTML=(l[0]==='ok'?'<span class="ok">✓ </span>':'<span class="tag">› </span>')+'<span class="t"></span><span class="cur"></span>';
      [].forEach.call(box.querySelectorAll('.cur'),function(c){c.remove();});
      box.appendChild(cur); var t=cur.querySelector('.t'); ci=0;
      (function type(){ t.textContent=l[1].slice(0,++ci); if(ci<l[1].length) setTimeout(type,l[0]==='ok'?8:28); else { li++; setTimeout(next,l[0]==='ok'?900:350); } })();
    }
    var started=false, o=new IntersectionObserver(function(es){ if(es[0].isIntersecting&&!started){started=true;next();} }); o.observe(box);
  });

  // checklist with progress
  document.querySelectorAll('[data-check]').forEach(function(wrap){
    var boxes=wrap.querySelectorAll('input[type=checkbox]'), out=wrap.querySelector('[data-progress]'), bar=wrap.querySelector('[data-bar]');
    function upd(){ var n=[].filter.call(boxes,function(b){return b.checked;}).length;
      out.textContent = n===boxes.length ? '✓ Ready to ship' : n+' / '+boxes.length+' · not ready';
      out.className = 'chip ' + (n===boxes.length?'ok':'wip'); bar.style.width=(n/boxes.length*100)+'%'; }
    [].forEach.call(boxes,function(b){ b.addEventListener('change',upd); }); upd();
  });

  // tabs/toggles: [data-tabs] buttons switch panels
  document.querySelectorAll('[data-tabs]').forEach(function(g){
    var btns=g.querySelectorAll('[data-tab]'), pans=g.querySelectorAll('[data-pane]');
    [].forEach.call(btns,function(b){ b.addEventListener('click',function(){
      [].forEach.call(btns,function(x){x.setAttribute('aria-pressed', x===b);});
      [].forEach.call(pans,function(p){p.hidden = p.getAttribute('data-pane')!==b.getAttribute('data-tab');}); }); });
  });
})();
