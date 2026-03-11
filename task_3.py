from typing import Dict


def create_dictionary(num: int) -> Dict[str, str]:
    """
    Creates a dictionary of antonyms from a given number of word pairs.

    Args:
        num (int): The number of word-antonym pairs to be counted.

    Returns:
        Dict[str, str]: Dictionary of antonyms, where the keys are the original words,
                       and the values are their antonyms.
    """

    ant_dict = {}

    for pair in range(num):
        word, antonym = input().strip().split()
        ant_dict[word] = antonym
        ant_dict[antonym] = word

    return ant_dict


def find_antonym(word: str, dictionary: Dict[str, str]) -> str:
    """
    Finds an antonym for a given word using an antonym dictionary.

    Args:
        word (str): The word for which an antonym is to be found.
        dictionary (Dict[str, str]): An antonym dictionary where the keys
         are the original words, the values are their antonyms.

    Returns:
        str: The antonym of the original word, if it is found in the dictionary.
             Otherwise, the original word is returned.
    """

    return dictionary.get(word, word)



def main() -> None:
    """
     The main function of the program.

     The function asks for the number of pairs of antonyms in the dictionary
     and  a word to search for an antonym, checks the correctness of the entered number,
     displays the result (the antonym or the original word).
    """

    try:
        num = int(input())

        if num <= 0:
            print("Ошибка. N должен быть натуральным")
            return

        dictionary_ant = create_dictionary(num)

        last_word = input()

        print(find_antonym(last_word, dictionary_ant))

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
