import streamlit as st
import pandas as pd

# Đường dẫn đến file Excel
FILE_PATH = "macro_us_data_cleaned.xlsx"  # hoặc đổi thành macro_us_data_cleaned_v2.xlsx nếu bạn dùng bản chuẩn hóa

# Đọc danh sách sheet
@st.cache_data
def load_sheet_names():
    xls = pd.ExcelFile(FILE_PATH)
    return xls.sheet_names

# Đọc dữ liệu từ một sheet
@st.cache_data
def load_data(sheet_name):
    df = pd.read_excel(FILE_PATH, sheet_name=sheet_name)
    # Đảm bảo kiểu dữ liệu
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    return df

# Giao diện
st.title("📈 Macro Dashboard – US Assets")

sheet_names = load_sheet_names()

# Chọn mã tài sản (sheet)
selected_sheet = st.selectbox("Chọn tài sản", sheet_names)

# Load và hiển thị dữ liệu
data = load_data(selected_sheet)

# Hiển thị bảng dữ liệu
st.subheader(f"Dữ liệu: {selected_sheet}")
st.dataframe(data.tail(10), use_container_width=True)

# Vẽ biểu đồ
st.line_chart(data.set_index('date')['value'])
