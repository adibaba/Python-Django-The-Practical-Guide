# Extracts section names from copy-pasted text from Udemy navigatoin HTML
for line in open('text.txt', 'r').readlines():
    if len(line.strip()) > 5:
        print (line.strip())