from typing import Dict


def create_dictionary(num: int) -> Dict[str, str]:
    """
    Creates a dictionary that matches objects with their shape.

    Args:
        num (int): The number of rows to process. Must be a positive integer.

    Returns:
        Dict[str, str]: A dictionary where the keys are the names of items
        and the values are their shapes
    """

    forms_dict = {}

    for word in range(num):
        words = input().strip().split()

        form = words[0]

        for obj in words[1:]:
            forms_dict[obj] = form

    return forms_dict


def find_form(object_name: str, dictionary: Dict[str, str]) -> str:
    """
    Finds a form for a given object using a dictionary of forms.

    Args:
        object_name (str): The name of the object for which the form is to be found.
        dictionary (Dict[str, str]): A dictionary of forms, where the keys are objects and the
                                    values are their forms.

    Returns:
        str: The form of the item if it is found in the dictionary.
             Otherwise, the original name of the item is returned.
    """

    return dictionary.get(object_name, object_name)


def main() -> None:
    """
    The main function of the program.

    The function asks for the number of rows in the dictionary of forms and the name
    of the item to search for its form, checks the correctness of the entered number,
    displays the result (the form of the item or the original name).
    """
    
    try:
        num = int(input())

        if num <= 0:
            print("Ошибка. N должен быть натуральным")
            return

        dictionary_form = create_dictionary(num)

        last_word = input()

        print(find_form(last_word, dictionary_form))

    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
