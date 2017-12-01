using System;
using System.CodeDom;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._2016
{
    public static class Day4
    {
        public static int SumValidSectorIds(string input)
        {
            var sum = 0;
            var list = input.Split(new[] { Environment.NewLine }, StringSplitOptions.None);
            foreach (var item in list)
            {
                var parts = item.Split('-').ToList();
                var sectorIdAndChecksum = parts.Last();
                parts.Remove(sectorIdAndChecksum);
                var allLetters = string.Join("", parts);
                var dictionary = new Dictionary<char, int>();
                foreach (var letter in allLetters)
                {
                    if (!dictionary.ContainsKey(letter))
                        dictionary.Add(letter, 1);
                    else
                        dictionary[letter]++;
                }

                var val = string.Join("", dictionary.OrderByDescending(x => x.Value).ThenBy(x => x.Key).Take(5).Select(x => x.Key));

                var sectorIdParts = sectorIdAndChecksum.Split('[');
                var sectorId = int.Parse(sectorIdParts[0]);
                var checkSum = sectorIdParts[1].TrimEnd(']');

                if (val == checkSum)
                    sum += sectorId;
            }
            return sum;
        }


        public static int GetSectorIdOfNorthPoleStorageRoom(string input)
        {
            var realRooms = new List<string>();
            var list = input.Split(new[] { Environment.NewLine }, StringSplitOptions.None);
            foreach (var item in list)
            {
                var parts = item.Split('-').ToList();
                var sectorIdAndChecksum = parts.Last();
                parts.Remove(sectorIdAndChecksum);
                var allLetters = string.Join("", parts);
                var dictionary = new Dictionary<char, int>();
                foreach (var letter in allLetters)
                {
                    if (!dictionary.ContainsKey(letter))
                        dictionary.Add(letter, 1);
                    else
                        dictionary[letter]++;
                }

                var val = string.Join("", dictionary.OrderByDescending(x => x.Value).ThenBy(x => x.Key).Take(5).Select(x => x.Key));

                var sectorIdParts = sectorIdAndChecksum.Split('[');
                var sectorId = int.Parse(sectorIdParts[0]);
                var checkSum = sectorIdParts[1].TrimEnd(']');

                if (val == checkSum)
                    realRooms.Add(item);
            }

            foreach (var item in realRooms)
            {
                var parts = item.Split('-').ToList();
                var sectorIdAndChecksum = parts.Last();
                parts.Remove(sectorIdAndChecksum);
                var sectorIdParts = sectorIdAndChecksum.Split('[');
                var sectorId = int.Parse(sectorIdParts[0]);

                var name = "";
                foreach (var part in parts)
                {
                    var partDecrypted = "";
                    foreach (var c in part)
                    {
                        var index = char.ToUpper(c) - 64;
                        index += sectorId;
                        index = index % 26;
                        if (index == 0) index = 26; //handle Z
                        index += 64;
                        partDecrypted += (char)index;
                    }
                    name += partDecrypted + " ";
                }
                if (name.Trim() == "NORTHPOLE OBJECT STORAGE")
                    return sectorId;
            }
            return -1;
        }
    }
}
