import pytest
from typing import Any, List
from src.interpreter import Interpreter
from src.parser import Parser
from src.tokenizer import Scanner
from src.tokens import Token, TokenType
from src.ast.printer import ASTPrinter

def pytest_generate_tests(metafunc):
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = sorted(funcarglist[0])
    metafunc.parametrize(
        argnames, [[funcargs[name] for name in argnames] for funcargs in funcarglist]
    )


rolls: List[str] = [
    '6',
    'd6',
    '5d6',
    '(4+1)d6',
    '(d4)d6',
    '11/3',
    '3*d6',
    '-d7',
    'sum 5d6',
    'sgn (d7-3)',
    'sum 3d6+4',
]
interpret_results: List[List[Any]] = [
    [6],
    [3.5],
    [[3.5, 3.5, 3.5, 3.5, 3.5]],
    [[3.5, 3.5, 3.5, 3.5, 3.5]],
    [[3.5, 3.5]],
    [11 // 3],
    [3 * 3.5],
    [-4],
    [5 * 3.5],
    [1],
    [3 * 3.5 + 4],
]

parse_results: List[List[str]] = [
    ['6'],
    ['(d 6)'],
    ['(d 5 6)'],
    ['(d (group (+ 4 1)) 6)'],
    ['(d (group (d 4)) 6)'],
    ['(/ 11 3)'],
    ['(* 3 (d 6))'],
    ['(- (d 7))'],
    ['(sum (d 5 6))'],
    ['(sgn (group (- (d 7) 3)))'],
    ['(+ (sum (d 3 6)) 4)'],
]

tokenizer_results = [
    1, 2, 3, 7, 6, 3, 4, 3, 4, 7, 6
]

class TestRolls:
    params = {
        "test_answers": [{'result_list': l} for l in [interpret_results, parse_results, tokenizer_results]],
        "test_interpret": [{'roll': roll, 'result': result} for roll, result in zip(rolls, interpret_results)],
        "test_parse": [{'roll': roll, 'result': result} for roll, result in zip(rolls, parse_results)],
        "test_tokenizer": [{'roll': roll, 'result': result} for roll, result in zip(rolls, tokenizer_results)]
    }

    def test_answers(self, result_list: List[Any]):
        assert len(result_list) == len(rolls)


    def test_parse(self, roll: str, result: List[str]):
        scanner = Scanner(roll)
        parser = Parser(scanner.scan_tokens())
        expression = parser.parse()
        res = ASTPrinter().print(expression)
        assert res == result


    def test_interpret(self, roll: str, result: List[Any]):
        scanner = Scanner(roll)
        parser = Parser(scanner.scan_tokens())
        expression = parser.parse()
        res = Interpreter().interpret(expression, average=True)
        assert res == result
            
    def test_tokenizer(self, roll: str, result: int):
        scanner = Scanner(roll)
        res = scanner.scan_tokens()
        assert len(res) == result + 1