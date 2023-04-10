using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Lang54cConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter radius: ");
            double r = double.Parse(Console.ReadLine());

            double area = 3.14159 * r * r;
            double cir = 2 * 3.14159 * r;

            Console.WriteLine("Area: " + area);
            Console.WriteLine("Circumference: " + cir);
            Console.ReadKey();
        }
    }
}
