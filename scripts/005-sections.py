import re

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
        
for line in open('005-sections.txt', 'r').readlines():
    line = line.strip()
    if len(line) < 1:
        continue
    if not is_integer(line[0:1]):
        filename = re.sub(r"[^A-Za-z0-9 ]", " ", line)
        filename = re.sub(r"\s\s+", " ", filename)
        filename = re.sub(r"\s", "-", filename)
        filename = filename + '.md'
        print('')
        print(filename)
        print('# ' + line)
    else:
        print('## ' + line)
    print('')