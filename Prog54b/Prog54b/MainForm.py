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
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label1.Location = System.Drawing.Point(22, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "number1"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(74, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(48, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._label2.Location = System.Drawing.Point(163, 16)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "number2"
		self._label2.Click += self.Label2Click
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(215, 16)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(48, 20)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Cyan
		self._label3.Location = System.Drawing.Point(22, 51)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "number3"
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(74, 51)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(48, 20)
		self._textBox3.TabIndex = 5
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Lime
		self._label4.Location = System.Drawing.Point(163, 51)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "number4"
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(215, 51)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(48, 20)
		self._textBox4.TabIndex = 7
		self._textBox4.TextChanged += self.TextBox4TextChanged
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.Highlight
		self._button1.ForeColor = System.Drawing.SystemColors.InactiveCaptionText
		self._button1.Location = System.Drawing.Point(92, 161)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(102, 37)
		self._button1.TabIndex = 8
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ScrollBar
		self._button2.Location = System.Drawing.Point(13, 204)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(99, 34)
		self._button2.TabIndex = 9
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.GrayText
		self._button3.Location = System.Drawing.Point(178, 204)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(94, 34)
		self._button3.TabIndex = 10
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.SandyBrown
		self._label5.Location = System.Drawing.Point(22, 91)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 11
		self._label5.Text = "sum"
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.SandyBrown
		self._label6.Location = System.Drawing.Point(163, 91)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 12
		self._label6.Text = "average"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		n1 = int(self._textBox1.Text)
		n2 = int(self._textBox2.Text)
		n3 = int(self._textBox3.Text)
		n4 = int(self._textBox4.Text)
		
		sum = n1 + n2 + n3 + n4
		ave = sum / 4
		
		self._label5.Text = "Sum: " + str(sum)
		self._label6.Text = "Average: " + str(ave)
		
	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label5.Text = "Sum: "
		self._label6.Text = "Average: "
		
	def Button3Click(self, sender, e):
		Application.Exit()

	

	def TextBox4TextChanged(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass