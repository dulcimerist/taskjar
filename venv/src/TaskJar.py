import csv

file = open('test.csv')
csv_reader = csv.reader(file, delimiter=',')
line_count = 0
next_line_control = 1
for row in csv_reader:
    if len(row) == 0:
        next_line_control = 1
        print()
        continue
    if next_line_control == 1:
        next_line_control = 0
        print(f'\t{float(row[0]) * 100} percent chance of drawing 2 of the previous level tasks')
        print(f'\t{float(row[1]) * 100} percent chance of drawing 1 next level task')
        print(f'\t{float(row[2]) * 100} percent chance of shuffling after the task is drawn')
        print()
    else:
        print(f'\t{row[2]} - {row[0]} of {row[1]} remaining')
    line_count += 1
print(f'Processed {line_count} lines.')