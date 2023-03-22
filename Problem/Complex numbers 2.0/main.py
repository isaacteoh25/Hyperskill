class ComplexNumber:
    def __init__(self, real_part, im_part):
        self.real_part = real_part
        self.im_part = im_part

    def __add__(self, other):
        real = self.real_part + other.real_part
        imaginary = self.im_part + other.im_part
        return ComplexNumber(real, imaginary)

    def __mul__(self, other):
        real = self.real_part * other.real_part - self.im_part * other.im_part
        imaginary = self.real_part * other.im_part + other.real_part * self.im_part
        return ComplexNumber(real, imaginary)

    def __eq__(self, other):
        return ((self.real_part == other.real_part) and
                (self.im_part == other.im_part))

    def __str__(self):
        if self.im_part < 0:
            sign = "-"
        else:
            sign = "+"
        string = "{} {} {}i".format(self.real_part, sign, abs(self.im_part))
        return string

    # define the rest of the methods here
    def __sub__(self, other):
        real = self.real_part - other.real_part
        imaginary = self.im_part - other.im_part
        return ComplexNumber(real, imaginary)

    def __truediv__(self, other):
        denom = other.real_part ** 2 + other.im_part ** 2
        conjugate_other = ComplexNumber(other.real_part, -1 * other.im_part)
        self_mult_conjugate = self.__mul__(conjugate_other)
        return ComplexNumber(self_mult_conjugate.real_part / denom, self_mult_conjugate.im_part / denom)


    #
    # num1 = a1 + b1i, num2 = a2 + b2i
    # num1 / num2 = (a1 + b1i) * (a2 - b2i) / (a2 + b2i) * (a2 - b2i)
    # = a1a2 - a1b2i + a2b1i - b1b2
    # i ^ 2 / a2a2 - a2b2i + a2b2i + b2b2
    # i ^ 2
    # = a1a2 - a1b2i + a2b1i + b1b2 / a2a2 + b2b2
    #
    # real = a1a2 + b1b2 / a2a2 + b2b2
    # imaginary = -a1b2i + a2b1i / a2a2 + b2b2
    # a1 -> self.real_part and b1 -> self.im_part
