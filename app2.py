import streamlit as st

def main() :
    st.text('웹 대시보드 개발하기')

    name = '홍길동'

    print(f'제 이름은 {name}입니다.')

    st.text(f'제 이름은 {name}입니다.')

    st.header('이 영역은 헤더')

    st.subheader('서브 헤더')

    st.success('작업이 성공했을때 사용하자.')
    st.warning('경고 문구를 보여주고 싶을때 사용하자.')
    st.info('정보를 보여주고 싶을때 사용하자.')
    st.error('문제가 있다는걸 알릴때 사용하자.')

if __name__=="__main__":
    main()