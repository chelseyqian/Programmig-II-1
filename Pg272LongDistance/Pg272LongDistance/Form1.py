
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent, msg):
		self.InitializeComponent()
		self.parent = parent
		self.msg = msg
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(27, 60)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(132, 31)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter time:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(165, 60)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 31)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(27, 144)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(259, 36)
		self._label2.TabIndex = 2
		self._label2.Text = "Charge:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(27, 289)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(86, 37)
		self._button1.TabIndex = 3
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.Location = System.Drawing.Point(196, 289)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(81, 37)
		self._button2.TabIndex = 4
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button3.Location = System.Drawing.Point(102, 235)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(111, 39)
		self._button3.TabIndex = 5
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(324, 394)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "Form1"
		self.Text = "Form1"
		self.Load += self.Form1Load
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._textBox1.Text = "" 

	def Button2Click(self, sender, e):
		Application.Exit()

	def Button3Click(self, sender, e):
		time = int(self._textBox1.Text)
		self._label2.Text = "Charge: " + str(time * 0.07)

	def Form1Load(self, sender, e):
		self._label1.Text = self.msg