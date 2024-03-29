﻿
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form2(Form):
	def __init__(self, parent, msg):
		self.InitializeComponent()
		self.parent = parent
		self.msg = msg
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(118, 240)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(111, 39)
		self._button3.TabIndex = 11
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(212, 294)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(81, 37)
		self._button2.TabIndex = 10
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(43, 294)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(86, 37)
		self._button1.TabIndex = 9
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(43, 149)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(259, 36)
		self._label2.TabIndex = 8
		self._label2.Text = "Charge:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(181, 65)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 7
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(43, 65)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(132, 31)
		self._label1.TabIndex = 6
		self._label1.Text = "Enter time:"
		# 
		# Form2
		# 
		self.ClientSize = System.Drawing.Size(345, 397)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "Form2"
		self.Text = "Form2"
		self.Load += self.Form2Load
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		time = int(self._textBox1.Text)
		self._label2.Text = "Charge: " + str(time * 0.12)
		
	
	def Button1Click(self, sender, e):
		self._textBox1.Text = "" 

	def Button2Click(self, sender, e):
		Application.Exit()

	def Form2Load(self, sender, e):
		self._label1.Text = self.msg