import random
import numpy as np

class IntegerMaze(object):
    def __init__(self, min=-9999, max=9999, max_num_ops=10, sel_num_ops=4, len_path=4, num_paths=10, op_min=1, op_max=10):
        self.min = min
        self.max = max
        self.max_num_ops = max_num_ops
        self.sel_num_ops = sel_num_ops
        self.len_path = len_path
        self.num_paths = num_paths
        self.op_min = op_min
        self.op_max = op_max

        self.op_pool = self.make_op_pool(self.max_num_ops)
        self.sel_ops = random.sample(self.op_pool, self.sel_num_ops)
        self.paths = self.make_op_paths(self.sel_ops, self.len_path, self.num_paths)

        self.op_counts = {}

    def make_op_pool(self, size):
        pool = []
        op_min = self.op_min
        op_max = self.op_max
        for i in range(op_min, op_max+1):
            pool.append(lambda x, i=i: ('+%d' % i, x+i))
        for i in range(op_min, op_max+1):
            pool.append(lambda x, i=i: ('-%d' % i, x-i))
        for i in range(op_min, op_max+1):
            pool.append(lambda x, i=i: ('*%d' % i, x*i))
        for i in range(op_min, op_max+1):
            pool.append(lambda x, i=i: ('/%d' % i, x/i))
        return random.sample(pool, size)

    def make_op_paths(self, sel_ops, len_path, num_paths):
        paths = []
        for i in range(num_paths):
            paths.append(np.random.choice(sel_ops, len_path))
        return paths

    def print_paths(self):
        for i in range(self.num_paths):
            path = self.paths[i]
            print(self.path_str(path))

    def path_str(self, path):
        return ', '.join(map(lambda f: f(0)[0], path))

    def sampler(self, num):
        samples = []
        for i in np.random.randint(len(self.paths), size=num):
            src = np.random.randint(self.min, high=self.max+1)
            dst = src
            for f in self.paths[i]:
                dst = f(dst)[1]
            print('src: %d, dst: %d, path: %s, possibilities: %d' % (src, dst, self.path_str(self.paths[i]), self.test_possibilities(src, dst)))
            samples.append([src, dst])
        return samples

    def test_possibilities(self, src, dst):
        count = 0
        for f1 in self.op_pool:
            v1 = f1(src)[1]
            for f2 in self.op_pool:
                v2 = f2(v1)[1]
                for f3 in self.op_pool:
                    v3 = f3(v2)[1]
                    for f4 in self.op_pool:
                        v4 = f4(v3)[1]
                        if v4 == dst:
                            count += 1
                            key = '%s, %s, %s, %s' % (f1(0)[0], f2(0)[0], f3(0)[0], f4(0)[0])
                            self.op_counts[key] = self.op_counts.get(key, 0) + 1
        return count


if __name__ == '__main__':
    integer_maze = IntegerMaze(op_min=1, op_max=20, max_num_ops=20, sel_num_ops=6)
    integer_maze.print_paths()
    samples = integer_maze.sampler(1000)

    for k, v in sorted(integer_maze.op_counts.iteritems(), key=lambda (k,v): (-v,k)):
        print('%s: %s' % (k, v))