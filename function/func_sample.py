# path : .\\function\\func_sample.py

# 파이썬에서 함수 만들어 사용하기

'''
함수(function): 반복 사용되는 소스코드를 분리 작성해서 이름 붙인 것
def 함수명(매개변수):  <- 매개변수(parameter)는 0 ~ n개
    함수가 실행할 코드 구문
    ...
    return | return 값 | return 값, 값, 값   <- 여러개 반환 시 타입은 튜플(tuple)임

* 함수의 사용(call 또는 호출) : 함수가 만들어진 형태에 맞춰서 사용해야 한다.
=> 함수 이름 : 대소문자 주의, _ 갯수 확인, 예약어 또는 공백 사용 불가
=> 매개변수 개수 일치 : 전달 인자의 갯수는 매개변수 갯수와 같아야 함
=> 반환값 여부 : return 값이 있는 함수는 다른 함수안에 중첩 사용 가능 => 함수명(반환값이 있는 함수())
'''

# 빈 함수는 pass 넣어 줌
def func():
    pass

# 함수명 하단에 함수 설명을 적을 수 있다(description) : '함수 설명...'
def hello():
    '이 함수는 함수 작성 연습용이다.'
    print('Wellcome!!')
    print('함수명에 예약어, 공백 사용 불가')
    return # 생략 가능

# 매개변수 있고, 반환값 있는 함수
def add(x, y):
    print(f'x : {x}, y : {y}')
    return x + y

# 여러개의 값 리턴 가능
def func2(a, b):
    print(f'a : {a}, b : {b}')
    return a * 2, b * 2


# 함수 실행
if __name__ == '__main__':
    func()
    hello()
    # help() : 함수 설명을 확인할 수 있다.
    # help(hello)
    # help(input)
    # help(print)
    
    result = add(10, 20)

    # 기본 사용법
    print('result :', result)

    # 함수안에 '반환값이 있는 함수'를 중첩 사용 가능
    print('result :', add(10, 20))
    result2 = func2(10, 20)
    print('result2 :', result2, type(result2))

    # 반환값을 각각의 변수에 담으면 자료형은 원래 자료형 그대로
    n1, n2 = func2(3.3, 4.4)
    print(n1, n2, type(n1), type(n2))