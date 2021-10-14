class Person:
    def __init__(self, name, personalNumber):
        self.name = name
        self.number_list = list(map(int, personalNumber))

        if len(self.number_list) == 6 or len(self.number_list) == 10:
            # ROK NAROZENÍ
            if self.number_list[0] not in [0, 1, 2]:  # ROKY 00-09, 10-19, 20-29 BERU JAKO 20XX OSTATNÍ JAKO 19XX
                self.birthYear = 1900
            else:
                self.birthYear = 2000
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
        else:
            print("Please enter your personal identification number correctly")
            exit(-1)

    def sayHello(self):
        print(f"Hi! My name is {self.name}.")
        print(f"I am {self.gender} and my birthday is {self.birthDay}.{self.birthMonth}.{self.birthYear}")


if __name__ == "__main__":
    martin = Person("Martin", "991231")
    martin.sayHello()
