import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)

def text_to_speech(title, content, output_audio_path):
    clips = []

    if title:
        print("Title: ", title)
        engine.say(title)
    if content:
        print("Content: ", content)
        engine.say(content)

    final = title
    if content:
        final += " " + content

    engine.save_to_file(final, output_audio_path)
    engine.runAndWait()
