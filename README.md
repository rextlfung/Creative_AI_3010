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
Our model generates different types of video game music. We added new songs to the data set so that our model can produce more complex and catchy music. A number of these generated songs are saved in a wav folder.

HEURISTICS:
We generated better data by including a new selection of songs from which our model develops music. We also added in a function called makeSongComponent(), which replacese generateTokenSentence() used in the core. The reason is because (in general) song componenets sound better when they have constant length, so instead of generating a sentence based for a desired length of tokens, makeSongComponent() generates sentences for a desired length measured in bars. Another function we implemented is buildupSong(), which is used to generate the pre-chorus, providing a feel of build-up similar to how EDM songs sound like before the beat drop. Finally, we changed runMusicGenerator() to reuse sentences to increase recognition and create a motif, with the chorus being the most repetitive as it is meant to be the catchiest part of a song.

SHOWMANSHIP:
We created graphs using Plotly to represent frequencies of different notes, as well as a Synthesia-styled representation of the song. We also created a Reddit bot. Our Reddit bot can be called from the menu that automatically comes up when the code is run. Entering "3" allows a user to run our Reddit bot. We designed the bot to run upon command, rather than automatically (to prevent spamming). Our menu prompts the user to enter the name of a Sub-Reddit until a valid name is entered. The bot then searches the top 100 hottest posts on the entered Sub-Reddit for the first post that includes the word "music". The bot then posts a randomly selected song from our wav folder that we have already generated with a Google Drive link to this song along with the message, "Speaking of music, what do you think of this new song that I made?" If no post is found with the word "music" or if our bot has already posted on that comment, the model will return to the initial menu. Reddit limits our bot to one post every 10 minutes. If a user attempts to make more than one post within a 10 minute interval, Reddit will cause an error. Our bot's posts may not be able to be seen from other Reddit accounts because of the Reddit spam filter, but they can be seen as posted comments on our bot's Reddit account. I included the account information and bot information below.

Reddit Account Information:
Username: GardenMan183 | Password: EECS183Project

Reddit Bot Information:
- [garden_music_bot]
- client_id=iTHFgNE__q9PXw
- client_secret=HOJWDBWYykXxR7qD1L-_wDrf7ys
- password=EECS183Project
- username=GardenMan183
- user_agent=Game Music Bot 0.1
