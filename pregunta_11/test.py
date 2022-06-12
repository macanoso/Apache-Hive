import fileinput
import glob
import os
from os.path import dirname

module_path = dirname(__file__)
os.chdir(module_path)

expected = [
    "E,3,5",
    "A,3,4",
    "B,4,4",
    "A,2,4",
    "C,4,4",
    "A,2,5",
    "A,3,6",
    "B,2,3",
    "E,4,6",
    "B,4,6",
    "C,4,5",
    "C,4,3",
    "D,4,5",
    "E,2,3",
    "B,2,5",
    "D,2,4",
    "E,3,6",
    "D,2,3",
    "E,4,3",
    "E,2,3",
    "E,2,3",
    "E,3,3",
    "D,3,3",
    "A,3,5",
    "E,2,6",
    "E,3,6",
    "A,3,3",
    "E,3,5",
    "A,2,5",
    "C,4,6",
    "A,2,5",
    "D,2,6",
    "E,2,4",
    "B,3,6",
    "B,3,5",
    "D,2,3",
    "B,2,5",
    "C,4,3",
    "E,2,3",
    "E,3,3",
]

if os.path.isdir("output"):
    os.system("rm -rf output")

os.system("docker run -v $PWD:/workspace jdvelasq/hive:classroom")

assert os.path.isdir("output") is True

result = []
with fileinput.input(files=glob.glob("output/*")) as f:
    for line in f:
        line = line.replace("\n", "")
        result.append(line)

for expected_line, result_line in zip(expected, result):
    assert (
        expected_line == result_line
    ), f"Expected: {expected_line}\nGot: {result_line}"
