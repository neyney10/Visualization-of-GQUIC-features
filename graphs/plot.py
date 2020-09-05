import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio
import numpy as np
import os
import random


def scatter_plot_plottly(packets, col1, col2,colors,colorValues):
    pd.options.plotting.backend = "plotly"
    print('['+col2+']')

    fig = packets.plot.scatter(x=col1, y=col2)
    fig.update_traces(marker=dict(size=6,
                                  color=colors,
                                  colorscale=colorValues),
                      selector=dict(mode='markers'))
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='rgba(55,55,55,0.5)')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='rgba(55,55,55,0.5)')

    fig.update_layout(
        xaxis_title="Time (seconds)",
        font=dict(
            size=22
        )
    )
    # fig.show()
    fig.write_image('images/img3_' + col2 + '.png', format="png", width=1440, height=700,
                    scale=1.2)  # use this to save instead of display


def scatter_plot_by_session(session_packets, col1, col2):
    title = session_packets[0]
    session_packets = session_packets[1]
    pd.options.plotting.backend = "plotly"
    print('[' + col2 + ']')

    fig = session_packets.plot.line(x=col1, y=col2)
    fig.update_traces(marker=dict(size=6,
                                  color='rgb(0,0,255)'),
                      selector=dict(mode='scatter'),mode='markers')
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='rgba(55,55,55,0.5)')
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='rgba(55,55,55,0.5)')

    fig.update_layout(title='Session id : '+title,
        xaxis_title="Time (seconds)",
        font=dict(
            size=22
        )
    )
    # fig.show()
    fig.write_image('images/img3_' + col2 + '.png', format="png", width=1440, height=700,
                    scale=1.2)  # use this to save instead of display





