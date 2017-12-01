using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode._2016
{
    public static class Day5
    {

        public static string GetCodeFromDoorKey(string input)
        {
            var code = "";
            var index = 0;

            //do this 8 times to get the code
            for (int i = 0; i < 8; i++)
            {
                var foundCodeDigit = false;
                while (!foundCodeDigit)
                {
                    var hash = CalculateMD5Hash(input + index);
                    index++;
                    if (hash.StartsWith("00000"))
                    {
                        code += hash.Substring(5, 1);
                        foundCodeDigit = true;
                    }
                }
            }
            return code.ToLower();
        }

        public static string GetCodeFromDoorKeyComplex(string input)
        {
            var code = new string[8];
            var index = 0;

            //do this 8 times to get the code
            for (int i = 0; i < 8; i++)
            {
                var foundCodeDigit = false;
                while (!foundCodeDigit)
                {
                    var hash = CalculateMD5Hash(input + index);
                    index++;
                    if (hash.StartsWith("00000"))
                    {
                        var positionStr = hash.Substring(5, 1);
                        var value = hash.Substring(6, 1);
                        if (int.TryParse(positionStr, out var position) && position <= 7 && code[position] == null)
                        {
                            code[position] = value;
                            foundCodeDigit = true;
                        }
                    }
                }
            }
            return string.Join("", code).ToLower();
        }




        private static string CalculateMD5Hash(string input)
        {

            // step 1, calculate MD5 hash from input

            MD5 md5 = System.Security.Cryptography.MD5.Create();

            byte[] inputBytes = System.Text.Encoding.ASCII.GetBytes(input);

            byte[] hash = md5.ComputeHash(inputBytes);

            // step 2, convert byte array to hex string

            StringBuilder sb = new StringBuilder();

            for (int i = 0; i < hash.Length; i++)

            {

                sb.Append(hash[i].ToString("X2"));

            }

            return sb.ToString();

        }
    }
}
