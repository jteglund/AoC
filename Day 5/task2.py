from task1_new import *

def parse_seeds_new(line):
    se = [int(s) for s in line.split() if s.isdigit()]
    seeds = []
    for i in range(int(len(se)/2)):
        seeds.append((se[i*2],se[i*2]+se[i*2+1]-1))
         
    return seeds

def parse_map_new(fd):
    line = fd.readline()
    line = fd.readline()
    map_ranges = []
    map_results = []
    while(line != "\n"): 
        numbers = [int(s) for s in line.split() if s.isdigit()]
        #[dest, src, range]
        map_ranges.append((numbers[1], numbers[1]+numbers[2]-1))
        map_results.append((numbers[0], numbers[0]+numbers[2]-1))
        line = fd.readline()
    return map_ranges, map_results

def parse_input_new(_file):
    f = open(_file, 'r')
    first_line = f.readline()
    seeds = parse_seeds_new(first_line)
    maps = []
    line_2 = f.readline()

    for i in range(7):
        maps.append(parse_map_new(f))
    
    return seeds, maps

def calculate_seed_to_mapping(seed, maps):
    # Seed = [(79, 92), (55, 67)]      52, 65 -> 54, 67
    # Maps = ([(98, 99), (50, 97)], [(50, 51), (52, 99)])
    # Map s_low, s_high -> s_low+offset, s_high+offset
    # Offset = m_low - s_low
    seed_mapping = []
    # Split seeds
    while(len(seed) > 0):
        seed_range = seed.pop()
        low = seed_range[0]
        upper = seed_range[1]
        map_possible = False

        for i in range(len(maps[0])):
            map_range = maps[0][i]
            mapping = maps[1][i]

            if low >= map_range[0] and upper <= map_range[1]:
                # Ingen split behövs -> Gör mapping direkt
                offset = maps[1][i][0] - map_range[0]
                seed_mapping.append((low+offset, upper+offset))
                map_possible = True
                #print("HEJ")
                #TODO Tror den kan breaka här
                break

            elif low < map_range[0] and upper >= map_range[0]:
                #print(seed_range)
                #print(low)
                #print(map_range[0])
                #print(upper)
                #print(map_range[1])
                # Skicka vidare nya splits som inte är i range
                seed.append((low, map_range[0]-1))
                # Spara ny mapping
                seed_mapping.append((mapping[0], mapping[0]+(upper-map_range[0])))
                map_possible = True
                #print("HEJ")
                break
            
            # Om allt är utanför => 2 splits och en mapping
            elif low < map_range[0] and upper > map_range[1]:
                split1 = (low, map_range[0]-1)
                split2 = (map_range[1]+1, upper)
                seed.append(split1)
                seed.append(split2)
                
                # low+offset, high+offset
                offset = maps[1][i][0] - map_range[0]
                m1 = (low+offset, upper+offset)
                seed_mapping.append(m1)
                map_possible = True
                #print("HEJ")
                break
            
            # Om low är innanför och high utanför -> En mapping och en split
            elif low <= map_range[1] and upper > map_range[1]:
                split = (map_range[1]+1, upper)
                seed.append(split)
                offset = maps[1][i][0] - map_range[0]
                m1 = (low+offset, mapping[1])
                seed_mapping.append(m1)
                map_possible = True
                #print("HEJ")
                break
        
        if not map_possible:
            seed_mapping.append(seed_range)
        
    return seed_mapping

def calculate_mapping(seeds, maps):
    i = 0
    for _map in maps:
        seeds = calculate_seed_to_mapping(seeds, _map)
        i+=1
        
    
    return seeds

seeds, maps = parse_input_new("input.txt")

li = calculate_mapping(seeds, maps)

print(min(li))
