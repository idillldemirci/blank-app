import streamlit as st
import math

st.title('İkinci Dereceden Denklemler Çözücü')

a = st.number_input("a katsayısını giriniz:", value=1)
b = st.number_input("b katsayısını giriniz:", value=1)
c = st.number_input("c katsayısını giriniz:", value=1)

denklem = f"{a}x²"
if b != 0:
    denklem += f" + {b}x" if b > 0 else f" - {abs(b)}x"
if c != 0:
    denklem += f" + {c}" if c > 0 else f" - {abs(c)}"
denklem += " = 0"
st.write(f"Girilen denklem: {denklem}")

delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    st.success(f"İki farklı kök var: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x = -b / (2*a)
    st.info(f"Çakışık kök var: x = {x}")
else:
    reel = -b / (2*a)
    sanal = math.sqrt(abs(delta)) / (2*a)
    st.warning(f"Karmaşık kökler var: x1 = {reel} + {sanal}i, x2 = {reel} - {sanal}i")
