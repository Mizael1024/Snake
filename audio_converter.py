## audio_converter.py
import speech_recognition as sr

class AudioFile:
    def __init__(self, file_path: str, format: str):
        self.file_path = file_path
        self.format = format
        self.text = ""

    def convert_to_text(self):
        try:
            # Initialize recognizer class (for recognizing the speech)
            r = sr.Recognizer()

            # Reading Audio file as source
            # listening the audio file and store in audio_text variable
            with sr.AudioFile(self.file_path) as source:
                audio_text = r.listen(source)

            # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
            try:
                # using google speech recognition
                self.text = r.recognize_google(audio_text)
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {0}".format(e))
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
        except Exception as e:
            print(f"An error occurred while converting audio to text: {str(e)}")
