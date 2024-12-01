pip install deep-translator
import streamlit as st
from deep_translator import GoogleTranslator

# Define the languages
LANGUAGES = {
    # European Languages
    1: {'name': 'English', 'code': 'en'},
    2: {'name': 'Spanish', 'code': 'es'},
    3: {'name': 'French', 'code': 'fr'},
    4: {'name': 'German', 'code': 'de'},
    5: {'name': 'Italian', 'code': 'it'},
    6: {'name': 'Portuguese', 'code': 'pt'},
    7: {'name': 'Dutch', 'code': 'nl'},
    8: {'name': 'Polish', 'code': 'pl'},
    9: {'name': 'Romanian', 'code': 'ro'},
    10: {'name': 'Greek', 'code': 'el'},

    # Asian Languages
    11: {'name': 'Chinese', 'code': 'zh'},
    12: {'name': 'Japanese', 'code': 'ja'},
    13: {'name': 'Korean', 'code': 'ko'},
    14: {'name': 'Vietnamese', 'code': 'vi'},
    15: {'name': 'Thai', 'code': 'th'},
    16: {'name': 'Hindi', 'code': 'hi'},
    17: {'name': 'Bengali', 'code': 'bn'},
    18: {'name': 'Turkish', 'code': 'tr'},
    19: {'name': 'Indonesian', 'code': 'id'},
    20: {'name': 'Malay', 'code': 'ms'},

    # Slavic Languages
    21: {'name': 'Russian', 'code': 'ru'},
    22: {'name': 'Ukrainian', 'code': 'uk'},
    23: {'name': 'Czech', 'code': 'cs'},
    24: {'name': 'Slovak', 'code': 'sk'},
    25: {'name': 'Croatian', 'code': 'hr'},
    26: {'name': 'Serbian', 'code': 'sr'},
    27: {'name': 'Bulgarian', 'code': 'bg'},
    28: {'name': 'Slovenian', 'code': 'sl'},
    29: {'name': 'Macedonian', 'code': 'mk'},
    30: {'name': 'Belarusian', 'code': 'be'},

    # Nordic and Baltic Languages
    31: {'name': 'Swedish', 'code': 'sv'},
    32: {'name': 'Danish', 'code': 'da'},
    33: {'name': 'Norwegian', 'code': 'no'},
    34: {'name': 'Finnish', 'code': 'fi'},
    35: {'name': 'Estonian', 'code': 'et'},
    36: {'name': 'Latvian', 'code': 'lv'},
    37: {'name': 'Lithuanian', 'code': 'lt'},
    38: {'name': 'Icelandic', 'code': 'is'},
    39: {'name': 'Irish', 'code': 'ga'},
    40: {'name': 'Welsh', 'code': 'cy'},

    # Other Languages
    41: {'name': 'Arabic', 'code': 'ar'},
    42: {'name': 'Hebrew', 'code': 'he'},
    43: {'name': 'Persian', 'code': 'fa'},
    44: {'name': 'Urdu', 'code': 'ur'},
    45: {'name': 'Swahili', 'code': 'sw'},
    46: {'name': 'Afrikaans', 'code': 'af'},
    47: {'name': 'Albanian', 'code': 'sq'},
    48: {'name': 'Armenian', 'code': 'hy'},
    49: {'name': 'Georgian', 'code': 'ka'},
    50: {'name': 'Maltese', 'code': 'mt'}
}

def get_target_language():
    """Get and validate user's language choice"""
    language_names = [lang['name'] for lang in LANGUAGES.values()]
    choice = st.selectbox("Choose the target language:", language_names)
    for key, value in LANGUAGES.items():
        if value['name'] == choice:
            return value['code']
    return None

def translate_text():
    """Main translation function"""
    text = st.text_input("Enter the text you want to translate: ").strip()
    target_language = get_target_language()
    if st.button("Translate"):
        if text and target_language:
            try:
                translator = GoogleTranslator(target=target_language)
                translation = translator.translate(text)
                st.write("\nResults:")
                st.write(f"Original: {text}")
                st.write(f"Translated: {translation}")
                st.write(f"Language: {next(lang['name'] for lang in LANGUAGES.values() if lang['code'] == target_language)}")
            except Exception as e:
                st.write(f"An error occurred: {str(e)}")
        else:
            st.write("Please enter some text and select a language to translate.")

if __name__ == "__main__":
    imagen = "imagen.jpg"  # Define the path to your image file
    st.image(imagen, use_container_width=True)
    st.title("Welcome to the Language Translator!")
    translate_text()