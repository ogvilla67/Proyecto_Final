#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.graph_objects as go
import numpy as np
import plotly.offline as py                               # para visualizar plots de plotly offline
# Inicializar modalidad offline para visualizar plots, sin conexion a internet y sin generar link de plot
py.offline.init_notebook_mode(connected=False)


# In[2]:


def g_boxplot_varios(p0_data):
    """
    :param p0_data: DataFrame : Data frame con 3 columnas con datos numericos, 1 columna por boxplot
    :return:
    debugging
    p0_data = pd.DataFrame({'var1': list(np.random.normal(0,1,12)),
                            'var2': list(np.random.normal(0,1,12)),
                            'var3': list(np.random.normal(0,1,12))})
    """

    x_data = list(p0_data.columns)
    y_data = [p0_data.iloc[:, i]/max(p0_data.iloc[:, i]) for i in range(0, len(list(p0_data.columns)))]

    fig = go.Figure()

    for xd, yd in zip(x_data, y_data):
        q1 = yd.quantile(0.25)
        q3 = yd.quantile(0.75)
        iqr = q3 - q1
        out_yd = list(yd[(yd < (q1 - 1.5 * iqr)) | (yd > (q3 + 1.5 * iqr))].index)

        fig.add_trace(go.Box(y=yd, name=xd, boxpoints='all', jitter=0.5, whiskerwidth=0.5, marker_size=7,
                             line_width=1, boxmean=True, selectedpoints=out_yd))

    fig.update_layout(title='Visualizacion de todas las variables (Normalizadas)',
                      yaxis=dict(autorange=True, showgrid=True, dtick=5,
                                 gridcolor='rgb(255, 255, 255)', gridwidth=1),
                      margin=dict(l=40, r=30, b=80, t=100),
                      showlegend=False)

    fig.update_yaxes(hoverformat='.2f')

    # Mostrar figura
    # fig.show()

    return fig


# In[ ]:




