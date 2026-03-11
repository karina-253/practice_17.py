from typing import Dict, List


def create_dictionary(num: int) ->Dict[str, List[str]]:
    """
    Creates a family tree based on parent-child relationships.
    the function also adds all descendants to the dictionary
    (even if they don't have any children) with empty lists.
    Args:
        num (int): The number of parent relationships to process.
        Must be a positive integer.

    Returns:
        Dict[str, List[str]]: A dictionary representing a family tree,
        where the keys are people's names and the values are lists of their children.
    """

    family_tree = {}

    for pair in range(num):
        parent_name, child_name = input().strip().split()

        if parent_name in family_tree:
            family_tree[parent_name].append(child_name)
        else:
            family_tree[parent_name] = [child_name]

        if child_name not in family_tree:
            family_tree[child_name] = []

    return family_tree


def count_children(name: str, tree_dict: Dict[str, List[str]]) -> int:
    """
    Recursively counts the number of all descendants for a given person.
    A recursive approach is used: for each child, we first count it
    itself, and then recursively all its descendants.

    Args:
        name (str): The name of the person for whom descendants need to be counted.
        tree_dict (Dict[str, List[str]]): A family tree where the keys are people's names
         and the values are lists of their children.

    Returns:
        int: The total number of descendants.
        If a person has no children or is not in the tree, 0 is returned.
    """

    if name not in tree_dict:
        return 0

    total = 0

    for child in tree_dict[name]:
        total += 1 + count_children(child, tree_dict)

    return total


def main() -> None:
    """
    The main function of the program.

    It asks for the number of parent relationships and a person's name
    to count their descendants, checks the correctness of the entered number,
    displays the result (the number of descendants).
    """

    try:
        num = int(input())

        if num <= 0:
            print("Ошибка. N должен быть натуральным")
            return

        dictionary_tree = create_dictionary(num)

        last_word = input()

        print(count_children(last_word, dictionary_tree))

    except ValueError:
        print("Ошибка. Неверный формат входных данных")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()

