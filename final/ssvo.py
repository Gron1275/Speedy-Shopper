import wx
grocery_list = []
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
    global grocery_list

    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        search(grocery_list)
        font_size = 15
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        full_box = wx.BoxSizer(wx.VERTICAL)

        self.first_output = wx.StaticText(self, wx.ID_ANY, u"Aisles Requested", wx.DefaultPosition, wx.DefaultSize, 0)
        self.first_output.SetFont(wx.Font(font_size, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        self.first_output.Wrap(-1)

        X_POSITION = 5
        y_determinate = 1
        grid = wx.GridSizer(0, 2, 0, 0)
        for key in requested_aisles_dict:

            globals()['self.%s' % key] = wx.StaticText(self, wx.ID_ANY, u"{}".format(str(key).title() + ':'), wx.Point(X_POSITION, y_determinate * 10), wx.DefaultSize, 0)
            globals()['self.%s' % str(key) + " items"] = wx.StaticText(self, wx.ID_ANY, u"{}".format(str(', '.join(requested_aisles_dict[key]).title())), wx.Point(X_POSITION, y_determinate * 10), wx.DefaultSize, 0)

            globals()['self.%s' % key].Wrap(-1)
            globals()['self.%s' % str(key) + " items"].Wrap(-1)

            grid.Add(globals()['self.%s' % key], 0, wx.ALL, 5)
            grid.Add(globals()['self.%s' % str(key) + " items"], 0, wx.ALL, 5)

            y_determinate += 1

        self.new_searchbutton = wx.Button(self, wx.ID_ANY, u"New Search", wx.DefaultPosition, wx.DefaultSize, 0)
        self.close_button = wx.Button(self, wx.ID_ANY, u"Close Program", wx.DefaultPosition, wx.DefaultSize, 0)

        full_box.Add(self.first_output, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)
        full_box.Add(grid, 0, wx.ALIGN_CENTER_HORIZONTAL, 5)
        full_box.Add(self.new_searchbutton, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL, 5)
        full_box.Add(self.close_button, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(full_box)
        self.Layout()
        self.Centre(wx.BOTH)

        self.new_searchbutton.Bind(wx.EVT_BUTTON, self.new_search)
        self.close_button.Bind(wx.EVT_BUTTON, self.close_app)

        self.Show()

    def new_search(self, event):
        grocery_list.clear()
        frame = MainFrame()
        self.Close()

    def close_app(self, event):
        self.Close()


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

        self.clear_list = wx.Button(self, wx.ID_ANY, u"Clear Grocery List", wx.DefaultPosition, wx.DefaultSize, 0)
        input_box.Add(self.clear_list, 0, wx.ALIGN_CENTER | wx.ALL, 5)

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
        self.clear_list.Bind(wx.EVT_BUTTON, self.clear_grocerylist)
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
        input_frame = OtherFrame(title="Requested Aisles")
        self.Close()

    def clear_grocerylist(self, event):
        grocery_list.clear()


def search(items):
    for item in items:
        for grocery in aisles_full:
            if grocery == item:
                if aisles_full[grocery] not in requested_aisles_dict:
                    requested_aisles_dict[aisles_full[grocery]] = set()
                (requested_aisles_dict[aisles_full[grocery]]).add(item)


if __name__ == '__main__':

    initialize('updated_item_locations.txt')
    app = wx.App(False)
    frame = MainFrame()
    app.MainLoop()
