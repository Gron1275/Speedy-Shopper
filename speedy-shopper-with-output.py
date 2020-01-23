import time
import os

import wx




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
        elif line == 'produce':
            aisle_designator = 'produce'
        elif line == 'bakery':
            aisle_designator = 'bakery'
        elif line == 'deli':
            aisle_designator = 'deli'
        elif line == 'meat':
            aisle_designator = 'meat'
        elif line == 'seafood':
            aisle_designator = 'seafood'
        elif line == 'dairy':
            aisle_designator = 'dairy'
        else:
            aisles[line.lower()] = 'aisle ' + str(aisle_designator)
    aisles_full = aisles


class OtherFrame(wx.Frame):

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        print(requested_aisles_dict)
        search(grocery_list)
        print(requested_aisles_dict)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        full_box = wx.BoxSizer(wx.VERTICAL)

        self.first_output = wx.StaticText(self, wx.ID_ANY, u"Aisles Requested", wx.DefaultPosition, wx.DefaultSize, 0)
        self.first_output.Wrap(-1)
        default_pos_x = 5
        counter = 1
        if produce != ["Produce:"]:
            for a in produce:
                self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(default_pos_x, counter * 20), wx.Size(200, 200), 0)
                counter = counter + 1
        if bakery != ["Bakery:"]:
            for a in bakery:
                self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(default_pos_x, counter * 20), wx.Size(200, 200), 0)
                counter = counter + 1
        if deli != ["Deli:"]:
            for a in deli:
                self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(default_pos_x, counter * 20), wx.Size(200, 200), 0)
                counter = counter + 1
        if back != ['Back:']:
            for a in back:
                self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(default_pos_x, counter * 20), wx.Size(200, 200), 0)
                counter = counter + 1
        if meat != ["Meat:"]:
            for a in meat:
                self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(default_pos_x, counter * 20), wx.Size(200, 200), 0)
                counter = counter + 1
        if seafood != ["Seafood:"]:
            for a in seafood:
                self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(default_pos_x, counter * 20), wx.Size(200, 200), 0)
                counter = counter + 1
        for i in range(1, 17):
            if globals()['req_aisle%s' % i] != [f'Aisle {i}' + ":"]:
                for a in globals()['req_aisle%s' % i]:
                    self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(default_pos_x, counter * 20),
                                                       wx.Size(200, 200), 0)
                    counter = counter + 1
        if dairy != ["Dairy:"]:
            for a in dairy:
                self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(default_pos_x, counter * 20), wx.Size(200, 200), 0)
                counter = counter + 1
        if hbc != ["Health and Body Care:"]:
            for a in hbc:
                self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(default_pos_x, counter * 20), wx.Size(200, 200), 0)
                counter = counter + 1
        if pharmacy != ["Pharmacy:"]:
            for a in pharmacy:
                self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(default_pos_x, counter * 20), wx.Size(200, 200), 0)
                counter = counter + 1
        if front != ["Front:"]:
            for a in front:
                self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, a, wx.Point(default_pos_x, counter * 20), wx.Size(200, 200), 0)
                counter = counter + 1


        full_box.Add(self.first_output, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(full_box)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Show()


class MainFrame(wx.Frame):

    global grocery_list

    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=u"Speedy Shopper Program", pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        full_box = wx.BoxSizer(wx.VERTICAL)

        welcome_box = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Welcome to speedy shopper program", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        welcome_box.Add(self.m_staticText1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        input_box = wx.BoxSizer(wx.VERTICAL)

        self.add_items_help = wx.StaticText(self, wx.ID_ANY, u"Add Items to Grocery List", wx.DefaultPosition, wx.DefaultSize, 0)
        self.add_items_help.Wrap(-1)

        input_box.Add(self.add_items_help, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.text_input = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        input_box.Add(self.text_input, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.append_button = wx.Button(self, wx.ID_ANY, u"Add To List", wx.DefaultPosition, wx.DefaultSize, 0)
        input_box.Add(self.append_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.search_button = wx.Button(self, wx.ID_ANY, u"Search Grocery List", wx.DefaultPosition, wx.DefaultSize, 0)
        input_box.Add(self.search_button, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        welcome_box.Add(input_box, 1, wx.ALIGN_CENTER | wx.EXPAND, 5)

        full_box.Add(welcome_box, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.SetSizer(full_box)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.text_input.Bind(wx.EVT_TEXT_ENTER, self.append_grocery)
        self.append_button.Bind(wx.EVT_BUTTON, self.append_grocery)
        self.search_button.Bind(wx.EVT_BUTTON, self.search)

        self.Show()

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def append_grocery(self, event):
        item = self.text_input.GetLineText(0)
        grocery_list.append(item.lower())
        self.text_input.Clear()

    def search(self, event):
        input_frame = OtherFrame(title="Input")
        self.Close()



def scan_reg(item):
    for grocery in aisles_full:
        if grocery == item:
            print(grocery)
            print(aisles_full[grocery] + " From [reg]")
            if aisles_full[grocery] not in requested_aisles_dict:  # take this out for multiple items in aisle
                requested_aisles_dict[aisles_full[grocery]] = []
            (requested_aisles_dict[aisles_full[grocery]]).append(item)


def search(items):
    for i in items:
        scan_reg(i)
    sort_aisles()

for i in range(1,17):
    globals()['req_aisle%s' % i] = [f'Aisle {i}' + ":"]
hbc = ["Health and Body Care:"]
back = ["Back:"]
front = ["Front:"]
pharmacy = ["Pharmacy:"]
produce = ["Produce:"]
bakery = ["Bakery:"]
deli = ["Deli:"]
meat = ["Meat:"]
seafood = ["Seafood:"]
dairy = ["Dairy:"]
def sort_aisles():

    for item in requested_aisles_dict.keys():
        for i in range(1, 17):
            if item == f'aisle {i}':
                for x in requested_aisles_dict[item]:
                    globals()['req_aisle%s' % i].append(requested_aisles_dict[item][requested_aisles_dict[item].index(x)])
        if item == "aisle hbc":
            for i in requested_aisles_dict[item]:
                hbc.append(requested_aisles_dict[item][requested_aisles_dict[item].index(i)])
        elif item == "aisle back":
            for i in requested_aisles_dict[item]:
                back.append(requested_aisles_dict[item][requested_aisles_dict[item].index(i)])
        elif item == "aisle front":
            for i in requested_aisles_dict[item]:
                front.append(requested_aisles_dict[item][requested_aisles_dict[item].index(i)])
        elif item == "aisle pharm":
            for i in requested_aisles_dict[item]:
                pharmacy.append(requested_aisles_dict[item][requested_aisles_dict[item].index(i)])
        elif item == "aisle produce":
            for i in requested_aisles_dict[item]:
                produce.append(requested_aisles_dict[item][requested_aisles_dict[item].index(i)])
        elif item == "aisle bakery":
            for i in requested_aisles_dict[item]:
                bakery.append(requested_aisles_dict[item][requested_aisles_dict[item].index(i)])
        elif item == "aisle deli":
            for i in requested_aisles_dict[item]:
                deli.append(requested_aisles_dict[item][requested_aisles_dict[item].index(i)])
        elif item == "aisle meat":
            for i in requested_aisles_dict[item]:
                meat.append(requested_aisles_dict[item][requested_aisles_dict[item].index(i)])
        elif item == "aisle seafood":
            for i in requested_aisles_dict[item]:
                seafood.append(requested_aisles_dict[item][requested_aisles_dict[item].index(i)])
        elif item == "aisle dairy":
            for i in requested_aisles_dict[item]:
                dairy.append(requested_aisles_dict[item][requested_aisles_dict[item].index(i)])

if __name__ == '__main__':

    initialize('item_locations.txt')

    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

    search(grocery_list)
    print(requested_aisles_dict)  # Print what item from grocery list is in the aisle

    print("Time Completed: " + str(time_completed))
