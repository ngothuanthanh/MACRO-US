
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ Excel
file_path = "macro_data.xlsx"  # đổi thành đúng tên file bạn upload
sheet_names = pd.ExcelFile(file_path).sheet_names

st.title("Dashboard Theo Dõi Macro – Việt Nam")

# Lặp qua tất cả sheet
for sheet in sheet_names:
    try:
        df = pd.read_excel(file_path, sheet_name=sheet)

        # Kiểm tra có cột 'Date' và 'Value' hay không
        if 'Date' in df.columns and 'Value' in df.columns:
            df = df.sort_values('Date')
            st.subheader(f"{sheet}")
            fig, ax = plt.subplots()
            ax.plot(df['Date'], df['Value'])
            ax.set_xlabel("Date")
            ax.set_ylabel("Value")
            st.pyplot(fig)
    except Exception as e:
        st.warning(f"Không đọc được sheet {sheet}: {e}")
