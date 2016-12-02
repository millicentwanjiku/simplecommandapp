"""Simple calculator

Usage:
  app.py <operation> <number1> <number2>
  app.py (-h | --help)

Arguments
  number1 First Number
  number2 Second Number

Options:
  -h --help     Show this screen.

"""
from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__, version='Simple calculator')
    functions = {
        'add': lambda number1, number2: number1 + number2,
        'subtract': lambda number1, number2: number1 - number2,
        'multiply': lambda number1, number2: number1 * number2,
        'divide': lambda number1, number2: number1 / number2
    }

    print functions[args['<operation>']](int(args['<number1>']), int(args['<number2>']))