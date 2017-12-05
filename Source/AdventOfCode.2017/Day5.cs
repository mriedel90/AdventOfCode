using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._2017
{
    public static class Day5
    {
        public static int CalculateJumpsTilExit(string input, bool decreaseIfGreaterThan3)
        {
            var jumps = input.Split(new[] { Environment.NewLine }, StringSplitOptions.None)
                .Select(x => int.Parse(x)).ToArray();
            
            var numJumps = 0;
            var currentIndex = 0;

            while (currentIndex < jumps.Length)
            {
                numJumps++;
                var newIndex = currentIndex + jumps[currentIndex];
                if (decreaseIfGreaterThan3 && jumps[currentIndex] >= 3)
                    jumps[currentIndex]--;
                else
                    jumps[currentIndex]++;
                currentIndex = newIndex;
            }

            return numJumps;
        }
    }
}
