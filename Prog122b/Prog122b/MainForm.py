import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(27, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(233, 264)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button1.Location = System.Drawing.Point(27, 319)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(120, 59)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button2.Location = System.Drawing.Point(176, 319)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(93, 26)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._button3.Location = System.Drawing.Point(176, 351)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(93, 27)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(295, 407)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122b"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		
		num = 1
		while num <= 40:
			self._listBox1.Items.Add(str(num) + "\t" + str(num * 4))
			num += 1

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		
	

	def Button3Click(self, sender, e):
		 Application.Exit()