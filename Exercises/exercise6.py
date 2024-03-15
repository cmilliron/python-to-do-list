filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"files/{filename}", 'w')
    file.write("Hello")
    file.write("MFer")
    file.close()


file = open('logs.txt', 'w')
file.write('101.102.103.222 GET 01.988')
file.write('171.131.104.108 POST 2.143')
file.close()