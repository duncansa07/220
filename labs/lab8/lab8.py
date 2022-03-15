"""
Name: Scarlett Duncan
lab8.py

Problem: Create a function that imports a file containing grades and calculates a students weighted average and class
average, printing it to a new file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    with open(in_file_name, "r") as in_file:
        with open(out_file_name, "w") as average_doc:
            student_numb = 0
            class_avg_add = 0
            for line_var in in_file:
                line_split = line_var.split(":")
                student_name = line_split[0]
                student_grades_weights = line_split[1]
                student_grades_weights = student_grades_weights.replace("\n", "")
                student_grades_weights = student_grades_weights.lstrip()
                student_grade_new = student_grades_weights.split()

                weighted_avg_add = 0
                weight_added = 0
                for i in range(0, len(student_grade_new), 2):
                    weight = student_grade_new[i]
                    weight_added = weight_added + eval(weight)
                if weight_added > 100:
                    output_line = student_name + "'s average: Error: The weights are more than 100\n"
                    average_doc.write(output_line)
                elif weight_added < 100:
                    output_line = student_name + "'s average: Error: The weights are less than 100\n"
                    average_doc.write(output_line)
                else:
                    student_numb = student_numb + 1
                    for i in range(0, len(student_grade_new), 2):
                        weight = student_grade_new[i]
                        grade = student_grade_new[i+1]
                        term_n = eval(weight) * eval(grade)
                        weighted_avg_add = weighted_avg_add + term_n

                    class_avg_add = class_avg_add + weighted_avg_add
                    weighted_avg = weighted_avg_add/100
                    weighted_avg = round(weighted_avg, 1)
                    weighted_average_string = str(weighted_avg)
                    output_line = student_name + "'s average: " + weighted_average_string + "\n"
                    average_doc.write(output_line)

            class_avg = (class_avg_add / student_numb) / 100
            class_avg = round(class_avg, 1)
            class_avg = str(class_avg)
            class_avg_line = "Class Average: " + class_avg
            average_doc.write(class_avg_line)


if __name__ == '__main__':
    weighted_average('grades.txt', 'avg.txt')