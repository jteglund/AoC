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
    

def parse_node(line):
    node_name = line[:3]
    node_left = line[7:10]
    node_right = line[12: 15]

    return Node(node_name, node_left, node_right)

def parse_input(file):
    nodes = {}
    fd = open(file, 'r')

    #Read instructions
    instructions = fd.readline()
    fd.readline()

    for line in fd:
        n = parse_node(line)
        nodes[n.getName()] = n

    return instructions, nodes

def follow_path(instructions, nodes):
    node = nodes['AAA']
    goal = 'ZZZ'
    count = 0
    while(True):
        for i in range(len(instructions)):
            if instructions[i] == '\n':
                continue
            if node.getName() == goal:
                return count
            if instructions[i] == "R":
                node = nodes[node.getRight()]
            elif instructions[i] == "L":
                node = nodes[node.getLeft()]
            count+=1
    
        

instructions, nodes = parse_input("input.txt")
print(follow_path(instructions, nodes))

