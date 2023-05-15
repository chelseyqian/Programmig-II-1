using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrInterview18
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter a string: ");
            string str = Console.ReadLine();
            Console.Write("Enter a character to remove: ");
            char c = char.Parse(Console.ReadLine());
            string result = "";

            for (int i = 0; i < str.Length; i++)
            {
                if (str[i] != c)
                {
                    result += str[i];
                }
            }

            Console.WriteLine("The string is " + result);
            Console.ReadLine();
        }
    }
}
