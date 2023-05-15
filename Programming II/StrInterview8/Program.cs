using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StrInterview8
{
    class Program
    {
        static void Main(string[] args)
        {
            int count = 0;
            Console.Write("Enter a string: ");
            string str = Console.ReadLine();
            Console.Write("Enter a character in the string: ");
            char c = char.Parse(Console.ReadLine());

            for (int i = 0; i < str.Length; i++)
            {
                if (str[i] == c)
                {
                    count++;
                }
            }

            Console.WriteLine("The number of occurence is " + count);
            Console.ReadLine();
        }
    }
}
