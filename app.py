import streamlit as st
import numpy as np
import plotly.graph_objects as go
from model.wing import WingConfig
from model.physics import calcular_tudo

st.set_page_config(page_title="AeroF1", page_icon="🏎️")

st.title("🏎️ AeroF1")
st.subheader("Simulador Aerodinâmico de Asa Simplificada")

st.sidebar.header("Parâmetros da Asa")

# Sliders para o utilizador controlar os parâmetros
angulo = st.sidebar.slider("Ângulo de Ataque (°)", 0.0, 25.0, 5.0)
velocidade = st.sidebar.slider("Velocidade (km/h)", 10.0, 400.0, 100.0)
area = st.sidebar.slider("Área (m²)", 0.1, 10.0, 1.5)
camber = st.sidebar.slider("Curvatura", 0.0, 0.2, 0.05)

# Cria a asa com os valores dos sliders
wing = WingConfig(
    angle_of_attack=angulo,
    velocity=velocidade,
    area=area,
    camber=camber
)

# Calcula os resultados
resultados = calcular_tudo(wing)

st.divider()

# Mostra as métricas principais
col1, col2, col3 = st.columns(3)
col1.metric("Downforce", f"{resultados['downforce']} N")
col2.metric("Drag", f"{resultados['drag']} N")
col3.metric("Eficiência", f"{resultados['eficiencia']}")

st.divider()
st.subheader("📈 Gráficos")

# --- Gráfico 1 — Downforce e Drag vs Ângulo de Ataque ---
angulos = np.linspace(0.1, 25, 100)
downforces_angulo = []
drags_angulo = []

for a in angulos:
    w = WingConfig(angle_of_attack=a, velocity=velocidade, area=area, camber=camber)
    r = calcular_tudo(w)
    downforces_angulo.append(r['downforce'])
    drags_angulo.append(r['drag'])

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=angulos, y=downforces_angulo, name="Downforce", line=dict(color="blue")))
fig1.add_trace(go.Scatter(x=angulos, y=drags_angulo, name="Drag", line=dict(color="red")))
fig1.add_vline(x=angulo, line_dash="dash", line_color="gray", annotation_text="atual")
fig1.update_layout(title="Downforce e Drag vs Ângulo de Ataque", xaxis_title="Ângulo (°)", yaxis_title="Força (N)")
st.plotly_chart(fig1, use_container_width=True)

# --- Gráfico 2 — Downforce e Drag vs Velocidade ---
velocidades = np.linspace(10, 400, 100)
downforces_vel = []
drags_vel = []

for v in velocidades:
    w = WingConfig(angle_of_attack=angulo, velocity=v, area=area, camber=camber)
    r = calcular_tudo(w)
    downforces_vel.append(r['downforce'])
    drags_vel.append(r['drag'])

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=velocidades, y=downforces_vel, name="Downforce", line=dict(color="blue")))
fig2.add_trace(go.Scatter(x=velocidades, y=drags_vel, name="Drag", line=dict(color="red")))
fig2.add_vline(x=velocidade, line_dash="dash", line_color="gray", annotation_text="atual")
fig2.update_layout(title="Downforce e Drag vs Velocidade", xaxis_title="Velocidade (km/h)", yaxis_title="Força (N)")
st.plotly_chart(fig2, use_container_width=True)

# --- Gráfico 3 — Eficiência vs Ângulo de Ataque ---
eficiencias_angulo = []

for a in angulos:
    w = WingConfig(angle_of_attack=a, velocity=velocidade, area=area, camber=camber)
    r = calcular_tudo(w)
    eficiencias_angulo.append(r['eficiencia'])

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=angulos, y=eficiencias_angulo, name="Eficiência", line=dict(color="green")))
fig3.add_vline(x=angulo, line_dash="dash", line_color="gray", annotation_text="atual")
fig3.update_layout(title="Eficiência vs Ângulo de Ataque", xaxis_title="Ângulo (°)", yaxis_title="Eficiência")
st.plotly_chart(fig3, use_container_width=True)