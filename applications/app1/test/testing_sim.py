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
        if self._testing_simavr.process_stdout(stdout, "Assert"):
            print("First test passed")
            return 0
        self._error_counter += 1
        print("First test not passed")
        return self._error_counter


class TestingSimAvr:
    def process_stdout(self, stdout, key: str):
        error_counter = 0
        for line in stdout:
            if key in line.decode("utf-8"):
                value_1, value_2 = self._split_string(line.decode("utf-8"))
                if not self._assert_equal(value_1, value_2):
                    error_counter += 1
        return self.return_error_counter(error_counter)

    def _split_string(self, line):
        value_assert = []
        for i in line.split("||"):
            value_assert.append(i.split("=")[-1])
        return value_assert

    def _assert_equal(self, value_1: int, value_2: int):
        if int(value_1) == int(value_2):
            return True
        return False

    @staticmethod
    def return_error_counter(error_counter):
        if error_counter > 0:
            return False
        return True
