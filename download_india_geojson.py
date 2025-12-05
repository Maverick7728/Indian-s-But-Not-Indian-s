"""
Script to download India states GeoJSON file for offline use.
This helps if the online sources are blocked or unavailable.
"""

import urllib.request
import json
import sys

GEOJSON_SOURCES = [
    {
        'name': 'GitHub - geohacker',
        'url': 'https://raw.githubusercontent.com/geohacker/india/master/state/india_telengana_29.geojson'
    },
    {
        'name': 'GitHub - Subhash9325',
        'url': 'https://raw.githubusercontent.com/Subhash9325/GeoJson-Data-of-Indian-States/master/Indian_States.json'
    },
    {
        'name': 'Gist - jbrobst',
        'url': 'https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson'
    }
]

def download_geojson(url, output_file='india_states.geojson'):
    """Download GeoJSON file from URL."""
    try:
        print(f"Downloading from: {url}")
        with urllib.request.urlopen(url, timeout=10) as response:
            data = response.read()
            geojson = json.loads(data.decode('utf-8'))
            
            # Validate it's a valid GeoJSON
            if not (geojson.get('type') == 'FeatureCollection' or geojson.get('features')):
                raise ValueError("Invalid GeoJSON format")
            
            # Save to file
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(geojson, f, indent=2, ensure_ascii=False)
            
            print(f"Successfully downloaded and saved to: {output_file}")
            print(f"   Features found: {len(geojson.get('features', []))}")
            return True
    except Exception as e:
        print(f"Failed: {e}")
        return False

def main():
    print("=" * 60)
    print("India States GeoJSON Downloader")
    print("=" * 60)
    print()
    
    output_file = 'india_states.geojson'
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
    
    # Try each source
    for source in GEOJSON_SOURCES:
        print(f"\nTrying source: {source['name']}")
        if download_geojson(source['url'], output_file):
            print(f"\nSuccess! GeoJSON file saved as: {output_file}")
            print("   You can now use this file with the map visualization.")
            return
    
    print("\nAll sources failed. Possible reasons:")
    print("   - No internet connection")
    print("   - GitHub is blocked in your region")
    print("   - Firewall/proxy blocking the requests")
    print("\nAlternative: Manually download a GeoJSON file from:")
    print("   - https://github.com/geohacker/india")
    print("   - https://github.com/Subhash9325/GeoJson-Data-of-Indian-States")
    print("   - Or search for 'India states GeoJSON' on GitHub")

if __name__ == '__main__':
    main()

