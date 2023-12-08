from prime_factors import primeFactors

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right
    
    def getName(self):
        return self.name
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def __str__(self):
        return self.getName()
    

def parse_node(line):
    node_name = line[:3]
    node_left = line[7:10]
    node_right = line[12:15]

    return Node(node_name, node_left, node_right)

def parse_input(file):
    nodes = {}
    startNodes = []
    fd = open(file, 'r')

    #Read instructions
    instructions = fd.readline()
    fd.readline()

    for line in fd:
        n = parse_node(line)
        nodes[n.getName()] = n
        if n.getName()[2] == 'A':
            startNodes.append(n)
        

    return instructions, nodes, startNodes

def is_goal(node):
    return node.getName()[2] == 'Z'

def is_finished(nodes):
    if len(nodes) == 0:
        return True
    return is_goal(nodes.pop()) and is_finished(nodes)


def follow_path(instructions, nodes, startNode):
    node = startNode
    count = 0
    while(True):
        for i in range(len(instructions)):
            if instructions[i] == '\n':
                continue
            if is_goal(node):
                return count
            if instructions[i] == "R":
                node = nodes[node.getRight()]
            elif instructions[i] == "L":
                node = nodes[node.getLeft()]
            count+=1

def calculate_convergance(instructions, nodes, startNodes):
    list_of_paths = []
    for n in startNodes:
        list_of_paths.append(follow_path(instructions, nodes, n))
    
    convergance = 1
    for path in list_of_paths:
        convergance = convergance *path

    return list_of_paths

def calc_total(list_of_paths):
    paths = list_of_paths.copy()
    prime = []
    for path in list_of_paths:
        prime += primeFactors(path)
    prime = list(dict.fromkeys(prime))

    sum_ = 1
    for p in prime:
        sum_ = sum_ * p

    return int(sum_)

instructions, nodes, startNodes = parse_input("input.txt")
#print(startNodes)
lp = calculate_convergance(instructions, nodes, startNodes)
print(calc_total(lp))