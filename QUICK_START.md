# Quick Start Guide - India Comments Map

## 🚀 Quick Start (3 Steps)

### Step 1: Process Your Data
```bash
python process_comments_for_map.py
```
This creates `comments_map_data.json` from your CSV file.

### Step 2: Open the Map
Simply open `india_comments_map.html` in your web browser (Chrome, Firefox, Edge, etc.)

### Step 3: Explore!
- Hover over any state/region on the map to see comments
- Use filters to view specific sentiments
- Check the statistics panel for overall insights

## 📋 What You Get

✅ **Interactive Map**: Hover over Indian states to see regional comments  
✅ **Sentiment Visualization**: Color-coded regions (Green=Positive, Red=Negative, Gray=Neutral)  
✅ **Comment Details**: See actual comments, video info, and sentiment on hover  
✅ **Statistics**: Total comments, sentiment breakdown, region counts  
✅ **Filtering**: Filter by sentiment type or specific regions  

## 🎯 Example Usage

1. **Process your latest data**:
   ```bash
   python process_comments_for_map.py youtube_sentiment_analysis_20251122_122916/sentiment_analysis_data_20251122_122916.csv
   ```

2. **Open `india_comments_map.html`** in your browser

3. **Hover over states** like:
   - Tamil Nadu (186 comments)
   - Uttar Pradesh (642 comments)
   - Maharashtra (132 comments)

4. **See the tooltip** showing:
   - Comment count
   - Sentiment breakdown
   - Sample comments with video information

## 📊 Current Data Summary

Based on your processed data:
- **Total Comments**: 2,491
- **Regions**: 25 states/regions
- **Positive**: 750 comments
- **Negative**: 535 comments
- **Neutral**: 1,206 comments

**Top Regions**:
1. Uttar Pradesh: 642 comments
2. Madhya Pradesh: 236 comments
3. Tamil Nadu: 186 comments
4. Maharashtra: 132 comments
5. Andhra Pradesh: 118 comments

## 💡 Tips

- **For better performance**: Use the processed JSON file instead of loading large CSV files
- **For custom data**: Upload your CSV/JSON file using the file input in the controls
- **For offline use**: The map requires internet for initial load (D3.js and TopoJSON libraries)

## 🐛 Troubleshooting

**Map not showing?**
- Check internet connection (needed for map libraries)
- Try refreshing the page

**No data visible?**
- Make sure `comments_map_data.json` is in the same folder as the HTML file
- Or upload your CSV/JSON file manually

**States not matching?**
- The Python script handles state name variations automatically
- Process your CSV first for best results

## 📁 Files Created

- `india_comments_map.html` - The interactive map visualization
- `process_comments_for_map.py` - Data processing script
- `comments_map_data.json` - Processed data (created after running the script)
- `README_MAP.md` - Detailed documentation

Enjoy exploring your comments data on the map! 🗺️✨

