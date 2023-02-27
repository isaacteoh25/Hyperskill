class Date:

    def __init__(self, day, month):
        self.day = day
        self.month = month

    # use appropriate decorator
    # @property
    # def date(self):
    #     return str(self.day) + "/" + str(self.month)

    @property
    def date(self):
        return f'{self.day}/{self.month}'
date_obj = Date(14, 5)
print(date_obj.date)  # 14/05

date_obj.day = 15
print(date_obj.date)  # 15/05