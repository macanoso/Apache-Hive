import fileinput
import glob
import os
from os.path import dirname

module_path = dirname(__file__)
os.chdir(module_path)

expected = [
    "2014,a,1",
    "2014,b,1",
    "2014,d,2",
    "2014,e,1",
    "2015,a,3",
    "2015,b,1",
    "2015,c,3",
    "2015,d,2",
    "2015,e,2",
    "2016,a,2",
    "2016,b,1",
    "2016,c,3",
    "2016,d,3",
    "2016,e,3",
    "2017,a,1",
    "2017,b,1",
    "2017,c,1",
    "2017,e,1",
    "2018,a,1",
    "2018,d,1",
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
