import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._label1 = System.Windows.Forms.Label()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._checkBox4 = System.Windows.Forms.CheckBox()
		self._checkBox5 = System.Windows.Forms.CheckBox()
		self._checkBox6 = System.Windows.Forms.CheckBox()
		self._checkBox7 = System.Windows.Forms.CheckBox()
		self._checkBox8 = System.Windows.Forms.CheckBox()
		self._checkBox9 = System.Windows.Forms.CheckBox()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(27, 43)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Regular Shade"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(165, 31)
		self._label1.TabIndex = 1
		self._label1.Text = "Select a style:"
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(27, 73)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 23)
		self._radioButton2.TabIndex = 2
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Folding Shade"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(27, 102)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 3
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Roman Shade"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(222, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(146, 27)
		self._label2.TabIndex = 4
		self._label2.Text = "Select a size:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 187)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(150, 29)
		self._label3.TabIndex = 9
		self._label3.Text = "Select a color:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 395)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(215, 31)
		self._label4.TabIndex = 15
		self._label4.Text = "Your total charge is:"
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(222, 395)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(106, 31)
		self._label5.TabIndex = 16
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._button1.Location = System.Drawing.Point(241, 213)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(104, 36)
		self._button1.TabIndex = 17
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._button2.Location = System.Drawing.Point(241, 268)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(104, 35)
		self._button2.TabIndex = 18
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.InactiveCaption
		self._button3.Location = System.Drawing.Point(241, 329)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(104, 35)
		self._button3.TabIndex = 19
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(241, 42)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 20
		self._checkBox1.Text = "25 inches wide"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(241, 73)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 21
		self._checkBox2.Text = "27 inches wide"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Location = System.Drawing.Point(241, 103)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 22
		self._checkBox3.Text = "32 inches wide"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# checkBox4
		# 
		self._checkBox4.Location = System.Drawing.Point(241, 133)
		self._checkBox4.Name = "checkBox4"
		self._checkBox4.Size = System.Drawing.Size(104, 24)
		self._checkBox4.TabIndex = 23
		self._checkBox4.Text = "40 inches wide"
		self._checkBox4.UseVisualStyleBackColor = True
		# 
		# checkBox5
		# 
		self._checkBox5.Location = System.Drawing.Point(27, 220)
		self._checkBox5.Name = "checkBox5"
		self._checkBox5.Size = System.Drawing.Size(104, 24)
		self._checkBox5.TabIndex = 24
		self._checkBox5.Text = "Natural"
		self._checkBox5.UseVisualStyleBackColor = True
		# 
		# checkBox6
		# 
		self._checkBox6.Location = System.Drawing.Point(27, 251)
		self._checkBox6.Name = "checkBox6"
		self._checkBox6.Size = System.Drawing.Size(104, 24)
		self._checkBox6.TabIndex = 25
		self._checkBox6.Text = "Blue"
		self._checkBox6.UseVisualStyleBackColor = True
		# 
		# checkBox7
		# 
		self._checkBox7.Location = System.Drawing.Point(27, 282)
		self._checkBox7.Name = "checkBox7"
		self._checkBox7.Size = System.Drawing.Size(104, 24)
		self._checkBox7.TabIndex = 26
		self._checkBox7.Text = "Teal"
		self._checkBox7.UseVisualStyleBackColor = True
		# 
		# checkBox8
		# 
		self._checkBox8.Location = System.Drawing.Point(27, 313)
		self._checkBox8.Name = "checkBox8"
		self._checkBox8.Size = System.Drawing.Size(104, 24)
		self._checkBox8.TabIndex = 27
		self._checkBox8.Text = "Red"
		self._checkBox8.UseVisualStyleBackColor = True
		# 
		# checkBox9
		# 
		self._checkBox9.Location = System.Drawing.Point(27, 340)
		self._checkBox9.Name = "checkBox9"
		self._checkBox9.Size = System.Drawing.Size(104, 24)
		self._checkBox9.TabIndex = 28
		self._checkBox9.Text = "Green"
		self._checkBox9.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ScrollBar
		self.ClientSize = System.Drawing.Size(424, 450)
		self.Controls.Add(self._checkBox9)
		self.Controls.Add(self._checkBox8)
		self.Controls.Add(self._checkBox7)
		self.Controls.Add(self._checkBox6)
		self.Controls.Add(self._checkBox5)
		self.Controls.Add(self._checkBox4)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "Pg485ShadeDesigner"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label5.Text = ""
		charge = 50
		if self._radioButton1.Checked:
			charge += 0
		if self._radioButton2.Checked:
			charge += 10
		if self._radioButton3.Checked:
			charge += 15
		if self._checkBox1.Checked:
			charge += 0
		if self._checkBox2.Checked:
			charge += 2
		if self._checkBox3.Checked:
			charge += 4
		if self._checkBox4.Checked:
			charge += 6
		if self._checkBox5.Checked:
			charge += 5
		if self._checkBox6.Checked:
			charge += 0
		if self._checkBox7.Checked:
			charge += 0
		if self._checkBox8.Checked:
			charge += 0
		if self._checkBox9.Checked:
			charge += 0
			
		self._label5.Text = str(charge)


	def Button2Click(self, sender, e):
		self._label5.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()