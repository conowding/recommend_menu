import itertools

feature = ["식사", "요리", "간식"]
otherperson = ["혼밥", "친구", "가족", "연인", "회식"]
country = ["한식", "중식", "일식", "양식", "아시아"]

# 모든 조합 생성
all = list(itertools.product(feature, otherperson, country))

# 생성된 모든 조합 출력
for i in all:
    print(i)
