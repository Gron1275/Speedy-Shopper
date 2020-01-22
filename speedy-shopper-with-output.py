import time
import os
import wx

grocery_list = []
time_completed = 0
requested_aisles = []
requested_aisles_dict = {}


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
        self.m_button5.Bind(wx.EVT_BUTTON, self.onClose)

    def __del__(self):
        pass
    # Virtual event handlers, overide them in your derived class
    def append_grocery(self, event):
        item = self.text_box.GetLineText(0)
        grocery_list.append(item.lower())
        self.text_box.Clear()
    def search(self, event):
        search(grocery_list)
        wx.Exit()  # Exits so that the multi-processing can begin. Need to find a work around but this be a temp fix
    def onClose(self, event):
        self.Close()

    def __del__(self):
        pass

class Output( wx.Frame ):
	def __init__( self, parent ):
            wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(578, 574), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

            self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

            bSizer1 = wx.BoxSizer(wx.VERTICAL)

            counter = 0
            for i in range(1, 17):
                if globals()['req_aisle%s' % i] != [f'Aisle {i}' + ":"]:
                    for a in globals()['req_aisle%s' % i]:
                        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(-1, counter * 20), wx.Size(200, 200), 0)
                        counter = counter + 1
            if hbc != ["Health and Body Care:"]:
                for a in hbc:
                    self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(-1, counter * 20), wx.Size(200, 200), 0)
                    counter = counter + 1
            if back != ["Back:"]:
                for a in back:
                    self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(-1, counter * 20), wx.Size(200, 200), 0)
                    counter = counter + 1
            if front != ["Front:"]:
                for a in front:
                    self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(-1, counter * 20), wx.Size(200, 200), 0)
                    counter = counter + 1
            if pharmacy != ["Pharmacy:"]:
                for a in pharmacy:
                    self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(-1, counter * 20), wx.Size(200, 200), 0)
                    counter = counter + 1
            #self.m_staticText2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

            #bSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

            self.SetSizer(bSizer1)
            self.Layout()

            self.Centre(wx.BOTH)


            def __del__(self):
                pass




aisles = {}
aisles_full = {}


def initialize(data2):
    global aisles
    global aisles_full
    data = open(data2).read().splitlines()

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

class Scan:
    global requested_aisles_dict
    global aisles_full

    def reg(self, item):
        print("Running: " + "[PID: " + str(os.getpid()) + "]")
        for grocery in aisles_full:
            if grocery == item:
                print(grocery)
                print(aisles_full[grocery] + " From [reg]")
                '''
                if aisles_full[grocery] not in requested_aisles_dict.keys():
                    requested_aisles_dict[aisles_full[grocery]] = item
                '''
                requested_aisles_dict[aisles_full[grocery]] = grocery
        print("Finished: " + "[PID: " + str(os.getpid()) + "]")


scan = Scan()


def search(items):
    global time_completed
    start_time = time.time()
    for i in items:
        scan.reg(i)
    time_completed = time.time() - start_time

for i in range(1,17):
    globals()['req_aisle%s' % i] = [f'Aisle {i}' + ":"]
hbc = ["Health and Body Care:"]
back = ["Back:"]
front = ["Front:"]
pharmacy = ["Pharmacy:"]
def sort_aisles():
    # Sorts groceries into their respective aisles and prints them in order
    for item in requested_aisles_dict.keys():
        for i in range(1, 17):
            if item == f'aisle {i}':
                globals()['req_aisle%s' % i].append(requested_aisles_dict[item])
        if item == "aisle hbc":
            hbc.append(requested_aisles_dict[item])

        elif item == "aisle back":
            back.append(requested_aisles_dict[item])

        elif item == "aisle front":
            front.append(requested_aisles_dict[item])

        elif item == "aisle pharm":
            pharmacy.append(requested_aisles_dict[item])



if __name__ == '__main__':
    app = wx.App()
    frame = Home(None).Show()
    app.MainLoop()
    initialize('info.txt')
    search(grocery_list)
    sort_aisles()
    print(requested_aisles_dict)  # Print what item from grocery list is in the aisle
    app2 = wx.App()
    frame2 = Output(None).Show()
    app2.MainLoop()
    print(requested_aisles_dict)
    print("Time Completed: " + str(time_completed))