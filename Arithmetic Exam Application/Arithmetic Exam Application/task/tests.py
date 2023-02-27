from hstest.stage_test import *
from hstest.test_case import *
from hstest import *
CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)

operations = ["+", "-", "*"]
wrong_format_msg = 'The task should have the following format: "number operation number"\n' \
                   '(e.g. "4 + 2", without quotes).\n' \
                   'However, the following output was found: '
corr_as_incorr_msg = 'The correct answer was given to the equation.\n' \
                     'The app should print \'Right!\'. \n' \
                     'However, this word was not found in the output.'
incorr_as_corr_msg = 'An incorrect answer was given to the equation.\n' \
                     'The app should print \'Wrong!\'. \n' \
                     'However, this word was not found in the output.'


def calc(task):
    original_task = task
    task = task.strip()
    op = None
    for i in operations:
        if i in task:
            op = i
            break

    if op is None:
        return None
    try:
        task = task.split(op)
        f = int(task[0].strip())
        s = int(task[1].strip())
    except ValueError:
        return None
    except IndexError:
        raise WrongAnswer(f"The format of the task {original_task} does not follow the required format.\n"
                          f"Please, print two numbers and an operation sign between them.")

    if op == "+":
        ans = f + s
    elif op == "-":
        ans = f - s
    else:
        ans = f * s
    return ans


class ExamTest(StageTest):
    @dynamic_test
    def test_correct_answer(self):
        pr = TestedProgram()
        task = pr.start()
        if not any([i in task for i in operations]):
            raise WrongAnswer('The app\'s first output should contain the task. \n'
                              'Task should contain one of the operations: "+", "-" or "*".\n'
                              'The following output was found:' + task)

        correct_ans = calc(task)

        if correct_ans is None:
            raise WrongAnswer(wrong_format_msg + task)

        output = pr.execute(str(correct_ans)).lower().strip()

        return CheckResult("right" in output and "wrong" not in output, corr_as_incorr_msg + "\nTask: " + task + '\nTested answer: ' + str(correct_ans))


    @dynamic_test
    def test_incorrect_answer(self):
        pr = TestedProgram()
        task = pr.start()
        if not any(['+' in task, '-' in task, '*' in task]):
            raise WrongAnswer('The app\'s first output should contain the task. \n'
                              'Task should contain one of the operations: "+", "-" or "*".\n'
                              'The following output was found:' + task)

        incorrect_ans = calc(task)

        if incorrect_ans is None:
            raise WrongAnswer(wrong_format_msg + task)

        incorrect_ans += 3

        output = pr.execute(str(incorrect_ans)).lower().strip()

        return CheckResult("wrong" in output and "right" not in output, incorr_as_corr_msg + '\nThe task: ' + task +
                           '\nThe answer: ' + str(incorrect_ans))

    @dynamic_test
    def test_random_generation(self):
        pr = TestedProgram()
        task = pr.start()
        for i in range(10):
            pr1 = TestedProgram()
            task1 = pr1.start()
            if task != task1:
                return CheckResult.correct()
        return CheckResult.wrong("Your app should generate different (random) tasks.\n"
                                 "The same task was repeated twice in a row. Make sure you generate random tasks.\n"
                                 "If you are sure that your program works correctly, re-run the tests.")

    @dynamic_test
    def test_generation_operation(self):
        ops = []
        for i in range(30):
            pr = TestedProgram()
            task = pr.start().replace('\n', '')
            ops += [j for j in task.split(' ') if not (j.isdigit() or j.replace('-', '').isdigit())]
        if len(set(ops)) == 3 and all(i in ops for i in operations ):
             return CheckResult.correct()
        else:
            return CheckResult.wrong("The app should generate tasks with all 3 types of operations, \n"
                                     "and use no other operations. \n"
                                     "However, the following operations were found:\n" + str(set(ops)))

    @dynamic_test
    def test_generation_numbers(self):
        numbers = [str(i) for i in range(2, 10)]
        nums = []
        for i in range(500):
            pr = TestedProgram()
            task = pr.start()
            nums += [j for j in task.split(" ") if j.isdigit() or j.replace('-', '').isdigit()]
        if len(set(nums)) == len(numbers) and all(i in nums for i in numbers):
            return CheckResult.correct()
        else:
            return CheckResult.wrong('The app should use all numbers from 2 to 9\n'
                                     'and shouldn\'t use any other numbers.\n'
                                     'The following numbers were found:\n' + str(set(nums)) +
                                     '\nMake sure you use all numbers from 2 to 9. \n'
                                     'If you are sure that your program works correctly, re-run the tests.')




if __name__ == '__main__':
    ExamTest().run_tests()
