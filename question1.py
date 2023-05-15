import random

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class Random:
    def __init__(self):
        self.randoms = []
        for i in range(10000000):
            self.randoms.append(random.uniform(0, 1))
            
    def get_randoms(self):
        return self.randoms

class State:
    def __init__(self):
        self.s1 = Node(100)
        self.s2 = Node(500)
        self.s3 = Node(1000)
        self.s4 = Node(5000)
        self.s5 = Node(10000)
        self.s6 = Node(50000)
        self.s7 = Node(100000)
        self.s8 = Node(500000)
        self.s9 = Node(1000000)
        self.s10 = Node(5000000)
        self.s1.next = self.s2
        self.s2.next = self.s3
        self.s3.next = self.s4
        self.s4.next = self.s5
        self.s5.next = self.s6
        self.s6.next = self.s7
        self.s7.next = self.s8
        self.s8.next = self.s9
        self.s9.next = self.s10

class Iterate:
    def __init__(self):
        self.stopper = False
        self.times_visited = {}
        self.value_function = {}
        self.head = None
        self.gamma = 1
        self.theta = 0.00005
        self.prob = [1, 0.99, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
        self.randoms = []
        self.itr = 0
        self.cnt = 0
        
        obj = State()
        self.head = obj.s1
        
        obj1 = Random()
        self.randoms = obj1.get_randoms()

    def print_state_transition(self):
        for state in self.times_visited:
            print(state, end=" ")
        print()
        for state in self.times_visited:
            print((self.times_visited[state] * 100) // self.cnt, end=" ")
        print()

    def get_stopper_state(self):
        return self.stopper

    def dfs(self, temp, curr_state):
        self.times_visited[curr_state] = self.times_visited.get(curr_state, 0) + 1
        if not temp:
            return (curr_state, 0)
        max_state_reached = curr_state
        answer_reward = 0
        mx = 0
        old_value = self.value_function.get(curr_state, 0)
        quit_reward = self.value_function.get(curr_state - 1, 0)
        if self.randoms[self.itr % 10000000] <= self.prob[curr_state]:
            self.itr += 1
            next_state_reward = self.dfs(temp.next, curr_state + 1)
            answer_reward = self.prob[curr_state] * (self.gamma * next_state_reward[1] + temp.val)
            max_state_reached = max(max_state_reached, next_state_reward[0])
            self.value_function[curr_state] = (self.value_function.get(curr_state, 0) * (self.times_visited[curr_state] - 1) + answer_reward) / (self.times_visited[curr_state])
            if abs(old_value - self.value
