import os
import time


def clear_screen(delay: float):
    time.sleep(delay)
    os.system("clear")


def transform_1(string: str, reps: int) -> str:
    return ""


def transform_2(string: str, reps: int) -> str:
    return ""


def transform_3(string: str, reps: int) -> str:
    return ""


def transform_4(string: str, reps: int) -> str:
    return ""


def transform_chain(string: str, reps: int) -> None:
    string = transform_1(string, reps)
    string = transform_2(string, reps)
    string = transform_3(string, reps)
    string = transform_4(string, reps)


initial_string = ""
transform_chain(initial_string, 5)
