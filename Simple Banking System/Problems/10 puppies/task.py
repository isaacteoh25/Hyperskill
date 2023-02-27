class Puppy:
    n_puppies = 0

    # define __new__
    def __new__(cls):
        if cls.n_puppies < 10:
            instance = object.__new__(cls)
            cls.n_puppies += 1
            return instance

    # def __new__(cls):
    #     if cls.n_puppies == 0:
    #         cls.n_puppies += 10
    #     return object.__new__(cls)
    # def __new__(cls):
    #     while cls.n_puppies < 10:
    #         cls.n_puppies += 1