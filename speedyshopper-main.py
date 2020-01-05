import time
import os
from multiprocessing import *

grocery_list = ["bread", "butter", "cereal"]
aisle1 = ["aisle1", "bread", "cereal", "cookies"]
aisle2 = ["aisle2", "butter", "milk", "cream"]
aisles = [aisle1, aisle2]
aisles_rev = aisles
aisles_rev.reverse()
requested_aisles = []


class Scan:
    global requested_aisles

    def reg(self, item):
        global requested_aisles
        print("Running: " + current_process().name + " [PID: " + str(os.getpid()) + "]")
        for aisle in aisles:
            if item in aisle:
                print(aisle[0] + " From [reg]")
                if aisle[0] not in requested_aisles:
                    requested_aisles.append(aisle[0])
        print("Finished: " + current_process().name)

    def rev(self, item):
        print("Running: " + current_process().name + " [PID: " + str(os.getpid()) + "]")
        for aisle in aisles_rev:
            if item in aisle:
                print(aisle[0] + " From [rev]")
                if aisle[0] not in requested_aisles:
                    requested_aisles.append(aisle[0])
        print("Finished: " + current_process().name)

    def sort(self, item):
        print("Running: " + current_process().name + " [PID: " + str(os.getpid()) + "]")
        for aisle in aisles:
            if item in aisle:
                print(aisle[0] + " From search sort")
                if aisle[0] not in requested_aisles:
                    requested_aisles.append(aisle[0])
        print("Finished: " + current_process().name)


scan = Scan()
cpu_quantity = cpu_count()


def create_processes(item):  # Multi-Process scan threaded to different cpus

    for i in range(cpu_quantity):  # Determine whether or not scan will be regular or reversed
        if i % 2 == 0:
            globals()['process%s' % i] = Process(target=scan.reg, args=(item,))  # Start regular search process
        else:
            globals()['process%s' % i] = Process(target=scan.rev, args=(item,))  # reverse search process

    for i in range(cpu_quantity):
        globals()['process%s' % i].start()  # Initialize all processes and distribute to cpu cores

    for i in range(cpu_quantity):
        globals()['process%s' % i].join()  # Hold program running until all process jobs are complete


if __name__ == '__main__':
    starttime = time.time()
    print(aisles)
    print(aisles_rev)
    print("Amount of CPU's: " + str(cpu_quantity))
    for i in grocery_list:
        create_processes(i)
    print(requested_aisles)
    print("Time Completed: " + str(time.time() - starttime))
