import streamlit as st
import langid
from googletrans import Translator

def detect_language_langid(text):
    lang, _ = langid.classify(text)
    return lang

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text  

st.title("Language Closeness Detection and Translation")

st.write("""
This app detects the language of the input text using langid and translates it to a different language.
""")

input_text = st.text_area("Enter a sentence or paragraph:")

languages_texts = {
    "en": "This is an example of English text.",
    "es": "Este es un ejemplo de texto en español.",
    "fr": "Ceci est un exemple de texte en français.",
    "de": "Dies ist ein Beispieltext in deutscher Sprache.",
    "it": "Questo è un esempio di testo in italiano."
}

if input_text:
    detected_language_langid = detect_language_langid(input_text)
    st.write(f"Detected Language (using langid.py): {detected_language_langid}")

    possible_languages = [lang for lang in languages_texts.keys() if lang != detected_language_langid]
    
    if possible_languages:
        closest_language = possible_languages[0]  
        st.write(f"Closest Language: {closest_language}")

        translated_text = translate_text(input_text, closest_language)
        st.write(f"Translated Text to {closest_language}: {translated_text}")
    else:
        st.write("No other language available for translation.")
