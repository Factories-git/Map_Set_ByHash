'''
시간초과. 이유는 K+M-1까지 그냥 예측하기 때문.
'''

import sys

input = sys.stdin.readline

n, k, m = map(int, input().split()) #입력 받음
copus = []
practice = {}
for i in range(n):
    copus.append(list(input().strip())) #훈련 코퍼스에 넣음
for sentence in copus: #문장마다 반복
    for i in range(len(sentence)-1): #다음 글자가 뭔지 넣음.
        letter = sentence[i]
        if letter not in practice:
            practice[letter] = {} #만약 현재 글자가 딕셔너리에 없다면, 딕셔너리 생성함.
        if sentence[i+1] not in practice[letter]: #다음 글자의 개수가 만약 아직 없다면:
            practice[letter][sentence[i+1]] = 1 #넣음
        else: #있다면
            practice[letter][sentence[i+1]] += 1 #개수를 하나 올려줌

#바로 밑 코드는 정렬. 나온 횟수, 그리고 아스키 코드가 작은것으로 정렬 (제일 비효율적일 것 같은 코드)
sorted_practice = {k : dict(sorted(v.items(), key=lambda item: (item[1], -ord(item[0])))) for k,v in practice.items()}
s = '[' #예측 시작을 뜻함
now_s = '['
for i in range(k+m-2): #[를 입력했으니 그 전까지만 반복
    if now_s == ']': #만약 예측을 끝냈다면,
        s += '.' #. 을 찍음
        continue
    p = sorted_practice[now_s].popitem()
    s += p[0] #예측 중이라면, 방금 전 예측한 문자의 다음 문자중 횟수, 아스키코드 순서로 가장 우선순위가 높은걸 뽑아옴.
    sorted_practice[now_s][s[-1]] = p[1] #뽑은 걸 다시 넣어줌.
    now_s = p[0] #방금 예측한 문자로 변경
print(s)