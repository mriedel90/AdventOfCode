using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._2016
{
    public static class Day1
    {
        public static int CalculateBlocks(string input, bool firstLocationVisitedTwice)
        {
            var blocksN = 0;
            var blocksE = 0;
            var locations = new List<(int blocksN, int blocksE)>() { (0, 0) };


            var currentDirection = "N";
            foreach (var step in input.Split(','))
            {
                var direction = step.Trim().Substring(0, 1);
                var blocks = int.Parse(step.Trim().Substring(1, step.Trim().Length - 1));

                if (currentDirection == "N")
                {
                    if (direction == "L")
                    {
                        currentDirection = "W";
                        for (int i = 1; i <= blocks; i++)
                        {
                            blocksE -= 1;
                            if (firstLocationVisitedTwice && locations.Any(x => x.blocksN == blocksN && x.blocksE == blocksE))
                                return Math.Abs(blocksE) + Math.Abs(blocksN);
                            locations.Add((blocksN, blocksE));
                        }
                    }
                    else if (direction == "R")
                    {
                        currentDirection = "E";
                        for (int i = 1; i <= blocks; i++)
                        {
                            blocksE += 1;
                            if (firstLocationVisitedTwice && locations.Any(x => x.blocksN == blocksN && x.blocksE == blocksE))
                                return Math.Abs(blocksE) + Math.Abs(blocksN);
                            locations.Add((blocksN, blocksE));
                        }
                    }
                }
                else if (currentDirection == "E")
                {
                    if (direction == "L")
                    {
                        currentDirection = "N";
                        for (int i = 1; i <= blocks; i++)
                        {
                            blocksN += 1;
                            if (firstLocationVisitedTwice && locations.Any(x => x.blocksN == blocksN && x.blocksE == blocksE))
                                return Math.Abs(blocksE) + Math.Abs(blocksN);
                            locations.Add((blocksN, blocksE));
                        }
                    }
                    else if (direction == "R")
                    {
                        currentDirection = "S";
                        for (int i = 1; i <= blocks; i++)
                        {
                            blocksN -= 1;
                            if (firstLocationVisitedTwice && locations.Any(x => x.blocksN == blocksN && x.blocksE == blocksE))
                                return Math.Abs(blocksE) + Math.Abs(blocksN);
                            locations.Add((blocksN, blocksE));
                        }
                    }
                }
                else if (currentDirection == "S")
                {
                    if (direction == "L")
                    {
                        currentDirection = "E";
                        for (int i = 1; i <= blocks; i++)
                        {
                            blocksE += 1;
                            if (firstLocationVisitedTwice && locations.Any(x => x.blocksN == blocksN && x.blocksE == blocksE))
                                return Math.Abs(blocksE) + Math.Abs(blocksN);
                            locations.Add((blocksN, blocksE));
                        }
                    }
                    else if (direction == "R")
                    {
                        currentDirection = "W";
                        for (int i = 1; i <= blocks; i++)
                        {
                            blocksE -= 1;
                            if (firstLocationVisitedTwice && locations.Any(x => x.blocksN == blocksN && x.blocksE == blocksE))
                                return Math.Abs(blocksE) + Math.Abs(blocksN);
                            locations.Add((blocksN, blocksE));
                        }
                    }
                }
                else if (currentDirection == "W")
                {
                    if (direction == "L")
                    {
                        currentDirection = "S";
                        for (int i = 1; i <= blocks; i++)
                        {
                            blocksN -= 1;
                            if (firstLocationVisitedTwice && locations.Any(x => x.blocksN == blocksN && x.blocksE == blocksE))
                                return Math.Abs(blocksE) + Math.Abs(blocksN);
                            locations.Add((blocksN, blocksE));
                        }
                    }
                    else if (direction == "R")
                    {
                        currentDirection = "N";
                        for (int i = 1; i <= blocks; i++)
                        {
                            blocksN += 1;
                            if (firstLocationVisitedTwice && locations.Any(x => x.blocksN == blocksN && x.blocksE == blocksE))
                                return Math.Abs(blocksE) + Math.Abs(blocksN);
                            locations.Add((blocksN, blocksE));
                        }
                    }
                }

            }
            return Math.Abs(blocksE) + Math.Abs(blocksN);
        }

    }
}
