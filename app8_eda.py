import streamlit as st
import pandas as pd
def run_eda():
    st.subheader('EDA 화면')

    # iris.csv 파일 읽어와서
    # 여러 컬럼들 선택 가능하도록 하여
    # 선택한 컬럼들만 화면에 보여주고,
    # 상관계수도 보여주도록 개발.
    df = pd.read_csv('./data/iris.csv')
    
    choice_columns = st.multiselect("컬럼을 선택하세요" , df.columns)

    if len(choice_columns) != 0:
        st.info('데이터프레임')
        st.dataframe(df[choice_columns])
        st.info('상관계수')
        st.dataframe(df[choice_columns].corr(numeric_only=True))
        if 'species' in choice_columns:
            st.warning('species 컬럼은 숫자 데이터가 아니기 때문에 상관계수 분석에서 제외됩니다.')
    else:
        pass


