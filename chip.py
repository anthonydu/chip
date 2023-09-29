import sys


def interpret(file):
    content = open(file, "r").read()
    content = content.replace("（", "(")
    content = content.replace("）", ")")
    content = content.replace("“", '"')
    content = content.replace("”", '"')
    content = content.replace("八", "8")
    content = content.replace("九", "9")
    content = content.replace("加", "+")
    content = content.replace("寫出", "print")
    return content


if __name__ == "__main__":
    exec(interpret(sys.argv[1]))
