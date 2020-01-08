class Home ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Speedy Shopper Program", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Welcome to speedy shopper program", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Add Items to Grocery List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer3.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_textCtrl1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Add To List", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.m_button5 = wx.Button( self, wx.ID_ANY, u"Search Grocery List", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_button5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer2.Add( bSizer3, 1, wx.ALIGN_CENTER|wx.EXPAND, 5 )


		bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button3.Bind( wx.EVT_BUTTON, self.append_grocery )
		self.m_button5.Bind( wx.EVT_BUTTON, self.search )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def append_grocery( self, event ):
		event.Skip()

	def search( self, event ):
		event.Skip()

