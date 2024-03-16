import speech_recognition as sr
import webbrowser
import pyttsx3

def speak(text):#Function for Speaking the given text using the computer's speakers.
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

def take_command():#Function for Listening from user voice command and returns it as text.
  r = sr.Recognizer()
  print("I am Grape")
  with sr.Microphone() as source:#bot start listening and stores the text
    print("Listening...") 
    audio = r.listen(source)
  try:
    command = r.recognize_google(audio)
    print(f"You said: {command}") #Bot reconizes command
  except sr.UnknownValueError:
    speak("Sorry, I didn't understand that. Could you repeat?")
    command = take_command()
  except sr.RequestError as e:
    speak(f"Could not request results from Google Speech Recognition service; {e}")
    command = None
  return command.lower()

speak("Hi!I am Grape. I can open websites for you. Just tell me the website name.")

while True:
  command = take_command()
  if "open" in command: #the text with "open" is split and website name is extracted 
    url = command.split("open ")[1] 
    a=url+".com"
    webbrowser.open(a)
    speak(f"Opening {url}")
  elif "quit" in command: #the bot quits the process
    speak("Thanks Goodbye!")
    break
  else:
    speak("Sorry, I can't understand. Please say 'open' followed by the website , or say 'quit' to exit.")  

