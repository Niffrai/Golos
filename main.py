import openai
import pyttsx3
import speech_recognition

openai.api_key = "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"
engine = pyttsx3.init()
engine.setProperty('rate', 180)

def opeai(prompts):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompts,
        max_tokens=512,
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    engine.say(completion.choices[0].text)
    engine.runAndWait()


def record_and_recognize_audio():
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            engine.say('Слушаю')
            engine.runAndWait()
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Проверьте состояние микрофона")
            return

        try:
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition.RequestError:
            print("Проверьте соединение с интернетом")
            engine.say("Проверьте соединение с интернетом")
            engine.runAndWait()

        return recognized_data

if __name__ == "__main__":

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        voice_input = record_and_recognize_audio()
        opeai(f"ответ {voice_input}")
        break