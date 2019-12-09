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
    # Generate the x values
    xVal = []
    xVal.extend(barDict.keys())
    rGone = False
    if "r" in xVal:
        xVal.remove("r")
        rGone = True
    xVal.sort(key=lambda x: (int(x[-1]), x[0]))
    if rGone:
        xVal.append("r")
    # Generate the y values
    yVal = []
    for pitch in xVal:
        yVal.append(barDict[pitch])
    # Generate an empty figure
    fig = go.Figure()
    # Adding a gradient colored bar chart
    fig.add_trace(go.Bar(
        x=xVal,
        y=yVal,
        marker=dict(
            cmax=len(xVal)-1,
            cmin=0,
            color=list(range(len(xVal))),
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

def makeScatterChart(song, WAVDIR, songName):
    '''
    Requires: song is a list of tuples, WAVDIR is the directory for wav files, \
              songName is name of song generated
    Modifies: nothing
    Effects:  creates a scatter chart representing the song in synthesia style
    '''
    # All notes ranging from a2 to g#6
    notes = ['a0',
             'a2','a#2','b2','c2','c#2','d2','d#2','e2','f2','f#2','g2','g#2',
             'a3','a#3','b3','c3','c#3','d3','d#3','e3','f3','f#3','g3','g#3',
             'a4','a#4','b4','c4','c#4','d4','d#4','e4','f4','f#4','g4','g#4',
             'a5','a#5','b5','c5','c#5','d5','d#5','e5','f5','f#5','g5','g#5',
             'a6','a#6','b6','c6','c#6','d6','d#6','e6','f6','f#6','g6','g#6',
             'r']
    # Generate the x values: the corresponding barstamp
    xVal = []
    cumulativeBar = 0.0
    yVal = []
    for note in song:
        xVal.append(cumulativeBar)
        cumulativeBar += (1.0 / note[1]) # longer notes have larger values
        # Generate the y values: the note at a given bar
        yVal.append(note[0])

    # Generate an empty figure
    fig = go.Figure()
    # Add in x and y values
    fig.add_trace(go.Scatter(x=xVal,y=yVal,mode="markers"))
    # Update figure layout
    fig.update_layout(
        title=("Number of occurances of notes used in " + songName + ".wav")
    )
    # Write figure to a html file
    fig.write_html(WAVDIR + songName + 'Data.html', auto_open=True)
