THE GARDEN MAN
------------------------------
- Connor Blesy; cblesy
- Tin Long Rex Fung; rexfung
- Isaac Lok-tin Li; isaliac
- Max Davis; caidavis

All Downloaded Python Libraries used:
* Praw
* Plotly
* Numpy

APPLICATION:
Our model generates different types of video game music. We added new songs and notes so that our model is able to produce more complex and realistic music. A number of these generated songs are saved in a wav folder.

HEURISTICS:
We generated better data by including a new selection of songs from which our model develops music.

SHOWMANSHIP:
We created graphs using Plotly to represent frequencies of different notes. We also created a Reddit bot. Our Reddit bot can be called from the menu that automatically comes up when the code is run. Entering "3" allows a user to run our Reddit bot. We designed the bot to run upon command, rather than automatically (to prevent spamming). Our menu prompts the user to enter the name of a Sub-Reddit until a valid name is entered. The bot then searches the top 100 hottest posts on the entered Sub-Reddit for the word "music". THe bot then post a randomly selected song from our wav folder that we have already generated and posts a comment with a Google Drive link to this song along with the message, "Speaking of music, what do you think of this new song that I made?" If no post is found with the word "music" or if our bot has already posted on that comment, the model will return to the initial menu. Reddit limits our bot to one post every 10 minutes. If a user attempts to make more than one post within a 10 minute interval, Reddit will cause an error.
Reddit Account Information:
Username: GardenMan183
Password: EECS183Project
