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
    # Generate an empty figure
    fig = go.Figure()
    # Adding a gradient colored bar chart
    fig.add_trace(go.Bar(
        x=xAxis,
        y=yAxis,
        marker=dict(
            cmax=len(xAxis)-1,
            cmin=0,
            color=list(range(len(xAxis))),
            colorscale=['#ffcb05', '#f2c209', '#e4ba0c', '#d7b210', '#caa914', '#bda117', '#b1991b', '#a4901e', '#978822', '#8b8025', '#7e7829', '#72702c', '#666830', '#5a6133', '#4d5936', '#41513a', '#35493d', '#284141', '#1c3944', '#0e3048', '#00274c']
        )
        )
    )
    # Update figure layout
    fig.update_layout(
        title=("Number of occurances of notes used in " + songName + ".wav")
    )
    # Write figure to a html file
    fig.write_html(WAVDIR + songName + 'Data.html', auto_open=True)
