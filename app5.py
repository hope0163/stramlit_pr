import streamlit as st

# 이미지 / 동영상 / 음악파일을 화면에 보여주는 방법

# 이미지 처리를 위한 라이브러리
from PIL import Image

def main():
    # 1. 저장되어있는 이미지 파일을 화면에 표시하는 방법
    img = Image.open('./data/image_03.jpg')
    st.image(img)
    st.image(img, width=500) # width= 가로폭 조절, 세로는 자동으로 조절됨
    st.image(img, use_column_width=True) # use_column_width=True를 해주면 자동으로 폭을 맞춰줌

    # 2. 인터넷상에 있는 이미지를 화면에 표시하는 방법
    # 인터넷상에 이미지 : URL 이 있다!
    st.image('https://i.imgur.com/QgWbK9D.gif')

    # 동영상 파일을 화면에 표시
    video_file = open('./data/video1.mp4', 'rb') # 비디오파일 불러오기
    st.video(video_file, loop=True, start_time=True)

    # 오디오 파일
    audio_file = open('./data/song.mp3', 'rb')
    st.audio(audio_file.read(), format='audio/mp3')
    
if __name__ == '__main__':
    main()