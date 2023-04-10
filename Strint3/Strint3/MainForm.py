import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(168, 61)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(108, 20)
		self._textBox1.TabIndex = 13
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.Location = System.Drawing.Point(168, 122)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(137, 38)
		self._label3.TabIndex = 12
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 122)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(154, 38)
		self._label2.TabIndex = 11
		self._label2.Text = "First non-repeated:"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(44, 52)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(122, 31)
		self._label1.TabIndex = 10
		self._label1.Text = "Enter text:"
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button3.Location = System.Drawing.Point(209, 249)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(96, 40)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button2.Location = System.Drawing.Point(25, 249)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(94, 40)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button1.Location = System.Drawing.Point(124, 186)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(89, 44)
		self._button1.TabIndex = 7
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(330, 341)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "First non-repeated:"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()
		
	def Button1Click(self, sender, e):
		self._label3.Text = ""
		str = self._textBox1.Text
		letter = ""
		check = False
		while check == False:
			for x in str:
				if str.index(x) == str.rindex(x):
					letter = x
					check = True
					self._label3.Text = x
				