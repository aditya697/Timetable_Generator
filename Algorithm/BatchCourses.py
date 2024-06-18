from Data import dfbatch, dfsemester_course

batch_courses = {}
for batch in dfbatch:
    batch_courses[batch['semester'] + batch['batch_name']] = []
    for semester_course in dfsemester_course:
        if batch['semester'] == semester_course['semester'] and batch['branch_name'] == semester_course['branch_name']:
            batch_courses[batch['semester'] + batch['batch_name']].append(semester_course['course_code'])
print(batch_courses)