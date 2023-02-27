class Robot:
    def greet(self):
        print("I am a robot")


class Android(Robot):
    def greet(self):
        super().greet()
        print("I am an android")


class PersonalAssistant(Robot):
    def greet(self):
        super().greet()
        print("I am a personal assistant")


class AssistantAndroid(Android, PersonalAssistant):
    def greet(self):
        super().greet()

a= AssistantAndroid()
a.greet()