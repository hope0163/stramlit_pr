import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def main():
    st.title('차트 그리기')

    df = pd.read_csv('./data/iris.csv')

    st.dataframe(df)

    # sepal_length 와 sepal_width 의 관계를 차트로 나타내시오.
    fig1 = plt.figure()                                        # 차트 범위를 잡아주고 변수에 저장
    plt.scatter(data=df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length vs Width')
    st.pyplot(fig1)                                            # st.pyplot() 로 차트 표시


    fig2 = plt.figure()
    sb.scatterplot(data=df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length vs Width')
    st.pyplot(fig2)
    

    fig3 = plt.figure()
    sb.regplot(data=df, x='sepal_length', y='sepal_width')
    plt.title('Sepal Length vs Width')
    st.pyplot(fig3)


    # sepal_length 로 히스토그램을 그린다.
    # bins의 갯수는 20개로
    fig4 = plt.figure()
    plt.hist(data=df, x='sepal_length', bins=20, rwidth=0.9)
    plt.title('Histogram')
    plt.xlabel('sepal_length')
    plt.ylabel('count')
    st.pyplot(fig4)


    # sepal_length 히스토그램을 그려라
    # bins의 갯수를 10개와 20개로
    # 두개의 차트를 수평으로 보여주세요
    

    fig5 = plt.figure(figsize=(10,4))
    plt.subplot(1, 2, 1)
    plt.hist(data=df, x='sepal_length', bins=10, rwidth=0.9)
    plt.title('Histogram 10 bins')
    plt.xlabel('sepal_length')
    plt.ylabel('count')

    plt.subplot(1, 2, 2)
    plt.hist(data=df, x='sepal_length', bins=20, rwidth=0.9)
    plt.title('Histogram 20 bins')
    plt.xlabel('sepal_length')
    plt.ylabel('count')

    st.pyplot(fig5)

    # 판다스의 데이터프레임의 차트도 그릴 수 있다.
    # species 는 각각 몇개인지 나타내시오.

    print(df['species'].value_counts())

    # 위의 결과를 bar차트로 나타내시오.
    fig6 = plt.figure()
    df['species'].value_counts().plot(kind='bar')
    st.pyplot(fig6)

    # sepal_length 컬럼을 히스토그램으로 나타내시오.
    fig7 = plt.figure()
    df['sepal_length'].hist()
    st.pyplot(fig7)

    # df의 상관계수를 구해서, 차트로 표시!
    choice_columns = st.multiselect("컬럼을 선택하세요" , df.columns)
    if len(choice_columns) != 0:
        if 'species' in choice_columns:
            st.warning('species 컬럼은 숫자 데이터가 아니기 때문에 상관계수 분석에서 제외됩니다.')
        df_corr = df[choice_columns].corr(numeric_only=True)
        fig9 = plt.figure()
        sb.heatmap(df_corr, annot=True)
        st.pyplot(fig9)
    else:
        pass



        # 요약
        # 차트를 그리기 위해선 plt.figure() 로 영역을 잡아주고 변수에 저장
        # 마지막줄에 st.pyplot(변수명) 을 써줘야 차트 표시


if __name__ == '__main__':
    main()