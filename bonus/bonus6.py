contents = ["dummy data 1", 'dummy data 2', 'dummy data 3']

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"../file/{filename}", 'w')
    file.write(content)