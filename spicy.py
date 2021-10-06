import pyttsx3
import speech_recognition as sr
import wikipedia
import smtplib



engine = pyttsx3.init()
converter = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
converter.setProperty('rPassate', 150)


#text-to-speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#voice recog
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as mic:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(mic)

    try:
        print("recognizing")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said: {query}")

    except Exception as e:
        return "none"
    return query

def sendEmail(to ,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email_id','password')
    server.sendmail('to_email_id', to, content)
    server.close()


#main
if __name__ == "__main__":
    while True:
        query = listen()

        if "hello spicy" in query:
            speak("Hello Pranav!")

        elif "how are you" in query:
            speak("i am fine!,how are you")

        elif "wikipedia" in query:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=1)
            print(result)
            speak(result)

        elif "mail to me" in query:
            try:
                print("what should i send")
                speak("what should i send")
                content = listen().lower()
                to = "a.krishna.pranav@gmail.com"
                sendEmail(to, content)
                print("email sent")
                speak("email sent")

            except Exception as e:
                print(e)
                speak("email failed")












