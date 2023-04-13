using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg273MassAndWeight
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int mass = int.Parse(textBox1.Text);
            double weight = mass * 9.8;
            if (weight > 1000)
            {
                label2.Text = "It's too heavy";
            }
            else if (weight < 10)
            {
                label2.Text = "It's too light";
            }
            else
            {
                label2.Text = "Its weight is " + weight;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label2.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
