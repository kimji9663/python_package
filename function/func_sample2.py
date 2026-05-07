# path : .\\function\\func_sample2.py

# 변수 생성과 사용 영역 (지역, 스코프 : scope, 생존범위)
# 지역변수(Local Variable)와 전역변수(Global Variable)

def func1():
    num = 10 # 함수 안에서 만든 변수 : 지역변수 (함수 실행 시 생성됨. 함수 종료 시 소멸됨)
    print(f'num : {num}')

# 지역변수는 함수 밖에서 사용 불가
# print(f'num : {num}') # NameError: name 'num' is not defined.


# 파이썬에서의 전역변수
GNUM = 100 # 선언된 위치 아래에서 사용가능 (인터프리터 언어의 특징)
print(GNUM)

def func_global():
    print(f'GNUM : {GNUM}')
    GNUM = 200 # 함수안에 다시만든 지역변수가 전역변수와 이름이 같으면 오류 발생
    # print(f'GNUM : {GNUM}') # UnboundLocalError

    
def func_global1():
    # print(f'GNUM : {GNUM}')
    # 전역변수 값 변경하려면, GNUM에 대한 전역 선언이 필요함
    global GNUM
    GNUM = 200 # 값 변경
    print(f'GNUM : {GNUM}') # UnboundLocalError

# 함수의 매개변수(parameter)는 전달받은 값을 사용만 함
# 함수쪽에서 함수 호출부(실행위치)의 변수 값 변경 불가
# 전달받은 값이 군집자료형(collection)일 때는 아이템(element, 요소)은 변경할 수 있음
def func_list(plist):
    print('plist가 받은 주소 :', id(plist)) # lst의 주소가 전달됨
    print('before :', plist)
    plist[1] = 10 # lst의 값이 변경됨
    print('after :', plist)


if __name__ == '__main__':
    # func_global()
    # func_global1()

    # 군집자료형 변수
    lst = [1, 2, 3, 4]
    print('lst가 참조하는 리스트 객체의 주소 : ', id(lst))
    print('lst :', lst)

    # 호출부
    func_list(lst) # lst의 주소를 전달인자에 대입함