
import plotly.express as plotlyExpress
import numpy as np
import plotly.graph_objects as go
from .coloring_methods import ColorByDefault

colorsArr=['rgb(0,0,255)','rgb(255,0,0)', 'rgb(0,255,0)','rgb(92, 138, 102)','rgb(0,0,0)','rgb(255, 253, 0)']

class ScatterPlotFactory():
    def __init__(self, plotTitle, xTitle, yTitle, markerSize=6, fontSize=22):
        self.markerSize = markerSize
        self.plotTitle = plotTitle
        self.xTitle = xTitle
        self.yTitle = yTitle
        self.fontSize = fontSize

    def createPlot(self, packets, col1, col2, coloringMethod=ColorByDefault()):
        print('Title: '+self.plotTitle + ', Columns: ' + self.xTitle+'|'+self.yTitle + ' ['+col1+'/'+col2+']')

        packetColors, numOfColors = coloringMethod.color(packets)

        fig = plotlyExpress.scatter(data_frame=packets, x=col1, y=col2,
                                    color=np.array(packetColors).astype(str),
                                    color_discrete_sequence=colorsArr[:numOfColors])
        fig.update_traces(marker=dict(size=self.markerSize))
        fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='rgba(55,55,55,0.5)')
        fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='rgba(55,55,55,0.5)')

        fig.update_layout(
            showlegend=False,
            title=self.plotTitle,
            xaxis_title=self.xTitle,
            yaxis_title=self.yTitle,
            font=dict(
                size=self.fontSize
            )
        )

        return Plot(fig)


class LinePlotFactory():
    def __init__(self, plotTitle, xTitle, yTitle, markerSize=12, fontSize=22):
        self.markerSize = markerSize
        self.plotTitle = plotTitle
        self.xTitle = xTitle
        self.yTitle = yTitle
        self.fontSize = fontSize

    def createPlot(self, packets, col1, col2, coloringMethod=ColorByDefault()):
        print('(Line) Title: '+self.plotTitle + ', Columns: ' + self.xTitle+'|'+self.yTitle + ' ['+col1+'/'+col2+']')

        packetColors, numOfColors = coloringMethod.color(packets)

        fig = go.Figure()
        for i in range(numOfColors):
            packetsGroup = packets[packetColors == i]
            firstCol = packetsGroup[col1]
            secondCol = packetsGroup[col2]
            fig.add_trace(go.Scatter(x=firstCol, y=secondCol,
                            mode='lines+markers',
                            name='',
                            connectgaps=True # override default to connect the gaps
                        ))

        fig.update_traces(marker=dict(size=self.markerSize))
        fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='rgba(55,55,55,0.5)')
        fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='rgba(55,55,55,0.5)')

        fig.update_layout(
            showlegend=False,
            title=self.plotTitle,
            xaxis_title=self.xTitle,
            yaxis_title=self.yTitle,
            font=dict(
                size=self.fontSize
            )
        )

        return Plot(fig)


class Plot():
    def __init__(self, plot):
        self.plot = plot

    def exportAsImage(self, filepath, width=1440, height=700, scale=1.2):
        if self.plot:
            self.plot.write_image(filepath + '.png', format="png", width=width, height=height,
                scale=scale)  # use this to save instead of display

    def launchInteractiveView(self):
        if self.plot:
            self.plot.show()

