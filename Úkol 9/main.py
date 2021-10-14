class Person:
    def __init__(self, name, personal_number):
        self.name = name
        try:
            self.pin_temp = int(personal_number)
        except ValueError:
            print("Not a number")
            exit(-1)
        try:
            if self.pin_temp < 0:
                raise Exception()
        except Exception:
            print("Negative umber")
            exit(-1)
        try:
            if len(personal_number) not in [6, 10]:
                raise Exception()
        except Exception:
            print("Incorrect length")
            exit(-1)
            
        self.number_list = list(map(int, personal_number))
        # ROK NAROZENÍ
        if self.number_list[0] in [0, 1, 2]:  # ROKY 00-09, 10-19, 20-29 BERU JAKO 20XX OSTATNÍ JAKO 19XX
            self.birthYear = 2000
        else:
            self.birthYear = 1900
        self.birthYear += 10 * self.number_list[0] + self.number_list[1]

        # POHLAVÍ A MĚSÍC NAROZENÍ
        if self.number_list[2] in [0, 1]:
            self.gender = "male"
            self.birthMonth = 10 * self.number_list[2] + self.number_list[3]
        else:
            self.gender = "female"
            self.birthMonth = 10 * (self.number_list[2] - 5) + self.number_list[3]

        # DEN NAROZENÍ
        self.birthDay = 10 * self.number_list[4] + self.number_list[5]

    def say_hello(self):
        print(f"Hi! My name is {self.name}.")
        print(f"I am {self.gender} and my birthday is {self.birthDay}.{self.birthMonth}.{self.birthYear}")


if __name__ == "__main__":
    martin = Person("Martin", "991231")
    martin.say_hello()
    print()
    test = Person(input("Your name: "), input("Your PIN:"))
    test.say_hello()
