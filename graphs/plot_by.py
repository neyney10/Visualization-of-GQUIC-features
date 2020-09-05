from coloring_methods import ColorByIP, ColorByTime
from plots import ScatterPlotFactory, LinePlotFactory

def plot_by_time(packets, fields, times):
    coloringMethod = ColorByTime(times)

    for field in fields:
        spFactory = ScatterPlotFactory(field + ' By time', 'Time (seconds)', field, markerSize=6)
        plot = spFactory.createPlot(packets,'Time', field, coloringMethod)
        plot.exportAsImage(filepath='img_'+field)


def plot_by_ip(packets, fields, IP):
    coloringMethod = ColorByIP(IP)

    for field in fields:
        spFactory = ScatterPlotFactory(field + ' By time', 'Time (seconds)', field, markerSize=6)
        plot = spFactory.createPlot(packets,'Time', field, coloringMethod)
        plot.exportAsImage(filepath='img_'+field)