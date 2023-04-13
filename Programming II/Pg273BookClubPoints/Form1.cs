﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg273BookClubPoints
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num = int.Parse(textBox1.Text);
            int points;
            if (num == 0)
            {
                points = 0;
            }
            else if (num == 1)
            {
                points = 5;
            }
            else if (num == 2)
            {
                points = 15;
            }
            else if (num == 3)
            {
                points = 30;
            }
            else
            {
                points = 60;
            }
            label3.Text = points.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label3.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
