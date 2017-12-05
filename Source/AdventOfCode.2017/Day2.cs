using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._2017
{
    public static class Day2
    {
        public static int CalculateChecksum(string input)
        {
            var result = 0;
            var list = input.Split(new[] {Environment.NewLine}, StringSplitOptions.None);
            foreach (var item in list)
            {
                var ints = item.Split(new[] {"\t"}, StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x))
                    .ToList();
                var difference = ints.Max() - ints.Min();
                result += difference;
            }
            return result;
        }


        public static int CalculateChecksum2(string input)
        {
            var result = 0;
            var list = input.Split(new[] { Environment.NewLine }, StringSplitOptions.None);
            foreach (var item in list)
            {
                var ints = item.Split(new[] { "\t" }, StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x))
                    .ToList();

                foreach (var i in ints)
                {
                    var copyOfInts = new int[ints.Count];
                    ints.CopyTo(copyOfInts);
                    var newList = copyOfInts.ToList();
                    newList.Remove(i);
                    foreach (var i1 in newList)
                    {
                        if (i % i1 == 0)
                            result += (i / i1);
                    }
                }
                
            }
            return result;
        }
    }
}
