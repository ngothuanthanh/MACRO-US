import streamlit as st
import pandas as pd

# File chứa dữ liệu
FILE_PATH = "macro_us_data_cleaned_v2.xlsx"  # hoặc macro_us_data_cleaned.xlsx nếu bạn đang dùng bản đó

# Lấy danh sách sheet
@st.cache_data
def load_sheet_names():
    return pd.ExcelFile(FILE_PATH).sheet_names

# Đọc dữ liệu từ từng sheet
@st.cache_data
def load_data(sheet_name):
    df = pd.read_excel(FILE_PATH, sheet_name=sheet_name)
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    return df

# Giao diện
st.title("📊 Macro Dashboard – Multi-Chart View")

sheet_names = load_sheet_names()

# Tùy chọn lọc sheet (nếu cần)
selected_sheets = st.multiselect("Chọn các tài sản để hiển thị", sheet_names, default=sheet_names)

# Vòng lặp qua từng sheet đã chọn
for sheet in selected_sheets:
    st.subheader(f"📈 {sheet}")
    df = load_data(sheet)
    st.line_chart(df.set_index('date')['value'])
