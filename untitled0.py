# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bJvDCGisWydaRO8vJEMbfe7zmHjkNorf
"""

pip install streamlit

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tạo bảng dữ liệu cho các mức độ yêu thích giảng viên
data = {
    "Mức độ yêu thích": ["Không thích", "Ít thích", "Bình thường", "Thích"],
    "Số lượng sinh viên": [39, 37, 20, 4]
}

# Tạo dataframe
df = pd.DataFrame(data)

# Hiển thị bảng dữ liệu trên ứng dụng Streamlit
st.write("### Bảng dữ liệu mức độ yêu thích giảng viên")
st.dataframe(df)

# Vẽ biểu đồ cột bằng matplotlib
fig, ax = plt.subplots()
ax.bar(df["Mức độ yêu thích"], df["Số lượng sinh viên"], color=["red", "orange", "yellow", "green"])
ax.set_xlabel("Mức độ yêu thích")
ax.set_ylabel("Số lượng sinh viên")
ax.set_title("Biểu đồ mức độ yêu thích giảng viên")
st.pyplot(fig)

# Hoặc sử dụng biểu đồ cột của Streamlit
st.write("### Biểu đồ cột - Mức độ yêu thích giảng viên")
st.bar_chart(df.set_index("Mức độ yêu thích"))