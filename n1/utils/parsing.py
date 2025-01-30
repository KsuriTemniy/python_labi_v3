from typing import Callable
import sympy as sp


def get_1d_function_from_input(text:str = "") -> Callable[[float], float]:
    x = sp.symbols('x')
    func_input = input(text)
    func = sp.lambdify(x, sp.sympify(func_input), 'math')
    return func