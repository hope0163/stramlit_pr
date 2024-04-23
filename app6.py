# 유저한테 숫자, 문자, 시간, 색을 입력받는 방법

import streamlit as st

def main():
    # 1. 이름입력 받기
    name = st.text_input("이름을 입력하세요!") # 파이썬에 input과 동일 , 문자열을 입력받으려면 st.text_input()

    if name != '': # 입력하지 않았을때는 아무것도 안나오게 하기
        st.text(name + ' 안녕하세요?')


    # 2. 입력 글자 갯수 제한
    address = st.text_input('주소를 입력하세요.', max_chars=10) # max_chars 는 입력글자수 제한
    st.text(address)

    # 3. 여러 행을 입력가능하도록
    message = st.text_area('메세지를 입력하세요.', height=3) # height= 높이설정
    st.text(message)

    # 4. 비밀번호 입력 (12 글자까지)
    password = st.text_input('비밀번호를 입력하세요.' , max_chars=12, type='password') # type= password로 지정하면 입력한 문자들을 숨겨줌
    st.text(password)


    # 5. 정수 입력 하는 방법
    st.number_input('숫자 입력하세요.', -10, 100) # 숫자를 입력받을 때는 st.number_input() 사용
    # min_valuem max_value 파라미터를 입력하여 범위 지정

    # 6. 실수 입력하는 방법
    st.number_input('숫자 입력하세요', -5.3, 10.8, step=0.5 ) # step= 파라미터를 지정해주면 원하는 크기만큼 이동 가능
    # min_value, max_value의 데이터 타입에 따라 정수형/실수형으로 바뀜

    # 7. 날짜 입력 하는 방법
    my_date = st.date_input('약속 날짜 선택') # default는 현재 날짜
    print(my_date)
    st.write(my_date)
    print(type(my_date))


    # 8. 요일 찍기
    st.text(my_date.weekday())
    st.text(my_date.strftime('%A'))

    # 9. 시간 입력 받기
    my_time = st.time_input('시간 선택')
    st.write(my_time)
    st.write(my_time.strftime('%H:%M'))

    # 10. 색깔 입력 받는 방법
    color = st.color_picker('색을 선택하세요')
    st.write(color)


if __name__ == '__main__':
    main()