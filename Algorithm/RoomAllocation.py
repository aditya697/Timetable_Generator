from Data import dfrooms, dfbatch

sessions = ["fn", "an"]
dfrooms1 = sorted(dfrooms, key=lambda k: k['room_capacity'])
dfbatch1 = sorted(dfbatch, key=lambda k: k['batch_size'])

room_batch = {}
allocated_rooms = []
# allocation classroom for lecture hours
for room in dfrooms1:
    count = 0
    for batch in dfbatch1:
        if room['room_capacity'] >= batch['batch_size']:
            current_session = sessions[count % len(sessions)]
            current_room = room['room_no']
            allocated_rooms.append(current_room)
            room_batch[batch['semester']+batch['batch_name']] = {"session": current_session, "room": current_room}
            batch['room_no'] = room['room_no']
            count += 1
            if count == 2:
                if len(dfbatch1) >= 1:
                    dfbatch1.pop(0)
                if len(dfbatch1) >= 1:
                    dfbatch1.pop(0)
                break
