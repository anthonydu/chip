import sys
import re
import json
import chinese2digits as c2d


def interpret(file):
    content = open(file, "r").read()
    for k, v in json.loads(open("dict.json", "r").read()).items():
        content = re.sub(k, v, content)
    content = c2d.takeChineseNumberFromString(content)["replacedText"]
    return content


if __name__ == "__main__":
    exec(interpret(sys.argv[1]))
