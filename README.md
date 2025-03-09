# Language Closeness Detection and Translation App

## Overview
This Streamlit application detects the language of a given text using `langid.py`, determines the closest alternative language based on similarity, and translates the text to that language using Google Translate. It leverages predefined language samples and similarity scoring to provide the most relevant translation.

## Features
- **Language Detection**: Utilizes `langid.py` to classify the input text and provide a confidence score.
- **Closest Language Matching**: Compares the detected language with a predefined set of language samples and ranks them based on similarity.
- **Translation**: Uses Google Translate API to convert the input text into the most similar alternative language.
- **Interactive UI**: Built with Streamlit for a seamless user experience.

## Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/yourusername/language-detection-translation.git
cd language-detection-translation
pip install -r requirements.txt
```

## Usage
Run the Streamlit app:
```bash
streamlit run app.py
```
Enter text in the provided text area, and the app will display:
- **Detected Language**: Identified using `langid.py`, along with a confidence score.
- **Closest Alternative Language**: Determined using a similarity comparison with predefined language texts.
- **Translated Text**: The input text translated into the closest alternative language.

## Functionality Breakdown
### `detect_language_langid(text)`
- Uses `langid.classify()` to determine the language of the input text.
- Returns the detected language code.

### `translate_text(text, target_language)`
- Uses Google Translate to translate the input text to the specified `target_language`.
- Returns the translated text or an error message if translation fails.

### Language Similarity Calculation
- The detected language is compared with other languages using two methods:
  1. **LangID ranking**: Uses `langid.rank(input_text)` to determine the next closest language.
  2. **Text similarity scoring**: Uses `SequenceMatcher` from the `difflib` module to measure similarity with predefined example texts.
- The language with the highest similarity score is selected as the closest alternative.

## File Structure
```
├── app.py                 # Main Streamlit application script
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

## Notes
- The Google Translate API may experience occasional delays or restrictions.
- `langid` provides confidence scores, but accuracy depends on input length and complexity.
- The predefined language samples help refine the closest language selection.

## Future Improvements
- Expand predefined language samples for more accurate similarity comparisons.
- Improve error handling for Google Translate API failures.
- Allow users to manually select the target language for translation.
- Implement caching to store previous translations for faster results.

## Contributing
Contributions are welcome! Feel free to fork the repository, open an issue, or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, open an issue on GitHub or contact `your.email@example.com`.


