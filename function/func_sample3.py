# path : .\\function\\func_sample3.py

# 매개변수들 설정 테스트
def tmax(a, b):
    '두 개의 값을 전달받아서, 둘 중 큰 값을 리턴하는 함수, call by value 방식 사용'
    print(f'a : {a}, b : {b}, type : {type(a)}, {type(b)}')

    # 권장하지 않는 방식
    # if a > b :
    #     return a
    # else :
    #     return b 
    
    # 권장하는 방식
    result = 0
    if a > b :
        result = a
    else :
        result = b
    return result

def func_callby_value():
    'tmax()함수 테스트용. 매개변수 전달인자 갯수 일치 확인용 함수'
    result = tmax(10, 20) # call by value : 값 전달
    print('큰 값 : ', result)
    result = tmax(33.3, 12.5)
    print('큰 값 : ', result)

    # 아스키 코드번호 기준
    print('큰 값 : ', tmax('M', 'm'))

    result = tmax(33.3, 12.5, 3)
    print('큰 값 : ', result)

# 군집자료형을 전달받는 매개변수는 주소를 받는다.
def list_in_max(plist):
    '리스트 객체를 전달받아서, 저장된 값들 중 가장 큰 값을 찾아내서 리턴하는 함수'
    print(f'plist : {plist}, 주소 : {id(plist)}')
    max = plist[0]
    for item in plist:
        if item > max:
            max = item
    return max
# list_in_max end -------------------

# 함수 호출 시 함수 쪽으로 주소를 전달 : call by address(call by reference)
def func_callby_reference():
    '함수 쪽으로 주소 전달 테스트'
    nlist = [45, 1, 33, 12, 90, 123, 7]
    print(f'nlist : {nlist}, 주소 : {id(nlist)}')
    result = list_in_max(nlist)
    print(f'가장 큰 값 : {result}') 

# 기본 매개변수 : 기본값을 가진 매개변수
# def 함수명(매개변수=기본값, 매개변수=기본값):
# 주의 : 뒤쪽(오른쪽 끝) 매개변수부터 기본값 지정해야 함
# 기본값이 없는 매개변수는 기본값 있는 매개변수의 왼쪽에 있어야 함.
# def 함수명(매개변수, 매개변수, 매개변수=기본값): 
# 함수 실행 시 기본값 있는 매개변수는 생략 가능 => 함수(값, 값)
def tmin(a=0, b=0, c=0):
    '3개의 값을 전달받아서, 가장 작은 값을 찾아내서 리턴하는 함수'
    print(f'a : {a}, b : {b}, c : {c}')
    result = 0
    if a < b and a < c:
        result = a
    elif b < c:
        result = b
    else:
        result = c
    return(result)
# tmin end -------------------------------

def func_default_param():
    '기본값 매개변수가 있는 함수 사용 테스트'
    print(f'가장 작은 값 : {tmin(12, 3, 45)}')
    print(f'가장 작은 값 : {tmin(12, 3)}')
    print(f'가장 작은 값 : {tmin(12)}')
    print(f'가장 작은 값 : {tmin()}')
# func_default_param end --------------------


if __name__ == '__main__':
    # func_callby_value()
    # func_callby_reference()
    func_default_param()

