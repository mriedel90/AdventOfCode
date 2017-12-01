using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._2016
{
    public static class Day2
    {
        public static string CalculateBathroomCode(string[] input, bool complex)
        {
            var currentDigit = "5";
            var result = "";

            foreach (var step in input)
            {
                foreach (var s in step)
                {
                    currentDigit = complex ? GetNextDigitComplex(currentDigit, s.ToString()) :
                        GetNextDigit(currentDigit, s.ToString());
                }
                result += currentDigit;
            }
            return result;
        }

        private static string GetNextDigit(string currentDigit, string direction)
        {
            if (currentDigit == "1" && direction == "L")
                return "1";
            if (currentDigit == "1" && direction == "R")
                return "2";
            if (currentDigit == "1" && direction == "U")
                return "1";
            if (currentDigit == "1" && direction == "D")
                return "4";

            if (currentDigit == "2" && direction == "L")
                return "1";
            if (currentDigit == "2" && direction == "R")
                return "3";
            if (currentDigit == "2" && direction == "U")
                return "2";
            if (currentDigit == "2" && direction == "D")
                return "5";

            if (currentDigit == "3" && direction == "L")
                return "2";
            if (currentDigit == "3" && direction == "R")
                return "3";
            if (currentDigit == "3" && direction == "U")
                return "3";
            if (currentDigit == "3" && direction == "D")
                return "6";

            if (currentDigit == "4" && direction == "L")
                return "4";
            if (currentDigit == "4" && direction == "R")
                return "5";
            if (currentDigit == "4" && direction == "U")
                return "1";
            if (currentDigit == "4" && direction == "D")
                return "7";

            if (currentDigit == "5" && direction == "L")
                return "4";
            if (currentDigit == "5" && direction == "R")
                return "6";
            if (currentDigit == "5" && direction == "U")
                return "2";
            if (currentDigit == "5" && direction == "D")
                return "8";

            if (currentDigit == "6" && direction == "L")
                return "5";
            if (currentDigit == "6" && direction == "R")
                return "6";
            if (currentDigit == "6" && direction == "U")
                return "3";
            if (currentDigit == "6" && direction == "D")
                return "9";

            if (currentDigit == "7" && direction == "L")
                return "7";
            if (currentDigit == "7" && direction == "R")
                return "8";
            if (currentDigit == "7" && direction == "U")
                return "4";
            if (currentDigit == "7" && direction == "D")
                return "7";

            if (currentDigit == "8" && direction == "L")
                return "7";
            if (currentDigit == "8" && direction == "R")
                return "9";
            if (currentDigit == "8" && direction == "U")
                return "5";
            if (currentDigit == "8" && direction == "D")
                return "8";

            if (currentDigit == "9" && direction == "L")
                return "8";
            if (currentDigit == "9" && direction == "R")
                return "9";
            if (currentDigit == "9" && direction == "U")
                return "6";
            if (currentDigit == "9" && direction == "D")
                return "9";

            return currentDigit;
        }


        private static string GetNextDigitComplex(string currentDigit, string direction)
        {
            if (currentDigit == "1" && direction == "L")
                return "1";
            if (currentDigit == "1" && direction == "R")
                return "1";
            if (currentDigit == "1" && direction == "U")
                return "1";
            if (currentDigit == "1" && direction == "D")
                return "3";

            if (currentDigit == "2" && direction == "L")
                return "2";
            if (currentDigit == "2" && direction == "R")
                return "3";
            if (currentDigit == "2" && direction == "U")
                return "2";
            if (currentDigit == "2" && direction == "D")
                return "6";

            if (currentDigit == "3" && direction == "L")
                return "2";
            if (currentDigit == "3" && direction == "R")
                return "4";
            if (currentDigit == "3" && direction == "U")
                return "1";
            if (currentDigit == "3" && direction == "D")
                return "7";

            if (currentDigit == "4" && direction == "L")
                return "3";
            if (currentDigit == "4" && direction == "R")
                return "4";
            if (currentDigit == "4" && direction == "U")
                return "4";
            if (currentDigit == "4" && direction == "D")
                return "8";

            if (currentDigit == "5" && direction == "L")
                return "5";
            if (currentDigit == "5" && direction == "R")
                return "6";
            if (currentDigit == "5" && direction == "U")
                return "5";
            if (currentDigit == "5" && direction == "D")
                return "5";

            if (currentDigit == "6" && direction == "L")
                return "5";
            if (currentDigit == "6" && direction == "R")
                return "7";
            if (currentDigit == "6" && direction == "U")
                return "2";
            if (currentDigit == "6" && direction == "D")
                return "A";

            if (currentDigit == "7" && direction == "L")
                return "6";
            if (currentDigit == "7" && direction == "R")
                return "8";
            if (currentDigit == "7" && direction == "U")
                return "3";
            if (currentDigit == "7" && direction == "D")
                return "B";

            if (currentDigit == "8" && direction == "L")
                return "7";
            if (currentDigit == "8" && direction == "R")
                return "9";
            if (currentDigit == "8" && direction == "U")
                return "4";
            if (currentDigit == "8" && direction == "D")
                return "C";

            if (currentDigit == "9" && direction == "L")
                return "8";
            if (currentDigit == "9" && direction == "R")
                return "9";
            if (currentDigit == "9" && direction == "U")
                return "9";
            if (currentDigit == "9" && direction == "D")
                return "9";

            if (currentDigit == "A" && direction == "L")
                return "A";
            if (currentDigit == "A" && direction == "R")
                return "B";
            if (currentDigit == "A" && direction == "U")
                return "6";
            if (currentDigit == "A" && direction == "D")
                return "A";

            if (currentDigit == "B" && direction == "L")
                return "A";
            if (currentDigit == "B" && direction == "R")
                return "C";
            if (currentDigit == "B" && direction == "U")
                return "7";
            if (currentDigit == "B" && direction == "D")
                return "D";

            if (currentDigit == "C" && direction == "L")
                return "B";
            if (currentDigit == "C" && direction == "R")
                return "C";
            if (currentDigit == "C" && direction == "U")
                return "8";
            if (currentDigit == "C" && direction == "D")
                return "C";

            if (currentDigit == "D" && direction == "L")
                return "D";
            if (currentDigit == "D" && direction == "R")
                return "D";
            if (currentDigit == "D" && direction == "U")
                return "B";
            if (currentDigit == "D" && direction == "D")
                return "D";

            return currentDigit;
        }
    }
}
