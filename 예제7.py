f = open('tset.txt', 'r')
body = f. read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()
