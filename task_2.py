from typing import Dict


def create_dictionary(num: int) -> Dict[str, str]:
    """
    Creates a russian-english dictionary from a given number of word pairs.

    Args:
        num (int): The number of word pairs to be read for the dictionary.

    Returns:
        Dict[str, str]: A dictionary where the keys are russian words and
         the values are english translations.
    """

    rus_eng_dict = {}

    for pair in range(num):
        rus, eng = input().strip().split()
        rus_eng_dict[rus] = eng

    return rus_eng_dict


def translate(string: str, dictionary: Dict[str, str]) -> str:
    """
    Translates text from Russian to English using the provided dictionary.

    Args:
        string (str): The original Russian phrase to be translated.
        dictionary (Dict[str, str]): A dictionary for translation,
         where the keys are Russian words, values - English translations.

    Returns:
        str: Translated phrase in English. Words that are not in the dictionary,
             remain in Russian.
    """

    words = string.split()
    translation_phrase = []

    for word in words:
        translation_phrase.append(dictionary.get(word, word))

    return ' '.join(translation_phrase)


def main() -> None:
    """
    The main function of the program.

    The function asks for the number of word pairs in the dictionary and the phrase
    for the translation, checks the correctness of the entered number,
    outputs the result of the transfer.
    """

    try:
        num = int(input())

        if num <= 0:
            print("Ошибка. N должен быть натуральным")
            return

        dictionary = create_dictionary(num)
        last_phrase = input()
        translated_phrase = translate(last_phrase, dictionary)
        print(translated_phrase)

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
