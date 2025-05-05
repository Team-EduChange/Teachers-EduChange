import streamlit as st
import pandas as pd
from datetime import datetime

# 페이지 기본 설정
st.set_page_config(
    page_title="서비스 이전 안내",
    page_icon="📢",
    layout="centered"
)

# CSS 스타일 적용
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #333333;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #333;
        margin-top: 2rem;
    }
    .date-info {
        font-size: 1.2rem;
        color: #555;
        font-weight: 500;
        margin-top: 0.5rem;
    }
    .highlight {
        background-color: #FFFDE7;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #FBC02D;
        margin: 1rem 0;
    }
    .promotion {
        background-color: #FFFDE7;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #FBC02D;
        margin: 1rem 0;
    }
    .feature {
        background-color: #F5F5F5;
        padding: 0.8rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        font-style: italic;
        color: #555;
    }
    .divider {
        margin: 1.5rem 0;
        border-top: 1px solid #C8E6C9;
    }
    .new-address {
        background-color: #E8F5E9;
        border: 2px solid #2E7D32;
        border-radius: 10px;
        padding: 1rem;
        margin: 1.5rem 0;
        text-align: center;
        font-size: 1.4rem;
        font-weight: bold;
        color: #2E7D32;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .table-container {
        margin: 1.5rem 0;
        border: 1px solid #C8E6C9;
        border-radius: 8px;
        padding: 1rem;
        background-color: #F1F8E9;
    }
    .bullet {
        color: #2E7D32;
        font-size: 1.2rem;
        margin-right: 8px;
    }
</style>
""", unsafe_allow_html=True)

# 헤더 섹션
st.markdown("<h1 class='main-header'>📢 서비스 이전 안내 📢</h1>", unsafe_allow_html=True)
st.markdown("안녕하세요, 선생님들! 👋", unsafe_allow_html=True)
st.markdown("2025년 5월 19일(월)부터 더욱 향상된 모습으로 새로운 웹사이트에서 운영됩니다.")

# 새로운 웹서비스 안내 섹션
st.markdown("<h2 class='sub-header'>새로운 웹서비스 안내</h2>", unsafe_allow_html=True)
st.markdown("<div class='date-info'>오픈 일자: 2025년 5월 19일(월)</div>", unsafe_allow_html=True)

# 새로운 주소를 눈에 띄게 강조
st.markdown("<div class='new-address'>🌐 새로운 주소: <a href='http://www.teacher-logbook.kr'>www.teacher-logbook.kr</a></div>", unsafe_allow_html=True)

# 프로모션 섹션
st.markdown("<h2 class='sub-header'>리오픈 기념 한정 프로모션</h2>", unsafe_allow_html=True)
st.markdown("<div class='promotion'><b>PDF 파일당 💎20 → 💎5 (75% 할인)</b><br>2025년 5월 19일(월) ~ 5월 31일(토)</div>", unsafe_allow_html=True)

# 서비스 변경사항 섹션
st.markdown("<h2 class='sub-header'>서비스 주요 변경사항</h2>", unsafe_allow_html=True)
st.markdown("<div class='highlight'>서비스명 변경: <b>'칼퇴근' → '쌤기부'</b></div>", unsafe_allow_html=True)

# 향상된 서비스 섹션
st.markdown("<h2 class='sub-header'>향상된 서비스</h2>", unsafe_allow_html=True)
features = [
    "여러 학생을 동시에 업로드",
    "더욱 고품질의 문장 생성 능력 향상",
    "생성한 문장을 저장하고 한눈에 볼 수 있는 표 기능 제공",
    "생활기록부 매뉴얼 유의사항을 반영한 결과 생성"
]

for feature in features:
    st.markdown(f"<div class='feature'><span class='bullet'>•</span>{feature}</div>", unsafe_allow_html=True)

# 서비스 비교표를 바로 표시 (제목 스타일 변경)
st.markdown("<h2 class='sub-header'>서비스 비교</h2>", unsafe_allow_html=True)
data = {
    "기능": ["동시 업로드", "저장 기능", "매뉴얼 반영"],
    "칼퇴근 (기존)": ["❌", "❌", "❌"],
    "쌤기부 (신규)": ["✅", "✅", "✅"]
}
    
comparison_df = pd.DataFrame(data)
st.table(comparison_df.set_index("기능"))

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# 푸터
st.markdown("<div class='footer'>더욱 향상된 서비스로 여러분을 기다리겠습니다.<br>새로운 '쌤기부'에서 만나요!<br><br>감사합니다. 😊</div>", unsafe_allow_html=True) 