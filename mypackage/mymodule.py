# path : .\\mypackage\\mymodule.py
# module : mypackage.mymodule (패키지명.모듈명)
# 사용자 정의 모듈

# 전역변수와 함수와 클래스들을 작성해 놓은 파이썬 소스 파일
# 실행 코드는 포함하지 않아야 함
# 자주 반복적으로 사요외는 코드를 따로 작성해놓고 필요시 다른 파이썬 파일에서 가져다 사용하려는 목적의 파일임
# 장점 1 : 소스 코드 중복 작성을 줄일 수 있음
# 장점 2 : 유지보수가 편함
# 장점 3 : 애플리케이션 구조 설정이 편해짐

# 전역 변수 (Global Variable : 함수 밖에 작성한 변수)
pi = 3.14159
count = 10

# 함수 (function)
def sum(a, b): # 매개변수(parameter)가 있는 함수
    '두 수를 전달받아서 더하기 결과 리턴'
    return a + b

def sub(a, b): # 매개변수(parameter)가 있는 함수
    '두 수를 전달받아서 빼기 결과 리턴'
    return a - b

def mul(a, b): # 매개변수(parameter)가 있는 함수
    '두 수를 전달받아서 곱하기 결과 리턴'
    return a * b

def div(a, b): # 매개변수(parameter)가 있는 함수
    '두 수를 전달받아서 나누기 결과 리턴, 나눌 수가 0이면 Exception 발생 시킴'
    if b == 0:
        raise Exception('0으로 나눌 수 없음')
    return a / b

def mod(a, b): # 매개변수(parameter)가 있는 함수
    '두 수를 전달받아서 나누기한 나머지 리턴, 나눌 수가 0이면 Exception 발생 시킴'
    if b == 0:
        raise Exception('0으로 나눌 수 없음')
    return a % b

def max(*args): # 가변 매개변수 : 여러개의 값을 받는 매개변수 (0 ~ n개)
    '가변 매개변수를 사용해서 전달받은 값들 중에 가장 큰 값을 리턴'
    try:
        max_value = args[0] # 매개변수가 0개이면 이 지점에서 에러 발생
        for data in args:
            if max_value < data:
                max_value = data
        return max_value    
    except:
        print('처리할 데이터 없음')
# max end -------------------------------

def min(*args): # 가변 매개변수 : 여러개의 값을 받는 매개변수 (0 ~ n개)
    '가변 매개변수를 사용해서 전달받은 값들 중에 가장 작은 값을 리턴'
    try:
        min_value = args[0] # 매개변수가 0개이면 이 지점에서 에러 발생
        for data in args:
            if min_value > data:
                min_value = data
        return min_value    
    except:
        print('처리할 데이터 없음')
# min end -------------------------------

def str_len(st=None): # 기본 매개변수 : 기본 값이 지정된 매개변수를 대입할 수 있다.
    '문자열을 전달받아서 글자 갯수 리턴'
    slen = 0
    if st != None: # st가 값이 있으면
        for ch in st:
            slen += 1
    return slen
# str_len end --------------------
