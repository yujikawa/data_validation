import streamlit as st
import pandas as pd

url = 'https://ckan.open-governmentdata.org/dataset/aad66771-0e86-4d38-b08e-7b74d31f442e/resource/111b9476-bc80-4700-9551-3ba8a4ffcebc/download/401005_kitakyushu_covid19_patients.csv'
data = pd.read_csv(url, encoding='cp932')

st.markdown('# データ一覧')
st.dataframe(data)

st.markdown('# 欠損値の確認')
columns = list(data.columns)

selected = st.selectbox(label='列名を選択してください', options=columns)
selected_data = data[data[selected].isna()]
unknown_count = len(selected_data)

if unknown_count == 0:
    st.markdown(f'### {selected} 列には欠損値はありません')
else:
    st.markdown(f'### {selected} 列には{unknown_count}件の欠損値がありました')
    st.dataframe(selected_data)
