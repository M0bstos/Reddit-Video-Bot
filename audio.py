import pyttsx3

def text_to_speech(title, content, output_audio_path):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')       
    engine.setProperty('voice', voices[0].id)
    final = title
    if content:
        final += " " + content
    engine.save_to_file(final, output_audio_path)
    engine.runAndWait()
