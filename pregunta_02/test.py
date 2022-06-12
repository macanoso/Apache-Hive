import fileinput
import glob
import os
from os.path import dirname

module_path = dirname(__file__)
os.chdir(module_path)

expected = [
    "A,1990-10-06,10",
    "A,1990-09-05,11",
    "A,1988-04-27,12",
    "A,1990-08-31,12",
    "A,1994-10-25,13",
    "A,1997-12-15,13",
    "A,1990-09-26,14",
    "A,1992-08-22,14",
    "A,1993-01-11,14",
    "A,1993-05-08,16",
    "A,1990-07-22,18",
    "A,1992-09-19,18",
    "B,1995-08-23,10",
    "B,1999-06-11,12",
    "B,1998-11-22,13",
    "B,1999-10-21,13",
    "B,1993-03-02,14",
    "B,1995-09-06,14",
    "B,1997-04-09,14",
    "B,1999-08-28,14",
    "B,1991-10-01,15",
    "B,1994-08-30,17",
    "C,1994-01-25,6",
    "C,1994-07-27,7",
    "C,1991-02-12,13",
    "C,1994-09-09,15",
    "D,1990-10-10,15",
    "E,1994-02-14,5",
    "E,1999-09-10,11",
    "E,1999-12-06,12",
    "E,1993-01-27,13",
    "E,1991-02-18,14",
    "E,1999-01-14,15",
    "E,1985-02-12,16",
    "E,1990-05-03,16",
    "E,1995-04-25,16",
    "E,1998-09-14,16",
    "E,1993-07-21,17",
    "E,1990-02-09,18",
    "E,1993-12-27,18",
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
