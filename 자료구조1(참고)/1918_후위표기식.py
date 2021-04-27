# n = input()

# stack = ['']
# result = ''

# for i in n:
#     if i == '(':
#         stack.append(i)
#     elif i == '+' or i == '-':
#         if stack[-1] == '+' or stack[-1] == '-':
#             result += stack.pop()
#             stack.append(i)
#         elif stack[-1] == '*' or stack[-1] == '/':
#             while len(stack) != 1:
#                 result += stack.pop()
#             stack.append(i)
#         else:
#             stack.append(i)
#     elif i == '*' or i == '/':
#         if stack[-1] == '+' or stack[-1] == '-' or stack[-1] == '(':
#             stack.append(i)
#         elif stack[-1] == '*' or stack[-1] == '/':
#             result += stack.pop()
#             stack.append(i)
#         else:
#             stack.append(i)
#     elif i == ')':
#         while stack[-1] != '(':
#             result += stack.pop()
#         stack.pop()
#     else:
#         result += i

# for i in stack:
#     result += stack.pop()

# print(result)

# ------------------시간 초과------------------

n = input()

stack = []
result = ''

for i in n:
    if i.isalpha():
        result += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                result += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()
while stack:
    result += stack.pop()
print(result)
