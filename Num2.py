passw = ["6574", "453762", "154", "10986", "294763", "4567890"]

for psw in passw:
    if len(psw) >= 6:
        print("Пароль надійний")

    elif len(psw) < 6:
        print("Пароль занадто короткий")