import re

symbols = {'(': ')', '[': ']', '<': '>', '{': '}'}
standard = {'(': 1, '[': 2, '<': 0.5, '{': 1}
values = {'(': '* 1', '[': '* 2', '<': '/ 2', '{': '** 2'}
pat = {'(': r'\(-?\d+\.?\d+\)', '[': r'\[-?\d+\]', '<': r'<-?\d+>', '{': r'\{-?\d+\}'}


# ULTRA EVAL PARENTHESIS
def ultra_eval_parenthesis(s):
    # [<(2)([22])>](12)<(-55)[<3>]>{{()()}}
    # <x> - x / 2
    # [x] - x * 2
    # {x} - x ** 2
    # (x) - x
    # (x)(x) - x + x
    groups = []
    curr_symbol = s[0]
    group = curr_symbol
    opened = 1
    for i, el in enumerate(s[1:]):
        group += el
        if el == symbols[curr_symbol]:
            opened -= 1
            if not opened:
                groups.append(group)
                try:
                    curr_symbol = s[i + 2]
                except IndexError:
                    break
                opened = 0
                group = ''
        elif el == curr_symbol:
            opened += 1
    result = 0
    print(groups)
    for curr_group in groups:
        if curr_group in ['<>', '()', '[]', '{}']:
            result += standard[curr_group[0]]
        else:
            m = re.match(pat[curr_group[0]], curr_group)
            if m:
                result += float(eval(curr_group[1:-1] + values[curr_group[0]]))
            else:
                result += float(eval(str(ultra_eval_parenthesis(curr_group[1:-1])) + values[curr_group[0]]))
    return result


templates = ['<>[]{()()}()', '<<<[[[()()]]]>>>', '[<(2)([22])>](12)<(-55)[<3>]>{{()()}}', '<{(12)[12]}>[(30)[<>]{-4}]', '<[{<[{<[{<[{(912)(2)}]>}]>}]><[{<[{<[{(912)(2)}]>}]>}]><[{<[{<[{(912)(2)}]>}]>}]><[{<[{<[{(912)(2)}]>}]>}]>}]>']
while True:
    expression = input('>>> ')
    if expression == 'templates':
        for i in templates:
            print(i, '-', ultra_eval_parenthesis(i))
        continue
    try:
        print(ultra_eval_parenthesis(expression), '!!!')
    except (KeyError, IndexError):
        print('incorrect parenthesis')