import time
import os
import wx
from multiprocessing import *

grocery_list = []

aisle1 = ["aisle1", "bread", "cereal", "cookies"]
aisle2 = ["aisle2", "butter", "milk", "cream"]
aisles = [aisle1, aisle2]
aisles_rev = [aisle2, aisle1]
requested_aisles = []


class Home(wx.Frame):
    global grocery_list

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Speedy Shopper Program", pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Welcome to speedy shopper program", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        bSizer2.Add(self.m_staticText1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Add Items to Grocery List", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        bSizer3.Add(self.m_staticText2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.text_box = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.text_box, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Add To List", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button3, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Search Grocery List", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button5, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add(bSizer3, 1, wx.ALIGN_CENTER | wx.EXPAND, 5)

        bSizer1.Add(bSizer2, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button3.Bind(wx.EVT_BUTTON, self.append_grocery)
        self.text_box.Bind(wx.EVT_TEXT_ENTER, self.append_grocery)
        self.m_button5.Bind(wx.EVT_BUTTON, self.search)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def append_grocery(self, event):
        item = self.text_box.GetLineText(0)
        grocery_list.append(item.lower())
        self.text_box.Clear()

    def search(self, event):
        search(grocery_list)
        wx.Exit()


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


def search(items):
    for i in items:
        create_processes(i)


if __name__ == '__main__':
    app = wx.App()
    frame = Home(None).Show()
    app.MainLoop()
    start_time = time.time()
    print("Amount of CPU's: " + str(cpu_quantity))
    print(requested_aisles)  # Print what item from grocery list is in the aisle
    print("Time Completed: " + str(time.time() - start_time))
