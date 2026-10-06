import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update project count in HTML
content = content.replace('>05 projects</span>', '>03 projects</span>')

# 2. Update HTML rows
html_rows_old = re.search(r'<div class="proj-row" data-index="0".*?Aether Social Platform.*?</div>\s*</div>\s*</div>', content, flags=re.DOTALL)
if html_rows_old:
    new_html = '''<div class="proj-row" data-index="0" onclick="window.open('https://mind-app-omega.vercel.app/', '_blank')" style="display:flex;align-items:center;justify-content:space-between;padding:28px 0;border-top:1px solid rgba(178,213,229,.08);cursor:pointer;transition:border-color .3s;">
        <div style="display:flex;align-items:baseline;gap:24px;">
          <span class="proj-num" style="font-family:'JetBrains Mono',monospace;font-size:.62rem;color:rgba(245,245,245,.5);transition:color .3s;">01</span>
          <h3 class="proj-title" style="font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(1.8rem,3.5vw,3rem);font-weight:800;letter-spacing:-.025em;color:rgba(245,245,245,.55);transition:color .35s,letter-spacing .35s;">Mind App</h3>
        </div>
        <div style="display:flex;align-items:center;gap:24px;">
          <span style="font-family:'JetBrains Mono',monospace;font-size:.6rem;letter-spacing:.14em;color:#C6FF34;opacity:0;transition:opacity .3s;" class="proj-cat">FULLSTACK</span>
          <span style="font-family:'JetBrains Mono',monospace;font-size:.6rem;color:rgba(245,245,245,.5);">2025</span>
          <span class="proj-arrow" aria-hidden="true" style="font-size:1.1rem;color:rgba(245,245,245,.5);transition:transform .35s,color .3s;display:inline-block;">↗</span>
        </div>
      </div>

      <div class="proj-row" data-index="1" onclick="window.open('https://forja-hypertrophy.vercel.app/', '_blank')" style="display:flex;align-items:center;justify-content:space-between;padding:28px 0;border-top:1px solid rgba(178,213,229,.08);cursor:pointer;transition:border-color .3s;">
        <div style="display:flex;align-items:baseline;gap:24px;">
          <span class="proj-num" style="font-family:'JetBrains Mono',monospace;font-size:.62rem;color:rgba(245,245,245,.5);transition:color .3s;">02</span>
          <h3 class="proj-title" style="font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(1.8rem,3.5vw,3rem);font-weight:800;letter-spacing:-.025em;color:rgba(245,245,245,.55);transition:color .35s,letter-spacing .35s;">Forja — Hypertrophy App</h3>
        </div>
        <div style="display:flex;align-items:center;gap:24px;">
          <span style="font-family:'JetBrains Mono',monospace;font-size:.6rem;letter-spacing:.14em;color:#B2D5E5;opacity:0;transition:opacity .3s;" class="proj-cat">FULLSTACK</span>
          <span style="font-family:'JetBrains Mono',monospace;font-size:.6rem;color:rgba(245,245,245,.5);">2025</span>
          <span class="proj-arrow" aria-hidden="true" style="font-size:1.1rem;color:rgba(245,245,245,.5);transition:transform .35s,color .3s;display:inline-block;">↗</span>
        </div>
      </div>

      <div class="proj-row" data-index="2" onclick="window.open('https://cyraquiz-frontend.vercel.app/', '_blank')" style="display:flex;align-items:center;justify-content:space-between;padding:28px 0;border-top:1px solid rgba(178,213,229,.08);border-bottom:1px solid rgba(178,213,229,.08);cursor:pointer;transition:border-color .3s;">
        <div style="display:flex;align-items:baseline;gap:24px;">
          <span class="proj-num" style="font-family:'JetBrains Mono',monospace;font-size:.62rem;color:rgba(245,245,245,.5);transition:color .3s;">03</span>
          <h3 class="proj-title" style="font-family:'Bricolage Grotesque',sans-serif;font-size:clamp(1.8rem,3.5vw,3rem);font-weight:800;letter-spacing:-.025em;color:rgba(245,245,245,.55);transition:color .35s,letter-spacing .35s;">CyraQuiz</h3>
        </div>
        <div style="display:flex;align-items:center;gap:24px;">
          <span style="font-family:'JetBrains Mono',monospace;font-size:.6rem;letter-spacing:.14em;color:#C6FF34;opacity:0;transition:opacity .3s;" class="proj-cat">FULLSTACK</span>
          <span style="font-family:'JetBrains Mono',monospace;font-size:.6rem;color:rgba(245,245,245,.5);">2025</span>
          <span class="proj-arrow" aria-hidden="true" style="font-size:1.1rem;color:rgba(245,245,245,.5);transition:transform .35s,color .3s;display:inline-block;">↗</span>
        </div>
      </div>
    </div>'''
    content = content[:html_rows_old.start()] + new_html + content[html_rows_old.end():]
