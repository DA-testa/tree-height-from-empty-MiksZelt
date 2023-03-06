# python3
# Miks Zeltiņš  221RDB123  13.Grupa

import sys
import threading
import numpy as np


def compute_height(n, parents):
    pos = np.zeros([n], dtype = np.int32)
    max_h_arr = np.zeros([n], dtype = np.int32)

    for i in range(n):
        if pos[i] == 0:
            node = i
            rep = 0
            while node != -1:
                pos[node] = 1
                rep = rep + 1
                max_h_arr[i] = rep
                node = parents[node]

    return max(max_h_arr)

def main():
    UserInput = input("Choose mode F/I")

    if "I" in UserInput:
        n = int(input())
        parents = np.array(list(map(int, input().strip().split())))
        print(compute_height(n, parents))


    elif "F" in UserInput:
        file_name = input().strip()

        if  "a" in file_name:
            return
        file_path = ("test/" + file_name)

        with open(file_path, "r" ) as f:
            n = int(f.readLine())
            parents = np.array(list(map(int, f.readLine().strip().split())))
            print(compute_height(n, parents))
    else:
        quit()  



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))