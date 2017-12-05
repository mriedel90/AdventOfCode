using NUnit.Framework;

namespace AdventOfCode._2016.Tests
{
    [TestFixture]
    public class Day5Tests
    {
        [Test]
        //[TestCase("abc", "18f47a30")]
        //[TestCase("reyedfim", "f97c354d")]
        public void Day5_Part1(string input, string expectedResult)
        {
            // Arrange


            // Act
            var result = Day5.GetCodeFromDoorKey(input);

            // Assert
            Assert.AreEqual(expectedResult, result);
        }

        [Test]
        //[TestCase("abc", "05ace8e3")]
        //[TestCase("reyedfim", "863dde27")]
        public void Day5_Part2(string input, string expectedResult)
        {
            // Arrange


            // Act
            var result = Day5.GetCodeFromDoorKeyComplex(input);

            // Assert
            Assert.AreEqual(expectedResult, result);
        }
    }
}