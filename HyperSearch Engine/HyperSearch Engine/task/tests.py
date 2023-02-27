from hstest.stage_test import *
from hstest.test_case import TestCase
from test.indexer import Indexer_Dict
from test.search import SearchEngine
import re
import os

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)

x = SearchEngine()
ind = Indexer_Dict()

dir1 = os.path.join("test", "files", "ex1")
dir2 = os.path.join("test", "files", "ex2")

query1 = "man"
query2 = "water"

params1 = [1, 1, 0]
params2 = [1, 2, 0]

input1 = f"{dir1}\n'{query1}',{','.join([str(elem) for elem in params1])}"
input2 = f"{dir2}\n'{query2}',{','.join([str(elem) for elem in params2])}"


class SearchTest(StageTest):
    def generate(self):
        return [TestCase(stdin=input1,
                         attach=x.get_modified_search(ind.get_index_dict(dir1),
                                                      query=query1, window_size=params1[0],
                                                      limit=params1[1], offset=params1[2])),
                TestCase(stdin=input2,
                         attach=x.get_modified_search(ind.get_index_dict(dir2),
                                                      query=query2, window_size=params2[0],
                                                      limit=params2[1], offset=params2[2]))]

    def check(self, reply: str, clue: Any) -> CheckResult:
        reply = reply.strip()
        reply = re.sub(r"['\"\[\]]", "", reply)

        for key, value in clue.items():
            key = os.path.split(key)[-1]
            if key not in reply:
                return CheckResult.wrong("Seems like one of the positions is missing.\n"
                                         f"Position {key} was not found in your output.")
            expected_line = f"{key}: {str(value)}"
            expected_line_modified = re.sub(r"['\"\[\]]", "", expected_line)
            if expected_line_modified not in reply:
                return CheckResult.wrong(f"Token positions \"{expected_line}\" were expected in the output,\n"
                                         f"but was not found.")
        return CheckResult.correct()


if __name__ == '__main__':
    SearchTest().run_tests()
