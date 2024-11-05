from math import gcd

class Rational:
    def __init__(self, num: int, denum: int):
        if denum == 0:
            raise ValueError("Знаменатель не может быть равен 0")
        common = gcd(num, denum)
        self.numerator = num // common
        self.denominator = denum // common
        
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    @staticmethod
    def reduce(numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен 0.")
        common = gcd(numerator, denominator)
        return numerator // common, denominator // common

    def __add__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
        else:
            new_numerator = self.numerator + other * self.denominator
            new_denominator = self.denominator
        return Rational(new_numerator, new_denominator)

    def __sub__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
            new_denominator = self.denominator * other.denominator
        else:
            new_numerator = self.numerator - other * self.denominator
            new_denominator = self.denominator
        return Rational(new_numerator, new_denominator)

    def __mul__(self, other):
        if isinstance(other, Rational):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
        else:
            new_numerator = self.numerator * other
            new_denominator = self.denominator
        return Rational(new_numerator, new_denominator)

    def __truediv__(self, other):
        if isinstance(other, Rational):
            if other.numerator == 0:
                raise ValueError("Знаменатель не может быть равен 0.")
            new_numerator = self.numerator * other.denominator
            new_denominator = self.denominator * other.numerator
        else:
            if other == 0:
                raise ValueError("Знаменатель не может быть равен 0.")
            new_numerator = self.numerator
            new_denominator = self.denominator * other
        return Rational(new_numerator, new_denominator)

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator == other.numerator and self.denominator == other.denominator
        else:
            return self.numerator == other * self.denominator

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator
        else:
            return self.numerator < other * self.denominator

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

if __name__ == "__main__":
    r1 = Rational(3, 4)
    r2 = Rational(2, 5)
    print(r1) 
    print(r2)  
    print(r1 + r2) 
    print(r1 - r2)  
    print(r1 * r2)  
    print(r1 / r2)  
    print(r1 == Rational(3, 4)) 
    print(r1 < r2)  