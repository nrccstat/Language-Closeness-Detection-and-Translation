import streamlit as st
import langid
from googletrans import Translator, LANGUAGES
from difflib import SequenceMatcher
import requests
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
import json  

def detect_language_langid(text):
    lang, _ = langid.classify(text)
    return lang

def translate_text(text, target_language):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language)
        return translated.text
    except Exception as e:
        return f"Error translating to {target_language}: {str(e)}"

def get_language_data(language_code):
    """Fetch countries where the language is official from Wikidata"""
    query = f"""
    SELECT ?country ?countryLabel ?coordinates WHERE {{
        ?country wdt:P37 ?language.
        ?language wdt:P218 '{language_code}'.
        ?country wdt:P625 ?coordinates.
        SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
    }}
    """
    url = "https://query.wikidata.org/sparql"
    response = requests.get(url, params={'query': query, 'format': 'json'})
    data = response.json()
    
    locations = []
    for item in data['results']['bindings']:
        country = item['countryLabel']['value']
        coords = item['coordinates']['value'].split('Point(')[1].rstrip(')').split()
        locations.append({
            'country': country,
            'latitude': float(coords[1]),
            'longitude': float(coords[0])
        })
    return pd.DataFrame(locations)

def get_population_data():
    """Load world population data from GeoJSON file"""
    try:
        with open('ne_110m_admin_0_countries.geojson.txt', encoding='utf-8') as f:
            geojson_data = json.load(f)
        
        df_pop = pd.DataFrame([feature['properties'] for feature in geojson_data['features']])
        
        df_pop = df_pop[['NAME', 'POP_EST']].rename(columns={'NAME': 'name', 'POP_EST': 'pop_est'})
        
        df_pop['pop_est'] = df_pop['pop_est'].fillna(0)  

        return geojson_data, df_pop
    
    except FileNotFoundError:
        print("Error: The specified GeoJSON file was not found.")
    except KeyError as e:
        print(f"Error: Missing expected key in GeoJSON data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def create_heatmap(language_code, df_lang, geojson_data, df_pop):
    """Create a heatmap combining language and population data"""
    m = folium.Map(location=[20, 0], zoom_start=2)
    
    if not df_lang.empty:
        HeatMap(
            data=df_lang[['latitude', 'longitude']].values,
            radius=15,
            name=f"{language_code} Language Density"
        ).add_to(m)
    else:
        st.write("No geographic data found for this language.")
    
    folium.Choropleth(
        geo_data=geojson_data,
        name='Population',
        data=df_pop,
        columns=['name', 'pop_est'],
        key_on='feature.properties.NAME',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Population'
    ).add_to(m)
    
    folium.LayerControl().add_to(m)
    return m


languages_texts = {
    "af": "Dit is 'n voorbeeld van Afrikaanse teks.",
    "am": "ይህ የአማርኛ ጽሑፍ ምሳሌ ነው።",
    "ar": "هذا مثال على نص باللغة العربية.",
    "bn": "এটি বাংলা ভাষায় লেখা একটি উদাহরণমূলক পাঠ্য।",
    "de": "Dies ist ein Beispieltext in deutscher Sprache.",
    "en": "This is an example of English text.",
    "es": "Este es un ejemplo de texto en español.",
    "fr": "Ceci est un exemple de texte en français.",
    "hi": "यह हिंदी में लिखा गया एक उदाहरण पाठ है।",
    "it": "Questo è un esempio di testo in italiano.",
    "ja": "これは日本語のテキストの例です。",
    "mr": "हे मराठीतले लेखनाचे उदाहरण आहे。",
    "pt": "Este é um exemplo de texto em português.",
    "ru": "Это пример текста на русском языке。",
    "zh": "这是一个中文文本的示例。",
}

st.title("Language Closeness Detection, Translation, and Heatmap")

st.write("""
This app detects the closest language to the input text based on langid, translates it to that language, 
and displays a heatmap showing the geographic distribution of the detected language and population density.
""")

input_text = st.text_area("Enter a sentence or paragraph:")

if input_text:
    detected_lang, detected_conf = langid.classify(input_text)
    st.write(f"Detected Language: {detected_lang} (Confidence: {detected_conf:.2%})")
    
    all_langs = langid.rank(input_text)
    
    closest_lang = None
    max_score = detected_conf  
    
    for lang_code, lang_score in all_langs:
        if lang_code in languages_texts:
            if lang_code == detected_lang:
                continue
            if lang_score > max_score:
                max_score = lang_score
                closest_lang = lang_code
    
    if not closest_lang:
        for lang_code, example_text in languages_texts.items():
            if lang_code == detected_lang:
                continue
            similarity = SequenceMatcher(None, input_text, example_text).ratio()
            if similarity > max_score:
                max_score = similarity
                closest_lang = lang_code

    if closest_lang:
        translated = translate_text(input_text, closest_lang)
        st.write(f"Closest Alternative Language: {LANGUAGES[closest_lang].title()} ({closest_lang})")
        st.write(f"Translated Text: {translated}")
    else:
        st.write("Showing detected language translation:")
        translated = translate_text(input_text, detected_lang)
        st.write(f"Translated Text: {translated}")
    
    st.subheader("Language and Population Density Heatmap")
    df_lang = get_language_data(detected_lang)
    geojson_data, df_pop = get_population_data()
    heatmap = create_heatmap(detected_lang, df_lang, geojson_data, df_pop)
    folium_static(heatmap)
