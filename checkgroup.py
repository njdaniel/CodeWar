def group_check(s):
    """Make sure a string is enclosed correctly
            eg.
            Good:
                ({})
                [[]()]
                [{()}]
            Bad:
                {(})
                ([]
                [])
    """
    parenthesis = ['(',')']
    brackets = ['[', ']']
    squirely = ['{', '}']
    parenthesis_num0 = 0
    brackets_num0 = 0
    squirely_num0 = 0
    parenthesis_num1 = 0
    brackets_num1 = 0
    squirely_num1 = 0
    expect = []
    for i in enumerate(s):
        if i == parenthesis[0]:
            parenthesis_num0+=1
            expect.append(parenthesis_num1)
        elif i == brackets[0]:
            brackets_num0+=1
            expect.append(brackets_num1)
        elif i == squirely[0]:
            squirely_num0+=1
            expect.append(squirely_num1)
        elif i == parenthesis[1]:
            parenthesis_num1+=1
            if parenthesis_num1>parenthesis_num0:
                return False
            if i == expect[:-1]:
                expect.pop(len(expect)-1)
            else:
                return False
        elif i == brackets[1]:
            brackets_num1+=1
            if brackets_num1>brackets_num0:
                return False
            if i == expect[:-1]:
                expect.pop(len(expect)-1)
            else:
                return False
        elif i == squirely[1]:
            squirely_num1+=1
            if squirely_num1>squirely_num0:
                return False
            if i == expect[:-1]:
                expect.pop(len(expect)-1)
            else:
                return False
    if parenthesis_num0 == parenthesis_num1 and brackets_num0 == brackets_num1 and squirely_num0 == squirely_num1:
        return True
    else:
        return False

# a = "{(})"
# b =  "([]"
# c = "[])"
# print(group_check(a))
# print(group_check(b))
# print(group_check(c))

def check_group(s):
    stack = []
    parenthesis = ['(', ')']
    brackets = ['[', ']']
    squirely = ['{', '}']
    for i in s:
        if i == parenthesis[0]:
            stack.append(i)
        elif i == parenthesis[1]:
            try:
                if stack[-1] == parenthesis[0]:
                    stack.pop(len(stack)-1)
                else:
                    return False
            except:
                return False

        elif i == brackets[0]:
            stack.append(i)
        elif i == brackets[1]:
            try:
                if stack[-1] == brackets[0]:
                    stack.pop(len(stack)-1)
                else:
                    return False
            except:
                return False

        if i == squirely[0]:
            stack.append(i)
        elif i == squirely[1]:
            try:
                if stack[-1] == squirely[0]:
                    stack.pop(len(stack)-1)
                else:
                    return False
            except:
                return False

    if stack == []:
        return True
    else:
        return False
a = "({})"
b =  "[[]()]"
c = "[{()}]"
print(check_group(a))
print(check_group(b))
print(check_group(c))




# Best solution
BRACES = { '(': ')', '[': ']', '{': '}' }

def group_check_best(s):
    stack = []
    for b in s:
        c = BRACES.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack