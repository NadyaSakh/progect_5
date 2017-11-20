"""

Вариант 2, задача 2
Создать класс Fraction, который должен иметь два поля: числитель a и знаменатель b.
Оба поля должны быть типа int. Реализовать методы: сокращение дробей, сравнение, сложение и умножение.

Данная программа может выполнять операции непосредственно с дробями, например a,b,c - дроби, тогда:
c = a + b, c = a * b, c.reduce(), операции сравнения: a < b, a > b, a == b, a != b, a <= b, a >= b.
Для демонстрации работы с более двумя дробями реализована функция интерфейс, функция сравнения выводит
результаты после сравнения по всем шести операциям сравнения

"""

class Fraction:
    def __init__(self, numerator, denominator):
        self.a = numerator
        self.b = denominator

# НОЗ или нок, находит общий знаменатель
    def _nok(self, number1, number2):
        result_number = 0
        if number1 >= 0 and number2 >= 0:
            result_number = int(number1 * number2 / self._nod(number1,number2))
        elif number1 < 0:
            number1 = number1 * -1
            return self._nok(number1,number2)
        else:
            number2 = number2 * -1
            return self._nok(number1,number2)
        return result_number

# нод по алгоритму Евклида
    def _nod(self, number1, number2):
        if number2 == 0:
            return int(number1)
        else:
            return self._nod(number2, number1 % number2)

# приведение к наименьшему общему знаменателю
    def _make_common_denominator(self, fraction):
        nok = self._nok(self.b, fraction.b)
        multiplyer_1 = int(nok / self.b)
        multiplyer_2 = int(nok / fraction.b)
        self.a = self.a * multiplyer_1
        self.b = self.b * multiplyer_1
        fraction.a = fraction.a * multiplyer_2
        fraction.b = fraction.b * multiplyer_2

# сокращение двух чисел
    def _reduce(self, numerator, denominator):
        nod = self._nod(numerator,denominator)
        res_numerator = int(numerator/nod)
        res_denominator = int(denominator/nod)
        return res_numerator, res_denominator

# сокращение дроби
    def reduce(self):
        nod = self._nod(self.a,self.b)
        self.a = int(self.a/nod)
        self.b = int(self.b/nod)
        return self

# сложение
    def __add__(self, fraction):
        #проверка на ноль
        if self.a == 0 and fraction.a != 0:
            res_numerator = fraction.a
            res_denominator = fraction.b
            res_number = Fraction(res_numerator, res_denominator)

        elif self.a != 0 and fraction.a == 0:
            res_numerator = self.a
            res_denominator = self.b
            res_number = Fraction(res_numerator, res_denominator)

        elif self.a == 0 and fraction.a == 0:
            res_numerator = 0
            res_denominator = 1
        # в результате должен получиться ноль. Запишу так, чтобы можно было выполнять поттом операции с числом ноль
            res_number = Fraction(res_numerator, res_denominator)


        # два числа с одинаковым заменателем
        elif self.b == fraction.b:
            res_numerator = self.a + fraction.a
            res_denominator = self.b
            res_number = Fraction(res_numerator, res_denominator)

        # числа с разными знаменателями
        else:
            self._make_common_denominator(fraction)
            res_numerator = self.a + fraction.a
            res_denominator = self.b
            # сократить
            res_numerator, res_denominator = self._reduce(res_numerator,res_denominator)
            res_number = Fraction(res_numerator, res_denominator)
        return res_number

# операции сравнения:
    # x<y
    def __lt__(self, fraction):
        if self.b == fraction.b:
            return self.a < fraction.a
        else:
            self._make_common_denominator(fraction)
            result = (self.a < fraction.a)
            self.a, self.b = self._reduce(self.a, self.b)
            fraction.a, fraction.b = self._reduce(fraction.a, fraction.b)
            return result

    # x<=y
    def __le__(self, fraction):
        if self.b == fraction.b:
            return self.a <= fraction.a
        else:
            self._make_common_denominator(fraction)
            result = (self.a <= fraction.a)
            self.a, self.b = self._reduce(self.a, self.b)
            fraction.a, fraction.b = self._reduce(fraction.a, fraction.b)
            return result

    # x == y
    def __eq__(self, fraction):
        if self.b == fraction.b:
            return self.a is fraction.a
        else:
            self._make_common_denominator(fraction)
            return self.a is fraction.a
            result = (self.a is fraction.a)
            self.a, self.b = self._reduce(self.a, self.b)
            fraction.a, fraction.b = self._reduce(fraction.a, fraction.b)
            return result

    # x != y
    def __ne__(self, fraction):
        if self.b == fraction.b:
            return self.a is not fraction.a
        else:
            self._make_common_denominator(fraction)
            result = (self.a is not fraction.a)
            self.a, self.b = self._reduce(self.a, self.b)
            fraction.a, fraction.b = self._reduce(fraction.a, fraction.b)
            return result

    # x>y
    def __gt__(self, fraction):
        if self.b == fraction.b:
            return self.a > fraction.a
        else:
            self._make_common_denominator(fraction)
            result = (self.a > fraction.a)
            self.a, self.b = self._reduce(self.a, self.b)
            fraction.a, fraction.b = self._reduce(fraction.a, fraction.b)
            return result

    # x>= y
    def __ge__(self, fraction):
        if self.b == fraction.b:
            return self.a >= fraction.a
        else:
            self._make_common_denominator(fraction)
            result = (self.a >= fraction.a)
            self.a, self.b = self._reduce(self.a, self.b)
            fraction.a, fraction.b = self._reduce(fraction.a, fraction.b)
            return result

