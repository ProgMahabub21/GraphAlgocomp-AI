graph = {
    "S": {"A": 2,"B": 1, "G": 9},
    "A": {"C": 2, "D": 3},
    "B": {"D": 2, "E": 4},
    "C": {"G": 4 },
    "D": {"G": 4},
    "E": {},
    "G": {},
}

heuristicVal={
    "S" : 6,
    "A" : 0,
    "B" : 6,
    "C" : 4,
    "D" : 1,
    "E" : 10,
    "G" : 0,
}
class graphProblem:

    def __init__(self,initial,goal,graph):

        self.initial=initial
        self.goal=goal
        self.graph=graph


    def actions(self,state):
        return list(graph[state].keys())

    def result(self,state,action):
        return action

    def goalTest(self,state):
        return state == self.goal

    def pathCost(self,cost_so_far, fromState,action,toState):
        return cost_so_far + graph[fromState][toState]


class Node:

    def __init__(self,state,parent=None,action=None,path_cost=0):
        
        self.state=state
        self.parent=parent
        self.action=action
        self.path_cost=path_cost


    def childNode(self,gp,action):
        
        childState=gp.result(self.state,action)
        path_cost_to_childNode = gp.pathCost(self.path_cost,self.state,action,childState)
        
        return Node(childState,self,action,path_cost_to_childNode)

    def expand(self,gp):

        return [self.childNode(gp,action) for action in gp.actions(self.state)]


def GBFS(gp):
    
    initNode = Node(gp.initial)
    frontier = []
    frontier.append(initNode)

    explored= set()

    while frontier:
        frontier.sort(key =lambda node:heuristicVal[node.state])      #gbfs called heuristic func to sort no other change than ufs

        print('Frontier: ')
        print([node.state for node in frontier])
        if len(frontier) == 0: return 'Failure'

        node = frontier.pop(0)
        print('Pop: ',node.state)

        if gp.goalTest(node.state): return node

        explored.add(node.state)

        for child in node.expand(gp):
            print('Child node : ',child.state)   
            if child.state not in explored and child not in frontier:
                frontier.append(child)
    return None

def UniformCostSearch(gp):
    
    initNode = Node(gp.initial)
    frontier = []
    frontier.append(initNode)

    explored= set()

    while frontier:
        frontier.sort(key =lambda node:node.path_cost)                  #ucs sorted frontier based on path cost

        print('Frontier: ')
        print([node.state for node in frontier])
        if len(frontier) == 0: return 'Failure'

        node = frontier.pop(0)
        print('Pop: ',node.state)

        if gp.goalTest(node.state): return node

        explored.add(node.state)

        for child in node.expand(gp):
            print('Child node : ',child.state)   
            if child.state not in explored and child not in frontier:
                frontier.append(child)
    return None


graphp1 =graphProblem("S","G",graph)

print('===================================')
print ( " Result of GBFS " )
print('===================================')
resultnode=GBFS(graphp1)
print("Path cost to goal : ",resultnode.path_cost)

print('===================================')
print ( " Result of UFS " )
print('===================================')
resultnode=UniformCostSearch(graphp1)
print("Path cost to goal : ",resultnode.path_cost)

