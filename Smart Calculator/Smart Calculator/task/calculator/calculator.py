# import sys
# import math
#
# usage_notes = """
# 1. Session prompts:
#     1. n: New session
#     2. c: Current session
#
# 2. Supported operators: +, -, *, /, ^, !
#
# 3. Precedence:
#     1. Parenthesization
#     2. Factorial
#     3. Exponentiation
#     4. Multiplication and Divison
#     5. Addition and Subtraction
#
# 4. Use of identifiers is supported. Use commas to separate them:
#     n: a=10,b=5
#     c: a+b
#     -> 15
#
# 5. Result of the previous expression can accessed by using the 'r'
# identifier:
#     n: 2+3
#     -> 5
#     c: r+10
#     -> 15
#
# 6. Special commands:
#     1. n: Stars a new session. Deletes all previous identifiers.
#     2. q: Quits the program
# """
#
# identifiers = {}
#
#
# def start():
#     # Creates a prompt dictionary to differentiate sessions.
#     # Starts the main loop of the program.
#     # Takes the input from the user and calls controller().
#
#     # prompts = {
#     #     'n': 'n: ',
#     #     'c': 'c: ',
#     # }
#
#     # prompt = prompts['n']
#     while True:
#         expr = input()
#         if expr.startswith('/'):
#             if expr == '/exit':
#                 print('Bye!')
#                 break
#             elif expr == '/help':
#                 print("A calculator class that implements basic calculator functions."
#                       "Calculator will also store variables in latin-character only strings.")
#                 continue
#             else:
#                 print("Unknown command")
#                 continue
#         elif expr == '':
#             continue
#         # if expr == 'n':
#         #     # prompt = prompts['n']
#         #     identifiers.clear()
#         else:
#             # res = controller(expr)
#             if '=' in expr:
#                 # expr_list = expr.replace(' ', '').split(',')
#                 # for stmt in expr_list:
#                 #     var, val = stmt.split('=')
#                 #     identifiers[var] = val
#                 # return 'i'
#                 # return create_identifiers(expr)
#                 variable, value = expr.replace(' ', '').split(sep='=', maxsplit=1)
#                 if has_number(variable):
#                     print('Invalid identifier')
#                     continue
#                 if value in identifiers:
#                     another_variable = value
#                     identifiers[variable] = identifiers[another_variable]
#                 else:
#                     try:
#                         identifiers[variable] = int(value)
#                     except ValueError:
#                         if has_number(value):
#                             print('Invalid assignment')
#                         else:
#                             print('Unknown variable')
#                     continue
#             elif ('+' in expr) or ('-' in expr) or ('*' in expr) \
#                     or ('/' in expr) or ('**' in expr) or ('^' in expr):
#                 try:
#                     postfix_expr = get_postfix(expr)
#                     print(postfix_eval(postfix_expr))
#                 except:
#                     print('Invalid expression')
#                 continue
#             # else:
#             #     variable = expr.replace(' ', '')
#             #
#             #     if has_number(variable):
#             #         print('Invalid identifier')
#             #         continue
#             #
#             #     elif variable in identifiers:
#             #         print(identifiers[variable])
#             #
#             #     else:
#             #         print('Unknown variable')
#             #         continue
#             # return postfix_eval(postfix_expr)
#             # if res == 'e':
#             #
#             #     print('Invalid expression')
#             # elif res == 'i':
#             #     pass
#                 # prompt = prompts['c']
#             # else:
#             #     print( identifiers['r'])
#                 # prompt = prompts['c']
#
# def controller(expr):
#     # Calls create_identifiers or passes the expr to get_postfix()
#     # to be converted into a postfix expression list. And, calls
#     # postfix_eval() for evaluation. All the Exceptions
#     # are terminated, so the main loop keeps running.
#
#     # try:
#     global postfix_expr
#     if '=' in expr:
#         # expr_list = expr.replace(' ', '').split(',')
#         # for stmt in expr_list:
#         #     var, val = stmt.split('=')
#         #     identifiers[var] = val
#         # return 'i'
#         # return create_identifiers(expr)
#         variable, value = expr.replace(' ', '').split(sep='=', maxsplit=1)
#         if has_number(variable):
#            print('Invalid identifier')
#            # continue
#         if value in identifiers:
#             another_variable = value
#             identifiers[variable] = identifiers[another_variable]
#         else:
#             try:
#                 identifiers[variable] = int(value)
#             except ValueError:
#                 if has_number(value):
#                     print('Invalid assignment')
#                 else:
#                     print('Unknown variable')
#             # continue
#     elif ('+' in expr) or ('-' in expr) or ('*' in expr)\
#             or ('/' in expr) or ('**' in expr) or ('^' in expr):
#          postfix_expr = get_postfix(expr)
#     return postfix_eval(postfix_expr)
#     # except Exception:
#     #     return 'e'
#
# def has_number(string):
#     return any(char.isdigit() for char in string)
#
# def create_identifiers(expr):
#     # Identifiers are implemented as a global dictionary. First,
#     # the string is split using ',' as a delimiter. The resulting
#     # substring are separated using '='. First substring is assigned
#     # as a key with second substring as the value.
#
#     expr_list = expr.replace(' ', '').split(',')
#
#     for stmt in expr_list:
#         var, val = stmt.split('=')
#         identifiers[var] = val
#     return 'i'
#
# def get_postfix(expr):
#     # Converts infix expressions to postfix expressions to remove ambiguity.
#     # Example: a+b*c -> abc*+
#
#     # Remove all the spaces in the given expression.
#     expr = expr.replace(' ', '')
#     sep_str = ''
#
#     # Insert spaces only around supported operators, so splitting
#     # can be done easily later.
#     for a_char in expr:
#         if a_char in '+-*/^!()':
#             sep_str += ' %s ' % a_char
#         else:
#             sep_str += a_char
#
#     # Use the default space as the delimiter and split the string.
#     token_list = sep_str.split()
#
#     # Only operators are pushed on to the op_stack, digits and identifiers
#     # are appended to the postfix_list.
#     op_stack = []
#     postfix_list = []
#
#     prec = {}
#     prec['!'] = 5
#     prec['^'] = 4
#     prec['/'] = 3
#     prec['*'] = 3
#     prec['+'] = 2
#     prec['-'] = 2
#     prec['('] = 1
#
#     # The current operator's precedence in the loop is compared with the
#     # operators in the stack. If it's higher, it's pushed on the stack.
#
#     # If it less than or equal, the operators are popped until the
#     # precedence of the operator at the top is less than the
#     # current operators'.
#
#     # When parentheses are used, ')' forces all the operators above '('
#     # to be popped.
#
#     # Whenever an operator is popped it's appended to the postfix_list.
#     for token in token_list:
#         if isnum(token) or token.isalpha():
#             postfix_list.append(token)
#         elif token == '(':
#             op_stack.append(token)
#         elif token == ')':
#             top_token = op_stack.pop()
#             while top_token != '(':
#                 postfix_list.append(top_token)
#                 top_token = op_stack.pop()
#         else:
#             while op_stack != [] and \
#                     (prec[op_stack[-1]] >= prec[token]):
#                 postfix_list.append(op_stack.pop())
#             op_stack.append(token)
#
#     while op_stack != []:
#         postfix_list.append(op_stack.pop())
#
#     return postfix_list
#
# def postfix_eval(postfix_list):
#     # Similar stack based approach is used here for evaluation. If a
#     # identifier or digit is found, push it on the operand_stack. If
#     # an operator is found, use it on the last two operands or the last
#     # in case of '!', and append the result on the stack.
#
#     operand_stack = []
#
#     for val in postfix_list:
#         if isnum(val):
#             operand_stack.append(float(val))
#         elif val.isalpha():
#             val = identifiers[val]
#             operand_stack.append(float(val))
#         elif val in '+-*/^!':
#
#             if val != '!':
#                 op2 = operand_stack.pop()
#                 op1 = operand_stack.pop()
#                 res = calc(op1, val, op2)
#                 operand_stack.append(res)
#             else:
#                 op = operand_stack.pop()
#                 res = math.factorial(op)
#                 operand_stack.append(res)
#
#     res = operand_stack[-1]
#     int_res = int(res)
#     if int_res == res:
#         res = int_res
#     print(str(res))
#     # identifiers['r'] = str(res)
#
# def isnum(val):
#     # Used as a helper function to check if the argument is a number.
#     try:
#         float(val)
#         return True
#     except Exception:
#         return False
#
# def calc(op1, op, op2):
#     # Performs the operation on the operands and returns the result.
#     if op == '+':
#         return op1 + op2
#     elif op == '-':
#         return op1 - op2
#     elif op == '*':
#         return op1 * op2
#     elif op == '/':
#         return op1 / op2
#     elif op == '^':
#         return op1 ** op2
#
# if sys.argv[-1] == 'n':
#     print(usage_notes)
#
# start()


