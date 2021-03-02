# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

"*** Answers to the sub questions ***"
'''
Question 1: Is the exploration order what you would have expected?(DFS)
Ans: 
Yes, Exploration order is what I expected. Though it also depends on the order in which we get the nodes from getSuccessor function.

Question 2: Does Pacman actually go to all the explored squares on his way to the goal? (DFS)
Ans: 
No, Pacman doesnot visit every single explored node. 

Question 3: Is this the least cost solution? If not, think about what depth-first search is doing wrong.
Ans: 
No, it is not a least cost solution. As DFS will explore left subtree first and then move on to right one even if the best path available is on the right subtree. 


Question 4: Does BFS find a least cost solution?
Ans: 
Yes, BFS finds the least cost solution provided all the edge costs are constant.

Question 5: What happens on openMaze for various search strategies? 

Ans : 
Pacman Manages to find the goal everytime but with a significant difference between the path cost for various startegies.
ucs produces same result as bfs since the edge cost is constant for all the nodes.
Even though a* with manhattan heuristic takes the same path as ucs abd bfs, I would say it was better becauseit expanded less number of nodes
compared to other strategies.

Strategy 			Nodes Expanded 			Path Cost 			Score
dfs 				806						298					212
bfs 				682						54					456
ucs 				682						54					456
a* (manhattan)		535						54					456


Question 6: Can you solve mediumSearch in a short time?
Ans: No, we cannot. 
'''
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    # "*** YOUR CODE HERE ***"

    from util import Stack
    startPosition = problem.getStartState()
    visited = set()
    path = []
    print("Start Position: ",startPosition)

    s = Stack()
    s.push([startPosition, path])
    # visited.add(startPosition)

    while s:
    	currState, pathTillNow = s.pop()
    	visited.add(currState)
    	if(problem.isGoalState(currState)):
    		print('goal State Found')
    		print(pathTillNow)
    		return pathTillNow
    	successors = problem.getSuccessors(currState)
    	for i in range(len(successors)):
    		nextState = successors[i][0]
    		nextAction = successors[i][1]
    		if(nextState not in visited):
    			s.push([nextState, pathTillNow+[nextAction]])
    			# print(nextState,pathTillNow)

    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # print("bfs called")
    from util import Queue
    startPosition = problem.getStartState()
    q = Queue()
    visited = []
    path = []
    q.push([startPosition, path])
    while q:
    	currState, pathTillNow = q.pop()
    	visited.append(currState)
    	if(problem.isGoalState(currState)):
            # print("here")
            return pathTillNow
    	successors = problem.getSuccessors(currState)
        # print("get successors called")
    	if successors:
            for i in range(len(successors)):
        		nextState = successors[i][0]
        		nextAction = successors[i][1]
        		# print("q list")
        		# for state in q.list:
        		# 	print(state[0])
        		if(nextState not in visited and  nextState not in (state[0] for state in q.list)):
        			q.push([nextState, pathTillNow+[nextAction]])

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue

    startPosition = problem.getStartState()

    pq = PriorityQueue()
    visited = []
    path = []
    pq.push([startPosition, path], 0)
    
    while pq:
        currState, pathTillNow = pq.pop()
        visited.append(currState)

        if(problem.isGoalState(currState)):
            return pathTillNow

        successors = problem.getSuccessors(currState)

        for i in range(len(successors)):
            nextState = successors[i][0]
            nextAction = successors[i][1]
            nextCost = successors[i][2]
            # print()
            if(nextState not in visited) and (nextState not in (state[2][0] for state in (pq.heap))):
                cost = problem.getCostOfActions(pathTillNow+[nextAction])
                pq.push([nextState,pathTillNow+[nextAction]], cost)
            elif(nextState not in visited) and (nextState in (state[2][0] for state in (pq.heap))):
                for state in pq.heap:
                    if state[2][0] == nextState:
                        prevPriority = problem.getCostOfActions(state[2][1])

                newPriority = problem.getCostOfActions(pathTillNow+[nextAction])

                if(prevPriority > newPriority):
                    pq.update([nextState,pathTillNow+[nextAction]], newPriority)



    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem. This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue

    startPosition = problem.getStartState()

    pq = PriorityQueue()
    visited = []
    path = []
    # gCost = 0
    pq.push([startPosition, []], 0)
    
    while pq:
        currState, pathTillNow = pq.pop()
        visited.append(currState)

        if(problem.isGoalState(currState)):
            return pathTillNow

        successors = problem.getSuccessors(currState)

        for i in range(len(successors)):
            nextState = successors[i][0]
            nextAction = successors[i][1]
            nextCost = successors[i][2]
            # print()
            if(nextState not in visited) and (nextState not in (state[2][0] for state in (pq.heap))):
                cost = problem.getCostOfActions(pathTillNow+[nextAction]) + heuristic(nextState, problem)
                pq.push([nextState,pathTillNow+[nextAction]], cost)
            elif(nextState not in visited) and (nextState in (state[2][0] for state in (pq.heap))):
                for state in pq.heap:
                    if state[2][0] == nextState:
                        prevPriority = problem.getCostOfActions(state[2][1])  + heuristic(nextState, problem)

                newPriority = problem.getCostOfActions(pathTillNow+[nextAction])  + heuristic(nextState, problem)

                if(prevPriority > newPriority):
                    pq.update([nextState,pathTillNow+[nextAction]], newPriority)
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
