
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
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._checkBox6 = System.Windows.Forms.CheckBox()
		self._button1 = System.Windows.Forms.Button()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox5 = System.Windows.Forms.CheckBox()
		self._label2 = System.Windows.Forms.Label()
		self._checkBox4 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(10, 359)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(171, 34)
		self._label1.TabIndex = 12
		self._label1.Text = "Your total charge:"
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(11, 406)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(91, 37)
		self._button3.TabIndex = 11
		self._button3.Text = "Show"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Silver
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(299, 406)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(97, 37)
		self._button2.TabIndex = 10
		self._button2.Text = "Close"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# checkBox6
		# 
		self._checkBox6.Location = System.Drawing.Point(7, 146)
		self._checkBox6.Name = "checkBox6"
		self._checkBox6.Size = System.Drawing.Size(360, 28)
		self._checkBox6.TabIndex = 3
		self._checkBox6.Text = "Network Security"
		self._checkBox6.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(152, 406)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(90, 37)
		self._button1.TabIndex = 9
		self._button1.Text = "Reset"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._groupBox1.Controls.Add(self._checkBox2)
		self._groupBox1.Controls.Add(self._checkBox1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(11, 9)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(390, 124)
		self._groupBox1.TabIndex = 7
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Conference"
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(7, 83)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(377, 32)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Opening night dinner and keynote"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(7, 38)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(377, 38)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Conference Registration"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox5
		# 
		self._checkBox5.Location = System.Drawing.Point(7, 107)
		self._checkBox5.Name = "checkBox5"
		self._checkBox5.Size = System.Drawing.Size(383, 32)
		self._checkBox5.TabIndex = 2
		self._checkBox5.Text = "Advanced Visual Basic"
		self._checkBox5.UseVisualStyleBackColor = True
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(187, 359)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(102, 34)
		self._label2.TabIndex = 13
		# 
		# checkBox4
		# 
		self._checkBox4.Location = System.Drawing.Point(7, 68)
		self._checkBox4.Name = "checkBox4"
		self._checkBox4.Size = System.Drawing.Size(383, 32)
		self._checkBox4.TabIndex = 1
		self._checkBox4.Text = "The future of the Web"
		self._checkBox4.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Location = System.Drawing.Point(7, 29)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(360, 32)
		self._checkBox3.TabIndex = 0
		self._checkBox3.Text = "Introduction to E-commerce"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._groupBox2.Controls.Add(self._checkBox6)
		self._groupBox2.Controls.Add(self._checkBox5)
		self._groupBox2.Controls.Add(self._checkBox4)
		self._groupBox2.Controls.Add(self._checkBox3)
		self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(11, 151)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(390, 188)
		self._groupBox2.TabIndex = 8
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Workshop"
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(411, 452)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._groupBox2)
		self.Name = "Form1"
		self.Text = "Form1"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)

	def Button2Click(self, sender, e):
		self.Close()
		self.parent.Show()
		

	def Button3Click(self, sender, e):
		charge = 0
		if self._checkBox1.Checked:
			charge += 895
		if self._checkBox2.Checked:
			charge += 30
		if self._checkBox3.Checked:
			charge += 295
		if self._checkBox4.Checked:
			charge += 295
		if self._checkBox5.Checked:
			charge += 395
		if self._checkBox6.Checked:
			charge += 395
			
		self._label2.Text = str(charge)
			
		

	def Button1Click(self, sender, e):
		self._label2.Text = ""