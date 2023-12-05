def parse_seeds(line):
    se = [int(s) for s in line.split() if s.isdigit()]
    return se

def parse_map(fd):
    line = fd.readline()
    line = fd.readline()
    _map = []
    while(line != "\n"): 
        numbers = [int(s) for s in line.split() if s.isdigit()]
        #[dest, src, range]
        _map.append(numbers)
        line = fd.readline()
    return _map

def parse_input(_file):
    f = open(_file, 'r')
    first_line = f.readline()
    seeds = parse_seeds(first_line)
    maps = []
    line_2 = f.readline()

    for i in range(7):
        maps.append(parse_map(f))
    
    return seeds, maps

def calculate_seed_to_location(seed, maps):
    for m in maps:
        ## M = Lista med listor [[dst, src, range], ...]
        for sub_map in m:
            if seed < sub_map[1]+sub_map[2] and seed >= sub_map[1]:
                index = seed-sub_map[1]
                seed = sub_map[0]+index
                break

    return seed

def find_lowest_location_number(seeds, maps):
    location_numbers = []
    for s in seeds:
        print(s)
        location_numbers.append(calculate_seed_to_location(s, maps))
    return min(location_numbers)

#seeds, maps = parse_input("input.txt")
#location = find_lowest_location_number(seeds, maps)