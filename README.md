# VIBE - YouTube Sentiment Analysis & Geographic Visualization

A comprehensive Python-based project for collecting YouTube comments, performing multilingual sentiment analysis, and visualizing sentiment distribution across Indian states using an interactive map.

## 🌟 Features

- **YouTube Data Collection**: Fetch comments from YouTube videos using YouTube Data API v3
- **Multilingual Support**: Handles comments in multiple Indian languages with translation capabilities
- **Sentiment Analysis**: Uses VADER sentiment analysis for accurate sentiment classification
- **Geographic Mapping**: Maps comments to Indian states and visualizes sentiment distribution
- **Interactive Visualization**: Interactive HTML map showing regional sentiment patterns
- **Data Processing**: Comprehensive data processing pipeline with multiple output formats

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Data Formats](#-data-formats)
- [Sentiment Analysis](#-sentiment-analysis)
- [Map Visualization](#-map-visualization)
- [API Setup](#-api-setup)
- [Contributing](#-contributing)

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- YouTube Data API v3 key
- Internet connection for API calls and map libraries

### Install Dependencies

```bash
pip install vaderSentiment textblob googletrans==4.0.0-rc1 langdetect geopandas folium wordcloud nltk emoji contractions googleapiclient pandas
```

Or install from the notebook:
```python
%pip install vaderSentiment textblob googletrans==4.0.0-rc1 langdetect geopandas folium wordcloud nltk emoji contractions
```

## 📁 Project Structure

```
VIBE/
├── youtube_multilingual_mapping.ipynb  # Main Jupyter notebook for data collection & analysis
├── process_comments_for_map.py         # Process CSV data for map visualization
├── download_india_geojson.py           # Download India states GeoJSON data
├── evaluate_vader_accuracy.py          # Evaluate VADER sentiment accuracy
├── india_comments_map.html             # Interactive map visualization
├── comments_map_data.json              # Processed data for map (generated)
├── india_states.geojson                # GeoJSON data for Indian states
├── QUICK_START.md                      # Quick start guide for map visualization
├── README_MAP.md                       # Detailed map documentation
└── youtube_sentiment_analysis_*/       # Output folders with sentiment data
    └── sentiment_analysis_data_*.csv   # CSV files with analyzed comments
```

## 🎯 Quick Start

### 1. Collect YouTube Comments

Open `youtube_multilingual_mapping.ipynb` and follow these steps:

1. **Set up your YouTube API key**:
   ```python
   api_key = "YOUR_API_KEY_HERE"
   ```

2. **Define video IDs** to analyze:
   ```python
   video_ids = ['VIDEO_ID_1', 'VIDEO_ID_2']
   ```

3. **Run the notebook** to:
   - Fetch comments from videos
   - Detect languages
   - Translate non-English comments
   - Perform sentiment analysis
   - Map comments to Indian regions
   - Save results to CSV

### 2. Create Interactive Map

```bash
python process_comments_for_map.py
```

This processes the latest CSV file and creates `comments_map_data.json`.

### 3. View Results

Open `india_comments_map.html` in your web browser to see the interactive visualization.

## 📖 Usage

### YouTube Comment Collection

The main notebook (`youtube_multilingual_mapping.ipynb`) provides functions to:

**Get Video Details**:
```python
video_details = get_video_details(video_id)
```

**Fetch Comments**:
```python
comments = get_comments(video_id, max_results=200)
```

**Process Multiple Videos**:
```python
all_comments = process_multiple_videos(video_ids, max_comments_per_video=200)
```

### Sentiment Analysis

The project uses **VADER (Valence Aware Dictionary and sEntiment Reasoner)** for sentiment analysis:

- **Positive**: Compound score ≥ 0.05
- **Negative**: Compound score ≤ -0.05
- **Neutral**: Compound score between -0.05 and 0.05

Evaluate VADER accuracy:
```bash
python evaluate_vader_accuracy.py
```

### Geographic Mapping

Comments are automatically mapped to Indian states based on:
- Explicit state mentions in comments
- Location data from user profiles
- Channel information
- Video metadata

**State Mapping Features**:
- Handles multiple name variations (e.g., "Tamil Nadu", "Tamilnadu", "TN")
- Supports 28 states and 8 union territories
- Intelligent fallback to "All India" for unidentifiable locations

### Map Processing

Process comments for visualization:

```bash
# Use default (latest CSV)
python process_comments_for_map.py

# Specify input and output files
python process_comments_for_map.py input_file.csv output_data.json
```

### Download GeoJSON Data

If you need offline GeoJSON data:

```bash
python download_india_geojson.py
```

## 📊 Data Formats

### CSV Output Format

Generated files contain these columns:
- `videoId`: YouTube video identifier
- `video_title`: Title of the video
- `channel`: Channel name
- `comment_text`: Original comment text
- `translated_text`: English translation (if applicable)
- `detected_language`: Language detected in comment
- `author`: Comment author username
- `likeCount`: Number of likes on comment
- `publishedAt`: Comment publication date
- `sentiment`: VADER compound sentiment score (-1 to 1)
- `sentiment_label`: Classification (positive/negative/neutral)
- `region`: Mapped Indian state/region

### JSON Output Format

Processed map data structure:
```json
{
  "regions": {
    "Tamil Nadu": {
      "total": 186,
      "positive": 80,
      "negative": 50,
      "neutral": 56,
      "comments": [
        {
          "text": "Great video!",
          "sentiment": 0.8,
          "video_title": "...",
          "channel": "..."
        }
      ]
    }
  },
  "summary": {
    "total_comments": 2491,
    "total_regions": 25,
    "positive": 750,
    "negative": 535,
    "neutral": 1206
  }
}
```

## 🗺️ Map Visualization

The interactive map provides:

### Visual Features
- **Color-coded states**: Green (positive), Red (negative), Gray (neutral)
- **Hover tooltips**: Show comment count, sentiment breakdown, and sample comments
- **Sentiment filters**: Filter by positive, negative, or neutral sentiments
- **Statistics panel**: Overall metrics and insights

### Using the Map

1. **Open** `india_comments_map.html` in a web browser
2. **Hover** over states to see comment details
3. **Click filters** to show specific sentiment types
4. **Upload** custom CSV/JSON files using the file input
5. **Explore** regional sentiment patterns

For detailed map instructions, see [QUICK_START.md](QUICK_START.md) or [README_MAP.md](README_MAP.md).

## 🔑 API Setup

### YouTube Data API v3

1. **Create a Google Cloud Project**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project

2. **Enable YouTube Data API v3**:
   - Navigate to "APIs & Services" > "Library"
   - Search for "YouTube Data API v3"
   - Click "Enable"

3. **Create API Credentials**:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "API Key"
   - Copy your API key

4. **Add to Project**:
   ```python
   api_key = "YOUR_API_KEY_HERE"
   youtube = build('youtube', 'v3', developerKey=api_key)
   ```

### API Quota Limits

- YouTube API has daily quota limits (typically 10,000 units/day)
- Each comment fetch uses approximately 1-5 units
- Plan your data collection accordingly

## 🎓 Use Cases

This project is ideal for:
- **Research**: Analyzing regional sentiment patterns on social media
- **Marketing**: Understanding audience sentiment across different regions
- **Education**: Learning sentiment analysis and data visualization
- **Content Analysis**: Tracking video performance across demographics
- **Geographic Studies**: Studying regional variations in online discourse

## 📈 Sample Results

Based on collected data (as of latest run):
- **Total Comments Analyzed**: 2,491
- **Regions Covered**: 25 Indian states/regions
- **Sentiment Distribution**: 
  - Positive: 30.1%
  - Negative: 21.5%
  - Neutral: 48.4%
- **Top Regions**: Uttar Pradesh (642), Madhya Pradesh (236), Tamil Nadu (186)

## 🔧 Troubleshooting

### Common Issues

**API Key Error**:
- Ensure API key is valid and YouTube Data API v3 is enabled
- Check quota limits haven't been exceeded

**Translation Errors**:
- `googletrans` may have rate limits; add delays between requests
- Consider using alternative translation APIs for large datasets

**Map Not Loading**:
- Check internet connection (required for D3.js and TopoJSON libraries)
- Ensure `comments_map_data.json` is in the same directory as HTML file

**State Mapping Issues**:
- Review and update `STATE_MAPPINGS` dictionary in `process_comments_for_map.py`
- Add custom state variations as needed

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Additional language support
- More sophisticated region detection algorithms
- Enhanced visualization features
- Performance optimizations for large datasets
- Integration with other social media platforms

## 📄 License

This project is created for educational purposes as part of BML Munjal University coursework.

## 🙏 Acknowledgments

- **VADER Sentiment**: Hutto, C.J. & Gilbert, E.E. (2014)
- **YouTube Data API**: Google LLC
- **D3.js & TopoJSON**: Interactive visualization libraries
- **NLTK**: Natural Language Toolkit
- **GeoJSON Data**: Indian states geographic boundaries

## 📞 Support

For questions or issues:
- Review the [QUICK_START.md](QUICK_START.md) guide
- Check [README_MAP.md](README_MAP.md) for map-specific help
- Examine sample CSV files in output folders for data format reference

---

**Project**: VIBE (YouTube Sentiment Analysis & Visualization)  
**Institution**: BML Munjal University  
**Academic Year**: 4th Year, 7th Semester  
**Last Updated**: December 2025
