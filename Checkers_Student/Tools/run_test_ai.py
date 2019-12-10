import os
from multiprocessing import  Pool
import time

'''
command1 = "python3 /home/yuerongz/Checkers_Student/Tools/AI_Runner.py 9 8 2 l /home/yuerongz/Checkers_Student/Tools/Sample_AIs/Poor_AI/main.py /home/yuerongz/Checkers_Student/src/checkers-python/main.py"
command2 = "python3 /home/yuerongz/Checkers_Student/Tools/AI_Runner.py 9 8 2 l /home/yuerongz/Checkers_Student/src/checkers-python/main.py /home/yuerongz/Checkers_Student/Tools/Sample_AIs/Poor_AI/main.py"
command3 = "python3 /home/yuerongz/Checkers_Student/Tools/AI_Runner.py 7 7 2 l /home/yuerongz/Checkers_Student/Tools/Sample_AIs/Poor_AI/main.py /home/yuerongz/Checkers_Student/src/checkers-python/main.py"
command4 = "python3 /home/yuerongz/Checkers_Student/Tools/AI_Runner.py 7 7 2 l /home/yuerongz/Checkers_Student/src/checkers-python/main.py /home/yuerongz/Checkers_Student/Tools/Sample_AIs/Poor_AI/main.py"
'''

command1 = "python3 /home/yuerongz/Checkers_Student/Tools/AI_Runner.py 9 8 2 l /home/yuerongz/Checkers_Student/Tools/Sample_AIs/Average_AI/main.py /home/yuerongz/Checkers_Student/src/checkers-python/main.py"
command2 = "python3 /home/yuerongz/Checkers_Student/Tools/AI_Runner.py 9 8 2 l /home/yuerongz/Checkers_Student/src/checkers-python/main.py /home/yuerongz/Checkers_Student/Tools/Sample_AIs/Average_AI/main.py"
command3 = "python3 /home/yuerongz/Checkers_Student/Tools/AI_Runner.py 7 7 2 l /home/yuerongz/Checkers_Student/Tools/Sample_AIs/Average_AI/main.py /home/yuerongz/Checkers_Student/src/checkers-python/main.py"
command4 = "python3 /home/yuerongz/Checkers_Student/Tools/AI_Runner.py 7 7 2 l /home/yuerongz/Checkers_Student/src/checkers-python/main.py /home/yuerongz/Checkers_Student/Tools/Sample_AIs/Average_AI/main.py"

test_time = 40

def run1(i):
    start = time.time()
    os.system(command1)
    print(i,time.time()-start)

def run2(i):
    start = time.time()
    os.system(command2)
    print(i,time.time()-start)

def run3(i):
    start = time.time()
    os.system(command3)
    print(i,time.time()-start)

def run4(i):
    start = time.time()
    os.system(command4)
    print(i,time.time()-start)

if __name__ == '__main__':
    p = Pool(test_time)
    for i in range(1, test_time+1):
        # Our AI as player 2
        #p.apply_async(run1, args=(i,))
        #p.apply_async(run3, args=(i,))

        #Our AI as player 1
        p.apply_async(run2, args=(i,))
        #p.apply_async(run4, args=(i,))
    print("Start running")
    p.close()
    p.join()
    print("Done")