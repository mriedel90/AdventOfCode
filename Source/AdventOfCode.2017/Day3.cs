using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._2017
{
    public static class Day3
    {
        public static int CalculateManhattanDistance(int input)
        {
            return BuildSquare(input).Where(x => x.Val == input).Select(x => Math.Abs(x.X) + Math.Abs(x.Y)).First();
        }


        private static List<(int X, int Y, int Val)> BuildSquare(int maxDistance)
        {
            var result = new List<(int X, int Y, int Val)>();
            result.Add((0, 0, 1));
            var currentDirection = "R";

            for (int i = 2; i <= maxDistance; i++)
            {
                var previousX = result.Last().X;
                var maxX = result.Max(x => x.X);
                var minX = result.Min(x => x.X);
                var previousY = result.Last().Y;
                var maxY = result.Max(x => x.Y);
                var minY = result.Min(x => x.Y);
                var newX = previousX;
                var newY = previousY;
                if (currentDirection == "R" && previousX == maxX)
                {
                    newX++;
                    currentDirection = "U";
                }
                else if (currentDirection == "R")
                {
                    newX++;
                }
                else if (currentDirection == "U" && previousY == maxY)
                {
                    newY++;
                    currentDirection = "L";
                }
                else if (currentDirection == "U")
                {
                    newY++;
                }
                else if (currentDirection == "L" && previousX == minX)
                {
                    newX--;
                    currentDirection = "D";
                }
                else if (currentDirection == "L")
                {
                    newX--;
                }
                else if (currentDirection == "D" && previousY == minY)
                {
                    newY--;
                    currentDirection = "R";
                }
                else if (currentDirection == "D")
                {
                    newY--;
                }
                
                result.Add((newX, newY, i));
            }
            return result;
        }

        public static int CalculateFirstValLargerThanInput(int maxDistance)
        {
            var result = new List<(int X, int Y, int Val)>();
            result.Add((0, 0, 1));
            var currentDirection = "R";

            for (int i = 2; i <= maxDistance; i++)
            {
                var previousX = result.Last().X;
                var maxX = result.Max(x => x.X);
                var minX = result.Min(x => x.X);
                var previousY = result.Last().Y;
                var maxY = result.Max(x => x.Y);
                var minY = result.Min(x => x.Y);
                var newX = previousX;
                var newY = previousY;
                if (currentDirection == "R" && previousX == maxX)
                {
                    newX++;
                    currentDirection = "U";
                }
                else if (currentDirection == "R")
                {
                    newX++;
                }
                else if (currentDirection == "U" && previousY == maxY)
                {
                    newY++;
                    currentDirection = "L";
                }
                else if (currentDirection == "U")
                {
                    newY++;
                }
                else if (currentDirection == "L" && previousX == minX)
                {
                    newX--;
                    currentDirection = "D";
                }
                else if (currentDirection == "L")
                {
                    newX--;
                }
                else if (currentDirection == "D" && previousY == minY)
                {
                    newY--;
                    currentDirection = "R";
                }
                else if (currentDirection == "D")
                {
                    newY--;
                }

                //val is sum of all adjacent squares
                var val = 0;
                val += result.Where(x => x.X == newX + 1 && x.Y == newY).Select(x => x.Val).FirstOrDefault();
                val += result.Where(x => x.X == newX + 1 && x.Y == newY + 1).Select(x => x.Val).FirstOrDefault();
                val += result.Where(x => x.X == newX && x.Y == newY + 1).Select(x => x.Val).FirstOrDefault();
                val += result.Where(x => x.X == newX - 1 && x.Y == newY + 1).Select(x => x.Val).FirstOrDefault();
                val += result.Where(x => x.X == newX - 1 && x.Y == newY).Select(x => x.Val).FirstOrDefault();
                val += result.Where(x => x.X == newX - 1 && x.Y == newY - 1).Select(x => x.Val).FirstOrDefault();
                val += result.Where(x => x.X == newX && x.Y == newY - 1).Select(x => x.Val).FirstOrDefault();
                val += result.Where(x => x.X == newX + 1 && x.Y == newY - 1).Select(x => x.Val).FirstOrDefault();

                if (val > maxDistance)
                    return val;

                result.Add((newX, newY, val));
            }
            return -1;
        }

    }
}
