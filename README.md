

# Language Detection, Translation, and Heatmap Visualization

This project is designed to detect the language of a given input text, find the closest language, translate the text to that language, and visualize language distribution and population density using a heatmap.

## Features

- **Language Detection**: Uses `langid` to detect the language of the input text.
- **Language Closeness**: Identifies the closest language to the detected one based on similarity and translation options.
- **Translation**: Translates the text into the closest language using `googletrans`.
- **Heatmap Visualization**: Displays a heatmap showing the geographic distribution of the detected language and population density using `folium`.
- **Wikidata Integration**: Fetches the geographic locations (latitude and longitude) of countries where the detected language is official using the Wikidata SPARQL API.
- **Population Data**: Uses GeoJSON data to display population density as a choropleth map.

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Dependencies

- `folium`: For map visualizations.
- `langid`: For language detection.
- `googletrans`: For translation.
- `requests`: For making HTTP requests to Wikidata API.
- `pandas`: For data manipulation.
- `streamlit`: For creating the interactive web interface.
- `streamlit_folium`: For integrating `folium` maps with `streamlit`.

## Usage

1. Clone this repository to your local machine.

```bash
git clone https://github.com/yourusername/language-detection-visualization.git
```

2. Navigate to the project directory and run the app:

```bash
streamlit run app.py
```

3. Enter a sentence or paragraph in the input field to see the detected language, the closest language, and the translated text.
4. View the heatmap displaying the geographic distribution of the detected language and population density.

## How it Works

### 1. **Language Detection**:
   - The `langid` package is used to detect the language of the input text.

### 2. **Language Closeness**:
   - The closest language is found based on the confidence score provided by `langid` or similarity with predefined example texts.
   - `SequenceMatcher` from Python's `difflib` module is used to compute similarity between the input text and predefined texts for various languages.

### 3. **Translation**:
   - The `googletrans` library is used to translate the detected text to the closest language.
   
### 4. **Heatmap Generation**:
   - Geographic data is fetched from Wikidata API for each country where the detected language is spoken.
   - Population data is fetched from a GeoJSON file containing world population estimates.
   - A heatmap is created using `folium`, which layers the language density and population density information.

### 5. **Visualization**:
   - The map is displayed in the Streamlit app, where the user can view the geographical regions where the language is spoken and the population density of those areas.

## Example Output

After inputting a text, the following results can be observed:

- **Detected Language**: "English"
- **Closest Language**: "Spanish"
- **Translated Text**: "Este es un ejemplo de texto en español."
- **Heatmap**: A map is displayed showing the distribution of Spanish speakers and population density across the globe.

## Files in this Repository

- `app.py`: The main application file that runs the Streamlit app.
- `ne_110m_admin_0_countries.geojson.txt`: The GeoJSON file containing population data for countries.
- `requirements.txt`: A file listing the required Python libraries for the project.
- `languages_texts.py`: A Python file containing example texts for various languages to compute similarity scores.
- `README.md`: This file.

## Contributing

Feel free to fork this repository, create issues, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- `langid` for language detection.
- `googletrans` for translation services.
- `folium` for map visualizations.
- `wikidata` for providing geographic language data.
```

---

### Methodology Summary:
- **Language Detection and Translation**: Used the `langid` package for automatic language identification. For translation, the `googletrans` library was utilized, with a fallback mechanism if translation fails.
- **Language Closeness Calculation**: Based on language confidence scores from `langid` and similarity measures using `SequenceMatcher` to determine the closest language.
- **Geographic Data Collection**: Wikidata API was leveraged to retrieve geographic coordinates for countries where the language is spoken. 
- **Visualization**: Employed `folium` and `streamlit` to create interactive maps and visualizations. `folium`'s `HeatMap` was used for visualizing language distribution and population density.

