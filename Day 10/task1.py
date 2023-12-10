def parse_input(file_):
    matrix = []
    fd = open(file_, 'r')
    for line in fd:
        if line[-1] == '\n':
            line = line[:-1]
        matrix.append(line)
    
    return matrix

def direction_converter(pipe, direction):
    dic = {'N': (-1, 0), 'W': (0, -1), 'E': (0, 1), 'S': (1, 0)}
    direction_index = {'N': 0, 'W': 1, 'E': 2, 'S': 3}
    p = pipe.copy()
    p[direction_index[direction]] = 0

    if p.index(1) == 0:
        return dic['N'], 'S'
    elif p.index(1) == 1:
        return dic['W'], 'E'
    elif p.index(1) == 2:
        return dic['E'], 'W'
    elif p.index(1) == 3:
        return dic['S'], 'N'

# Direction [N, W, E, S]
def new_index_calculator(pipe, current_index, direction):
    dic = {'|': [1, 0, 0, 1], 
           '-': [0, 1, 1, 0], 
           'L': [1, 0, 1, 0], 
           'J': [1, 1, 0, 0], 
           '7': [0, 1, 0, 1], 
           'F': [0, 0, 1, 1]}
                #N, W, E, S
    way, direction = direction_converter(dic[pipe], direction)
    return (current_index[0]+way[0], current_index[1]+way[1]), direction

def find_s(pipe_matrix):
    for i in range(len(pipe_matrix)):
        for j in range(len(pipe_matrix[i])):
            if pipe_matrix[i][j] == "S":
                return (i, j)
    return -1

def check_valid(pipe, direction):
    dic = {'|': ['N', 'S'], 
           '-': ['E', 'W'], 
           'L': ['N', 'E'], 
           'J': ['N', 'W'], 
           '7': ['W', 'S'], 
           'F': ['E', 'S'],
           '.': []}
    
    return direction in dic[pipe]
    

def find_neighbours(s_coord, pipe_matrix):
    dic = {'S': (-1, 0), 'E': (0, -1), 'W': (0, 1), 'N': (1, 0)}
    neighbor = []

    for direction in ['N', 'W', 'E', 'S']:
        new_coord = s_coord[0]+dic[direction][0], s_coord[1]+dic[direction][1]
        
        if(new_coord[0] > -1 and new_coord[0] < len(pipe_matrix) and new_coord[1] > -1 and new_coord[1] < len(pipe_matrix[new_coord[0]])):
            pipe = pipe_matrix[new_coord[0]][new_coord[1]]

            if check_valid(pipe, direction):
                neighbor.append((new_coord, direction))

    if len(neighbor) != 2:
        return TypeError
    
    return neighbor

def is_nest_part(path_matrix, coord):
    return path_matrix[coord[0]][coord[1]] != "#"

def check_is_valid_coord(coord, pipe_matrix):
    return coord[0] >= 0 and coord[0] < len(pipe_matrix) and coord[1] >= 0 and coord[1] < len(pipe_matrix[coord[0]])

def right_coord(coord, direction):
    if direction == 'N':
        right_coord = (coord[0], coord[1]-1)
    elif direction == 'S':
        right_coord = (coord[0], coord[1]+1)
    elif direction == 'W':
        right_coord = (coord[0]+1, coord[1])
    elif direction == 'E':
        right_coord = (coord[0]-1, coord[1])
    
    return right_coord
     

def find_path(pipe_matrix):
    path = [0]
    s_coord = find_s(pipe_matrix)
    neigh = find_neighbours(s_coord, pipe_matrix)
    finished = False
    coord = neigh[0][0]
    direction = neigh[0][1]

    while(not finished):
        pipe = pipe_matrix[coord[0]][coord[1]]
        if pipe == 'S':
            finished = True
            break

        path.append(0)
        coord, direction = new_index_calculator(pipe, coord, direction)

    return len(path)/2

def find_nests(pipe_matrix, path_matrix, coord, direction):
    nests = []
    finished = False
    while(not finished):
        pipe = pipe_matrix[coord[0]][coord[1]]
        if pipe == 'S':
            r_coord = right_coord(coord, direction) 
            if check_is_valid_coord(r_coord, pipe_matrix):
                if is_nest_part(path_matrix, r_coord):
                    if not (r_coord in nests):
                        nests.append(r_coord)

            finished = True
            break
        
        r_coord = right_coord(coord, direction) 
        if check_is_valid_coord(r_coord, pipe_matrix):
            if is_nest_part(path_matrix, r_coord):
                if not (r_coord in nests):
                    nests.append(r_coord)
        
        coord, direction = new_index_calculator(pipe, coord, direction)
        
    return nests

def get_new_coord(coord, i):
    if i == 0:
        new_coord = (coord[0]-1, coord[1])
    if i == 1:
        new_coord = (coord[0]+1, coord[1])
    if i == 2:
        new_coord = (coord[0], coord[1]-1)
    if i == 3:
        new_coord = (coord[0], coord[1]+1)

    return new_coord

def find_all_nests(nests, path_matrix):
    to_check = nests.copy()
    result = nests.copy()

    while(len(to_check) >0):
        c = to_check.pop()
        for i in range(4):
            new_coord = get_new_coord(c, i)
            if check_is_valid_coord(new_coord, path_matrix):
                if is_nest_part(path_matrix, new_coord) and not(new_coord in result):
                    result.append(new_coord)
                    to_check.append(new_coord)
    
    return result


def find_path(pipe_matrix):
    path_matrix = find_path_2(pipe_matrix)

    s_coord = find_s(pipe_matrix)
    neigh = find_neighbours(s_coord, pipe_matrix)
    finished = False

    first_coord = neigh[0][0]
    first_direction = neigh[0][1]

    second_coord = neigh[1][0]
    second_direction = neigh[1][1]

    first_nest = find_nests(pipe_matrix, path_matrix, first_coord, first_direction)
    second_nest = find_nests(pipe_matrix, path_matrix, second_coord, second_direction)

    if len(first_nest) < len(second_nest):
        nests = find_all_nests(first_nest, path_matrix)
    else:
        nests = find_all_nests(second_nest, path_matrix) 

    return nests

def find_path_2(pipe_matrix):
    path = []

    for i in range(len(pipe_matrix)):
        tmp = []
        for j in range(len(pipe_matrix[i])):
            tmp.append('.')
        path.append(tmp)

    s_coord = find_s(pipe_matrix)
    neigh = find_neighbours(s_coord, pipe_matrix)
    finished = False
    coord = neigh[0][0]
    direction = neigh[0][1]
    path[s_coord[0]][s_coord[1]] = "#"

    while(not finished):
        pipe = pipe_matrix[coord[0]][coord[1]]
        if pipe == 'S':
            finished = True
            break

        path[coord[0]][coord[1]] = "#"
        coord, direction = new_index_calculator(pipe, coord, direction)

    return path

def find_nest(path):
    for i in range(len(path)):
        if "#" in path[i]:
            start = (i, path[i].index("#"))
            break

    print(start)

pipe_matrix = parse_input("input.txt")
path = find_path_2(pipe_matrix)

li = find_all_nests(find_path(pipe_matrix), path)
li = list(dict.fromkeys(li))

print(len(li))

