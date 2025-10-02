#집합연산은 객체둘다 세트형일때 사용가능
sd1 = {1,2,3,4}
sd2 = {3,4,5,6}

#합집합 나타내기
print(set.union(sd1, sd2)) #{1, 2, 3, 4, 5, 6}
print(sd1.union(sd2)) #{1, 2, 3, 4, 5, 6}
print(sd1 | sd2) #{1, 2, 3, 4, 5, 6}  |=>유니언표시
print()

#교집합 나탄내기
print(set.intersection(sd1, sd2)) #{3, 4}
print(sd1.intersection(sd2)) #{3, 4}
print(sd1 & sd2) #{3, 4}  &=>AND 표시
print()

#차집합나타내기
print(set.difference(sd1, sd2)) #{1, 2} 변수먼저 넣어주는거 위주로 계산됨.. 여기선 1,2,3,4 기준으로 잡아주고 3,4,5,6에는 포함안되있는게 표시됨
print(sd1.difference(sd2)) #{1, 2}
print(sd1 - sd2) #{1, 2}

#대칭차집합
print(set.symmetric_difference(sd1, sd2)) #{1, 2, 5, 6}
print(sd1.symmetric_difference(sd2)) #{1, 2, 5, 6}
print(sd1 ^ sd2) #{1, 2, 5, 6} ^ => XOR 표시 