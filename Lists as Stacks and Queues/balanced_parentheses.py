# {[()]}	YES
# {[(])}	NO

input_line = input()
opening_brackets =[]
open_br = '{[('
pairs = '(){}[]'
balance = True

for ch in input_line:
    if ch in open_br:
        opening_brackets.append(ch)
    elif not opening_brackets:
        balance = False
    else:
        last_opening_br = opening_brackets.pop()

        if f'{last_opening_br}{ch}' not in pairs:
            balance = False

if balance and not opening_brackets:
    print('YES')

else:
    print('NO')


