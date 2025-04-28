import streamlit as st
import numpy as np
import plotly.graph_objs as go

# Tytuł aplikacji
st.title("Wykres funkcji liniowej: f(x) = ax + b")

# Suwaki dla parametrów a i b
a = st.slider('Wybierz współczynnik a:', -10.0, 10.0, 1.0, step=0.1)
b = st.slider('Wybierz współczynnik b:', -20.0, 20.0, 0.0, step=0.1)

# Przygotowanie danych
x = np.linspace(-10, 10, 400)
y = a * x + b

# Tworzenie wykresu
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'f(x) = {a}x + {b}'))

# Dodanie osi x i y
fig.add_shape(type="line", x0=-10, x1=10, y0=0, y1=0,
              line=dict(color="black", width=2))  # Oś X
fig.add_shape(type="line", x0=0, x1=0, y0=-50, y1=50,
              line=dict(color="black", width=2))  # Oś Y

# Dodanie punktów przecięcia z osiami
fig.add_trace(go.Scatter(x=[-b/a] if a != 0 else [], y=[0],
                         mode='markers', marker=dict(color='red', size=10),
                         name='Miejsce zerowe'))
fig.add_trace(go.Scatter(x=[0], y=[b],
                         mode='markers', marker=dict(color='blue', size=10),
                         name='Przecięcie z osią Y'))

# Aktualizacja wyglądu wykresu
fig.update_layout(title=f'Wykres funkcji: f(x) = {a}x + {b}',
                  xaxis_title='x',
                  yaxis_title='f(x)',
                  template='plotly_white',
                  showlegend=True,
                  xaxis=dict(zeroline=False, showgrid=True),
                  yaxis=dict(zeroline=False, showgrid=True))

# Wyświetlenie wykresu
st.plotly_chart(fig)
