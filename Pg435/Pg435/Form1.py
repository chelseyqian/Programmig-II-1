
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent = parent
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(63, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(181, 39)
		self._label1.TabIndex = 0
		self._label1.Text = "General sales"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(49, 86)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(195, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Select a section:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Location = System.Drawing.Point(103, 130)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(114, 50)
		self._button1.TabIndex = 2
		self._button1.Text = "Section A"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button2.Location = System.Drawing.Point(103, 210)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(114, 49)
		self._button2.TabIndex = 3
		self._button2.Text = "Section B"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button3.Location = System.Drawing.Point(103, 291)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(114, 50)
		self._button3.TabIndex = 4
		self._button3.Text = "Section C"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(321, 395)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.FormClosing += self.Form1FormClosing
		self.ResumeLayout(False)
		
	


	def Button1Click(self, sender, e):
		from FormA import *
		forma = FormA(self)
		forma.Show()
		self.Hide()

	def Button2Click(self, sender, e):
		from FormB import *
		formb = FormB(self)
		formb.Show()
		self.Hide()

	def Button3Click(self, sender, e):
		from FormC import *
		formc = FormC(self)
		formc.Show()
		self.Hide()
		
	def Form1FormClosing(self, sender, e):
		self.parent.Show()