from collections import deque


class Calculator:
    def __init__(self):
        self.variables_dict = {}

    @staticmethod
    def addition(first, second):
        return first + second

    @staticmethod
    def subtraction(first, second):
        return first - second

    @staticmethod
    def multiplication(first, second):
        return first * second

    @staticmethod
    def division(first, second):
        return int(first / second)

    @staticmethod
    def power(first, second):
        return first ** second

    def add_variable(self, string):
        try:
            variable, value = string.split("=")
        except ValueError:
            print("Invalid assignment")
        else:
            variable = variable.strip()
            value = value.strip()
            if not variable.isalpha():
                print("Invalid identifier")
            elif not value.isdigit() and not value.isalpha():
                print("Invalid assignment")
            else:
                if value in self.variables_dict.keys():
                    self.variables_dict[variable] = self.variables_dict[value]
                elif value.isalpha():
                    print("Unknown variable")
                else:
                    self.variables_dict[variable] = value

    @staticmethod
    def parse_command(command):
        if command == "/help":
            print("The program calculates the sum of numbers")
            return 1
        if command == "/exit":
            print("Bye!")
            return 0
        print("Unknown command")
        return 1

    @staticmethod
    def clean_input(line):
        # remove all spaces
        clean_line = line.replace(' ', '')
        # check duplicates of */^ signs (using math rule)
        if any((rule in clean_line) for rule in ["**", "//", "^^", "+*", "-*", "+/", "-/",
                                                 "+^", "-^", "/*", "*/", "*^", "^*", "/^", "^/"]):
            print("Invalid expression")
            return False
        # unite all +- signs (using math rule)
        while any((rule in clean_line) for rule in ["--", "+-", "-+", "++"]):
            clean_line = clean_line.replace('--', '+')
            clean_line = clean_line.replace('++', '+')
            clean_line = clean_line.replace('-+', '-')
            clean_line = clean_line.replace('+-', '-')
        # add space before and after sign
        clean_line = clean_line.replace('+', ' + ').replace('-', ' - ')
        if clean_line.startswith(" - "):  # for "-" at start of line
            clean_line = "-" + clean_line[3:]
        clean_line = clean_line.replace('* + ', "*").replace('* - ', '*-')
        clean_line = clean_line.replace('/ + ', "/").replace('/ - ', '/-')
        clean_line = clean_line.replace('^ + ', "^").replace('^ - ', '^-')
        clean_line = clean_line.replace('*', ' * ').replace('/', ' / ').replace('^', ' ^ ')
        clean_line = clean_line.replace('(', ' ( ').replace(')', ' ) ')
        return clean_line

    @staticmethod
    def calculate_postfix_expression(tokens):
        numbers_stack = deque()
        for el in tokens:
            if el in ["+", "-", "*", "/", "^"]:
                b = numbers_stack.pop()  # second operand is popped first
                a = numbers_stack.pop()
                if el == "+":
                    numbers_stack.append(Calculator.addition(a, b))
                elif el == "-":
                    numbers_stack.append(Calculator.subtraction(a, b))
                elif el == "*":
                    numbers_stack.append(Calculator.multiplication(a, b))
                elif el == "/":
                    numbers_stack.append(Calculator.division(a, b))
                elif el == "^":
                    numbers_stack.append(Calculator.power(a, b))
            else:
                numbers_stack.append(el)
        return numbers_stack[0]

    @staticmethod
    def transform_to_postfix(tokens):
        output_stack = deque()
        operators_stack = deque()
        priority = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
        for el in tokens:
            if isinstance(el, int):
                output_stack.append(el)
            elif el in priority.keys():
                if (not operators_stack or operators_stack[-1] == "(") or (priority[el] > priority[operators_stack[-1]]):
                    operators_stack.append(el)
                else:
                    while operators_stack and operators_stack[-1] != "(" \
                            and priority[el] <= priority[operators_stack[-1]]:
                        output_stack.append(operators_stack.pop())
                    operators_stack.append(el)
            elif el == "(":
                operators_stack.append(el)
            elif el == ")":
                try:
                    while operators_stack[-1] != "(":
                        output_stack.append(operators_stack.pop())
                    operators_stack.pop()  # pop "("
                except IndexError:
                    print("Invalid expression")
                    return False
        while operators_stack:
            if operators_stack[-1] != "(":
                output_stack.append(operators_stack.pop())
            else:
                print("Invalid expression")
                return False
        return output_stack

    def parse_token(self, token):
        try:
            if token.isalpha():
                return int(self.variables_dict[token])
            if token.isdigit() or (token.startswith("-") and len(token) > 1):
                return int(token)
            return token
        except KeyError:
            print("Unknown variable")
            return False
        except ValueError:
            print("Invalid identifier")
            return False

    def parse_string(self, string):
        string = Calculator.clean_input(string)
        if not string:
            return False
        tokens = string.split()
        tokens = [self.parse_token(el) for el in tokens]
        if not all(tokens):
            return False
        tokens = Calculator.transform_to_postfix(tokens)
        if tokens:
            print(Calculator.calculate_postfix_expression(tokens))
    def run(self):
        while True:
            user_input = input()
            if user_input.startswith("/"):
                if not self.parse_command(user_input):
                    break
            elif user_input == "":
                continue
            elif "=" in user_input:
                self.add_variable(user_input)
            else:
                try:
                    self.parse_string(user_input)
                except (ValueError, IndexError):
                    print("Invalid expression")


