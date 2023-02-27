class Area:

    def __init__(self, figure_name):
        self.figure_name = figure_name

    # use appropriate decorator
    @staticmethod
    def rhombus_area(a, b):
        return (a * b)/ 2

# user = Area.rhombus_area(8, 9)
# print(user)