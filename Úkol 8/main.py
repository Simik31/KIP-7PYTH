class Date:
    def __init__(self, date):
        self.split_sep = ["", ""]
        self.date = date
        self.monthNumber = 0
        for sep in separators:
            if sep in self.date:
                self.split_sep[0] = sep
                self.day = self.date.split(self.split_sep[0])[0]
                self.date = self.date.replace(self.day + self.split_sep[0], "")
                break
        for sep in separators:
            if sep in self.date:
                self.split_sep[1] = sep
                self.month, self.year = self.date.split(self.split_sep[1])
                break

    def test(self):
        # PŘESTUPNÝ ROK - UPRAVENÝ KÓD Z https://www.programiz.com/python-programming/examples/leap-year
        if (int(self.year) % 4) == 0:
            if (int(self.year) % 100) == 0:
                if (int(self.year) % 400) == 0:
                    daysInMonth[1] = 29
            else:
                daysInMonth[1] = 29

        # MĚSÍC
        if self.month.isdigit():
            if int(self.month) in range(1, len(czech_months) + 1):
                self.monthNumber = int(self.month)
            else:
                if int(self.month) < 1:
                    print(f"Wrong month. Correcting {self.month} -> 1\nCORRECTED ", end="")
                    self.month = self.monthNumber = 1
                else:
                    print(f"Wrong month. Correcting {self.month} -> ", end="")
                    self.month = self.monthNumber = len(czech_months)
                    print(self.month, "CORRECTED ", sep="\n", end="")
        else:
            for x in range(0, len(czech_months)):
                if self.month == czech_months[x]:
                    self.monthNumber = x + 1
            if self.monthNumber == 0:
                print(f"Wrong month. Correcting {self.month} -> {czech_months[0]}\nCORRECTED ", end="")
                self.month = czech_months[0]

        # DEN
        if int(self.day) < 1:
            print(f"Wrong day. Correcting {self.day} -> 1\nCORRECTED ", end="")
            self.day = 1
        elif int(self.day) > daysInMonth[self.monthNumber - 1]:
            print(f"Wrong day. Correcting {self.day} -> ", end="")
            self.day = daysInMonth[self.monthNumber - 1]
            print(self.day, "CORRECTED ", sep="\n", end="")

        print(f"DATE IS: {self.day}{self.split_sep[0]}{self.month}{self.split_sep[1]}{self.year}\n")


separators = ["/", ". ", ".", " "]
daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
czech_months = ["ledna", "února", "března", "dubna", "května", "června", "července", "srpna", "září", "října",
                "listopadu", "prosince"]

if __name__ == "__main__":
    # DATA Z MOODLE
    date_1 = Date("29. června 2020")
    date_2 = Date("29. 6. 2020")
    date_3 = Date("29.6.2020")
    date_4 = Date("29/6/2020")

    # DATUM Z EMAILU
    date_5 = Date("31. 4. 2020")

    date_1.test()
    date_2.test()
    date_3.test()
    date_4.test()
    date_5.test()
