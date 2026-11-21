import json
B='/home/claude/icons/node_modules/@iconify-json/'
_sets={s:json.load(open(f'{B}{s}/icons.json')) for s in ['logos','vscode-icons','simple-icons']}
def _svg(ref, color=None):
    s,k=ref.split(':'); d=_sets[s]; ic=d['icons'][k]
    w=ic.get('width',d.get('width',16)); h=ic.get('height',d.get('height',16)); l=ic.get('left',0); t=ic.get('top',0)
    body=ic['body']
    if color: body=body.replace('currentColor',color)
    fill=f' fill="{color}"' if color and s=='simple-icons' else ''
    return f'<svg width="20" height="20" viewBox="{l} {t} {w} {h}" aria-hidden="true"{fill}>{body}</svg>'
def _mono(txt,bg,fg='#fff'):
    return f'<svg width="20" height="20" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="10" fill="{bg}"/><text x="20" y="25.5" text-anchor="middle" font-family="Archivo,Arial,sans-serif" font-weight="800" font-size="{15 if len(txt)<3 else 12}" fill="{fg}">{txt}</text></svg>'
T={
 'monday':('Monday.com','logos:monday-icon'),'airtable':('Airtable','logos:airtable'),'asana':('Asana','logos:asana-icon'),
 'notion':('Notion','logos:notion-icon'),'slack':('Slack','logos:slack-icon'),'n8n':('n8n','logos:n8n-icon'),
 'sheets':('Google Sheets',('simple-icons:googlesheets','#1FA463')),'docs':('Google Docs',('simple-icons:googledocs','#4285F4')),
 'drive':('Google Drive','logos:google-drive'),'gmail':('Gmail','logos:google-gmail'),
 'excel':('Excel','vscode-icons:file-type-excel'),'ppt':('PowerPoint','vscode-icons:file-type-powerpoint'),'word':('Word','vscode-icons:file-type-word'),
 'claude':('Claude','logos:claude-icon'),'mcp':('MCP connectors','logos:model-context-protocol-icon'),
 'fireflies':('Fireflies.ai',('mono','Ff','#7B3FF2')),
 'ga4':('Google Analytics 4','logos:google-analytics'),'tableau':('Tableau','logos:tableau-icon'),
 'sprout':('Sprout Social',('fav','sproutsocial.com')),'sprinklr':('Sprinklr',('fav','sprinklr.com')),'brandwatch':('Brandwatch',('fav','brandwatch.com')),
 'instagram':('Instagram','logos:instagram-icon'),'tiktok':('TikTok','logos:tiktok-icon'),'linkedin':('LinkedIn','logos:linkedin-icon'),
 'youtube':('YouTube','logos:youtube-icon'),'facebook':('Facebook','logos:facebook'),'meta':('Meta Ads','logos:meta-icon'),
 'photoshop':('Photoshop','logos:adobe-photoshop'),'frameio':('Frame.io',('fav','frame.io')),'veeva':('Veeva',('mono','Vv','#F28C00')),
}
def svg(k):
    n,r=T[k]
    if isinstance(r,tuple):
        if r[0]=='mono': return _mono(r[1],r[2])
        if r[0]=='fav': return f'<img src="https://www.google.com/s2/favicons?domain={r[1]}&amp;sz=64" width="20" height="20" alt="" loading="lazy" decoding="async">'
        return _svg(r[0],r[1])
    return _svg(r)
def name(k): return T[k][0]
