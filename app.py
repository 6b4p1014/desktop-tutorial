# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:35:06 2026

@author: user
"""

import streamlit as st

# --- 網頁基礎設定 ---
st.set_page_config(
    page_title="Peter Tsai | 個人簡歷 & 南台資訊",
    page_icon="💼",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- 隱藏 Streamlit 預設樣式（提升高質感 Vibe） ---
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stButton>button {
        border-radius: 20px;
        background-color: #1E3A8A;
        color: white;
        border: none;
        padding: 10px 24px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #3B82F6;
        color: white;
        transform: scale(1.05);
    }
    </style>
"""
st.markdown(hide_style, unsafe_html=True)

# --- 側邊欄：聯絡資訊 (Sidebar) ---
with st.sidebar:
    st.markdown("## 聯絡資訊 \n---")
    st.markdown("### 📞 電話")
    st.markdown("[06-253-3131](tel:062533131)")
    
    st.markdown("### ✉️ 電子郵件")
    st.markdown("[6B4P1014@stust.edu.tw](mailto:6B4P1014@stust.edu.tw)")
    
    st.markdown("### 🌐 社群連結")
    st.link_button("🌐 Facebook 專頁", "https://www.facebook.com/keepbusytsai")
    
    st.write("")
    st.caption("© 2026 Peter Tsai. All rights reserved.")

# --- 主頁面：個人簡歷 ---
st.title("👨‍💻 Peter Tsai")
st.subheader("南台資訊有限公司 | 職稱：學生")

st.markdown("""
> **「持續忙碌，持續卓越。用程式碼與創新邏輯，為企業打造下一世代的數位藍圖。」**
""")

st.write("")
st.write("")

# --- 公司宣傳標語 ---
st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>💡 企業核心與宣傳標語</h2>", unsafe_html=True)
st.markdown("<h3 style='text-align: center; font-style: italic; color: #4B5563;'>「連結數據，驅動未來；南台資訊，您最信賴的數位轉型夥伴。」</h3>", unsafe_html=True)
st.write("")

# --- 常見服務項目 (以美觀的卡片/欄位呈現) ---
st.markdown("### 🛠️ 專業服務項目 (Services)")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("#### 🌐 響應式網頁開發")
        st.write("量身打造高質感、跨平台的企業官網、電商系統與 Web App，兼顧 SEO 與流暢的使用者體驗。")

    with st.container(border=True):
        st.markdown("#### ☁️ 雲端架構與系統整合")
        st.write("提供 AWS / GCP 雲端部署與維護，協助企業架構優化，打造高可用性且安全的系統環境。")

with col2:
    with st.container(border=True):
        st.markdown("#### 📊 數據分析與 AI 應用")
        st.write("自動化數據採集（爬蟲）、資料視覺化分析，並導入 AI 模型提升企業決策效率。")

    with st.container(border=True):
        st.markdown("#### 🔒 網路安全與維護")
        st.write("全方位的資訊安全檢測、伺服器定期備份與即時監控，確保企業資產萬無一失。")

# --- 頁尾互動 ---
st.write("")
st.markdown("---")
st.markdown("<center><b>對我們的服務感興趣？歡迎點擊左側聯絡方式，或直接透過 Facebook 與我聯繫！</b></center>", unsafe_html=True)