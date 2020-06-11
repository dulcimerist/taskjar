import csv

file = open('example_files/test.csv')
csv_reader = csv.reader(file, delimiter=',')
line_count = 0
next_line_control = True
for row in csv_reader:
    if len(row) == 0:
        next_line_control = True
        print()
        continue
    if next_line_control:
        next_line_control = False
        print(f'\t{float(row[0]) * 100} percent chance of drawing 2 of the previous level tasks')
        print(f'\t{float(row[1]) * 100} percent chance of drawing 1 next level task')
        print(f'\t{float(row[2]) * 100} percent chance of shuffling after the task is drawn')
        print()
    else:
        print(f'\t{row[2]} - {row[0]} of {row[1]} remaining')
    line_count += 1
print(f'Processed {line_count} lines.')