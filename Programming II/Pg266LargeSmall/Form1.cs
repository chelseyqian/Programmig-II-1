using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg266LargeSmall
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num = 0;
            bool first = int.TryParse(textBox1.Text, out num);
            bool second = int.TryParse(textBox1.Text, out num);
            if (first && second)
            {
                int n1 = int.Parse(textBox1.Text);
                int n2 = int.Parse(textBox2.Text);
                if (n1 == n2)
                {
                    label3.Text = "n1 is equals to n2";
                } 
                else if (n1 > n2) 
                {
                    label3.Text = "n1 is greater than n2";
                }
                else
                {
                    label3.Text = "n1 is smaller than n2";
                }
            }
            else
            {
                label3.Text = "The numbers are invalid.";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
