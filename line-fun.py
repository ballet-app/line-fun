import numpy as np
import plotly.graph_objs as go
import ipywidgets as widgets
from IPython.display import display

# Przygotuj dane początkowe
x = np.linspace(-10, 10, 400)
y = 1 * x + 0

# Utwórz początkowy wykres
fig = go.FigureWidget()
fig.add_scatter(x=x, y=y, mode='lines')
fig.update_layout(title='Wykres funkcji liniowej: f(x) = ax + b',
                  xaxis_title='x',
                  yaxis_title='f(x)',
                  template='plotly_white')

# Funkcja aktualizująca dane wykresu
def update_plot(a, b):
    with fig.batch_update():
        fig.data[0].y = a * x + b
        fig.layout.title = f'Wykres funkcji liniowej: f(x) = {a}x + {b}'

# Suwaki
a_slider = widgets.FloatSlider(value=1.0, min=-10.0, max=10.0, step=0.1, description='a:')
b_slider = widgets.FloatSlider(value=0.0, min=-20.0, max=20.0, step=0.1, description='b:')

# Połącz suwaki z funkcją aktualizującą
ui = widgets.VBox([a_slider, b_slider])
out = widgets.interactive_output(update_plot, {'a': a_slider, 'b': b_slider})

# Wyświetl
display(ui, fig, out)
