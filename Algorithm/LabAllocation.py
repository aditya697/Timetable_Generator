# import copy
#
# from Data import dfcourses, dfbatch, dfrooms, dfbatch_course_classroom
# from RoomAllocation import allocated_rooms
#
# timetable = {}
#
# for entry in dfbatch_course_classroom:
#     semester = entry['semester']
#     batch_name = entry['batch_name']
#     room_no = entry['room_no']
#     sessions = entry['sessions']
#     course_code = entry['course_display_name']
#     teacher_id = entry['teacher_id']
#     slot = entry['slot']
#
#     if semester not in timetable:
#         timetable[semester] = {}
#     if batch_name not in timetable[semester]:
#         timetable[semester][batch_name] = {}
#     if room_no not in timetable[semester][batch_name]:
#         timetable[semester][batch_name][room_no] = {}
#     if sessions not in timetable[semester][batch_name][room_no]:
#         timetable[semester][batch_name][room_no][sessions] = []
#
#     timetable[semester][batch_name][room_no][sessions].append({
#         'course_code': course_code,
#         'teacher_id': teacher_id,
#         'slot': slot
#     })
#
# print(timetable)
#
# # available_slots = {'A': 2, 'B': 2, 'C': 1, 'D': 2, 'E': 2, 'F': 1}
# available_slots = ['AL11', 'AL12', 'AL13', 'AL14', 'BL11', 'BL12', 'BL13', 'BL14', 'CL11', 'CL12', 'CL13',
#                    'CL14', 'DL11', 'DL12', 'DL13', 'DL14', 'EL11', 'EL12', 'EL13', 'EL14', 'FL11', 'FL12']
#
# elective_slots = set()
#
# for semester, batches in timetable.items():
#     for batch, rooms in batches.items():
#         for room, sessions in rooms.items():
#             for session, courses in sessions.items():
#                 for course in courses:
#                     if 'elective' in course['course_code'].lower():
#                         if course['slot'] == "A":
#                             elective_slots.append('BL11')
#                             elective_slots.append('BL12')
#                             elective_slots.append('DL11')
#                             elective_slots.append('DL12')
#                             elective_slots.append('DL13')
#                             elective_slots.append('DL14')
#                             elective_slots.append('EL13')
#                             elective_slots.append('EL14')
#                         elif course['slot'] == "B":
#                             elective_slots.append('DL11')
#                             elective_slots.append('DL12')
#                             elective_slots.append('EL11')
#                             elective_slots.append('EL12')
#                             elective_slots.append('EL13')
#                             elective_slots.append('EL14')
#                             elective_slots.append('FL11')
#                             elective_slots.append('FL12')
#                         elif course['slot'] == "C":
#                             elective_slots.append("EL11")
#                             elective_slots.append("EL12")
#                             elective_slots.append("AL13")
#                             elective_slots.append("AL14")
#                             elective_slots.append("FL11")
#                             elective_slots.append("FL12")
#                         elif course['slot'] == "D":
#                             elective_slots.append("AL11")
#                             elective_slots.append("AL12")
#                             elective_slots.append("AL13")
#                             elective_slots.append("AL14")
#                             elective_slots.append("CL11")
#                             elective_slots.append("CL12")
#                         elif course['slot'] == "E":
#                             elective_slots.append("BL13")
#                             elective_slots.append("BL14")
#                             elective_slots.append("CL11")
#                             elective_slots.append("CL12")
#                             elective_slots.append("AL11")
#                             elective_slots.append("AL12")
#                         elif course['slot'] == "F":
#                             elective_slots.append("BL11")
#                             elective_slots.append("BL12")
#                             elective_slots.append("BL13")
#                             elective_slots.append("BL14")
#                             elective_slots.append("DL13")
#                             elective_slots.append("DL14")
#
# print("Elective Slots:", elective_slots)
# elective_slots = list(elective_slots)
# print("Elective Slots:", elective_slots)
#
#
# def filter_available_slots(available_slots, elective_slots):
#     for slot in elective_slots:
#         if slot in available_slots:
#             available_slots.remove(slot)
#     return available_slots
#
#
# # Initialize available_batches and available_rooms dynamically based on dfbatches and dfrooms
# available_batches = {}
# for batch_info in dfbatch:
#     batch_name = batch_info['batch_name']
#     available_batches[batch_name] = filter_available_slots(available_slots.copy(), elective_slots)
#
# available_rooms = {}
# for room in dfrooms:
#     if room["room_no"] not in allocated_rooms:
#         available_rooms[room['room_no']] = {
#             'fn': filter_available_slots(available_slots.copy(), elective_slots),
#             'an': filter_available_slots(available_slots.copy(), elective_slots)
#         }
#
# alternative_slots = {'A': ['CL11', 'CL12', 'CL13', 'CL14', 'FL11', 'FL12'],
#                      'B': ['CL11', 'CL12', 'CL13', 'CL14'],
#                      'C': ['DL11', 'DL12', 'DL13', 'DL14', 'BL11', 'BL12', 'BL13', 'BL14'],
#                      'D': ['BL11', 'BL12', 'BL13', 'BL14', 'EL11', 'EL12', 'EL13', 'EL14'],
#                      'E': ['DL11', 'DL12', 'DL13', 'DL14', 'FL11', 'FL12'],
#                      'F': ['AL11', 'AL12', 'AL13', 'AL14', 'EL11', 'EL12', 'EL13', 'EL14']}
#
# course_lab_hours = {}
# for course_detail in dfcourses:
#     course_lab_hours[course_detail['course_code']] = course_detail['practical_hours']
#
#
# def allocate_room(slot, session, batch):
#     for room in available_rooms:
#         for i, s1 in available_rooms[room][session]:
#             for s2 in available_batches[batch]:
#                 if s1.startswith(slot) and s2.startswith(slot):
#                     return room, available_rooms[room][session][i], available_rooms[room][session][i + 1]
#     return None, None
#
#
# def allocate_alternative_slot(slot, available_slots):
#     for i, alt_slot in alternative_slots[slot]:
#         return alt_slot[0]
#     return None
#
#
# labtimetable = {}
# prev_room = None
# allocated_rooms = []
#
# for semester, batches in timetable.items():
#     labtimetable.setdefault(semester, {})
#     for batch, rooms in batches.items():
#         labtimetable[semester].setdefault(batch, {})
#         for room, sessions in rooms.items():
#             for session, courses in sessions.items():
#                 if session == 'fn':
#                     new_session = 'an'
#                 else:
#                     new_session = 'fn'
#                 for course in courses:
#                     if course['course_code'] not in course_lab_hours:
#                         continue
#                     lab_hours = course_lab_hours[course['course_code']]
#                     if lab_hours >= 2:
#                         slot = course['slot']
#                         allocated_room, new_slot = allocate_room(slot, new_session, batch)
#                         if allocated_room is None and new_slot is None:
#                             allocated_room, new_slot = allocate_alternative_slot(slot, available_slots)
#                         if allocated_room is not None and new_slot is not None and new_slot not in elective_slots:
#                             available_slots.remove(new_slot)
#                             course_copy = copy.deepcopy(course)
#                             course_copy['slot'] = new_slot
#                             allocated_rooms.append(allocated_room)
#                             labtimetable[semester][batch].setdefault(allocated_room, {})
#                             labtimetable[semester][batch][allocated_room].setdefault(new_session, [])
#                             labtimetable[semester][batch][allocated_room][new_session].append(course_copy)
# print(labtimetable)
# print(timetable)


