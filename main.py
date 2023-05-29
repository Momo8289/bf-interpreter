import time


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


def run(raw, state=None):
    # Clean input
    raw = "".join([c for c in raw if c in "<>,.[]+-"])
    if state is None:
        state = {}
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
            if not state.get(pointer):
                state[pointer] = 0
            state[pointer] = (state[pointer] + 1) % 256

        elif char == "-":
            if not state.get(pointer):
                state[pointer] = 0
            state[pointer] = (state[pointer] - 1) % 256
            if state[pointer] == 0:
                del state[pointer]

        elif char == ".":
            output.append(state.get(pointer) or 0)

        elif char == ",":
            i = input()
            if i == "":
                continue
            try:
                state[pointer] = int(ord(i))
            except TypeError:
                state[pointer] = int(i)
        elif char == "[":
            if (state.get(pointer) or 0) == 0:
                index = opened[index]

        elif char == "]":
            if (state.get(pointer) or 0) != 0:
                index = closed[index]

        index += 1

    return output, state


with open("program.bf", "r") as file:
    raw = file.read()

output, state = run(raw)
print("".join(chr(c) for c in output))
print(state)
