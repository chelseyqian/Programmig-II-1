using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pg435TicketSale
{
    public partial class StudentForm : Form
    {
        private Form myParent;

        public StudentForm(Form prt)
        {
            InitializeComponent();
            this.myParent = prt;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }

        decimal decTAXRATE = 0.06m; // Sales Tax Rate
        private decimal CalcTax(decimal cost)
        {
            // Returns the sales tax on ticket sales
            return cost * decTAXRATE;
        }

        private void StudentForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            this.myParent.Show();
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            int tickets = int.Parse(textBox1.Text);
            double ticCost = tickets * 7;
            double tax = ticCost * 0.06;
            double total = ticCost + tax;
            label5.Text = tickets.ToString();
            label6.Text = "0.06";
            label7.Text = total.ToString();
        }
    }
}
