import streamlit as st
import requests

# Streamlit 설정
st.title("Naver Search Dashboard")
st.write("검색어를 입력하세요:")

# 사용자 입력 받기
query = st.text_input("Search Query")

# API 키 설정 (예: .env 파일 또는 Streamlit secrets에 저장)
API_KEY = st.secrets["API_KEY"]

if query:
    # Vercel에 배포된 Flask 서버의 API 호출
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }



    response = requests.get(f"https://flask-naver-search.vercel.app/search_api?query={query}", headers=headers)

    response = requests.get(f"https://flask-naver-search-omega.vercel.app/search_api?query={query}", headers=headers)

    if response.status_code == 200:
        results = response.json()
        items = results.get('items', [])

        # 검색 결과 표시
        if items:
            for item in items:
                st.markdown(f"**{item['title']}**", unsafe_allow_html=True)
                st.markdown(f"{item['description']}", unsafe_allow_html=True)
                st.markdown(f"[Read more]({item['link']})", unsafe_allow_html=True)
                st.write("---")
        else:
            st.write("검색 결과가 없습니다.")
    else:
        st.write(f"Error: {response.status_code}")

