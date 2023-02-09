from main import findMinimalSpanningSubnet
import unittest

class Test_UnitTests(unittest.TestCase):
    def testInvalidInput(self):
        assert findMinimalSpanningSubnet(["192.168.1.1", "invalid.ip.address.1", "192.168.0.1"]) == "Invalid input"
    def testEmptyInput(self):
        assert findMinimalSpanningSubnet([]) == "Invalid input"
    def testSameInput(self):
        assert findMinimalSpanningSubnet(["192.168.0.1", "192.168.0.1"]) == "192.168.0.1"
    def testSingleInput(self):
        assert findMinimalSpanningSubnet(["192.168.0.1"]) == "192.168.0.1"
    def testNoMatch(self):
        assert findMinimalSpanningSubnet(["192.168.0.1", "1.0.0.0"]) == "0.0.0.0"
    def testHalfMatch(self):
        assert findMinimalSpanningSubnet(["192.168.1.1", "192.168.0.1"]) == "192.168.0.0"
    def testEarlyMatch(self):
        assert findMinimalSpanningSubnet(["192.168.0.1", "192.168.1.0", "192.165.0.1"]) == "192.0.0.0"

if __name__ == '__main__':
    unittest.main()