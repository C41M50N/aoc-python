
from solutions.p1_sol1 import run as sol_p1
from solutions.p2_sol1 import run as sol_p2

def test_p1_small ():
    lines = open('./year_2020/day01/inputs/input_small.txt').readlines()
    assert sol_p1(lines) == 514579

def test_p1 ():
    lines = open('./year_2020/day01/inputs/input.txt').readlines()
    assert sol_p1(lines) == 437931

def test_p2_small ():
    lines = open('./year_2020/day01/inputs/input_small.txt').readlines()
    assert sol_p2(lines) == 241861950

def test_p2 ():
    lines = open('./year_2020/day01/inputs/input.txt').readlines()
    assert sol_p2(lines) == 157667328
