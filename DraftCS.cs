using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace Kuddelmuddel_CSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Kuddelmuddel!");
            Console.WriteLine("Starting...");

            string[,] GermanEnglishArray = new string[3, 16];
            string[] helparray = new string[30];

            StreamReader reader = new StreamReader("words.txt");

            int i = 0;
            while (reader.EndOfStream == false)
            {
                string line = reader.ReadLine();
                helparray = line.Split(',');

                GermanEnglishArray[0, i] = helparray[0];
                GermanEnglishArray[1, i] = helparray[1];
                i++;
            }

            Console.WriteLine("Done!");



            Console.WriteLine("Press any key to exit...");
            Console.ReadKey();
        }
    }
}
