def isOctal(word):
    octals = ["1", "2", "3", "4", "5", "6", "7"]
    if word in octals:
        return True
    return False


def isSingleOperator(word):
    operators = ["=", "+", "-", "*", "/", "%", ">", "<", "and", "or", "not", "in",
                 "not in", "&", "|", "^","[","]"]
    if word in operators:
        return True
    return False


def isDoubleOperator(word):
    operators = ["**", "//", "==", "!=", ">=", "<=", "<<", ">>"]
    if word in operators:
        return True
    return False


def isKeyword(word):
    keywords = ["False", "None", "True", "as", "break", "class", "continue", "def", "elif", "else", "except", "for",
                "global", "if", "import", "is", "return", "while", "with"]
    if word in keywords:
        return True
    return False


if __name__ == "__main__":

    f = open("input.txt", "r")
    lines = f.readlines()
    use = ""
    # print(lines)
    for line in lines:
        # print(line,end="")
        i = 0
        while i < len(line):
            use = ""
            if line[i] == '(' or line[i] == ')' or line[i] == ',' or line[i] == ':':
                i = i + 1
            elif line[i] == ' ':
                print(line[i], end='')
                i += 1
            elif '\n' in line[i] or '\t' in line[i]:
                print(line[i], end='')
                i += 1
            elif line[i] == "#":
                while line[i] != "\n" and line[i] != '':
                    use = use + line[i]
                    i = i + 1
                i = i + 1
                # print(i)
                print("<comment line, " + use + ">")
            elif line[i].isalpha():
                use = use + line[i]
                i = i + 1
                while line[i].isalpha() or line[i].isdigit() or line[i] == '_':
                    use = use + line[i]
                    i = i + 1
                if isKeyword(use):
                    print("<keyword, " + use + ">", end='')
                elif isSingleOperator(use):
                    print("<operator, " + use + ">", end='')
                else:
                    print("<identifier, " + use + ">", end='')
            elif line[i] == '"' or line[i] == "'":
                use = use + line[i]
                i += 1
                if i+2 < len(line) and (line[i+1] == "'" and line[i+2] == "'") or (line[i+1] == '"' and line[i+2] == '"'):
                    use = use + line[i]
                    i += 1
                    use = use + line[i]
                    i += 1
                    if line[i-1] == "'":
                        while line[i] != "'":
                            use = use + line[i]
                            i += 1
                        use = use + line[i]
                        i += 1
                        use = use + line[i]
                        i += 1
                        use = use + line[i]
                        i += 1
                    else:
                        while line[i] != '"':
                            use = use + line[i]
                            i += 1
                        use = use + line[i]
                        i += 1
                        use = use + line[i]
                        i += 1
                        use = use + line[i]
                        i += 1
                else:
                    if line[i - 1] == "'":
                        while line[i] != "'":
                            use = use + line[i]
                            i += 1
                        use = use + line[i]
                        i += 1
                    else:
                        while line[i] != '"':
                            use = use + line[i]
                            i += 1
                        use = use + line[i]
                        i += 1
                    print("<stringConstant, " + use + ">", end='')
            elif line[i].isdigit() or (i + 1 < len(line) and line[i] == '-' and line[i].isdigit()):
                if not isOctal(line[i]):
                    print(f"<Error: {line[i]} is not octal>")
                    i += 1
                    continue
                use = use + line[i]
                i += 1
                isdobule = False
                while line[i].isdigit() or line[i] == ".":
                    if line[i] == '.':
                        isdobule = True
                    elif not isOctal(line[i]):
                        print(f"<Error: {line[i]} is not octal>")
                        i += 1
                        continue
                    use = use + line[i]
                    i += 1
                if isdobule:
                    print("<doubleConstant, " + use + ">", end='')
                else:
                    print("<intConstant, " + use + ">", end='')
            elif (i + 1) < len(line) and isDoubleOperator(line[i] + line[i + 1]):
                print("<operator, " + line[i] + line[i + 1] + ">", end='')
                i += 2
            elif isSingleOperator(line[i]):
                print("<operator, " + line[i] + ">", end='')
                i += 1
