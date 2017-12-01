using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._2017
{
    public static class Day1
    {
        public static int SolveCaptcha(string input, bool nextTo)
        {
            var captcha = 0;
            for (var i = 0; i < input.Length; i++)
            {
                var currentDigit = int.Parse(input[i].ToString());
                var nextIndex = 0;

                if (nextTo)
                {
                    nextIndex = i == input.Length - 1 ? 0 : i + 1;
                }
                else
                {
                    nextIndex = Convert.ToInt32(input.Length / 2) + i;
                    if (nextIndex >= input.Length)
                        nextIndex -= input.Length;
                }

                var nextDigit = int.Parse(input[nextIndex].ToString());


                if (currentDigit == nextDigit)
                    captcha += currentDigit;
            }

            return captcha;
        }
    }
}
