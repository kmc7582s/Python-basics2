a = int()                   # 정수라면 가져야하는 속성과 특징을 a 인스턴스에게 부여
b = float()               # 실수라면 가져야하는 속성과 특징을 b 인스턴스에게 부여
c = str()                   # 문자열이라면 가져야하는 속성과 특징을 c 인스턴스에게 부여
d = list()                  # 리스트라면 가져야하는 속성과 특징을 d 인스턴스에게 부여
e = tuple()               # 튜플이라면 가져야하는 속성과 특징을 e 인스턴스에게 부여
f = set()                   # 세트라면 가져야하는 속성과 특징을 f 인스턴스에게 부여
g = dict()                 # 딕셔너리라면 가져야하는 속성과 특징을 g 인스턴스에게 부여

c.format()
d.append()
d.copy()
d.count()
d.insert()
e.count()
f.add()
g.keys()                    # 이것들이 다 클래스 내에서 구현되어 있던 기능입니다!

#ex)
# class List():
#        def append(self, X):
