import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 🧠 앱 제목
# -----------------------------
st.set_page_config(page_title="이차함수 학습 앱", page_icon="📈")
st.title("📈 이차함수 시각화 앱")
st.write("이차함수의 일반형 **y = a(x - p)² + q** 에서 a, p, q 값을 조절해 그래프가 어떻게 변하는지 확인해보세요!")

# -----------------------------
# 🎚️ 슬라이더로 매개변수 조절
# -----------------------------
st.sidebar.header("⚙️ 매개변수 설정")

a = st.sidebar.slider("a (그래프의 방향 및 폭)", -5.0, 5.0, 1.0, step=0.1)
p = st.sidebar.slider("p (좌우 이동)", -10.0, 10.0, 0.0, step=0.1)
q = st.sidebar.slider("q (상하 이동)", -10.0, 10.0, 0.0, step=0.1)

# -----------------------------
# 📊 그래프 계산
# -----------------------------
x = np.linspace(-10, 10, 400)
y = a * (x - p) ** 2 + q

# -----------------------------
# 🎨 그래프 그리기
# -----------------------------
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, y, color="dodgerblue", linewidth=2, label=f"y = {a:.1f}(x - {p:.1f})² + {q:.1f}")
ax.axhline(0, color="gray", linewidth=0.8)
ax.axvline(0, color="gray", linewidth=0.8)
ax.scatter(p, q, color="red", label="꼭짓점 (p, q)")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.6)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("이차함수 그래프")

st.pyplot(fig)

# -----------------------------
# 🧩 수식 설명
# -----------------------------
st.markdown("""
### 🧮 그래프 해석
- **a** 값이 양수면 위로 열린 포물선, 음수면 아래로 열린 포물선입니다.  
- **|a|** 값이 커질수록 그래프가 **좁아지고**, 작아질수록 **넓어집니다.**  
- **p** 값은 그래프를 **좌우로 이동**시킵니다.  
- **q** 값은 그래프를 **위아래로 이동**시킵니다.  
- 꼭짓점은 항상 **(p, q)** 에 있습니다.
""")
