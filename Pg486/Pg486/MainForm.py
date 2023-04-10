import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._button10 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(121, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(239, 39)
		self._label1.TabIndex = 0
		self._label1.Text = "Choose a planet:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(27, 61)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(111, 31)
		self._button1.TabIndex = 1
		self._button1.Text = "Mercury"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(27, 115)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(111, 34)
		self._button2.TabIndex = 2
		self._button2.Text = "Venus"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.White
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(27, 171)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(111, 36)
		self._button3.TabIndex = 3
		self._button3.Text = "Earth"
		self._button3.UseVisualStyleBackColor = False
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.Location = System.Drawing.Point(177, 61)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(113, 31)
		self._button4.TabIndex = 4
		self._button4.Text = "Mars"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.Silver
		self._button5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.Location = System.Drawing.Point(177, 115)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(113, 34)
		self._button5.TabIndex = 5
		self._button5.Text = "Jupiter"
		self._button5.UseVisualStyleBackColor = False
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.Location = System.Drawing.Point(177, 171)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(113, 36)
		self._button6.TabIndex = 6
		self._button6.Text = "Saturn"
		self._button6.UseVisualStyleBackColor = False
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
		self._button7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.Location = System.Drawing.Point(325, 61)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(108, 31)
		self._button7.TabIndex = 7
		self._button7.Text = "Uranus"
		self._button7.UseVisualStyleBackColor = False
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button8.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.Location = System.Drawing.Point(325, 115)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(108, 34)
		self._button8.TabIndex = 8
		self._button8.Text = "Neptune"
		self._button8.UseVisualStyleBackColor = False
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.Color.Peru
		self._button9.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.Location = System.Drawing.Point(325, 171)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(108, 36)
		self._button9.TabIndex = 9
		self._button9.Text = "Pluto"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# button10
		# 
		self._button10.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button10.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button10.Location = System.Drawing.Point(149, 253)
		self._button10.Name = "button10"
		self._button10.Size = System.Drawing.Size(172, 38)
		self._button10.TabIndex = 10
		self._button10.Text = "Exit"
		self._button10.UseVisualStyleBackColor = False
		self._button10.Click += self.Button10Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlLight
		self.ClientSize = System.Drawing.Size(467, 330)
		self.Controls.Add(self._button10)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg486"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from Mercury import *
		mercury = Mercury(self)
		mercury.Show()
		self.Hide()

	

	def Button10Click(self, sender, e):
		Application.Exit()

	def Button4Click(self, sender, e):
		from Mars import *
		mars = Mars(self)
		mars.Show()
		self.Hide()

	def Button9Click(self, sender, e):
		from Pluto import *
		pluto = Pluto(self)
		pluto.Show()
		self.Hide()