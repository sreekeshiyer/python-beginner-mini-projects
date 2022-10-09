import argparse
from translate import Translator


def main():
    # Initializing Argument Parser
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--from_lang", help="Language to translate from.", type=str)
    parser.add_argument(
        "--to_lang", help="Language to translate to. (defaults to English)",
        type=str)
    text = input("Enter text to translate: ")
    args = parser.parse_args()
    # Checking if a from_language is provided. (defaults automatically to English)
    # If provided, set from_language in the Translator object.
    if args.from_lang:
        translator = Translator(
            to_lang=args.to_lang if args.to_lang else "English",
            from_lang=args.from_lang
        )
    # Else, do not pass anything for from_language.
    else:
        translator = Translator(
            to_lang=args.to_lang if args.to_lang else "English")
    try:
        translation = translator.translate(text)
    except Exception:
        print("Translation Error. Returning...")
        return None
    print(translation)


if __name__ == "__main__":
    main()
