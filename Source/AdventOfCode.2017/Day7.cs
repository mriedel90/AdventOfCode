using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._2017
{
    public static class Day7
    {
        public static string FindBottomOfTower(string input)
        {
            var list = input.Split(new[] {Environment.NewLine}, StringSplitOptions.None);
            var dictionary = new Dictionary<string, List<string>>();

            foreach (var item in list)
            {
                var parts = item.Split('>');
                var name = parts[0].Split(' ')[0];
                var children = parts.Length == 2 ? parts[1].Split(',').Select(x => x.Trim()).ToList() : new List<string>();
                
                dictionary.Add(name, children);
            }

            foreach (var item in dictionary)
            {
                if (!dictionary.Any(x => x.Value.Any(y => y == item.Key)))
                    return item.Key;
            }
            return "";
        }

        public static int FindCorrectWeightOfOffDisk(string input)
        {
            var list = input.Split(new[] { Environment.NewLine }, StringSplitOptions.None);
            var dictionaryParentChild = new Dictionary<string, List<string>>();
            var dictionaryDiskWeight = new Dictionary<string, int>();

            foreach (var item in list)
            {
                var parts = item.Split('>');
                var name = parts[0].Split(' ')[0];
                var children = parts.Length == 2 ? parts[1].Split(',').Select(x => x.Trim()).ToList() : new List<string>();
                var weight = int.Parse(parts[0].Split('(')[1].Split(')')[0]);
                dictionaryParentChild.Add(name, children);
                dictionaryDiskWeight.Add(name, weight);
            }

            var dictionaryParentWeight = new Dictionary<string, int>();
            foreach (var item in dictionaryParentChild)
            {
                bool reachedTop = false;
                var allChildren = new List<string>();
                var children = item.Value;
                while (!reachedTop)
                {
                    foreach (var child in children)
                    {
                        allChildren.Add(child);
                    }
                    children = children.SelectMany(x => dictionaryParentChild[x]).ToList();
                    reachedTop = children.Count == 0;
                }
                var weight = allChildren.Sum(x => dictionaryDiskWeight[x]) + dictionaryDiskWeight[item.Key];
                dictionaryParentWeight.Add(item.Key, weight);
            }

            
            foreach (var item in dictionaryParentChild)
            {
                //find unbalanced
                var childrenWeights = new Dictionary<string, int>();
                foreach (var childName in item.Value)
                {
                    childrenWeights.Add(childName, dictionaryParentWeight[childName]);
                }
                var groupedChildrenByWeight = childrenWeights.GroupBy(x => x.Value);
                if (groupedChildrenByWeight.Count() > 1)
                {
                    //count should be 2 (2 different weights
                    //this is the unbalanced item
                    //find the unbalanced child
                    return findWeight(groupedChildrenByWeight, dictionaryParentChild, dictionaryParentWeight, dictionaryDiskWeight);
                    
                }
            }
            return 0;
        }

        private static int findWeight(IEnumerable<IGrouping<int, KeyValuePair<string, int>>> groupedChildrenByWeight, Dictionary<string, List<string>> dictionaryParentChild, Dictionary<string, int> dictionaryParentWeight, Dictionary<string, int> dictionaryDiskWeight)
        {

            var unbalanced = groupedChildrenByWeight.Where(x => x.Count() == 1);
            var unbalancedWeight = unbalanced.First().Key;
            var balanced = groupedChildrenByWeight.Where(x => x.Count() > 1);
            var balancedWeight = balanced.First().Key;

            var unbalancedName = unbalanced.First().First().Key;

            var unbalancedChildren = dictionaryParentChild[unbalancedName];

            var unabalancedChildrenWeights = new Dictionary<string, int>();
            foreach (var childName in unbalancedChildren)
            {
                unabalancedChildrenWeights.Add(childName, dictionaryParentWeight[childName]);
            }
            var unbalancedGroupedChildrenByWeight = unabalancedChildrenWeights.GroupBy(x => x.Value);

            if (unbalancedGroupedChildrenByWeight.Count() > 1)
            {
                //children are unbalanced! - need to do some recursive call or another loop
                var a = "STOP HERE!";

                return findWeight(unbalancedGroupedChildrenByWeight, dictionaryParentChild, dictionaryParentWeight, dictionaryDiskWeight);
            }

            var childWeights = unbalancedChildren.Sum(x => dictionaryParentWeight[x]);
            var unbalancedDiskWeight = dictionaryDiskWeight[unbalancedName];

            //this should be true
            var true1 = unbalancedDiskWeight + childWeights == unbalancedWeight;

            var weightDiff = unbalancedWeight - balancedWeight;
            var result = unbalancedDiskWeight - weightDiff;
            return result;

        }
    }
}
