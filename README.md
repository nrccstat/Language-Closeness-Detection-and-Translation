# Language Closeness Detection and Translation App

## Overview
This Streamlit application detects the language of a given text using `langid.py`, determines the closest alternative language based on similarity, and translates the text to that language using Google Translate.

## Features
- **Language Detection**: Uses `langid.py` to determine the language of the input text.
- **Closest Language Matching**: Compares the detected language with a set of predefined language samples to find the most similar alternative.
- **Translation**: Uses Google Translate API to translate the text into the closest alternative language.
- **User-Friendly Interface**: Built with Streamlit for an interactive experience.

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
- Detected language and confidence score
- Closest alternative language based on similarity
- Translated text in the closest alternative language

## File Structure
```
├── app.py                 # Main Streamlit application script
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```

## Notes
- The Google Translate API might experience occasional delays or errors.
- `langid` provides confidence scores, but accuracy depends on input length and complexity.
- The predefined language samples help in determining the closest alternative language when `langid`'s ranking is inconclusive.

## Future Improvements
- Add more predefined language samples for better similarity matching.
- Integrate more robust translation APIs to improve accuracy.
- Provide users with an option to select a target language manually.
- Implement a database to store past translations for quick retrieval.

## Contributing
Contributions are welcome! Feel free to fork the repository, open an issue, or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any inquiries, open an issue on GitHub or contact `your.email@example.com`.

