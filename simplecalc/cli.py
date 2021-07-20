"""Console script for simplecalc."""
import argparse
import sys

import simplecalc


def main():
    """Console script for simplecalc."""
    parser = argparse.ArgumentParser(
        description="A basic CLI calculator", usage="simplecalc [command] ..."
    )
    subparsers = parser.add_subparsers(
        title="Commands",
        prog="simplecalc",
        metavar="",
    )

    # Fibonacci sub-command
    fibonacci = subparsers.add_parser("fibonacci", help="Find fibonacci of n")
    fibonacci.add_argument("n", type=int, help="An integer")
    fibonacci.set_defaults(func=simplecalc.fibonacci)

    # Factorial sub-command
    factorial = subparsers.add_parser("factorial", help="Find factorial of n")
    factorial.add_argument("n", type=int, help="An integer")
    factorial.set_defaults(func=simplecalc.factorial)

    # Prime Check sub-command
    prime = subparsers.add_parser("prime", help="Determine if this is a prime")
    prime.add_argument("n", type=int, help="An integer")
    prime.set_defaults(func=simplecalc.is_prime)

    # Add sub-command
    add = subparsers.add_parser("add", help="Add the integer(s)")
    add.add_argument("n", nargs="+", type=int, help="An integer or integers")
    add.set_defaults(func=simplecalc.add)

    # Subtract sub-command
    subtract = subparsers.add_parser("subtract", help="Subtract the integer(s)")
    subtract.add_argument("n", nargs="+", type=int, help="An integer or integers")
    subtract.set_defaults(func=simplecalc.subtract)

    # Multiply sub-command
    multiply = subparsers.add_parser("multiply", help="Multiply the integers")
    multiply.add_argument("n", nargs="+", type=int, help="An integer or integers")
    multiply.set_defaults(func=simplecalc.multiply)

    # Divide sub-command
    divide = subparsers.add_parser("divide", help="Divide the integers")
    divide.add_argument("n", nargs="+", type=int, help="An integer or integers")
    divide.set_defaults(func=simplecalc.divide)

    # Power sub-command
    power = subparsers.add_parser(
        "power",
        help="Find the first integer to the power of the second integer provided",
    )
    power.add_argument("x", type=int, help="Base integer")
    power.add_argument("y", type=int, help="Exponent integer")
    power.set_defaults(func=simplecalc.power)

    args = parser.parse_args()

    # print(args)
    print(args.func(args))

    return 0


if __name__ == "__main__":
    main()  # pragma: no cover
