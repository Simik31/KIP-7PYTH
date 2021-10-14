def choose_inputted_correctly(choose_from):
    ret = []
    for user in choose_from:
        name, surname = user.split(" ")
        if not (name.islower() or surname.islower()):
            ret.append(user)
    return ret


def choose_inputted_incorrectly(choose_from):
    ret = []
    for user in choose_from:
        name, surname = user.split(" ")
        if name.islower() or surname.islower():
            ret.append(user)
    return ret


def correct_inputted_incorrectly(choose_from):
    full_name = ""
    ret = []
    for user in choose_from:
        name, surname = user.split(" ")
        if name.islower():
            full_name = name.capitalize()
        else:
            full_name = name
        full_name += " "
        if surname.islower():
            full_name += surname.capitalize()
        else:
            full_name += surname
        ret.append(full_name)
    return ret


if __name__ == '__main__':
    users = ['pepa novák', 'Jiří Sládek', 'Ivo navrátil', 'jan Poledník']
    correctly = choose_inputted_correctly(users)
    incorrectly = choose_inputted_incorrectly(users)
    corrected = correct_inputted_incorrectly(users)
    print("All: ", users)
    print("Correctly: ", correctly)
    print("Incorrectly: ", incorrectly)
    print("Corrected: ", corrected)