else:
    print("Could not find HTML rows")

# 3. Update projects array in JS
projects_js_old = re.search(r'const projects = \[.*?\];', content, flags=re.DOTALL)
if projects_js_old:
    new_js = '''const projects = [
    {
      cat:'FULLSTACK', catColor:'#C6FF34',
      title:'Mind App',
      desc:'Productivity system unifying tasks, habits, and 12-week goals with wellbeing metrics.',
      tags:['React','Node.js','PostgreSQL'],
      bg:'linear-gradient(135deg,#050e1e,#0c1e38)',
      thumb:`<svg viewBox="0 0 88 88" width="88" height="88"><defs><linearGradient id="t0" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#C6FF34" stop-opacity=".3"/><stop offset="100%" stop-color="#B2D5E5" stop-opacity=".1"/></linearGradient></defs><rect width="88" height="88" fill="#050e1e"/><rect x="10" y="10" width="68" height="68" rx="5" fill="none" stroke="rgba(178,213,229,.2)" stroke-width="1"/><rect x="18" y="22" width="32" height="5" rx="2.5" fill="rgba(198,255,52,.35)"/><rect x="18" y="33" width="50" height="3" rx="1.5" fill="rgba(178,213,229,.2)"/><rect x="18" y="41" width="38" height="3" rx="1.5" fill="rgba(178,213,229,.14)"/><rect x="18" y="52" width="24" height="16" rx="8" fill="url(#t0)" stroke="rgba(198,255,52,.4)" stroke-width="1"/></svg>`,
      link: 'https://mind-app-omega.vercel.app/'
    },
    {
      cat:'FULLSTACK', catColor:'#B2D5E5',
      title:'Forja — Hypertrophy App',
      desc:'Premium training intelligence platform for serious athletes with progressive logic.',
      tags:['Astro','TypeScript','PostgreSQL'],
      bg:'linear-gradient(135deg,#120820,#1e0f32)',
      thumb:`<svg viewBox="0 0 88 88" width="88" height="88"><rect width="88" height="88" fill="#120820"/><circle cx="44" cy="44" r="32" fill="none" stroke="rgba(198,255,52,.13)" stroke-width="1" stroke-dasharray="5 9"/><circle cx="44" cy="44" r="21" fill="none" stroke="rgba(178,213,229,.2)" stroke-width="1"/><circle cx="44" cy="44" r="10" fill="rgba(198,255,52,.07)" stroke="rgba(198,255,52,.35)" stroke-width="1.5"/><line x1="12" y1="44" x2="76" y2="44" stroke="rgba(178,213,229,.1)" stroke-width="1"/><line x1="44" y1="12" x2="44" y2="76" stroke="rgba(178,213,229,.1)" stroke-width="1"/><text x="44" y="48" text-anchor="middle" font-family="monospace" font-size="9" fill="rgba(198,255,52,.65)">◎</text></svg>`,
      link: 'https://forja-hypertrophy.vercel.app/'
    },
    {
      cat:'FULLSTACK', catColor:'#C6FF34',
      title:'CyraQuiz',
      desc:'Real-time interactive educational quiz platform with AI generation and teacher dashboard.',
      tags:['React','Node.js','Sockets'],
      bg:'linear-gradient(135deg,#5A0E24,#851535)',
      thumb:`<svg viewBox="0 0 88 88" width="88" height="88"><rect width="88" height="88" fill="#5A0E24"/><text x="10" y="30" font-family="monospace" font-size="7" fill="rgba(245,245,245,.7)">? CYRA</text><text x="10" y="44" font-family="monospace" font-size="7" fill="rgba(255,218,179,.9)"># JOIN 1234</text><text x="10" y="58" font-family="monospace" font-size="7" fill="rgba(245,245,245,.7)">→ START</text><text x="10" y="72" font-family="monospace" font-size="8" fill="rgba(245,245,245,.2)">▊</text></svg>`,
      link: 'https://cyraquiz-frontend.vercel.app/'
    }
  ];'''
    content = content[:projects_js_old.start()] + new_js + content[projects_js_old.end():]
else:
    print("Could not find projects JS array")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
