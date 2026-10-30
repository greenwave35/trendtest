import streamlit as st# 페이지 기본 설정

st.set_page_config(page_title="Trend Catcher",    page_icon="📊",    layout="centered")

# 첫 화면
st.title("Trend Catcher")
st.subheader("유튜브 트렌드 분석 앱")
st.write("관심 있는 키워드의 유튜브 트렌드를 분석합니다.")
st.info("현재는 2주차 화면 테스트 버전입니다.")

# 버튼
if st.button("START", use_container_width=True):    
    st.success("시작 버튼이 정상적으로 작동합니다!")
    st.caption("MindFirst Coding Lab | 2026")
