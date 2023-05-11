using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg334LoanCalculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void groupBox3_Enter(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            int months = int.Parse(textBox3.Text);
            double loan = double.Parse(textBox1.Text) - double.Parse(textBox2.Text);
            double rate = 0.089;
            double interest = 0;
            double principal = 0;

            double payment = 0.089 / 12 * months * loan;

            for (int count = 1; count <= months; count++)
            {
                interest = 0.089 / 12 * count;
                principal = loan * count;
            }

            listBox1.Items.Add("Month: " + months);
            listBox1.Items.Add("\nPayment: " + payment);
            listBox1.Items.Add("\nInterest: " + interest);
            listBox1.Items.Add("\nPrincipal: " + principal);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }
    }
}
