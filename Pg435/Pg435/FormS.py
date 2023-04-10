
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class FormS(Form):
	def __init__(self, parent):
		self.InitializeComponent()
		self.parent = parent
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 42)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(229, 49)
		self._label1.TabIndex = 0
		self._label1.Text = "Number of tickets:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(203, 48)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(26, 112)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(291, 40)
		self._label2.TabIndex = 2
		self._label2.Text = "Tickets: "
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(26, 175)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(291, 40)
		self._label3.TabIndex = 3
		self._label3.Text = "Tax: "
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(27, 237)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(290, 42)
		self._label4.TabIndex = 4
		self._label4.Text = "Total: "
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Silver
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 348)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 38)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.GradientInactiveCaption
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(126, 348)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(94, 38)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(242, 348)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 38)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# FormS
		# 
		self.ClientSize = System.Drawing.Size(339, 428)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "FormS"
		self.Text = "FormS"
		self.FormClosing += self.FormSFormClosing
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num = int(self._textBox1.Text)
		self._label2.Text = "Tickets: " + str(num)
		tax = int(float(num) * 7 * 0.06)
		self._label3.Text = "Tax: " + str(tax)
		total = num * 7 + tax
		self._label4.Text = "Total: " + str(total)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

	def FormSFormClosing(self, sender, e):
		self.parent.Show()