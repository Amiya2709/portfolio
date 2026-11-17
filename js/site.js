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
})();
