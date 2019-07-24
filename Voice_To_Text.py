import random
import time
import sys
import os
import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.
    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source,duration=0.25)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

# create recognizer and mic instances
recognizer = sr.Recognizer()
microphone = sr.Microphone()
command = recognize_speech_from_mic(recognizer, microphone)
print("You said: {}".format(command["transcription"]))
print("You said: {}".format(command["error"]))

# Turn the Statement into Tello Commands
# set up the response object
Final_Command = {
        "Command" : None,
        "Value" : None
    }

#Open File for Writing Commands
file = open("command.txt","a")

#Final_Command = command["transcription"]
i = 0
tempCom = command["transcription"]
com_list = tempCom.split()

#identifies Command

for word in (com_list):
    if(com_list[i] == "forward"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "back"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "left"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "right"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "up"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "down"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "takeoff"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "land"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "emergency"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "flip"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    elif (com_list[i] == "speed"):
        print("WRITE TO FILE")
        file.write(com_list[i])
        file.write(" ")
        i=i+1
    else:
        print("Incorrect Command")
        i=i+1

#identifies magnitude

i = 0
for word in (com_list):
    if(com_list[i].isdigit()):
        print("Magnitude of Command to be WRITTEN TO FILE")
        file.write(com_list[i])
        break
    else:
        i = i + 1
         
file.write("\n")

os.system('python tello_test.py')

