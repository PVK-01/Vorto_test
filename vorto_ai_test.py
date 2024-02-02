import math

def parsing(path):
    loads = []
    with open(path, 'r') as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split()
            load_id = int(parts[0])
            pick = tuple(map(float, parts[1].strip("()").split(',')))
            drop = tuple(map(float, parts[2].strip("()").split(',')))
            loads.append((load_id, pick, drop))
    return loads

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
def n_n(loads, max_driving_time=12*60):
    drivers = []
    while loads:
        route = []
        time = 0
        curr_loc = (0, 0)

        while loads:
            nearest_load = None
            min_dist = float('inf')

            for load in loads:
                pickup_dist = dist(curr_loc, load[1])
                if pickup_dist < min_dist:
                    total_distance = pickup_dist + dist(load[1], load[2])
                    if time + total_distance + dist(load[2], (0, 0)) <= max_driving_time:
                        min_dist = pickup_dist
                        nearest_load = load

            if nearest_load is None:
                break

            route.append(nearest_load[0])
            time += min_dist + dist(nearest_load[1], nearest_load[2])
            curr_loc = nearest_load[2]
            loads.remove(nearest_load)

        drivers.append(route)

    return drivers
def main(file_path):
    loads = parsing(file_path)
    driver_routes = n_n(loads)

    for i, route in enumerate(driver_routes):
        print(route)

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1]
    main(file_path)
