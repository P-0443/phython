import  textwrap
with open('file', 'r') as filedata:
 for line in filedata:
    # print(len(line))
     print(textwrap.wrap(line,45))