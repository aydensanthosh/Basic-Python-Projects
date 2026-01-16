import win32com.client as wincom


if __name__=="__main__":
    speak = wincom.Dispatch("SAPI.SpVoice")
    print("Welcome to your Robo speaker!\n")
    while True:
        command=input("What would you like me to speak? ")
        if command!='q':
            speak.Speak(command)
        else:
            speak.Speak("\nThank you for using Robo Speaker. Goodbye!")
            break
    print("Thank you for using Robo-Speaker.")

