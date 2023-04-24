# Reddit-Video-Bot

Converts reddit posts to a tts video

This is a Python script that uses the praw and pyttsx3 libraries to retrieve and read aloud top posts from a specified subreddit.

The praw library is used to authenticate the script with Reddit using a set of client credentials, a username, and password. The script then uses this authenticated connection to access a specified subreddit (TwoSentenceHorror) and retrieve the top post(s).

change the "subreddit" in an editor to change the subreddit and change "num" to change the number of posts to push out.

The pyttsx3 library is used to convert text to speech, allowing the script to read the retrieved post(s) aloud. The engine object is initialized with pyttsx3.init() and a voice is selected (in this case, the second voice available in the voices list).

To shift between male and female voices, change the "x" in voices[x] to "0" for Male and "1" for Female.

The script loops through the top posts of the specified subreddit (in this case, only the top post) and retrieves the post's title and content. The title and content are then printed to the console and read aloud using the engine.say() method.

Finally, the engine.runAndWait() method is called to ensure that all text has been read aloud before the script terminates.
