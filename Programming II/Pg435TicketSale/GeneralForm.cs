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
    public partial class GeneralForm : Form
    {
        private Form myParent;

        public GeneralForm(Form prt)
        {
            InitializeComponent();
            myParent = prt;
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

        private void GeneralForm_FormClosing(object sender, FormClosingEventArgs e)
        {
            this.myParent.Show();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int tickets = int.Parse(textBox1.Text);
            double cost = 0;
            if (radioButton1.Checked) cost = 20;
            else if (radioButton2.Checked) cost = 15;
            else if (radioButton3.Checked) cost = 10;
            double ticCost = tickets * cost;
            double tax = ticCost + 0.06;
            double total = ticCost + tax;
            label5.Text = tickets.ToString();
            label6.Text = "0.06";
            label7.Text = total.ToString();
        }
    }
}
