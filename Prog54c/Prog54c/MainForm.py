import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Orange
		self._label1.Location = System.Drawing.Point(69, 36)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(165, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "radius"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(134, 36)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._button1.Location = System.Drawing.Point(94, 177)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(104, 37)
		self._button1.TabIndex = 2
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button2.Location = System.Drawing.Point(26, 220)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(86, 29)
		self._button2.TabIndex = 3
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button3.Location = System.Drawing.Point(169, 220)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(90, 29)
		self._button3.TabIndex = 4
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Silver
		self._label2.LiveSetting = System.Windows.Forms.Automation.AutomationLiveSetting.Polite
		self._label2.Location = System.Drawing.Point(94, 88)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Area"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Silver
		self._label3.Location = System.Drawing.Point(94, 129)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Perimeter"
		self._label3.Click += self.Label3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		r = float(self._textBox1.Text)
		pi = 3.14159
		
		area = pi * r * r
		perim = 2 * pi * r
		
		self._label2.Text = "Area: " + str(area)
		self._label3.Text = "Perimeter: " + str(perim)
		
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label2.Text = "Area: "
		self._label3.Text = "Perimeter: "
		
	def Button3Click(self, sender, e):
		Application.Exit()

	def Label3Click(self, sender, e):
		pass