# умножение дробей
    def __mul__(self, fraction):
        res_numerator = self.a * fraction.a
        res_denominator = self.b * fraction.b
        res_numerator, res_denominator = self._reduce(res_numerator, res_denominator)
        res_number = Fraction(res_numerator, res_denominator)
        return res_number

# сравнение по всем операциям
    def compare(self, fraction):
        if self.__lt__(fraction):
            print("Первая дробь меньше второго.\n")
        if self.__le__(fraction):
            print("Первая дробь меньше или равна второй.\n")
        if self.__eq__(fraction):
            print("Первая дробь равна второй.\n")
        if self.__ne__(fraction):
            print("Первая дробь не равна второй.\n")
        if self.__gt__(fraction):
            print("Первая дробь больше второй.\n")
        if self.__ge__(fraction):
            print("Первая дробь больше или равна второй.\n")

#функция введения нескольких дробей
def enter_fractions():
    lst = []
    while 1:
        select = str(input("Ввести число? Введите да - y, нет - n.\n"))
        if select == 'y':
            fraction = enter_fraction()
            lst.append(fraction)
        elif select == 'n':
            break
        else:
            print("Нет такой команды. Попробуйте ввести ещё раз.\n")
    return lst

# функция введения одной дроби
def enter_fraction():
    try:
        numerator = int(input("Введите числитель:\n"))
        denominator = int(input("Введите знаменатель:\n"))
        # Число является нулём, когда числитель равен нулю, а знаменатель не равен нулю
        if denominator != 0:
            enter_number = Fraction(numerator, denominator)
            return enter_number
        else:
            print("Знаменатель не должен быть равен нулю, на ноль делить нельзя.\n")
            return enter_fraction()
    except ValueError:
        print("Неверный ввод. Числитель и знаменатель должны быть целыми числами.\n")
        return enter_fraction()

#интерфейс для ввода
def input_interface():
    print("Какие операции над дробями вы хотите произвести?\n"
          "1 - сложить дроби,\n"
          "2 - перемножить дроби,\n"
          "3 - сократить дробь,\n"
          "4 - сравнить две дроби,\n"
          "0 - выход из программы.\n")
    try:
        select = int(input())
    except ValueError:
        print("Введенное значение должно быть числом от 0 до 4. Введите ещё раз. \n")
        return input_interface()
# сложение
    if select == 1:
        # sum так запишем дробь, равную нулю, т.к. в знаменателе не может быть 0
        result = Fraction(0, 1)
        fractions = enter_fractions()

        if not fractions:
            while not fractions:
                fractions = enter_fractions()

        for fraction in fractions:
            result = result + fraction
        result.reduce()
        if result.a == 0:
            print("sum = 0.\n")
        else:
            print("sum = ", result.a, "/", result.b, "\n")
        return result
# произведение
    elif select == 2:
        result = Fraction(1,1)
        fractions = enter_fractions()

        if not fractions:
            while not fractions:
                fractions = enter_fractions()

        for fraction in fractions:
            result = result * fraction
        result.reduce()
        if result.a == 0:
            print("mul = 0.\n")
        else:
            print("mul = ", result.a, "/", result.b, "\n")
        return result
# сокращение
    elif select == 3:
        result = enter_fraction()
        result.reduce()
        if result.a == 0:
            print("reduce = 0.\n")
        else:
            print("reduce = ", result.a, "/", result.b, "\n")
        return result
# cравнение
    elif select == 4:
        first_fraction = enter_fraction()
        second_fraction = enter_fraction()
        first_fraction.compare(second_fraction)
# выход
    elif select == 0:
        exit()

    else:
        print("Нет такого пункта меню. Введите число от 0 до 4.\n")
        return input_interface()

def main():
    input_interface()

if __name__ == "__main__":
    main()