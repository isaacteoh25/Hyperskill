# get this year free seats
max_number_of_student = int(input())

# open and read file with applicants, save them into list
with open('applicant_list_7.txt', 'r') as f:
    applicants = []
    for line in f:
        applicants.append(line.rstrip().split(' '))

# the sorted list of departments
departments = sorted(['Mathematics', 'Physics', 'Biotech', 'Chemistry', 'Engineering'])

# dict for people who are on the boat
successful_applicants = {key: [] for key in departments}


def find_mean_or_specexam_result(organization, applicant):
    particular_exam = {'Mathematics': ['Math'], 'Physics': ['Physics', 'Math'],
                       'Biotech': ['Chemistry', 'Physics'],
                       'Chemistry': ['Chemistry'], 'Engineering': ['Computer science', 'Math']}
    exam_results = {'Physics': 2, 'Chemistry': 3, 'Math': 4, 'Computer science': 5}

    result = 0
    number_of_exams = 0
    for exam in particular_exam[organization]:
        result += float(applicant[exam_results[exam]])
        number_of_exams += 1
    return [max(result / number_of_exams, float(applicant[6])), result / number_of_exams]


# applying mechanism
for priority in range(7, 10):
    for department in departments:
        next_wave = []
        sorted_list = sorted(applicants, key=lambda x: (-float(find_mean_or_specexam_result(department, x)[0]),
                                                        x[0], x[7], x[8], x[9], x[1]))
        for student in sorted_list:
            if student[priority] == department and len(successful_applicants[department]) < max_number_of_student:
                successful_applicants[student[priority]].append(student)
            else:
                next_wave.append(student)
        applicants = next_wave

# Stage 5/7 printing mechanism
for depart in successful_applicants.keys():
    print(depart)
    depart_file = open(depart.lower() + '.txt', 'a', encoding='utf-8')
    sorted_department = sorted(successful_applicants[depart],
                               key=lambda x: (-float(find_mean_or_specexam_result(depart, x)[0]), x[0], x[1]))
    for student in sorted_department:
        name = student[0]
        surname = student[1]
        score = find_mean_or_specexam_result(depart, student)[0]
        print(name, surname, score)
        depart_file.write(' '.join([name, surname, str(score)]) + '\n')
    depart_file.close()

# Stage 5/7
# # printing mechanism
# for depart in successful_applicants.keys():
#     print(depart)
#     sorted_department = sorted(successful_applicants[depart], key=lambda x: (-float(x[particular_exam[depart]]), x[0], x[1]))
#     for student in sorted_department:
#         name = student[0]
#         surname = student[1]
#         score = student[particular_exam[depart]]
#         print(name, surname, score)

# Stage 4/7

# # sort list
# sorted_list = sorted(applicants, key=lambda x: (-float(x[2]), x[0], x[3], x[4], x[5], x[1]))
#
#
# # applying mechanism
# for priority in range(3, 6):
#     next_wave = []
#     for student in sorted_list:
#         if len(successful_applicants[student[priority]]) < max_number_of_student:
#             successful_applicants[student[priority]].append(student)
#         else:
#             next_wave.append(student)
#     sorted_list = next_wave
#
# # printing mechanism
# for depart in successful_applicants.keys():
#     print(depart)
#     sorted_department = sorted(successful_applicants[depart], key=lambda x: (-float(x[2]), x[0], x[1]))
#     for student in sorted_department:
#         name = student[0]
#         surname = student[1]
#         GPA = student[2]
#         print(name, surname, GPA)

# sol2
# N = int(input())
# with open('applicant_list_7.txt', 'r') as f:
#     data = [line.split() for line in f]
#
# count = {'Biotech': 0, 'Chemistry': 0, 'Engineering': 0, 'Mathematics': 0, 'Physics': 0}
# final = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
# grade = {'Biotech': [3, 2], 'Chemistry': 3, 'Engineering': [5, 4], 'Mathematics': 4, 'Physics': [2, 4]}
# used = []
#
# for i in range(7, 10):
#     for department in final.keys():
#         if type(grade[department]) == list:
#             sorted_data = sorted(data, key=lambda x: (-max(float(x[6]), ((float(x[grade[department][0]]) + float(x[grade[department][1]])) / 2)), x[0], x[1]))
#         else:
#             sorted_data = sorted(data, key=lambda x: (-max(float(x[6]), float(x[grade[department]])), x[0], x[1]))
#         for entry in sorted_data:
#             name = ' '.join([entry[0], entry[1]])
#             if count[entry[i]] == N or name in used or entry[i] != department:
#                 continue
#             else:
#                 if type(grade[department]) == list:
#                     final[entry[i]].append(' '.join([name, str(max(float(entry[6]), (float(entry[grade[department][0]]) + float(entry[grade[department][1]])) / 2))]))
#                 else:
#                     final[entry[i]].append(' '.join([name, str(max(float(entry[6]), float(entry[grade[department]])))]))
#                 count[entry[i]] += 1
#                 used.append(name)
#
# for department in final.keys():
#     with open('{}.txt'.format(department), 'w') as f:
#         f.writelines(line + '\n' for line in sorted(final[department], key=lambda x: (-float(x.rsplit(' ', 1)[1]), x.rsplit(' ', 1)[0])))