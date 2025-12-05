"""
Script to process CSV comments data and prepare it for the interactive map.
This script maps comments to Indian states/regions and creates a JSON file.
"""

import csv
import json
import re
from collections import defaultdict

# State name mappings
STATE_MAPPINGS = {
    'tamil nadu': 'Tamil Nadu',
    'tamilnadu': 'Tamil Nadu',
    'tn': 'Tamil Nadu',
    'uttar pradesh': 'Uttar Pradesh',
    'up': 'Uttar Pradesh',
    'west bengal': 'West Bengal',
    'wb': 'West Bengal',
    'bengal': 'West Bengal',
    'maharashtra': 'Maharashtra',
    'maharastra': 'Maharashtra',
    'karnataka': 'Karnataka',
    'karnatka': 'Karnataka',
    'kerala': 'Kerala',
    'keral': 'Kerala',
    'gujarat': 'Gujarat',
    'gujrat': 'Gujarat',
    'rajasthan': 'Rajasthan',
    'rajastan': 'Rajasthan',
    'madhya pradesh': 'Madhya Pradesh',
    'mp': 'Madhya Pradesh',
    'andhra pradesh': 'Andhra Pradesh',
    'ap': 'Andhra Pradesh',
    'telangana': 'Telangana',
    'tg': 'Telangana',
    'odisha': 'Odisha',
    'orissa': 'Odisha',
    'punjab': 'Punjab',
    'haryana': 'Haryana',
    'bihar': 'Bihar',
    'assam': 'Assam',
    'jharkhand': 'Jharkhand',
    'chhattisgarh': 'Chhattisgarh',
    'chhatisgarh': 'Chhattisgarh',
    'himachal pradesh': 'Himachal Pradesh',
    'himachal': 'Himachal Pradesh',
    'hp': 'Himachal Pradesh',
    'uttarakhand': 'Uttarakhand',
    'uttaranchal': 'Uttarakhand',
    'goa': 'Goa',
    'delhi': 'Delhi',
    'nct': 'Delhi',
    'new delhi': 'Delhi',
    'jammu and kashmir': 'Jammu and Kashmir',
    'j&k': 'Jammu and Kashmir',
    'jammu kashmir': 'Jammu and Kashmir',
    'ladakh': 'Ladakh',
    'manipur': 'Manipur',
    'meghalaya': 'Meghalaya',
    'mizoram': 'Mizoram',
    'nagaland': 'Nagaland',
    'sikkim': 'Sikkim',
    'tripura': 'Tripura',
    'arunachal pradesh': 'Arunachal Pradesh',
    'arunachal': 'Arunachal Pradesh',
    'puducherry': 'Puducherry',
    'pondicherry': 'Puducherry',
    'chandigarh': 'Chandigarh',
    'dadra and nagar haveli': 'Dadra and Nagar Haveli',
    'dnh': 'Dadra and Nagar Haveli',
    'daman and diu': 'Daman and Diu',
    'dd': 'Daman and Diu',
    'lakshadweep': 'Lakshadweep',
    'andaman and nicobar islands': 'Andaman and Nicobar Islands',
    'a&n': 'Andaman and Nicobar Islands',
}

def normalize_state_name(region):
    """Normalize state/region name to standard format."""
    if not region or region.lower() in ['all india', 'unknown region', '']:
        return None
    
    region_lower = region.lower().strip()
    
    # Direct mapping
    if region_lower in STATE_MAPPINGS:
        return STATE_MAPPINGS[region_lower]
    
    # Check if any mapping key is contained in the region name
    for key, value in STATE_MAPPINGS.items():
        if key in region_lower or region_lower in key:
            return value
    
    # Check if region mentions a state name in comment text
    for key, value in STATE_MAPPINGS.items():
        if value.lower() in region_lower:
            return value
    
    # Return original if it looks like a valid state name (capitalized)
    if region and region[0].isupper():
        return region
    
    return None

