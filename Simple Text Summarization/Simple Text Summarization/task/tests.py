from typing import List
from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from test import content, answers


class TextSumTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(time_limit=-1, files={'news.xml': content})]

    def check(self, reply, attach):
        incorrect = [answer.strip() in reply for answer in answers].count(False)
        if incorrect:
            return CheckResult.wrong(
                '{} out of {} news texts were summarized incorrectly. Try again!'.format(incorrect, len(answers)))
        return CheckResult.correct()


if __name__ == '__main__':
    TextSumTest('textsum.textsum').run_tests()
