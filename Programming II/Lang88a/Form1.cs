using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lang88a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int n1 = int.Parse(textBox1.Text);
            int n2 = int.Parse(textBox2.Text);

            int sum = n1 + n2;
            int diff = n1 - n2;
            int product = n1 * n2;
            double ave = sum / 2.0;
            int distance = Math.Abs(n1 - n2);
            int max = 0;
            int min = 0;

            if (n1 > n2)
            {
                max = n1;
                min = n2;
            }
            else
            {
                max = n2;
                min = n1;
            }

            label9.Text = sum.ToString();
            label10.Text = diff.ToString();
            label11.Text = product.ToString();
            label12.Text = ave.ToString();
            label13.Text = distance.ToString();
            label14.Text = max.ToString();
            label16.Text = min.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label9.Text = "";
            label10.Text = "";
            label11.Text = "";
            label12.Text = "";
            label13.Text = "";
            label14.Text = "";
            label16.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
