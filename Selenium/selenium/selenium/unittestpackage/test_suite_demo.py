import unittest
from unittestpackage.test_case_demo1 import TestCaseDemo1
from unittestpackage.test_case_demo2 import TestCaseDemo2
from unittestpackage.AssertDemo import AssertDemo
# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)
tc3 = unittest.TestLoader().loadTestsFromTestCase(AssertDemo)

# Create a test suite combining TestClass1 and TestClass2
smoke_test = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smoke_test)