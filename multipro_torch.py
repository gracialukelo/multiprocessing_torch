import torch.multiprocessing as mp
import os

def worker1():
    # printing process id
    print("ID of process running worker1: {}".format(os.getpid()))

def worker2():
    # printing process id
    print("ID of process running worker2: {}".format(os.getpid()))

if __name__ == "__main__":
    # printing main program process id
    print("ID of main process: {}".format(os.getpid()))

    # Start method for compatibility with CUDA (use "spawn")
    mp.set_start_method('spawn', force=True)

    # creating processes
    p1
