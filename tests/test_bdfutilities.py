import os
import unittest
import subprocess
from parameterized import parameterized
from bdfutilities.bdf_utils import BDFUtils, readBDF

baseDir = os.path.dirname(os.path.abspath(__file__))
class TestExamples(unittest.TestCase):
    # Get all example scripts in the example folder and its subfolders
    exampleDir = os.path.abspath(os.path.join(baseDir, "../examples"))
    examples = []
    for root, _, files in os.walk(exampleDir):
        for file in files:
            # Note: if matching extension we cd into dir as each script assumes to be run in current folder
            if file.endswith(".sh"):
                cmd = f"cd {root} && bash {file}"
                examples.append([file, cmd])

            if file.endswith(".py"):
                cmd = f"cd {root} && python {file}"
                examples.append([file, cmd])

    # Generate a custom test function name for each script that will be run
    def generateFuncName(testcase_func, _, param):
        return "{}_{}".format(
            testcase_func.__name__,
            parameterized.to_safe_name(param.args[0]),
        )

    @parameterized.expand(examples, name_func=generateFuncName)
    def test_example(self, _, cmd):
        """
        Extract and run all examples from the examples folder.
        We assume that all have a .sh extension. Note that this test
        does not guarantee that they make sense, only that they run.
        """
        out = subprocess.run(cmd, shell=True)
        self.assertFalse(out.returncode)


if __name__ == "__main__":
    unittest.main()
