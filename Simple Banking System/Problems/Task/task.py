class Task:
    def __init__(self, description, team):
        self.description = description
        self.team = team

    # create the method
    def __add__(self, other):
        """Addition of complex numbers."""
        description = self.description + "\n" + other.description
        team = self.team + ", " + other.team
        return Task(description, team)
        # return self
    # def __add__(self, other):
    #     return Task(f"{self.description}\n{other.description}", f"{self.team}, {other.team}")

# task1 = Task("Finish the assignment.", "Kate")
# task2 = Task("Prepare the project for class.", "James, Ann")
# task3 = task1 + task2
# print(task3.description)  # "Finish the assignment.\nPrepare the project for class."
# print(task3.team)