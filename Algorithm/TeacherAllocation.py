from Data import dfbatch, dfcourseteacher
from BatchCourses import batch_courses

def get_available_teachers(course_teacher_list):
    available_teachers_dict = {}
    for entry in course_teacher_list:
        course_code = entry['course_code']
        teacher_id = entry['teacher_id']
        if course_code in available_teachers_dict:
            available_teachers_dict[course_code].append(teacher_id)
        else:
            available_teachers_dict[course_code] = [teacher_id]
    return available_teachers_dict


available_teachers = get_available_teachers(dfcourseteacher)


def Teachers_Allocation(batch_courses, available_course_teachers):
    allocated_teachers = {}
    result = {}

    for batch, courses in batch_courses.items():
        course_teacher_dict = []
        for course in courses:
            if course in available_course_teachers:
                teachers = available_course_teachers[course]
                for teacher_id in teachers:
                    if teacher_id not in allocated_teachers:
                        allocated_teachers[teacher_id] = 0
                    if allocated_teachers[teacher_id] < 2:
                        allocated_teachers[teacher_id] += 1
                        course_teacher_dict.append({course: teacher_id})
                        break
        result[batch] = course_teacher_dict

    return result


Allocated_Batch_Course_Teacher = Teachers_Allocation(batch_courses, available_teachers)
print(Allocated_Batch_Course_Teacher)

def generate_branch_batch(df_batch, branch_code):
    branch_batch = {}
    for batch in df_batch:
        semester_branch = batch['semester'] + branch_code[batch['branch_name']]
        branch = batch['branch_name']
        if branch in branch_batch:
            branch_batch[branch].append(semester_branch)
        else:
            branch_batch[branch] = [semester_branch]

    for k, v in branch_batch.items():
        branch_batch[k] = list(sorted(set(v)))
    return branch_batch


def generate_branch_course(branch_batch, batch_courses):
    branch_course = {}
    for branch in branch_batch:
        batch_list = branch_batch[branch]
        for batch in batch_list:
            branch_course[batch] = batch_courses[batch + "A"]
    return branch_course


def assign_teachers_to_branch_courses(branch_course, allocated_teachers):
    Branch_Course_Teachers = {}
    for branch, courses in branch_course.items():
        Branch_Course_Teachers[branch] = []
        for course in courses:
            combined_course = {course: set()}
            for key, values in allocated_teachers.items():
                if branch in key:
                    for value in values:
                        if isinstance(value, dict):
                            if course in value:
                                combined_course[course].add(list(value.values())[0])
            if combined_course[course]:
                Branch_Course_Teachers[branch].append(combined_course)
    return Branch_Course_Teachers


branch_code = {
    "Computer Science and Engineering": "CSE",
    "Electronics and Communication and Engineering": "ECE",
    "Artificial Intelligence and Engineering": "AIE",
    "Electrical and Computer Engineering": "ELC"
}

branch_batch = generate_branch_batch(dfbatch, branch_code)
branch_course = generate_branch_course(branch_batch, batch_courses)
batch_course_teachers = assign_teachers_to_branch_courses(branch_course, Allocated_Batch_Course_Teacher)
batch_course_teacher = {}
for branch, courses in batch_course_teachers.items():
    for course_set in courses:
        for cour, teacher_ids in course_set.items():
            batch_course_teacher.setdefault(branch, {}).setdefault(cour, []).extend(teacher_ids)