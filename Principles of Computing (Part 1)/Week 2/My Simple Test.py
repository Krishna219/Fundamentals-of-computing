"""
This program is a simple test suite used to test any function and 
gives result comparing the Computed and Expected output
"""

class TestSuite:
    """
    creating testsuite class that contains necessary testing features
    """
    def __init__(self):
        """
        initialises test suite with total_test = 0 failures = 0 and test_details = []
        """
        self.total_tests = 0
        self.failures = 0
        self.test_details = { 0 : "------------------------------\nTest Details\n------------------------------" } 
        
    def run_test(self, computed, expected, message = ""):
        """
        runs the test
        """
        self.total_tests += 1
        
        msg = "#Test " + str(self.total_tests) + " computed : " + str(computed)
        msg = msg + " expected : " + str(expected)
        
        if computed != expected:
            self.failures += 1
            message += " FAILURE"
            print msg
        else:
            message += " SUCCESS"
            
        self.test_details[self.total_tests] = msg + " " + message
        
    def report_results(self):
        """
        Gives the overall results Tests conducted and tests failed
        """
        msg = "Ran " + str(self.total_tests) + " tests. "
        msg += str(self.failures) + " failures."
        print msg
        
    def test_detail(self, test_num = 0):
        """
        Gives a detailed report about a test
        """
        
        print self.test_details[0]
        
        if test_num == 0:
            for test in range(self.total_tests):
                print self.test_details[test + 1]
        else:
            print self.test_details[test_num]
        
        