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

# Dodanie osi x i y z grotami strzałek
fig.add_annotation(x=10.5, y=0, ax=10, ay=0,
                   xref='x', yref='y', axref='x', ayref='y',
                   showarrow=True, arrowhead=2, arrowsize=1.5, arrowwidth=2, arrowcolor="black")
fig.add_annotation(x=0, y=55, ax=0, ay=50,
                   xref='x', yref='y', axref='x', ayref='y',
                   showarrow=True, arrowhead=2, arrowsize=1.5, arrowwidth=2, arrowcolor="black")

# Dodanie osi bez grotów (podstawowe linie)
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

# Dodanie podpisów przy grotach osi
fig.add_annotation(x=11, y=0, text="x", showarrow=False,
                   xanchor='left', yanchor='bottom', font=dict(size=14))
fig.add_annotation(x=0, y=57, text="y", showarrow=False,
                   xanchor='left', yanchor='bottom', font=dict(size=14))

# Aktualizacja wyglądu wykresu
fig.update_layout(title=f'Wykres funkcji: f(x) = {a}x + {b}',
                  xaxis_title=None,
                  yaxis_title=None,
                  template='plotly_white',
                  showlegend=True,
                  xaxis=dict(zeroline=False, showgrid=True, range=[-11, 11]),
                  yaxis=dict(zeroline=False, showgrid=True, range=[-55, 60]),
                  margin=dict(l=40, r=40, t=80, b=40))

# Wyświetlenie wykresu
st.plotly_chart(fig)
