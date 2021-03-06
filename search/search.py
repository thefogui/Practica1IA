# -*- coding: utf-8 -*-
#
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
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

class State:
    def __init__(self, node, nodeFather):
        if len(node) == 3:
            self.position = node[0]
            self.score = node[2]
            self.direction = node[1]
        else:
            self.position = node
        self.tuple_node = node
        self.nodeFather = nodeFather

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
    "*** YOUR CODE HERE ***"
    closed = []
    solution = []
    frontier = util.Stack()
    """ if the node initial is a solution return build list """
    """ if is not a solution then we put it in the stack """
    i = 0
    nodo = State((0, 0), (0,0))
    while True:
        """ """
        if frontier.isEmpty() and i == 1:
            return []
        if i == 0:
            node = State(problem.getStartState(), (0, 0))
            frontier.push(node)
            i = 1;
        actual_state = frontier.pop()
<<<<<<< HEAD
        """  """
        while not found:
            """ """
            found = problem.isGoalState(actual_state)
            if not not problem.getSuccessors(actual_state) and not found:
                actual_state_successors = problem.getSuccessors(actual_state)
                for state in actual_state_successors:
                    frontier.push(state)
                    family[state] = actual_state
                family_list.append(family)
            if actual_state not in closed:
                closed.append(actual_state)
            if found:
                print "end"
                return []
            actual_state = frontier.pop()
            actual_state = actual_state[0]
=======
        if problem.isGoalState(actual_state.position):
            while nodo != node:
                solution.append(nodo.direction)
                nodo = nodo.nodeFather
            solution.reverse()
            return solution
        if actual_state.position not in closed:
            closed.append(actual_state.position)
            actual_state_successors = problem.getSuccessors(actual_state.position)
            for state in actual_state_successors:
                nodo = State(state, actual_state)
                frontier.push(nodo)
>>>>>>> cad7b64aba19b561834ba109f8fe7683d0d01543
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
