class Time:

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    # use appropriate decorator
    @classmethod
    def from_string(cls, data):
        name, surname = data.split(':')
        return cls(name, surname)

# time = Time.from_string('14:05')
# print(time.hour)  # 14
# print(time.minute)