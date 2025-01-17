import time
import os
import wx
from multiprocessing import cpu_count, Pipe, Process, current_process
from aisles import aisles_full
print(aisles_full)
grocery_list = ['bread', 'wine']
time_completed = 0
requested_aisles = []


class Scan:
    global requested_aisles
    global aisles_full

    def reg(self, item, conn):
        global requested_aisles
        print("Running: " + current_process().name + " [PID: " + str(os.getpid()) + "]")
        for grocery in aisles_full:
            if grocery == item:
                print(grocery)
                print(aisles_full[grocery] + " From [reg]")
                if aisles_full[grocery] not in requested_aisles:
                    conn.send(aisles_full[grocery])  # Pipes info out of sub-process back into main stream
                    conn.close()
        print("Finished: " + current_process().name)

    def rev(self, item, conn):
        print("Running: " + current_process().name + " [PID: " + str(os.getpid()) + "]")
        for grocery in aisles_full:
            if grocery == item:
                print(aisles_full[grocery] + " From [rev]")
                if aisles_full[grocery] not in requested_aisles:
                    conn.send(aisles_full[grocery])  # Pipes info out of sub-process back into main stream
                    conn.close()
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


"""
def search(items):
    global time_completed
    start_time = time.time()
    for i in items:
        create_processes(i)
    time_completed = time.time() - start_time
"""

if __name__ == '__main__':
    """app = wx.App()
    frame = Home(None).Show()
    app.MainLoop()"""
    start_time = time.time()
    for i in grocery_list:
        create_processes(i)
    time_completed = time.time() - start_time
    print("Amount of CPU's: " + str(cpu_quantity))
    print(requested_aisles)  # Print what item from grocery list is in the aisle
    print("Time Completed: " + str(time_completed))
