files_to_read = ["1.txt", "2.txt", "3.txt"]
count_lines = {}
for currient_file in files_to_read:
    with open(currient_file, encoding="utf-8") as file:
        data = file.read()
        count_lines[currient_file] = data.count('\n') + 1

sorted_count_lines = sorted(count_lines.items(), key=lambda x:x[1])

for file in sorted_count_lines:
    with open("res.txt", "a", encoding="utf-8") as f:
        f.write(file[0])
        f.write('\n')
        f.write(str(file[1]))
        f.write('\n')
        with open(file[0], encoding="utf-8") as reading_file:
            text_to_write = reading_file.read()
        f.write(text_to_write)
        f.write('\n')
