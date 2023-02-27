from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

usernames = "hyper", "hyper_test", "hyper_user"
menu_options = "ex", "save", "up", "m"

tests = {0: (f"{menu_options[0]}\ns\ns\n2", "7", "10"), 1: (f"{menu_options[0]}\ns\ns\ns\ns\n3", "27", "hyperskill"),
         2: (f"{menu_options[0]}\ns\n2\nex\n1", "11", "48")}  # test number: stdin, expected titanium after exploration(s) (in order), seed

class DuskersTest(StageTest):
    test = 0
    def generate(self):
        """We test the command line arguments, and if the seed is implemented.
        Please test this as the results could vary depending on the implementation, in which case the tests / stage instructions would hav to be changed."""
        return [TestCase(stdin=f"play\n{usernames[0]}\nyes\n{tests[0][0]}\nm\nexit",
                         args=[tests[0][2], "0", "0", "Old,power,plant/Abandoned,warehouse/Zombie,canteen"]),
                TestCase(stdin=f"play\n{usernames[1]}\nyes\n{tests[1][0]}\nm\nexit",
                         args=[tests[1][2], "0", "0", "Old,power,plant/Abandoned,warehouse/Zombie,canteen"]),
                TestCase(stdin=f"play\n{usernames[2]}\nyes\n{tests[2][0]}\nm\nexit",
                         args=["20", "0", "0", "Middle,of,nowhere/Ice,desert/Underground,city"])
                ]

    def check(self, reply, attach):
        if "\n" not in reply:
            return CheckResult.wrong("Output too short")
        user_output = reply.split("\n")
        text = "".join(user_output).lower()
        if len(user_output) < 10:
            return CheckResult.wrong("Output too short. Your title should take up exactly 8 lines (including blank space),\n"
                                     "then the main menu options should be displayed on separate lines")
        try:
            split_point = text.index("menu")
            end_point = text.index("save")
        except ValueError:
            return CheckResult.wrong("Some game options are missing from the output")
        text_part2 = text[split_point:end_point]
        if "titanium" not in text_part2:
            return CheckResult.wrong("Titanium amount not displayed inside the hub")
        if "0" not in text_part2:
            return CheckResult.wrong("Wrong titanium balance displayed")
        if self.test == 3:
            if tests[self.test][1] not in text and tests[self.test][2] not in text:
                return CheckResult.wrong("Something went wrong with the exploration.\n"
                                         "Make sure the titanium amount from exploration is based on the seed")
        else:
            if tests[self.test][1] not in text:
                return CheckResult.wrong("Something went wrong with the exploration.\n"
                                         "Make sure the titanium amount from exploration is based on the seed")
            split_point2 = text.index(tests[self.test][1])
            if tests[self.test][1] not in text[split_point2 + 2:]:
                return CheckResult.wrong("New titanium balance not displayed/updated")
        self.test += 1
        return CheckResult.correct()


if __name__ == '__main__':
    DuskersTest('duskers.duskers').run_tests()