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

    inp = input("Choose mode F/I")

    if "I" in inp:
        n = int(input())
        parents = np.array(list((map(int, input().strip().split()))))[:n]
        print(compute_height(n, parents))


    elif "F" in inp:
        file_name = input()

        if "a" not in file_name:
            file = "test/" + file_name
            with open(file, encoding="utf8") as f:
                n = int(f.readLine())
                parents = np.array(list((map(int, f.readLine().strip().split()))))[:n]
                print(compute_height(n, parents))
    




sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)  
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))