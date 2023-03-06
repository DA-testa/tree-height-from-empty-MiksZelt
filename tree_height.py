
# Miks Zeltiņš  221RDB123  13.Grupa

import sys
import threading
import numpy as np


def compute_height(sk, parents):
    pos = np.zeros([sk], dtype = np.int32)
    max_h_arr = np.zeros([sk], dtype = np.int32)

    for i in range(sk):
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

    inp = input()

    if "I" in inp:
        sk = int(input())
        parents = np.array(list((map(int, input().strip().split()))))[:sk]
        height = compute_height(sk, parents)
        print(height)


    elif "F" in inp:
        file_name = input()

        if "a" not in file_name:
            file = "test/" + file_name
            with open(file, encoding="utf8") as f:
                sk = int(f.readLine())
                parents = np.array(list((map(int, f.readLine().strip().split()))))[:sk]
                height = compute_height(sk, parents)
                print(height)
    




sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)  
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))