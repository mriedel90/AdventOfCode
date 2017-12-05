using NUnit.Framework;

namespace AdventOfCode._2017.Tests
{
    [TestFixture]
    public class Day3Tests
    {
        [Test]
        //[TestCase(312051, 430)]
        [TestCase(1, 0)]
        [TestCase(12, 3)]
        [TestCase(23, 2)]
        [TestCase(1024, 31)]
        public void Day3_Part1(int input, int expectedResult)
        {
            // Arrange


            // Act
            var result = Day3.CalculateManhattanDistance(input);
            var spiralResult = Day3.calcDistspiral(input);

            // Assert
            Assert.AreEqual(expectedResult, result);
            Assert.AreEqual(expectedResult, spiralResult);
        }
    }
}