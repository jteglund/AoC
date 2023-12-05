import threading

def parse_seeds(line):
    se = [int(s) for s in line.split() if s.isdigit()]
    return se

def parse_map(fd):
    line = fd.readline()
    print(line)
    line = fd.readline()
    #     [src, dst]
    _map = {}
    while(line != "\n"): 
        numbers = [int(s) for s in line.split() if s.isdigit()]
        #[dest, src, range]
        for i in range(numbers[2]):
            _map[numbers[1]+i] = numbers[0]+i
        line = fd.readline()
    return _map

def parse_map_2(fd):
    line = fd.readline()
    print(line)
    line = fd.readline()
    _map = []
    while(line != "\n"): 
        numbers = [int(s) for s in line.split() if s.isdigit()]
        #[dest, src, range]
        _map.append(numbers)
        line = fd.readline()
    return _map

def calc_map(_map, return_map, index):
    c_map = {}
    for m in _map:
        for i in range(m[2]):
            c_map[m[1]+i] = m[0]+i
    return_map[index] = c_map
    return c_map

def parse_input(_file):
    f = open(_file, 'r')
    first_line = f.readline()
    seeds = parse_seeds(first_line)
    maps = []
    line_2 = f.readline()

    for i in range(7):
        maps.append(parse_map_2(f))

    c_map = [{},{},{},{},{},{},{}]
    #Parallellisera skiten
    t0 = threading.Thread(target=calc_map, args=(maps[0], c_map, 0))
    t1 = threading.Thread(target=calc_map, args=(maps[1], c_map, 1))
    t2 = threading.Thread(target=calc_map, args=(maps[2], c_map, 2))
    t3 = threading.Thread(target=calc_map, args=(maps[3], c_map, 3))
    t4 = threading.Thread(target=calc_map, args=(maps[4], c_map, 4))
    t5 = threading.Thread(target=calc_map, args=(maps[5], c_map, 5))
    t6 = threading.Thread(target=calc_map, args=(maps[6], c_map, 6))

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    
    return seeds, c_map

def calculate_seed_to_location(seed, maps):
    for m in maps:
        if seed in m:
            seed = m[seed]
    return seed

def find_lowest_location_number(seeds, maps):
    location_numbers = []
    for s in seeds:
        location_numbers.append(calculate_seed_to_location(s, maps))

    return min(location_numbers)

seeds, maps = parse_input("input.txt")
location = find_lowest_location_number(seeds, maps)
print(location)