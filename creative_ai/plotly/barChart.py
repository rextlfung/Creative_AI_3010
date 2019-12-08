import plotly.graph_objects as go
import numpy

def makeBarChart(song, WAVDIR, songName):
    '''
    Requires: song is a list of tuples, WAVDIR is the directory for wav files, \
              songName is name of song generated
    Modifies: nothing
    Effects:  creates a bar chart consisting of notes in the song and their
              corresponding frequency
    '''
    # Generate a dictionary of notes and their corresponding counts:
    barDict = {}
    for note in song:
        if note[0] in barDict:
            barDict[note[0]] += 1
        else:
            barDict[note[0]] = 1
    # Generate the xAxis values
    xAxis = []
    xAxis.extend(barDict.keys())
    rGone = False
    if "r" in xAxis:
        xAxis.remove("r")
        rGone = True
    xAxis.sort(key=lambda x: (int(x[-1]), x[0]))
    if rGone:
        xAxis.append("r")
    # Generate the yAxis values
    yAxis = []
    for pitch in xAxis:
        yAxis.append(barDict[pitch])
    # Generate a figure
    fig = go.Figure(data=go.Bar(x=xAxis, y=yAxis))
    # Update figure layout (ADDME)

    # Write figure to a html file
    fig.write_html(WAVDIR + songName + 'Data.html', auto_open=True)
