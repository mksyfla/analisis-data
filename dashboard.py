import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

monthly_sum = pd.read_csv("data/monthly_sum.csv")
season_sum = pd.read_csv("data/season_sum.csv")

st.header('Bike Sharing :sparkles:')

st.subheader('pengguna perbulan')
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(monthly_sum["yr_mnth"].astype(str), monthly_sum["cnt"], marker='o', linestyle='-')
ax.set_title("Jumlah pengguna Bike Sharing setiap bulannya")
ax.set_xlabel('Bulan')
ax.set_ylabel('Jumlah Pengguna')
ax.tick_params(axis='x', rotation=45)
ax.grid(True)
plt.tight_layout()
plt.show()

st.pyplot(fig)

st.subheader('pengguna permusim')
fig, ax = plt.subplots(figsize=(10,5))
ax.bar(season_sum["season"], season_sum["cnt"])
ax.set_title("Pengguna Bike Sharing setiap musim")
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Pengguna')
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()

st.pyplot(fig)
