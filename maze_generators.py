from collections import defaultdict
import random

import numpy as np
import matplotlib.pyplot as plt

N = 19

class Trace(object):
    def __init__(self, root, maze):
        self.root = root
        self.body = set([self.root])
        self.heads = set([self.root])
        maze.add_pos(root, root)
        self.maze = maze
        self.edges = []

    def grow(self):
        picked = self._grow_from_head()
        if picked == 0:
            picked = self._grow_from_body()
        return picked

    def _grow_from_head(self):
        candidates = set(self.heads)
        picked = 0
        while len(candidates) > 0 and picked == 0:
            pos = random.sample(candidates, 1)[0]
            dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            random.shuffle(dirs)
            for d in dirs:
                pos_next = (pos[0]+d[0], pos[1]+d[1])
                if pos_next[0] < 0 or pos_next[0] >= N or pos_next[1] < 0 or pos_next[1] >= N:
                    continue
                if self.maze.find_root(pos_next) is None:
                    self.heads.remove(pos)
                    self.heads.add(pos_next)
                    self.body.add(pos_next)
                    self.maze.add_pos(self.root, pos_next)
                    self.edges.append([pos, pos_next])
                    picked = 1
                    break
                elif self.maze.find_root(pos_next) == self.root:
                    # self.edges.append([pos, pos_next])
                    # break
                    pass
            candidates.remove(pos)
        return picked

    def _grow_from_body(self):
        candidates = set(self.body)
        picked = 0
        while len(candidates) > 0 and picked == 0:
            pos = random.sample(candidates, 1)[0]
            dirs = [(-1,0),(0,-1),(1,0),(0,1)]
            random.shuffle(dirs)
            for d in dirs:
                pos_next = (pos[0]+d[0], pos[1]+d[1])
                if pos_next[0] < 0 or pos_next[0] >= N or pos_next[1] < 0 or pos_next[1] >= N:
                    continue
                if self.maze.find_root(pos_next) is None:
                    if pos in self.heads:
                        self.heads.remove(pos)
                    self.heads.add(pos_next)
                    self.body.add(pos_next)
                    self.maze.add_pos(self.root, pos_next)
                    self.edges.append([pos, pos_next])
                    picked = 1
                    break
                elif self.maze.find_root(pos_next) == self.root:
                    # self.edges.append([pos, pos_next])
                    # break
                    pass
            candidates.remove(pos)
        return picked

class Maze(object):
    def __init__(self):
        self.roots = [(0,0), (N-1,0), (0,N-1), (N-1,N-1)]
        self.traces = {}
        self.map = {}
        for root in self.roots:
            self.traces[root] = Trace(root, self)

    def add_pos(self, root, pos):
        self.map[pos] = root

    def find_root(self, pos):
        return self.map.get(pos, None)

    def build(self):
        growable = True
        while growable:
            picked = 0
            for root in self.roots:
                picked += self.traces[root].grow()
            growable = picked > 0

    def broken_walls(self):
        for root in self.roots:
            for (p1, p2) in self.traces[root].edges:
                if p1[0] == p2[0]:
                    yield ((p1[0], max(p1[1], p2[1])), (p1[0]+1, max(p1[1], p2[1])))
                else:
                    yield ((max(p1[0], p2[0]), p1[1]), (max(p1[0], p2[0]), p1[1] + 1))

def visualize(maze):
    map = {}
    for x in xrange(N+1):
        for y in xrange(N+1):
            if x < N:
                map[((x, y), (x+1, y))] = 1
            if y < N:
                map[((x, y), (x, y+1))] = 1
    for (p1, p2) in maze.broken_walls():
        map[(p1, p2)] = 0
    for e, b in map.iteritems():
        p1 = e[0]
        p2 = e[1]
        if b:
            plt.plot((p1[0], p2[0]), (p1[1], p2[1]), 'ro-')
    plt.plot((N+1)/2-0.5, (N+1)/2-0.5, 'bo', markersize=14)
    plt.plot(0.5, 0.5, 'b*', markersize=14)
    plt.plot(0.5, N-0.5, 'b*', markersize=14)
    plt.plot(N-0.5, 0.5, 'b*', markersize=14)
    plt.plot(N-0.5, N - 0.5, 'b*', markersize=14)
    plt.xlim(-1, N+1)
    plt.ylim(-1, N+1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.gca().set_xticks([])
    plt.gca().set_yticks([])
    # plt.show()
    plt.savefig("maze.png")

if __name__ == '__main__':
    maze = Maze()
    maze.build()
    visualize(maze)