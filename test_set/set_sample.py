# path : .\\test_set\\set_sample.py
# module : test_set.set_sample (패키지명.모듈명)

# 집합(set) 자료형
# 교집합(&), 합집합(|), 차집합(-) 연산이 가능한 자료형
# 저장방식 : 중복 불가, 인덱싱 불가(저장 순서 없음)

# set 정의 방법 1 : {} 중괄호 사용
def test1():
    set1 = {1, 2, 3, 4, 1, 2}
    print(f'set1 : {set1}')

# set 정의 방법 2 : set() 함수 사용
def test2():
    set1 = set()
    print(f'set1 : {set1}')

# set에 문자열을 저장하는 경우 : 문자 하나씩 저장
def test3():
    set1 = set('Hello') # 중복 저장 안 함 => 'ㅣ'은 하나만 저장됨
    print(f'set1 : {set1}')
    
    set2 = set('Python python') # 공백도 하나의 값, 대소문자 구분함
    print(f'set2 : {set2}')

# set에 list 저장할 수 있음
# 리스트 자체는 값 순서대로 저장함 => set이 저장 순서를 유지하게 하는 방법
def test4():
    set1 = set([1, 2, 3, 4]) # 순서대로 저장됨
    print(f'set1 : {set1}')
    set2 = set([4, 5, 6, 7]) # 순서대로 저장됨
    print(f'set2 : {set2}')

    # set 자료형은 집합 연산 가능함 : 합집합, 교집합, 차집합
    # 교(곱)집합 : & 연산자 또는 intersection() 함수 사용
    print('set1 & set2 :', set1 & set2)
    print('intersection :', set1.intersection(set2))

    # set 자료형은 집합 연산 가능함 : 합집합, 교집합, 차집합
    # 합집합 : | 연산자 또는 union() 함수 사용
    print('set1 | set2 :', set1 | set2)
    print('union :', set1.union(set2))

    # set 자료형은 집합 연산 가능함 : 합집합, 교집합, 차집합
    # 차집합 : - 연산자 또는 difference() 함수 사용
    print('set1 - set2 :', set1 - set2)
    print('difference :', set1.difference(set2))

    # 값 추가 : add() 함수 사용
    set1.add(99)
    print(set1, type(set1))

    # 값 여러개 추가 : update() 함수 사용
    set1.update([77, 33, 44, 55])
    print(set1, type(set1))

    # 값 삭제 : remove() 함수 사용
    set1.remove(77)
    print(set1, type(set1))

def test5():
    # list의 값 중복을 제거하고자 할 때 set을 이용한다.
    lst = [1, 1, 2, 2, 2, 3, 3, 4, 4, 4]
    print('lst :', lst)
    set1 = set(lst) # 중복 값 제거
    print('set1 :', set1)
    

# 실행 확인
if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    test5()

