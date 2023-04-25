using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg347Sum
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
            int sum = 0;
            if (num <= 0)
            {
                label2.Text = "The number is invalid";
            } else {
                for (int i = 1; i <= num; i++) {
                    sum += i;
                }
                label2.Text = "The sum is " + sum.ToString();
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
