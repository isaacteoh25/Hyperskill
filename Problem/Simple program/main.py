import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--number", nargs='?', default=1)
# args = parser.parse_args()
#
# print(args.number)

parser = argparse.ArgumentParser(usage="This program prints a number you provide.")
parser.add_argument("-n", "--number", help="Print inputted number and exit")
parser.add_argument('--print_answer', action="store_true")
args = parser.parse_args()
print(args.number)
print(args.print_answer)

parser = argparse.ArgumentParser(usage="Print --number")
parser.add_argument('--number', default=True)
args = parser.parse_args()
if args.number:
    print(args.number)