import copy

from Data import dfcourses, dfbatch, dfrooms, dfbatch_course_classroom
from RoomAllocation import allocated_rooms

timetable = {}

for entry in dfbatch_course_classroom:
    semester = entry['semester']
    batch_name = entry['batch_name']
    room_no = entry['room_no']
    sessions = entry['sessions']
    course_code = entry['course_display_name']
    teacher_id = entry['teacher_id']
    slot = entry['slot']

    if semester not in timetable:
        timetable[semester] = {}
    if batch_name not in timetable[semester]:
        timetable[semester][batch_name] = {}
    if room_no not in timetable[semester][batch_name]:
        timetable[semester][batch_name][room_no] = {}
    if sessions not in timetable[semester][batch_name][room_no]:
        timetable[semester][batch_name][room_no][sessions] = []

    timetable[semester][batch_name][room_no][sessions].append({
        'course_code': course_code,
        'teacher_id': teacher_id,
        'slot': slot
    })

print(timetable)

available_slots = {'A': 2, 'B': 2, 'C': 1, 'D': 2, 'E': 2, 'F': 1}

# Initialize available_batches and available_rooms dynamically based on dfbatches and dfrooms
available_batches = {}
for batch_info in dfbatch:
    batch_name = batch_info['batch_name']
    available_batches[batch_name] = available_slots.copy()


available_rooms = {}
for room in dfrooms:
    if room["room_no"] not in allocated_rooms:
        available_rooms[room['room_no']] = {
            'fn': available_slots.copy(),
            'an': available_slots.copy()
        }

alternative_slots = {'A': ['C', 'F'], 'B': ['C'], 'C': ['D', 'B'], 'D': ['B', 'E'], 'E': ['D', 'F'],
                     'F': ['A', 'E']}

course_lab_hours = {}
for course_detail in dfcourses:
    course_lab_hours[course_detail['course_code']] = course_detail['practical_hours']


def allocate_room(slot, session, batch):
    for room in available_rooms:
        if (
                slot in available_rooms[room][session]
                and available_rooms[room][session][slot] > 0
                and available_batches[batch][slot] > 0
        ):
            available_rooms[room][session][slot] -= 1
            return room, slot

        # If unable to allocate in any existing room or batch, allocate in a new room
        else:
            if available_rooms[room][session][slot] == 0 or available_batches[batch][slot] == 0:
                new_slot = allocate_alternative_slot(slot, available_rooms[room][session])
                if new_slot is not None:
                    return room, new_slot

    return None, None

def allocate_alternative_slot(slot, available_slots):
    for alt_slot in alternative_slots[slot]:
        if available_slots[alt_slot] > 0:
            available_slots[alt_slot] -= 1
            return alt_slot
    return None


labtimetable = {}
prev_room = None
allocated_rooms = []

for semester, batches in timetable.items():
    labtimetable.setdefault(semester, {})
    for batch, rooms in batches.items():
        labtimetable[semester].setdefault(batch, {})
        for room, sessions in rooms.items():
            for session, courses in sessions.items():
                if session == 'fn':
                    new_session = 'an'
                else:
                    new_session = 'fn'
                for course in courses:
                    if course['course_code'] not in course_lab_hours:
                        continue
                    lab_hours = course_lab_hours[course['course_code']]
                    if lab_hours >= 2:
                        slot = course['slot']
                        allocated_room, new_slot = allocate_room(slot, new_session, batch)
                        course_copy = copy.deepcopy(course)
                        course_copy['slot'] = new_slot
                        if new_slot is not None:
                            available_batches[batch][new_slot] -= 1
                        allocated_rooms.append(allocated_room)
                        labtimetable[semester][batch].setdefault(allocated_room, {})
                        labtimetable[semester][batch][allocated_room].setdefault(new_session, [])
                        labtimetable[semester][batch][allocated_room][new_session].append(
                            course_copy)  # Append the copied course
print(labtimetable)
print(timetable)