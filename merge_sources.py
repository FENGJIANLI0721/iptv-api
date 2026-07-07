import urllib.request, os

sources = {
    'imDazui': 'https://raw.githubusercontent.com/imDazui/Tvlist-awesome-m3u-m3u8/master/m3u/国内电视台202509.m3u',
    'sports': 'https://iptv-org.github.io/iptv/categories/sports.m3u',
    'ent': 'https://iptv-org.github.io/iptv/categories/entertainment.m3u',
    'movies': 'https://iptv-org.github.io/iptv/categories/movies.m3u',
    'news': 'https://iptv-org.github.io/iptv/categories/news.m3u',
    'general': 'https://iptv-org.github.io/iptv/categories/general.m3u',
    'hk': 'https://iptv-org.github.io/iptv/countries/hk.m3u',
    'tw': 'https://iptv-org.github.io/iptv/countries/tw.m3u',
    'jp': 'https://iptv-org.github.io/iptv/countries/jp.m3u',
    'kr': 'https://iptv-org.github.io/iptv/countries/kr.m3u',
    'us': 'https://iptv-org.github.io/iptv/countries/us.m3u',
    'gb': 'https://iptv-org.github.io/iptv/countries/gb.m3u',
}

seen = set()
output = '#EXTM3U
# IPTV merged list
'
total = 0

for name, url in sources.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req, timeout=30).read().decode('utf-8', errors='replace')
        for line in data.split('
'):
            s = line.strip()
            if not s or s.startswith('#EXTM3U'): continue
            if s.startswith('#EXTINF'):
                output += s + '
'
            elif s.startswith('http') and s not in seen:
                seen.add(s)
                output += s + '
'
                total += 1
    except:
        pass

os.makedirs('output', exist_ok=True)
with open('output/result.m3u', 'w', encoding='utf-8') as f:
    f.write(output)
print(f'Done: {total} channels')
