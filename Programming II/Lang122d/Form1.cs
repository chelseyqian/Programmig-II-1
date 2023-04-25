using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lang122d
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("x\t\ty");
            for (int i = -12; i <= 16; i++)
            {
                double y = Math.Pow(i, 6) - 3 * Math.Pow(i, 5) - 93 * Math.Pow(i, 4) 
                    + 87 * Math.Pow(i, 3) + 1596 * Math.Pow(i, 2) - 1380 * i - 2800;
                listBox1.Items.Add(i + "\t\t" + (int)y);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
