import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    
    # Optional: set voice rate and volume
    engine.setProperty('rate', 150)     # Speed of speech (default ~200)
    engine.setProperty('volume', 1.0)   # Volume (0.0 to 1.0)

    # Optional: choose a voice (male/female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change index if needed (0 for male, 1 for female)

    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    user_input = input("Enter text to speak: ")
    text_to_speech(user_input)