def extract_state_from_comment(comment_text, language):
    """Try to extract state name from comment text."""
    if not comment_text:
        return None
    
    comment_lower = comment_text.lower()
    
    # Look for state mentions in comment
    for key, value in STATE_MAPPINGS.items():
        if key in comment_lower or value.lower() in comment_lower:
            return value
    
    # Look for common regional indicators
    regional_keywords = {
        'tamil': 'Tamil Nadu',
        'telugu': 'Andhra Pradesh',
        'kannada': 'Karnataka',
        'malayalam': 'Kerala',
        'marathi': 'Maharashtra',
        'gujarati': 'Gujarat',
        'bengali': 'West Bengal',
        'punjabi': 'Punjab',
        'hindi': 'Uttar Pradesh',  # Default, but could be multiple states
    }
    
    for keyword, state in regional_keywords.items():
        if keyword in comment_lower:
            return state
    
    return None

def process_csv_file(csv_file_path, output_json_path):
    """Process CSV file and create JSON output for map visualization."""
    
    region_comments = defaultdict(lambda: {
        'positive': [],
        'negative': [],
        'neutral': [],
        'all': []
    })
    
    all_comments = []
    
    print(f"Processing {csv_file_path}...")
    
    with open(csv_file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            if not row.get('comment_text'):
                continue
            
            # Get region from CSV
            region = normalize_state_name(row.get('region', ''))
            
            # If region is not found, try to extract from comment
            if not region:
                region = extract_state_from_comment(row.get('comment_text', ''), row.get('language', ''))
            
            # If still no region, skip or assign to "All India"
            if not region:
                # For "All India" comments, we can distribute them or skip
                # For now, we'll create a special category
                region = 'All India'
            
            sentiment = row.get('sentiment_label', 'neutral').lower()
            
            comment_data = {
                'text': row.get('comment_text', ''),
                'author': row.get('author', ''),
                'video_title': row.get('video_title', ''),
                'channel': row.get('channel', ''),
                'video_id': row.get('video_id', ''),
                'like_count': row.get('like_count', '0'),
                'published_at': row.get('published_at', ''),
                'sentiment': sentiment,
                'sentiment_score': row.get('sentiment', '0'),
                'language': row.get('language', ''),
            }
            
            region_comments[region]['all'].append(comment_data)
            
            if sentiment == 'positive':
                region_comments[region]['positive'].append(comment_data)
            elif sentiment == 'negative':
                region_comments[region]['negative'].append(comment_data)
            else:
                region_comments[region]['neutral'].append(comment_data)
            
            all_comments.append(comment_data)
    
    # Convert to regular dict and prepare summary
    output_data = {
        'regions': {},
        'summary': {
            'total_comments': len(all_comments),
            'total_regions': len([r for r in region_comments.keys() if r != 'All India']),
            'positive_count': sum(len(data['positive']) for data in region_comments.values()),
            'negative_count': sum(len(data['negative']) for data in region_comments.values()),
            'neutral_count': sum(len(data['neutral']) for data in region_comments.values()),
        }
    }
    
    for region, data in region_comments.items():
        output_data['regions'][region] = {
            'total': len(data['all']),
            'positive': len(data['positive']),
            'negative': len(data['negative']),
            'neutral': len(data['neutral']),
            'comments': data['all'][:10],  # Store first 10 comments per region
            'all_comments_count': len(data['all'])
        }
    
    # Save to JSON
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nProcessed {len(all_comments)} comments")
    print(f"Found {output_data['summary']['total_regions']} regions with data")
    print(f"Positive: {output_data['summary']['positive_count']}")
    print(f"Negative: {output_data['summary']['negative_count']}")
    print(f"Neutral: {output_data['summary']['neutral_count']}")
    print(f"\nOutput saved to {output_json_path}")
    
    # Print region breakdown
    print("\nTop regions by comment count:")
    sorted_regions = sorted(
        [(r, d['total']) for r, d in output_data['regions'].items() if r != 'All India'],
        key=lambda x: x[1],
        reverse=True
    )[:10]
    
    for region, count in sorted_regions:
        print(f"  {region}: {count} comments")

if __name__ == '__main__':
    import sys
    
    # Default file path
    csv_file = 'youtube_sentiment_analysis_20251122_122916/sentiment_analysis_data_20251122_122916.csv'
    output_file = 'comments_map_data.json'
    
    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    try:
        process_csv_file(csv_file, output_file)
    except FileNotFoundError:
        print(f"Error: File not found: {csv_file}")
        print("Usage: python process_comments_for_map.py [csv_file] [output_json]")
    except Exception as e:
        print(f"Error processing file: {e}")
        import traceback
        traceback.print_exc()

