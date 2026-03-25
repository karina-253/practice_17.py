from typing import Dict


def build_graph() -> Dict[str, Dict[str, int]]:
    """
    Constructs a road graph from the input data.

    Returns:
        Dict[str, Dict[str, int]]: A graph where the key is a city,
        and the value is a dictionary of neighbors and distances
    """

    cities_count = int(input().strip())
    roads_count = int(input().strip())

    road_map = {}

    for road in range(roads_count):
        city_1, city_2, dist = input().split()
        city_1 = city_1.lower()
        city_2 = city_2.lower()
        distance = int(dist)

        if city_1 not in road_map:
            road_map[city_1] = {}
        if city_2 not in road_map:
            road_map[city_2] = {}

        road_map[city_1][city_2] = distance
        road_map[city_2][city_1] = distance

    return road_map


def find_shortest_path(road_map: Dict[str, Dict[str, int]],
                       locality_1: str, locality_2: str) -> int:
    """
    Finds the shortest distance between two cities.

     Args:
        road_map: Road graph
        locality_1: Starting city
        locality_2: Ending city

    Returns:
        int: The shortest distance or -1 if there is no path
    """

    if locality_1 not in road_map or locality_2 not in road_map:
        return -1

    if locality_1 == locality_2:
        return 0

    shortest_dist = {city: float('inf') for city in road_map}
    shortest_dist[locality_1] = 0

    unvisited = set(road_map.keys())

    while unvisited:
        current_city = None
        min_dist = float('inf')

        for city in unvisited:
            if shortest_dist[city] < min_dist:
                min_dist = shortest_dist[city]
                current_city = city

        if current_city is None or min_dist == float('inf'):
            break

        if current_city == locality_2:
            break

        unvisited.remove(current_city)

        for neighbor, road_length in road_map[current_city].items():
            if neighbor in unvisited:
                new_dist = shortest_dist[current_city] + road_length
                if new_dist < shortest_dist[neighbor]:
                    shortest_dist[neighbor] = new_dist

    result = shortest_dist[locality_2]
    return result if result != float('inf') else -1


def main() -> None:
    """
    The main function of the program.

    1. Reads the data using read_graph()
    2. Finds the shortest distance using find_shortest_path()
    3. Displays the result on the screen
    """

    try:
        road_map = build_graph()

        locality_1, locality_2 = input().lower().split()

        result = find_shortest_path(road_map, locality_1, locality_2)

        if result == -1:
            print("Путь не найден")
        else:
            print(result)

    except ValueError:
        print("Ошибка при вводе городов")


if __name__ == "__main__":
    main()
  
