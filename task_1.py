from typing import List


def sort_words(string: str) -> List[str]:
    """
    Sorts words in a string by descending frequency of occurrence.

    Args:
        string (str): An input string containing words separated by spaces.

    Returns:
        List[str]: A list of unique words sorted by decreasing frequency.
    """

    words = string.split()

    frequancy = {}

    for word in words:
        if word in frequancy:
            frequancy[word] += 1
        else:
            frequancy[word] = 1

    result = sorted(frequancy.keys(), key=lambda x: frequancy[x], reverse=True)

    return result


def main() -> None:
    """
    The main function of the program.

    Prompts the user to enter a string, processes it using the function
    sort_words() and outputs the result line by line.
    """

    try:
        string = input('Введите слова через пробел: ')

        if not string:
            raise ValueError('Введена пустая строка.')

        for word in sort_words(string):
            print(word)
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
