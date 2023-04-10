import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._radioButton10 = System.Windows.Forms.RadioButton()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._checkBox4 = System.Windows.Forms.CheckBox()
		self._checkBox5 = System.Windows.Forms.CheckBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.SystemColors.ControlLight
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(207, 119)
		self._groupBox1.TabIndex = 0
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Decks"
		# 
		# groupBox2
		# 
		self._groupBox2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._groupBox2.Controls.Add(self._radioButton6)
		self._groupBox2.Controls.Add(self._radioButton5)
		self._groupBox2.Controls.Add(self._radioButton4)
		self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(258, 13)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(205, 118)
		self._groupBox2.TabIndex = 1
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Truck Assemblies"
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(6, 25)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(194, 24)
		self._radioButton1.TabIndex = 3
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "The Master Thrasher"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(7, 56)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(193, 24)
		self._radioButton2.TabIndex = 4
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "The Dictator of Grind"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(7, 86)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(193, 24)
		self._radioButton3.TabIndex = 5
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "The Street King"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton4
		# 
		self._radioButton4.Location = System.Drawing.Point(7, 23)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(104, 24)
		self._radioButton4.TabIndex = 0
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "7.5 axle"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# radioButton5
		# 
		self._radioButton5.Location = System.Drawing.Point(7, 55)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(104, 24)
		self._radioButton5.TabIndex = 1
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "8 axle"
		self._radioButton5.UseVisualStyleBackColor = True
		# 
		# radioButton6
		# 
		self._radioButton6.Location = System.Drawing.Point(7, 85)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(104, 24)
		self._radioButton6.TabIndex = 2
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "8.5 axle"
		self._radioButton6.UseVisualStyleBackColor = True
		# 
		# groupBox3
		# 
		self._groupBox3.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._groupBox3.Controls.Add(self._radioButton10)
		self._groupBox3.Controls.Add(self._radioButton9)
		self._groupBox3.Controls.Add(self._radioButton8)
		self._groupBox3.Controls.Add(self._radioButton7)
		self._groupBox3.Location = System.Drawing.Point(12, 156)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(207, 152)
		self._groupBox3.TabIndex = 2
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Wheel sets"
		# 
		# radioButton7
		# 
		self._radioButton7.Location = System.Drawing.Point(6, 26)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(194, 24)
		self._radioButton7.TabIndex = 0
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "51 mm"
		self._radioButton7.UseVisualStyleBackColor = True
		# 
		# radioButton8
		# 
		self._radioButton8.Location = System.Drawing.Point(7, 57)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(104, 24)
		self._radioButton8.TabIndex = 1
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "55 mm"
		self._radioButton8.UseVisualStyleBackColor = True
		# 
		# radioButton9
		# 
		self._radioButton9.Location = System.Drawing.Point(7, 88)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(104, 24)
		self._radioButton9.TabIndex = 2
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "58 mm"
		self._radioButton9.UseVisualStyleBackColor = True
		# 
		# radioButton10
		# 
		self._radioButton10.Location = System.Drawing.Point(7, 119)
		self._radioButton10.Name = "radioButton10"
		self._radioButton10.Size = System.Drawing.Size(104, 24)
		self._radioButton10.TabIndex = 3
		self._radioButton10.TabStop = True
		self._radioButton10.Text = "61 mm"
		self._radioButton10.UseVisualStyleBackColor = True
		# 
		# groupBox4
		# 
		self._groupBox4.BackColor = System.Drawing.SystemColors.ScrollBar
		self._groupBox4.Controls.Add(self._checkBox5)
		self._groupBox4.Controls.Add(self._checkBox4)
		self._groupBox4.Controls.Add(self._checkBox3)
		self._groupBox4.Controls.Add(self._checkBox2)
		self._groupBox4.Controls.Add(self._checkBox1)
		self._groupBox4.Location = System.Drawing.Point(258, 156)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(205, 179)
		self._groupBox4.TabIndex = 3
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Additional things"
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(7, 26)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(192, 24)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Grip tape"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(7, 57)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(192, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Bearings"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Location = System.Drawing.Point(7, 88)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(192, 24)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "Riser pads"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# checkBox4
		# 
		self._checkBox4.Location = System.Drawing.Point(7, 119)
		self._checkBox4.Name = "checkBox4"
		self._checkBox4.Size = System.Drawing.Size(192, 24)
		self._checkBox4.TabIndex = 3
		self._checkBox4.Text = "Nuts and bolts kit"
		self._checkBox4.UseVisualStyleBackColor = True
		# 
		# checkBox5
		# 
		self._checkBox5.Location = System.Drawing.Point(7, 150)
		self._checkBox5.Name = "checkBox5"
		self._checkBox5.Size = System.Drawing.Size(192, 24)
		self._checkBox5.TabIndex = 4
		self._checkBox5.Text = "Assembly"
		self._checkBox5.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(19, 359)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(116, 23)
		self._label1.TabIndex = 4
		self._label1.Text = "Your charge is: "
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(131, 359)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._button1.Location = System.Drawing.Point(32, 412)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(103, 28)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._button2.Location = System.Drawing.Point(183, 412)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(88, 28)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button3.Location = System.Drawing.Point(332, 412)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(83, 28)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(477, 457)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "Pg485SkateboardDesigner"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox4.ResumeLayout(False)
		self.ResumeLayout(False)


	

	def Button1Click(self, sender, e):
		self._label2.Text = ""
		charge = 0
		if self._radioButton1.Checked:
			charge += 60
		if self._radioButton2.Checked:
			charge += 45
		if self._radioButton3.Checked:
			charge += 50
		if self._radioButton4.Checked:
			charge += 35
		if self._radioButton5.Checked:
			charge += 40
		if self._radioButton6.Checked:
			charge += 45
		if self._radioButton7.Checked:
			charge += 20
		if self._radioButton8.Checked:
			charge += 22
		if self._radioButton9.Checked:
			charge += 24
		if self._radioButton10.Checked:
			charge += 26
		if self._checkBox1.Checked:
			charge += 10
		if self._checkBox2.Checked:
			charge += 30
		if self._checkBox3.Checked:
			charge += 2
		if self._checkBox4.Checked:
			charge += 3
		if self._checkBox5.Checked:
			charge += 10
		
		self._label2.Text = str(charge)
		
		

	def Button2Click(self, sender, e):
		self._label2.Text = ""
		
		
	def Button3Click(self, sender, e):
		Application.Exit()