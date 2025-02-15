def solution(record):
    answer = []
    nicknames = {}
    for i in record:
        if len(i.split()) == 3:
            cmd, id, name = i.split()
            nicknames[id] = name

    for i in record:
        if len(i.split()) == 3:
            cmd, id, name = i.split()
            if cmd == 'Enter':
                answer.append(f'{nicknames[id]}님이 들어왔습니다.')
        else:
            cmd, id = i.split()
            if cmd == 'Leave':
                answer.append(f'{nicknames[id]}님이 나갔습니다.')
    return answer
