import streamlit as st
import numpy as np
import plotly.graph_objs as go

# Tytuł aplikacji
st.title("Wykres funkcji liniowej: f(x) = ax + b")

# Suwaki dla parametrów a i b
a = st.slider('Wybierz współczynnik a:', -10.0, 10.0, 1.0, step=0.1)
b = st.slider('Wybierz współczynnik b:', -20.0, 20.0, 0.0, step=0.1)

# Dane wykresu
x = np.linspace(-10, 10, 400)
y = a * x + b

# Tworzenie wykresu
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'f(x) = {a}x + {b}'))
fig.update_layout(title=f'Wykres funkcji: f(x) = {a}x + {b}',
                  xaxis_title='x',
                  yaxis_title='f(x)',
                  template='plotly_white',
                  showlegend=False)

# Wyświetlenie wykresu
st.plotly_chart(fig)
