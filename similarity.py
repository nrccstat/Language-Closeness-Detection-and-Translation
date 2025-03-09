import streamlit as st
import langid
from googletrans import Translator, LANGUAGES
from difflib import SequenceMatcher

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
    "ru": "Это пример текста на русском языке.",
    "zh": "这是一个中文文本的示例.",
}

st.title("Language Closeness Detection and Translation (using langid.py and Google Translate)")

st.write("""
This app detects the closest language to the input text based on langid and translates it to that language.
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
