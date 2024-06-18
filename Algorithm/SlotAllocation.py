from Data import dfcourses, dfelectivecourses
from TeacherAllocation import batch_course_teachers, branch_course

course_lecture_hours = {}
for branch, courses in branch_course.items():
    course_lecture_hours[branch] = {}
    for course in courses:
        for course_detail in dfcourses:
            if course == course_detail['course_code']:
                course_lecture_hours[branch][course] = course_detail['lecture_hours'] + course_detail['tutorial_hours']

teachers_slot = {}
used_slots = {}
Branch_course_teacher_slot = {}
branch_elective_slot = {}
elective_courses = set()
elective_slot = {}
course_slot = {}
elective_name_course = {}


def get_lecture_hours(lec_course):
    for branch, courses in course_lecture_hours.items():
        for course, hours in courses.items():
            if lec_course == course:
                return hours


def elective_name(course_code):
    for dfcourse in dfelectivecourses:
        if dfcourse["course_code"] == course_code:
            return dfcourse['elective_name']
    return ""


def update_used_slots(branch):
    for course in branch_course[branch]:
        elecname = elective_name(course)
        if elecname != "":
            if elecname in elective_slot.keys():
                used_slots[branch].append(elective_slot[elecname])


def update_used_slots_course(branch):
    for course in branch_course[branch]:
        if course in course_slot.keys():
            used_slots[branch].append(course_slot[course])


def electivecourses():
    for course in dfelectivecourses:
        if course['elective_name'] != "":
            if course['elective_name'] in elective_name_course.keys():
                elective_name_course[course['elective_name']].append(course['course_code'])
            else:
                elective_name_course[course['elective_name']] = [course['course_code']]


for branch, courses in batch_course_teachers.items():
    electivecourses()
    branch_elective_slot = {}
    Branch_course_teacher_slot.setdefault(branch, {})
    used_slots.setdefault(branch, [])
    update_used_slots_course(branch)
    sorted_courses = sorted(courses, key=lambda x: get_lecture_hours(list(x.keys())[0]), reverse=True)
    slot_counts = {'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4}
    for course_set in sorted_courses:
        for cour, teacher_ids in course_set.items():
            lec_hours = get_lecture_hours(cour)
            assigned = False
            available_slots = [slot for slot in slot_counts if slot not in used_slots[branch]]
            for slot in available_slots:
                slot_hours = slot_counts[slot]
                if slot_hours >= lec_hours:
                    assigned_teachers = set()
                    is_slot_allocated = False
                    electivename = elective_name(cour)
                    for teacher_id in teacher_ids:
                        if teacher_id not in teachers_slot or teachers_slot[teacher_id] != slot:
                            teachers_slot[teacher_id] = slot
                            if electivename != "":
                                cours = []
                                if electivename in elective_name_course.keys():
                                    cours = elective_name_course[electivename]
                                if any(c in course_slot.keys() for c in cours):
                                    elective = Branch_course_teacher_slot[branch]
                                    if electivename not in elective:
                                        elective.setdefault(electivename, {})
                                    for c in cours:
                                        if c in course_slot.keys():
                                            Branch_course_teacher_slot[branch][electivename][teacher_id] = course_slot[c]
                                            course_slot[cour] = course_slot[c]
                                            break
                                else:
                                    course_slot[cour] = slot
                                    Branch_course_teacher_slot[branch].setdefault(electivename, {})
                                    Branch_course_teacher_slot[branch][electivename][teacher_id] = course_slot[cour]
                                    is_slot_allocated = True
                                if cour not in elective_courses:
                                    elective_courses.add(cour)
                            else:
                                if Branch_course_teacher_slot[branch] == {}:
                                    Branch_course_teacher_slot[branch].setdefault(cour, {})
                                else:
                                    branchcourse = Branch_course_teacher_slot[branch]
                                    if cour not in branchcourse:
                                        branchcourse.setdefault(cour, {})
                                Branch_course_teacher_slot[branch][cour][teacher_id] = slot
                            assigned_teachers.add(teacher_id)
                    if len(assigned_teachers) == len(teacher_ids):
                        if electivename == "":
                            slot_counts[slot] -= lec_hours
                            used_slots[branch].append(slot)
                        else:
                            slot_counts[course_slot[cour]] -= lec_hours
                        assigned = True
                        break  # Break after assigning one slot per course
            if not assigned:
                # Assign to remaining slots if all teachers couldn't be assigned to available slots
                remaining_slots = [slot for slot in slot_counts if slot_counts[slot] >= lec_hours]
                for slot in remaining_slots:
                    assigned_teachers = set()
                    is_slot_allocated = False
                    electivename = elective_name(cour)
                    for teacher_id in teacher_ids:
                        if teacher_id not in teachers_slot or teachers_slot[teacher_id] != slot:
                            teachers_slot[teacher_id] = slot
                            if electivename != "":
                                cours = elective_name_course[electivename]
                                if any(c in course_slot.keys() for c in cours):
                                    elective = Branch_course_teacher_slot[branch]
                                    if electivename not in elective:
                                        elective.setdefault(electivename, {})
                                    for c in cours:
                                        if c in course_slot.keys():
                                            Branch_course_teacher_slot[branch][electivename][teacher_id] = course_slot[
                                                c]
                                            course_slot[cour] = course_slot[c]
                                            break
                                else:
                                    course_slot[cour] = slot
                                    Branch_course_teacher_slot[branch].setdefault(electivename, {})
                                    Branch_course_teacher_slot[branch][electivename][teacher_id] = course_slot[cour]
                                    is_slot_allocated = True
                                if cour not in elective_courses:
                                    elective_courses.add(cour)
                            else:
                                if Branch_course_teacher_slot[branch] == {}:
                                    Branch_course_teacher_slot[branch].setdefault(cour, {})
                                else:
                                    branchcourse = Branch_course_teacher_slot[branch]
                                    if cour not in branchcourse:
                                        branchcourse.setdefault(cour, {})
                                Branch_course_teacher_slot[branch][cour][teacher_id] = slot
                            assigned_teachers.add(teacher_id)
                    if len(assigned_teachers) == len(teacher_ids):
                        if electivename == "":
                            slot_counts[slot] -= lec_hours
                            used_slots[branch].append(slot)
                        else:
                            slot_counts[course_slot[cour]] -= lec_hours
                        assigned = True
                        break  # Break after assigning one slot per course
                if not assigned and cour not in elective_courses:
                    print(f"Could not assign a slot for {cour} in {branch}")
                    print(f"Available slots: {available_slots}")
                    print(f"Remaining slots: {remaining_slots}")
                    pass
print(Branch_course_teacher_slot)
# batch elective courses
# 23CSE331 is there for S1CSE,S1AIE,S1ECE
