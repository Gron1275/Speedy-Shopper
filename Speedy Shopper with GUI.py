import time
import os
import wx

grocery_list = []

time_completed = 0
requested_aisles = []
requested_aisles_dict = {}
aisles = {}
aisles_full = {}


def initialize(file):
    global aisles
    global aisles_full
    data = open(file).read().splitlines()

    aisle_designator = 0

    for line in data:
        if line == '':
            aisle_designator += 1
        elif line == 'hbc':
            aisle_designator = 'hbc'
        elif line == 'front':
            aisle_designator = 'front'
        elif line == 'back':
            aisle_designator = 'back'
        elif line == 'pharmacy':
            aisle_designator = 'pharmacy'
        else:
            aisles[line.lower()] = 'aisle ' + str(aisle_designator)
    aisles_full = aisles


class Output(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=u'Output Frame', pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        self.wait_pls = wx.StaticText(self, wx.ID_ANY, u"Gathering Information", wx.DefaultPosition, wx.DefaultSize, 0)
        self.wait_pls.Wrap(-1)
        bSizer2.Add(self.wait_pls, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.gauge = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL)
        self.gauge.SetValue(0)
        bSizer2.Add(self.gauge, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        bSizer1.Add(bSizer2, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)


class Home(wx.Frame):
    global grocery_list

    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=u'speedy shop', pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)
        self.welcome = wx.StaticText(self, wx.ID_ANY, u"Welcome to speedy shopper program", wx.DefaultPosition, wx.DefaultSize, 0)
        self.welcome.Wrap(-1)
        bSizer2.Add(self.welcome, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        bSizer3 = wx.BoxSizer(wx.VERTICAL)
        self.instructions = wx.StaticText(self, wx.ID_ANY, u"Add Items to Grocery List", wx.DefaultPosition, wx.DefaultSize, 0)
        self.instructions.Wrap(-1)
        bSizer3.Add(self.instructions, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.text_box = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.text_box, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.append_button = wx.Button(self, wx.ID_ANY, u"Add To List", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.append_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.search_button = wx.Button(self, wx.ID_ANY, u"Search Grocery List", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.search_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        bSizer2.Add(bSizer3, 1, wx.ALIGN_CENTER | wx.EXPAND, 5)
        bSizer1.Add(bSizer2, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)
        # Connect Events
        self.append_button.Bind(wx.EVT_BUTTON, self.append_grocery)
        self.text_box.Bind(wx.EVT_TEXT_ENTER, self.append_grocery)
        self.search_button.Bind(wx.EVT_BUTTON, self.search)

        # Connect Events

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class

    def load_outFrame(self):

        wx.Frame.Close(self)

    def append_grocery(self, event):
        item = self.text_box.GetLineText(0)
        grocery_list.append(item.lower())
        self.text_box.Clear()

    def search(self, event):
        # self.frame.Show()
        search(grocery_list)
        wx.Exit()

    def onClose(self, event):
        self.Close()


def scan_reg(item):
    print("Running: " + "[PID: " + str(os.getpid()) + "]")
    for grocery in aisles_full:
        if grocery == item:
            print(grocery)
            print(aisles_full[grocery] + " From [reg]")
            # if aisles_full[grocery] not in requested_aisles_dict.keys():  # take this out for multiple items in aisle
            requested_aisles_dict[aisles_full[grocery]] = item
            #  integrate dict requested_aisles = {aisle 1: ['bread', 'wine', etc.], aisle 2: ['cheese']}
    print("Finished: " + "[PID: " + str(os.getpid()) + "]")


def search(items):
    time.sleep(0.5)
    output = Output()
    global time_completed
    start_time = time.time()
    percentage_complete = 1 / len(grocery_list)
    for i in items:
        scan_reg(i)
        # print("Percent Complete: " + str(output.gauge.GetValue()))
        # output.gauge.SetValue = output.gauge.GetValue() + percentage_complete

    time_completed = time.time() - start_time


if __name__ == '__main__':

    initialize('item_locations.txt')
    app = wx.App()
    frame1 = Home()
    frame1.Show()
    # frame2 = Output().Show()
    app.MainLoop()

    print(requested_aisles_dict)  # Print what item from grocery list is in the aisle
    print("Time Completed: " + str(time_completed))