calculator = Calculator()
calculator.run()


# def token_parsing(num_stack, op_stack, tokens):
#     for idx in range(len(tokens) - 1, -1, -1):
#         t = tokens[idx]
#
#         if set(t) == set('+'):
#             op_stack.append('+')
#
#         elif set(t) == set('-'):
#             if len(t) % 2 == 0:
#                 op_stack.append('+')
#             else:
#                 op_stack.append('-')
#
#         else:
#
#             try:
#                 num_stack.append(int(t))
#
#             except ValueError:
#
#                 if t in variable_value_dict:
#                     num_stack.append(variable_value_dict[t])
#
#                 else:
#                     print('Unknown variable')
#                 return False
#
#     return True
#
#
# def calculate_expression(num_stack, op_stack):
#     while op_stack:
#
#         a = num_stack.pop()
#         b = num_stack.pop()
#
#         op = op_stack.pop()
#         if op == '+':
#             result = a + b
#             num_stack.append(result)
#         elif op == '-':
#             result = a - b
#             num_stack.append(result)
#
#     return
#
#
# def has_number(string):
#     return any(char.isdigit() for char in string)
#
#
# # --------------------------------------------------------
#
# variable_value_dict = {}
#
#
# def test_bench():
#     while True:
#         cur_input = input()
#
#         if cur_input.startswith('/'):
#
#             if cur_input == '/exit':
#                 print('Bye!')
#                 break
#
#             elif cur_input == '/help':
#                 print('The program calculates the expression')
#                 continue
#
#             else:
#                 print('Unknown command')
#                 continue
#         elif cur_input == '':
#             continue
#         else:
#             if '=' in cur_input:
#                 variable, value = cur_input.replace(' ', '').split(sep='=', maxsplit=1)
#
#                 if has_number(variable):
#                     print('Invalid identifier')
#                     continue
#
#                 if value in variable_value_dict:
#                     another_variable = value
#                     variable_value_dict[variable] = variable_value_dict[another_variable]
#
#                 else:
#                     try:
#                         variable_value_dict[variable] = int(value)
#
#                     except ValueError:
#
#                         if has_number(value):
#                             print('Invalid assignment')
#                         else:
#                             print('Unknown variable')
#
#                         continue
#
#
#             elif ('+' in cur_input) or ('-' in cur_input):
#                 tokens = cur_input.split()
#
#                 # print( tokens )
#
#                 num_stack, op_stack = [], []
#
#                 valid = token_parsing(num_stack, op_stack, tokens)
#
#                 if len(op_stack) != (len(num_stack) - 1):
#                     # operator is too much or to less
#                     valid = False
#
#                 if not valid:
#                     print('Invalid expression')
#
#                 else:
#                     # print('num_stack {}'.format(num_stack))
#                     # print('op_stack {}'.format(op_stack))
#
#                     calculate_expression(num_stack, op_stack)
#
#                     final_answer = num_stack[-1]
#                     print(final_answer)
#
#             else:
#
#                 variable = cur_input.replace(' ', '')
#
#                 if has_number(variable):
#                     print('Invalid identifier')
#                     continue
#
#                 elif variable in variable_value_dict:
#                     print(variable_value_dict[variable])
#
#                 else:
#                     print('Unknown variable')
#                     continue
#
#
# if __name__ == '__main__':
#     test_bench()