def filter_scores(scores, min_score):
    for s in scores:
        if s >= min_score:
            yield s

user_input = input('정수들을 입력하세요: ')
scores = list(map(int, user_input.split()))

threshold = int(input('합격 기준 정수를 입력하세요: '))
print('\n합격 점수: ')

for score in filter_scores(scores, threshold):
    print(score, end=' ')
