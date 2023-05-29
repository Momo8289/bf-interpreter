import sys
import json


# https://stackoverflow.com/questions/29991917/indices-of-matching-parentheses-in-python
def find_parens(s):
    toret = {}
    pstack = []

    for i, c in enumerate(s):
        if c == '[':
            pstack.append(i)
        elif c == ']':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret[pstack.pop()] = i

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret


raw = "+[-->-[>>+>-----<<]<--<---]>-.>>>+.>>..+++[.>]<<<<.+++.------.<<-.>>>>"
state = [0] * 3000
pointer = 0
index = 0
opened = find_parens(raw)
closed = {v: k for k, v in opened.items()}
output = []
while index < len(raw):
    char = raw[index]
    # print(index, char)
    if char == ">":
        pointer += 1

    elif char == "<":
        pointer -= 1

    elif char == "+":
        state[pointer] = (state[pointer] + 1) % 256

    elif char == "-":
        state[pointer] = (state[pointer] - 1) % 256

    elif char == ".":
        output.append(state[pointer])
        print(state[pointer])

    elif char == ",":
        state[pointer] = int(input())

    elif char == "[":
        if state[pointer] == 0:
            index = opened[index]

    elif char == "]":
        if state[pointer] != 0:
            index = closed[index]

    index += 1

print(output)
print([chr(c) for c in output])
