using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._2017
{
    public static class Day4
    {
        public static int Foo(string input, bool anagram)
        {
            int result = 0;

            foreach (var passphrase in input.Split(new[] { Environment.NewLine }, StringSplitOptions.RemoveEmptyEntries))
            {
                var words = passphrase.Split(' ').ToList();
                if (words.GroupBy(x => x).Count() == words.Count)
                {
                    if (anagram)
                    {
                        var countOfAnagrams = 0;
                        foreach (var word in words)
                        {
                            var wordOrdered = string.Concat(word.OrderBy(x => x)).ToLower();
                            foreach (var word2 in words)
                            {
                                var word2Ordered = string.Concat(word2.OrderBy(x => x)).ToLower();
                                if (wordOrdered == word2Ordered)
                                    countOfAnagrams++;
                            }
                        }
                        if (countOfAnagrams <= words.Count)
                            result++;
                    }
                    else
                        result++;
                }
            }

            return result;
        }

        private static bool AreEqual(IOrderedEnumerable<IGrouping<char, char>> set1, IOrderedEnumerable<IGrouping<char, char>> set2)
        {
            if (set1.Count() != set2.Count())
                return false;

            foreach(var item in set1)
            {
            }
            return true;
        }
    }
}
