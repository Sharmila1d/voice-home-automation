import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("\n🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio)

        print("You said:", text)

        return text

    except sr.UnknownValueError:

        print("Sorry, I couldn't understand.")

        return None

    except sr.RequestError:

        print("Speech Recognition service unavailable.")

        return None