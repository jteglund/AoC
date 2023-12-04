NUM_ROWS = 10

def input_to_array():
    f = open("input.txt", 'r')
    array_of_rows = []
    for i in range(140):
        array_of_rows.append(f.readline())
    return array_of_rows

def is_symbol(character):
    symbols = ['*', '%', '$', '+', '-', '#', '&', '@', '/', '=']
    if character in symbols:
        return True
    else:
        return False

def is_gear_symbol_2(character):
    if character == '*':
        return True
    else:
        return False

def is_digit(character):
    if ord(character) >= 48 and ord(character) <= 57:
        return True
    else:
        return False
    
def parse_row(row):
    number = ""
    index = []
    indices = []
    numbers = []
    for i in range(len(row)):
        
        if(is_digit(row[i])):
            number += row[i]
            index.append(i)
        elif(len(index) > 0):
            indices.append(index)
            numbers.append(int(number))
            index = []
            number = ""

    return indices, numbers

def check_above_or_underneath(indices, row):
    index_to_check = indices.copy()
    to_append = []
    if(indices[0] != 0):
        to_append.append(indices[0]-1)
    if(indices[-1] != len(row)-1):
        to_append.append(indices[-1]+1)
    index_to_check += to_append
    
    for i in index_to_check:
        if is_symbol(row[i]):
            return True
    return False

def check_same_row(indices, row):
    index_to_check = []
    if(indices[0] != 0):
        index_to_check.append(indices[0]-1)
    if(indices[-1] != len(row)-1):
        index_to_check.append(indices[-1]+1)
    
    for i in index_to_check:
        if is_symbol(row[i]):
            return True
    return False 



array_of_rows = input_to_array()
indices = []
numbers = []
for row in array_of_rows:
    index, number = parse_row(row)
    indices.append(index)
    numbers.append(number)

valid_engine_parts = []
for i in range(140):
    valid_engine_parts.append([])

for i in range(len(numbers)):
    check_total = False
    for j in range(len(numbers[i])):
        if i > 0 and i < len(numbers)-1:
            check_above = check_above_or_underneath(indices[i][j], array_of_rows[i-1])
            check_under = check_above_or_underneath(indices[i][j], array_of_rows[i+1])
            check_same = check_same_row(indices[i][j], array_of_rows[i])
            if(check_above or check_same or check_under):
                check_total = True
        elif i == 0:
            check_under = check_above_or_underneath(indices[i][j], array_of_rows[i+1])
            check_same = check_same_row(indices[i][j], array_of_rows[i])
            if(check_same or check_under):
                check_total = True 
        elif i == len(numbers)-1:
            check_above = check_above_or_underneath(indices[i][j], array_of_rows[i-1])
            check_same = check_same_row(indices[i][j], array_of_rows[i])
            if(check_above or check_same):
                check_total = True
        
        if check_total:
            valid_engine_parts[i].append(numbers[i][j])
            check_total = False

total = 0
for i in range(140):
    for j in range(len(valid_engine_parts[i])):
        total += valid_engine_parts[i][j]

print(total)
        
        
