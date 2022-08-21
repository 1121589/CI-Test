import sys


class DefineTests:
    def __init__(self):
        self._testing_simavr = TestingSimAvr()
        self._error_counter = 0

    def _verify_errors(self):
        return self._error_counter

    def run_tests(self, stdout):
        self._first_test(stdout)

        return self._verify_errors()

    def _first_test(self, stdout):
        if self._testing_simavr.process_stdout(stdout):
            print("First test passed")
            return 0
        self._error_counter += 1
        print("First test not passed")
        return self._error_counter


class TestingSimAvr:
    def __init__(self):
        pass

    def process_stdout(self, stdout):
        error_counter = 0
        for line in stdout:
            if "Assert" in line.decode("utf-8"):
                value_assert_list = self._split_string(line.decode("utf-8"))
                if not self._assert_equal(value_assert_list):
                    error_counter += 1
        if error_counter > 0:
            return False
        return True

    def _split_string(self, line):
        value_assert = []
        for i in line.split("||"):
            value_assert.append(i.split("=")[-1])
        return value_assert

    def _assert_equal(self, value_assert):
        if int(value_assert[0]) == int(value_assert[1]):
            return True
        return False
