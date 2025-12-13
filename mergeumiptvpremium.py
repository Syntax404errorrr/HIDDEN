import requests
from datetime import datetime

# List of M3U source URLs
urls = [
    "http://drewlive24.duckdns.org:8081/Tims247.m3u8",
    "https://raw.githubusercontent.com/Syntax404errorrr/HIDDEN/refs/heads/main/TheTVApp.m3u",
    "https://raw.githubusercontent.com/Syntax404errorrr/HIDDEN/refs/heads/main/IPTV%20PREMIUM"
]

EPG_URL = "https://tinyurl.com/DrewLive002-epg"
output_file = "UMIPTVPREMIUM.m3u"

with open(output_file, "w", encoding="utf-8") as outfile:
    # ALWAYS write header + metadata (forces diff)
    outfile.write("#EXTM3U\n")
    outfile.write(f'#EXTM3U url-tvg="{EPG_URL}"\n')
    outfile.write(f"# Generated: {datetime.utcnow().isoformat()} UTC\n\n")

    for url in urls:
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()

            for line in response.text.splitlines():
                if not line.strip().startswith("#EXTM3U"):
                    outfile.write(line + "\n")

            print(f"✅ Downloaded and merged: {url}")

        except Exception as e:
            outfile.write(f"# ERROR fetching {url}: {e}\n")
            print(f"❌ Failed to fetch {url}: {e}")

print(f"\n🎉 Merge complete! Output saved to: {output_file}")
