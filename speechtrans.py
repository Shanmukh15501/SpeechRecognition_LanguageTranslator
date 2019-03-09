import speech_recognition as shanu
from translate import Translator

test = shanu.Recognizer()
translator= Translator(to_lang="te")
with shanu.Microphone() as source:
    print("Now Start Speacking")
    audio = test.listen(source)
try:
    print("You said " + test.recognize_google(audio))   
    answer=test.recognize_google(audio)
except LookupError:
    print("Could not understand audio")

translation = translator.translate(answer)

print(translation)
