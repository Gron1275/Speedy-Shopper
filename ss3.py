import time
import os
from multiprocessing import *

grocery_list = ["bread", "milk", "cereal", "butter", "cookies", "cream"]

aisle1 = ["aisle1", "bread", "cereal", "cookies"]
aisle2 = ["aisle2", "butter", "milk", "cream"]
aisles = [aisle1, aisle2]
aisles_rev = [aisle2, aisle1]
requested_aisles = []


class Scan:
    global requested_aisles

    def reg(self, item, conn):
        global requested_aisles
        print("Running: " + current_process().name + " [PID: " + str(os.getpid()) + "]")
        for aisle in aisles:
            if item in aisle:
                print(aisle[0] + " From [reg]")
                if aisle[0] not in requested_aisles:
                    conn.send(aisle[0])  # Pipes info out of sub-process back into main stream
                    conn.close()
        print("Finished: " + current_process().name)

    def rev(self, item, conn):
        print("Running: " + current_process().name + " [PID: " + str(os.getpid()) + "]")
        for aisle in aisles_rev:
            if item in aisle:
                print(aisle[0] + " From [rev]")
                if aisle[0] not in requested_aisles:
                    conn.send(aisle[0])  # Pipes info out of sub-process back into main stream
                    conn.close()
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
cpu_quantity = cpu_count() // 2


def create_processes(item):  # Multi-Process scan threaded to different cpu's
    for i in range(cpu_quantity):
        globals()['parent_conn%s' % i], globals()['child_conn%s' % i] = Pipe()
    for i in range(cpu_quantity):  # Determine whether or not scan will be regular or reversed
        if i % 2 == 0:
            globals()['process%s' % i] = Process(target=scan.reg, args=(item, globals()['child_conn%s' % i],))  # Start regular search process
        else:
            globals()['process%s' % i] = Process(target=scan.rev, args=(item, globals()['child_conn%s' % i],))  # reverse search process

    for i in range(cpu_quantity):
        globals()['process%s' % i].start()  # Initialize all processes and distribute to cpu cores
        temp_rcv = globals()['parent_conn%s' % i].recv()
        if temp_rcv not in requested_aisles:
            requested_aisles.append(temp_rcv)

    for i in range(cpu_quantity):
        globals()['process%s' % i].join()  # Hold program running until all process jobs are complete


if __name__ == '__main__':

    start_time = time.time()

    print(aisles)
    print(aisles_rev)
    print("Amount of CPU's: " + str(cpu_quantity))
    for i in grocery_list:
        create_processes(i)
    print(requested_aisles)  # Print what item from grocery list is in the aisle
    print("Time Completed: " + str(time.time() - start_time))
