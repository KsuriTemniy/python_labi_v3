from utils import get_1d_function_from_input

from typing import Callable
import logging

import math

def func_c(x: float, y: float, f: Callable[[float], float] = (lambda x:x**2)) -> float | None:
    if x - y == 0:
        return f(x) ** 2 + y ** 2 + math.sin(y)
    elif x - y > 0:
        return (f(x) - y) ** 2 + math.cos(y)
    else:
        if y == math.pi / 2:
            logging.warning("Тангенс не определен в точке pi/2")
            return None
        return (y - f(x)) ** 2 + math.tan(y)

def main():
    x = int(input("Введите x: "))
    y = int(input("Введите y: "))
    f = get_1d_function_from_input("Введите f(x): ")

    res = func_c(x,y,f)

    print(round(res,2))

if __name__=="__main__":
    main()