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
		self._label4 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(174, 45)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(108, 20)
		self._textBox1.TabIndex = 13
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
		self._label3.Location = System.Drawing.Point(174, 125)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(137, 38)
		self._label3.TabIndex = 12
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 125)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(156, 38)
		self._label2.TabIndex = 11
		self._label2.Text = "Anagrams?"
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 34)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(156, 31)
		self._label1.TabIndex = 10
		self._label1.Text = "Enter word1:"
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button3.Location = System.Drawing.Point(200, 257)
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
		self._button2.Location = System.Drawing.Point(12, 257)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(94, 40)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.GradientActiveCaption
		self._button1.Location = System.Drawing.Point(106, 196)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(89, 44)
		self._button1.TabIndex = 7
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ActiveBorder
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 76)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(156, 30)
		self._label4.TabIndex = 14
		self._label4.Text = "Enter word2:"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(174, 86)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(108, 20)
		self._textBox2.TabIndex = 15
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(330, 424)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Strint2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = ""
		word = self._textBox1.Text
		anagram = self._textBox2.Text
		word = word.lower()
		anagram = anagram.lower()
		
		if len(word) != len(anagram):
			self._label3.Text = "False"
		else:
			for lcv in range(len(word)):
				c = word[lcv]
				index = anagram.index(c)
				
				if index != -1:
					anagram = anagram[0:index] + anagram[index+1:]
				else:
					self._label3.Text = "False"
		self._label3.Text = str(len(anagram) == 0)

	def Button3Click(self, sender, e):
		Application.Exit()
		
	
