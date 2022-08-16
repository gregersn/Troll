"""Troll reserved keywords."""
from .tokens import TokenType

KEYWORDS = {
    'choose': TokenType.CHOOSE,
    'count': TokenType.COUNT,
    'different': TokenType.DIFFERENT,
    'drop': TokenType.DROP,
    'keep': TokenType.KEEP,
    'max': TokenType.MAX,
    'maximal': TokenType.MAXIMAL,
    'median': TokenType.MEDIAN,
    'min': TokenType.MIN,
    'minimal': TokenType.MINIMAL,
    'mod': TokenType.MODULO,
    'pick': TokenType.PICK,
    'sgn': TokenType.SIGN,
    'sum': TokenType.SUM,
    'if': TokenType.IF,
    'then': TokenType.THEN,
    'else': TokenType.ELSE,
    'foreach': TokenType.FOREACH,
    'in': TokenType.IN,
    'do': TokenType.DO,
    'repeat': TokenType.REPEAT,
    'until': TokenType.UNTIL,
    'while': TokenType.WHILE,
    'accumulate': TokenType.ACCUMULATE,
}
