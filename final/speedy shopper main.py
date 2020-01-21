
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


class OtherFrame(wx.Frame):

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        search(grocery_list)
        print(requested_aisles_dict)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        full_box = wx.BoxSizer(wx.VERTICAL)

        self.first_output = wx.StaticText(self, wx.ID_ANY, u"Aisles Requested", wx.DefaultPosition, wx.DefaultSize, 0)
        self.first_output.Wrap(-1)

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


if __name__ == '__main__':

    initialize('item_locations.txt')
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()

    print(requested_aisles_dict)  # Print what item from grocery list is in the aisle
    print("Time Completed: " + str(time_completed))
