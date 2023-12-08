def parse_line(line):
    #Return string::card, int::bid
    parsed = line.split(" ")
    return parsed[0], int(parsed[1])

def calculate_hand_type(hand):
    counter = {}
    for letter in hand:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    three_matches = False
    two_matches = False

    for key in counter:
        if counter[key] == 5:
            return 7
        if counter[key] == 4:
            return 6
        if counter[key] == 3:
            three_matches = True
        if counter[key] == 2:
            if two_matches:
                return 3
            else:
                two_matches = True
    
    if three_matches and two_matches:
        return 5
    if three_matches and not two_matches:
        return 4
    if two_matches:
        return 2
    
    return 1

def compare_two_hands(hand1, hand2, ranking):
    for i in range(len(hand1)):
        if ranking[hand1[i]] > ranking[hand2[i]]:
            return 0
        if ranking[hand1[i]] < ranking[hand2[i]]:
            return 1
        
    # TODO KOMMER KRACHA OM DET FINNS IDENTISKA HÄNDER

def break_ties(sorted_list, ranking, list_of_entries):
    new_sorted = []
    for x in sorted_list:
        insert_index = 0
        hand1 = list_of_entries[x[1]][0]
        print("hand1", hand1)
        for i in range(len(new_sorted)):
            hand2 = list_of_entries[new_sorted[i][1]][0]
            print("hand2", hand2)
            
            cmp_ = compare_two_hands(hand1, hand2, ranking)
            if cmp_ == 0:
                insert_index = i
                break
            elif cmp_ == 1:
                insert_index += 1
        new_sorted.insert(insert_index, x)
    return new_sorted
        

f = open("input.txt", 'r')
list_of_entries = []
## [(r, i)]
list_of_rankings = []
sorted_ = []
ranking = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
types = [1, 2, 3, 4, 5, 6, 7]

for line in f:
    list_of_entries.append(parse_line(line))

for i in range(len(list_of_entries)):
    list_of_rankings.append((calculate_hand_type(list_of_entries[i][0]), i))

#x = [(4, 3), (4, 2)]
#print(break_ties(x, ranking, list_of_entries))

sort = sorted(list_of_rankings, reverse=True)
final = []

build_tie = []
rank = -1
for i in range(len(sort)):
    if len(build_tie) == 0:
        build_tie.append(sort[i])
        rank = sort[i][0]
    elif rank == sort[i][0]:
        build_tie.append(sort[i])
    else: 
        print(build_tie)
        final = final + break_ties(build_tie, ranking, list_of_entries)
        build_tie = [sort[i]]
        rank = sort[i][0]

final = final + break_ties(build_tie, ranking, list_of_entries)

total = 0
for i in range(len(final)):
    total += (len(final)-i) * list_of_entries[final[i][1]][1]

print(total)