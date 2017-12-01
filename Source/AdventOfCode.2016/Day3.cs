using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._2016
{
    public static class Day3
    {
        public static int CountValidTriangles(string input)
        {
            var count = 0;
            var list = input.Split(new[] { Environment.NewLine }, StringSplitOptions.None);
            foreach (var item in list)
            {
                var parts = item.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                var side1 = int.Parse(parts[0]);
                var side2 = int.Parse(parts[1]);
                var side3 = int.Parse(parts[2]);

                if (side1 + side2 > side3 &&
                    side1 + side3 > side2 &&
                    side2 + side3 > side1)
                    count++;
            }
            return count;
        }
        public static int CountValidTrianglesVertical(string input)
        {
            var count = 0;
            var list = input.Split(new[] { Environment.NewLine }, StringSplitOptions.None);
            var rows = new List<(int Col1, int Col2, int Col3)>();
            foreach (var item in list)
            {
                var parts = item.Split(new[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);
                rows.Add((int.Parse(parts[0]), int.Parse(parts[1]), int.Parse(parts[2])));
            }
            //get all numbers as a full list
            var allNums = rows.Select(x => x.Col1).ToList();
            allNums.AddRange(rows.Select(x => x.Col2));
            allNums.AddRange(rows.Select(x => x.Col3));

            var trianlges = new List<(int Side1, int Side2, int Side3)>();
            //count valid triangles
            for (int i = 0; i < allNums.Count; i += 3)
            {
                trianlges.Add((allNums[i], allNums[i+1], allNums[i+2]));
                var side1 = allNums[i];
                var side2 = allNums[i + 1];
                var side3 = allNums[i + 2];

                if (side1 + side2 > side3 &&
                    side1 + side3 > side2 &&
                    side2 + side3 > side1)
                    count++;
            }
            return count;
        }
    }
}
