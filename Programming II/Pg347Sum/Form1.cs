using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;

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
            int num = int.Parse(Interaction.InputBox("Enter a number: "));
            if (num <= 0)
            {
                MessageBox.Show("The number is invalid");
            }
            else
            {
                int sum = 0;
                for (int i = 1; i <= num; i++) {
                    sum += i;
                }
                MessageBox.Show("The sum is " + sum);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        
    }
}
