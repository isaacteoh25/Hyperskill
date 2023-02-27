class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # define your methods here
    def __iadd__(self, height):
        """Addition with assignment (+=) for complex numbers."""
        self.height += height
        return self

    def __isub__(self, height):
        """Addition with assignment (+=) for complex numbers."""
        self.height -= height
        return self