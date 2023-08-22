# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-370-gc831f1f7)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Calculator", wx.DefaultPosition, wx.Size( 500,-1 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText1.Wrap( -1 )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 500,-1 ), wx.TE_CENTER )
		bSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Square", wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
		bSizer1.Add( self.m_button2, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), wx.TE_CENTER )
		bSizer1.Add( self.m_textCtrl21, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button2.Bind( wx.EVT_BUTTON, self.Square )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def Square( self, event ):
		# Your event handling code here
		inputValue = self.m_textCtrl2.GetValue()
		try:
			number = float(inputValue)
			squareValue = number * number
			self.m_textCtrl21.SetValue(str(squareValue))
		except ValueError:
			wx.MessageBox("Please enter a valid number!", "Error", wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame1(None)
    frame.Show(True)
    app.MainLoop()