import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Please speak now...")
    recognizer.adjust_for_ambient_noise(source) 
    audio = recognizer.listen(source)  
try:
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Sorry, I could not understand the audio.")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
