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

namespace Pg514SalesData
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private bool GetSalesData(ref decimal[] decSales)
        {
            decimal[] decSalesData;
            int days = 0;
            int lcv;
            bool blnSuccess;
            string strDays = Interaction.InputBox("For how many days do you have sales?");
            days = int.Parse(strDays);
            decSalesData = new decimal[days];
            for (lcv = 0; lcv < days; lcv++)
            {
                bool blnValid = false;
                while (blnValid != true)
                {
                    blnValid = decimal.TryParse(Interaction.InputBox("Enter the sales " + "for day " + ((lcv + 1).ToString())), out decSalesData[lcv]);
                    if (blnValid != true)
                    {
                        MessageBox.Show("Please enter a valid number");
                    }
                }
            }
            decSales = decSalesData;
            blnSuccess = true;
            return blnSuccess;
        }

        private decimal getTotal(decimal[] decVales)
        {
            decimal total = 0;
            for (int i = 0; i < decVales.Length; i++)
            {
                total += decVales[i];
            }
            return total;
        }

        private decimal getAverage(decimal[] decVales)
        {
            return getTotal(decVales) / decVales.Length;
        }

        private decimal getHeight(decimal[] decVales)
        {
            decimal height = decVales[0];
            for (int i = 1; i < decVales.Length; i++)
            {
                if (decVales[i] > height) height = decVales[i];
            }
            return height;
        }

        private decimal getLowest(decimal[] decVales)
        {
            decimal low = decVales[0];
            for (int i = 1; i < decVales.Length; i++)
            {
                if (decVales[i] < low) low = decVales[i];
            }
            return low;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            decimal[] decSales = null;
            decimal total = 0;
            decimal ave = 0;
            decimal high = 0;
            decimal low = 0;

            if (GetSalesData(ref decSales))
            {
                total = getTotal(decSales);
                ave = getAverage(decSales);
                high = getHeight(decSales);
                low = getLowest(decSales);

                label5.Text = total.ToString();
                label6.Text = ave.ToString();
                label7.Text = high.ToString();
                label8.Text = low.ToString();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
