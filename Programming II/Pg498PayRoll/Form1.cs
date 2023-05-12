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

namespace Pg498PayRoll
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        const decimal HOURLY_PAY_RATE = 6.0m;
        const int MAX_EMPLOYEES = 5;


        private void button1_Click(object sender, EventArgs e)
        {
            int[] hours = new int[MAX_EMPLOYEES];
            int lcv = 0;
            int empHours = 0;
            decimal empPay = 0.0m;

            for (lcv = 0; lcv < MAX_EMPLOYEES; lcv++)
            {
                while (int.TryParse
                (
                    Interaction.InputBox("Enter the hours worked by employee #" + 
                        (lcv + 1).ToString(), "Need hours worked"), 
                        out empHours) == false)
                    MessageBox.Show("Please enter an integer for hours worked");
                hours[lcv] = empHours;
            }

            listBox1.Items.Clear();
            for (lcv = 0; lcv < MAX_EMPLOYEES; lcv++)
            {
                empPay = hours[lcv] * HOURLY_PAY_RATE;
                listBox1.Items.Add("Employee " + (lcv + 1).ToString() + " earned " + empPay.ToString());
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
