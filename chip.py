import sys
import logging
import re
import json
import cn2an
from io import StringIO
from contextlib import redirect_stdout


def interpret(file):
    content = open(file, "r").read()
    stringLiterals = re.findall("「(.*?)」", content)
    for s in stringLiterals:
        content.replace(s, "「」")
    for k, v in json.loads(open("dict.json", "r").read()).items():
        content = re.sub(k, v, content)
    content = cn2an.transform(content, "cn2an")
    for s in stringLiterals:
        content.replace("「」", f"「{s}」", 1)
    return content


if __name__ == "__main__":
    o = StringIO()
    with redirect_stdout(o):
        exec(interpret(sys.argv[1]))
    print(cn2an.transform(o.getvalue(), "an2cn"), end="")
