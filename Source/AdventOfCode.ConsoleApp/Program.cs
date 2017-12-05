using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AdventOfCode._2017;
//sing AdventOfCode._2016;
namespace AdventOfCode.ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine($"Result is: {result}");

            //var result = Day3.CalculateFirstValLargerThanInput(312051);

            

            var input2 = @"abcde xyz ecdab
abcde fghij";

            var result = Day5.CalculateJumpsTilExit(input2);


            Console.WriteLine(result);
            Console.ReadLine();
        }
    }
}
