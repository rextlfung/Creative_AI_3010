import plotly.graph_objects as go
import plotly.figure_factory as ff
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
    # Sort pitches by octave, then pitch
    xVal.sort(key=lambda x: (int(x[-1]), x[0]))
    # Sort sharp (#) pitches
    for i in range(len(xVal) - 1):
        if xVal[i][::2] == xVal[i + 1]:
            temp = xVal[i]
            xVal[i] = xVal[i + 1]
            xVal[i + 1] = temp
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
            colorscale=['#ffcb05', '#f2c309', '#e6bb0c', '#d9b210', '#ccaa13', '#bfa217', '#b39a1a', '#a6921e', '#998921', '#8c8125', '#807929', '#73712c', '#666930', '#596033', '#4d5837', '#40503a', '#33483e', '#264041', '#1a3745', '#0d2f48', '#00274c']
            )
        )
    )
    # Update figure layout
    fig.update_layout(
        title=("Number of occurances of notes used in " + songName + ".wav")
    )
    # Write figure to a html file
    fig.write_html(WAVDIR + songName + 'BarChart.html', auto_open=True)

def makeSynthesia(song, WAVDIR, songName):
    '''
    Requires: song is a list of tuples, WAVDIR is the directory for wav files, \
              songName is name of song generated
    Modifies: nothing
    Effects:  creates a scatter chart representing the song in synthesia style
    '''
    colorscale = ['#ffcb05', '#fcc906', '#f8c707', '#f5c408', '#f1c209', '#eec00a', '#eabe0b', '#e7bb0c', '#e3b90d', '#e0b70e', '#dcb50f', '#d9b210', '#d5b011', '#d2ae12', '#ceac13', '#cba914', '#c7a715', '#c4a516', '#c0a317', '#bda017', '#b99e18', '#b69c19', '#b29a1a', '#af971b', '#ab951c', '#a8931d', '#a4911e', '#a18e1f', '#9d8c20', '#9a8a21', '#968822', '#938523', '#8f8324', '#8c8125', '#887f26', '#857c27', '#817a28', '#7e7829', '#7a762a', '#77732b', '#73712c', '#706f2d', '#6c6d2e', '#696a2f', '#656830', '#626631', '#5e6432', '#5b6133', '#575f34', '#545d35', '#505b36', '#4d5837', '#495638', '#465439', '#42523a', '#3f4f3a', '#3b4d3b', '#384b3c', '#34493d', '#31463e', '#2d443f', '#2a4240', '#264041', '#233d42', '#1f3b43', '#1c3944', '#183745', '#153446', '#113247', '#0e3048', '#0a2e49', '#072b4a', '#03294b', '#00274c']
    # All notes ranging from a1 to g#6 + kick 'a0' and rest 'r'. Total 73 notes
    notes = ['a0',
             'a1','a#1','b1','c1','c#1','d1','d#1','e1','f1','f#1','g1','g#1',
             'a2','a#2','b2','c2','c#2','d2','d#2','e2','f2','f#2','g2','g#2',
             'a3','a#3','b3','c3','c#3','d3','d#3','e3','f3','f#3','g3','g#3',
             'a4','a#4','b4','c4','c#4','d4','d#4','e4','f4','f#4','g4','g#4',
             'a5','a#5','b5','c5','c#5','d5','d#5','e5','f5','f#5','g5','g#5',
             'a6','a#6','b6','c6','c#6','d6','d#6','e6','f6','f#6','g6','g#6',
             'r']
    # Generate an empty figure
    fig = go.Figure()
    # Update figure layout
    fig.update_layout(
        title=("Synthesia-styled representation of " + songName + ".wav"),
        xaxis=dict(
            tickvals=list(range(len(notes))),
            ticktext=notes,
            autorange=False,
            range=[0,74]
        ),
        yaxis=dict(
            tick0=0,
            dtick=1,
            autorange=False,
            rangemode="nonnegative",
            range=[0,32]
        ),
        autosize=False,
        height=7000,
        width=1700
    )
    # Add in rectangles representative of note durations
    cumulativeBar = 0.0
    for note in song:
        currNote = notes.index(note[0])
        currDur = abs(1.0 / note[1])
        fig.add_shape(
            go.layout.Shape(
                type="rect",
                x0=currNote - 0.3,
                y0=cumulativeBar,
                x1=currNote + 0.3,
                y1=cumulativeBar + currDur,
                line=dict(
                    color=colorscale[currNote],
                    width=0
                ),
                fillcolor=colorscale[currNote],
        ))
        cumulativeBar += currDur # longer notes have larger values
    # Write figure to a html file
    fig.write_html(WAVDIR + songName + 'Synthesia.html', auto_open=True)
