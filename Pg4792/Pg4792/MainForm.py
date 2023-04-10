import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox8 = System.Windows.Forms.TextBox()
		self._textBox7 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._label8 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label6 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# textBox8
		# 
		self._textBox8.Location = System.Drawing.Point(301, 120)
		self._textBox8.Name = "textBox8"
		self._textBox8.Size = System.Drawing.Size(100, 26)
		self._textBox8.TabIndex = 15
		# 
		# textBox7
		# 
		self._textBox7.Location = System.Drawing.Point(301, 88)
		self._textBox7.Name = "textBox7"
		self._textBox7.Size = System.Drawing.Size(100, 26)
		self._textBox7.TabIndex = 14
		# 
		# textBox6
		# 
		self._textBox6.Location = System.Drawing.Point(301, 54)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(100, 26)
		self._textBox6.TabIndex = 13
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(45, 215)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(215, 48)
		self._button1.TabIndex = 7
		self._button1.Text = "Select conference optoins"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(301, 22)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(100, 26)
		self._textBox5.TabIndex = 12
		# 
		# label8
		# 
		self._label8.Location = System.Drawing.Point(233, 123)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(62, 23)
		self._label8.TabIndex = 11
		self._label8.Text = "Zip"
		# 
		# label7
		# 
		self._label7.Location = System.Drawing.Point(233, 91)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(62, 23)
		self._label7.TabIndex = 10
		self._label7.Text = "State"
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(184, 293)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(132, 40)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.Silver
		self._groupBox1.Controls.Add(self._textBox8)
		self._groupBox1.Controls.Add(self._textBox7)
		self._groupBox1.Controls.Add(self._textBox6)
		self._groupBox1.Controls.Add(self._textBox5)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._textBox4)
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(38, 16)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(426, 161)
		self._groupBox1.TabIndex = 6
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Registration"
		# 
		# label6
		# 
		self._label6.Location = System.Drawing.Point(233, 58)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(62, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "Email"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(233, 25)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(62, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "Phone"
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(94, 120)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 26)
		self._textBox4.TabIndex = 7
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(94, 88)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 26)
		self._textBox3.TabIndex = 6
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(94, 55)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 26)
		self._textBox2.TabIndex = 5
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(94, 23)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 26)
		self._textBox1.TabIndex = 4
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(7, 123)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(81, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "City"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(7, 88)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(81, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Address"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(7, 58)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(81, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Company"
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(7, 26)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(81, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Name"
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(305, 215)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(114, 48)
		self._button2.TabIndex = 8
		self._button2.Text = "Reset"
		self._button2.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(502, 349)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._button2)
		self.Name = "MainForm"
		self.Text = "Pg4792"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)

	

	def Button1Click(self, sender, e):
		from Form1 import *
		form1 = Form1(self)
		form1.Show()
		self.Hide()

	def Button3Click(self, sender, e):
		Application.Exit()