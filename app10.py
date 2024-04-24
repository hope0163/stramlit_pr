# 스트림릿의 내장 차트 함수와 유명한 라이브러리인 plotly 차트
# plotly => https://plotly.com/python/

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def main():
    # 스트림릿에서 제공해 주는 차트
    # line_chart, area_chart

    df1 = pd.read_csv('./data/lang_data.csv')
    print(df1)
    
    column_list = df1.columns[1 : ]
    choice_list = st.multiselect('언어를 선택하세요.' , column_list)

    if len(choice_list) != 0:
        df_choice = df1[choice_list]
        st.dataframe(df_choice)
        
        st.line_chart(df_choice)            # line_chart는 streamlit에서 제공하는 차트이므로 따로 plt.figure()로 영역을 잡아주지 않아도 된다. / 선으로 그래프 표시

        st.area_chart(df_choice)            # 영역을 표시해줌     

    

    df2 = pd.read_csv('./data/iris.csv')
    # 스트림릿이 제공하는 bar_chart
    df_iris = df2.iloc[: , 0:-2+1]

    st.bar_chart(df_iris)



    df3 = pd.read_csv('./data/location.csv', index_col=0)     # 위도, 경도 데이터가 있는 csv파일
    print(df3)
    st.map(df3)                                               # st.map() 지도를 불러오기


    df4 = pd.read_csv('./data/prog_languages_data.csv', index_col=0)

    # plotly 의 pie 차트
    # pie차트는 비율을 한눈에 알고 싶을 때 사용

    fig1 = px.pie(data_frame=df4, names='lang', values='Sum', title='각 언어별 파이차트')  # plotly.express 라이브러리에 pie()함수 사용 
                                                                #data_frame=데이터프레임명 , names=표시할 컬럼이름 , values= 표시할 컬럼 값 , title= 차트 이름
    st.plotly_chart(fig1)                   # plotly 라이브러리에 차트함수를 가져오기 때문에 streamlit에서 표시하려면 st.plotly_chart() 함수를 써줘야함.

    # plotly의 bar 차트
    print(df4.sort_values('Sum'))

    df_sorted = df4.sort_values('Sum')

    fig2 = px.bar(data_frame=df_sorted, x='lang', y='Sum')
    st.plotly_chart(fig2)


    df_sorted2 = df4.sort_values('Sum', ascending=False)

    fig3 = px.bar(data_frame=df_sorted2, x='lang', y='Sum')
    st.plotly_chart(fig3)


if __name__ == '__main__':
    main()