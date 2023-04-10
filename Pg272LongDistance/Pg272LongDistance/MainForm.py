import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleTurquoise
		self._button1.Location = System.Drawing.Point(98, 46)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(128, 59)
		self._button1.TabIndex = 0
		self._button1.Text = "Daytime"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button2.Location = System.Drawing.Point(98, 159)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(128, 56)
		self._button2.TabIndex = 1
		self._button2.Text = "Evening"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button3.Location = System.Drawing.Point(98, 275)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(128, 55)
		self._button3.TabIndex = 2
		self._button3.Text = "Off-peak"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(335, 379)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg272LongDistance"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self, "Enter time: ")
		form1.Show()
		self.Hide()

	def Button2Click(self, sender, e):
		from Form2 import *
		form2 = Form2(self, "Enter time: ")
		form2.Show()
		self.Hide()
		

	def Button3Click(self, sender, e):
		from Form3 import *
		form3 = Form3(self, "Enter time: ")
		form3.Show()
		self.Hide()