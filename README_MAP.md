# India Comments Sentiment Map

An interactive map visualization that displays YouTube comments and their sentiment analysis across different regions of India.

## Features

- 🗺️ **Interactive India Map**: Hover over states to see comments and sentiment data
- 📊 **Sentiment Visualization**: Color-coded regions based on positive/negative/neutral comments
- 💬 **Comment Details**: View sample comments, video information, and sentiment scores on hover
- 📈 **Statistics Dashboard**: See total comments, sentiment breakdown, and region counts
- 🔍 **Filtering**: Filter by sentiment type or specific regions
- 📁 **Multiple Data Formats**: Supports both CSV and JSON input files

## How to Use

### Option 1: Using Processed JSON Data (Recommended)

1. **Process your CSV data**:
   ```bash
   python process_comments_for_map.py
   ```
   
   Or specify custom files:
   ```bash
   python process_comments_for_map.py path/to/your/data.csv output.json
   ```

2. **Open the HTML file**:
   - Simply open `india_comments_map.html` in a web browser
   - The script will automatically try to load `comments_map_data.json` if available
   - Or use the "Load Default Data" button

### Option 2: Using CSV Directly

1. **Open the HTML file** in a web browser
2. **Upload your CSV file** using the file input in the controls section
3. The map will automatically process and display the data

### Option 3: Using JSON File

1. **Process your data** using the Python script to create a JSON file
2. **Upload the JSON file** using the file input
3. The map will load the pre-processed data

## Data Format

### CSV Format Expected:
The CSV should contain the following columns:
- `region`: State/region name (e.g., "Tamil Nadu", "Uttar Pradesh", "All India")
- `sentiment_label`: Sentiment classification ("positive", "negative", "neutral")
- `comment_text`: The comment text
- `video_title`: Title of the video
- `channel`: Channel name
- `author`: Comment author
- `sentiment`: Sentiment score
- Other metadata fields are optional

### JSON Format (from Python script):
```json
{
  "regions": {
    "Tamil Nadu": {
      "total": 150,
      "positive": 80,
      "negative": 50,
      "neutral": 20,
      "comments": [...]
    }
  },
  "summary": {
    "total_comments": 1000,
    "total_regions": 15,
    ...
  }
}
```

## State/Region Mapping

The tool automatically maps various state name formats to standard names:
- "Tamil Nadu", "Tamilnadu", "TN" → Tamil Nadu
- "Uttar Pradesh", "UP" → Uttar Pradesh
- "West Bengal", "WB", "Bengal" → West Bengal
- And many more variations...

## Features Explained

### Map Colors:
- **Green**: Regions with predominantly positive comments
- **Red**: Regions with predominantly negative comments
- **Gray**: Regions with predominantly neutral comments
- **Yellow**: Regions with mixed sentiments

### Hover Tooltip:
When you hover over a state, you'll see:
- State name
- Total comment count
- Sentiment breakdown (positive/negative/neutral counts)
- Sample comments (up to 3)
- Video information for each comment
- Sentiment badges

### Statistics Panel:
- Total Comments: Sum of all comments across all regions
- Positive Comments: Count of positive sentiment comments
- Negative Comments: Count of negative sentiment comments
- Regions with Data: Number of states/regions that have comments

## Troubleshooting

### Map not loading?
- Check your internet connection (map data is loaded from a CDN)
- Try using a local GeoJSON file if the CDN is blocked

### No data showing?
- Ensure your CSV/JSON file is properly formatted
- Check that the `region` column in CSV contains valid state names
- Try processing the CSV with the Python script first

### States not matching?
- The Python script includes better state name normalization
- Process your CSV first to get better region matching

## Browser Compatibility

- Chrome/Edge (recommended)
- Firefox
- Safari
- Modern browsers with JavaScript enabled

## Dependencies

The HTML file uses:
- D3.js v7 (for map rendering)
- TopoJSON (for map data processing)

All dependencies are loaded from CDN, so an internet connection is required for the initial load.

## Notes

- "All India" comments: Comments marked as "All India" are currently excluded from state-specific visualization. You can modify the code to distribute them across states if needed.
- Large datasets: For very large CSV files (>10MB), consider processing them with the Python script first to create a smaller JSON file.
- Performance: The map works best with processed JSON data for faster loading.

## Future Enhancements

- Click on states to see all comments in a sidebar
- Export filtered data
- Time-based filtering
- Language-based filtering
- More detailed statistics per region

