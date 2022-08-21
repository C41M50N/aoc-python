
import pathlib
from sys import prefix
from typing import Literal
import typing
import click

YEARS   = Literal["2019", "2020", "2021"]

COMMON_PY = ("""
def transform_input (lines: list[str]) -> any:
    pass
""")

SOL_PY = ("""
from .common import transform_input

def run (lines: list[str]) -> int:
    pass
""")

def GET_TESTS_PY (file_path: str) -> str:
    return (
f"""
from solutions.p1_sol1 import run as sol_p1
from solutions.p2_sol1 import run as sol_p2

def test_p1_small ():
    lines = open('{prefix}/inputs/input_small.txt').readlines()
    assert sol_p1(lines) == 1

def test_p1 ():
    lines = open('{prefix}/inputs/input.txt').readlines()
    assert sol_p1(lines) == 1

def test_p2_small ():
    lines = open('{prefix}/inputs/input_small.txt').readlines()
    assert sol_p2(lines) == 1

def test_p2 ():
    lines = open('{prefix}/inputs/input.txt').readlines()
    assert sol_p2(lines) == 1
""" )


@click.command("create-scaffold")
@click.option('--year', '-y', type=click.Choice(typing.get_args(YEARS)), required=True)
@click.option('--day', '-d', type=int, required=True)
def main (year, day):

    if day not in range(1,26):
        print("Day must be from 1 to 25")
        return

    prefix = f"./year_{year}/day_{day:02}"

    files = {
        f"{prefix}/inputs/input.txt"        : "",
        f"{prefix}/inputs/input_small.txt"  : "",
        f"{prefix}/solutions/common.py"     : COMMON_PY,
        f"{prefix}/solutions/p1_sol1.py"    : SOL_PY,
        f"{prefix}/solutions/p2_sol1.py"    : SOL_PY,
        f"{prefix}/tests.py"                : GET_TESTS_PY(prefix),
    }

    for file_path, file_text in files.items():
        path = pathlib.Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(file_text)

if __name__ == '__main__':
    main()
