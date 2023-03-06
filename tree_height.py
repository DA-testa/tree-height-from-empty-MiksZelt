
# Miks Zeltiņš  221RDB123  13.Grupa

import sys
import threading
import numpy as np


def compute_height(sk, parents):
    # 2 arrays
    pos = np.zeros([sk], dtype = int)
    max_h_arr = np.zeros([sk], dtype = int)
    # Calculates max height
    for i in range(sk):
        if pos[i] == 0:
            node = i
            rep = 0
            while node != -1:      
                pos[node] = 1
                rep = rep + 1
                node = parents[node]
                max_h_arr[i] = rep
    return max(max_h_arr)

def main():

    inp = input()
    # capital I code
    if "I" in inp:
        sk = int(input())
        parents = (list(map(int, input().strip().split())))
        print(compute_height(sk, parents))

    # capital F code
    elif "F" in inp:
        file_name = input()
        # Outputs error if "a" is in name
        if "a" in file_name:
            print("Error")
            return
        file = "test/" + file_name

        with open(file, encoding="utf8") as f:
            sk = int(f.readline())
            parents = (list(map(int, f.readline().strip().split())))
            print(compute_height(sk, parents))
    else:
        quit()




sys.setrecursionlimit(10**7)  
threading.stack_size(2**27)  
threading.Thread(target=main).start()
# main()
# print(numpy.array([1,2,3]))