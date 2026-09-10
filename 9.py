def passwordValidator(pwd):
    def containsUppercase(pwd):
        for c in str(pwd):
            if c.isupper():
                return True
        return False

    def containsNumber(pwd):
        for c in str(pwd):
            if c.isdigit():
                return True
        return False

    pwd = str(pwd)
    if not len(pwd) >= 8:
        return False
    if not containsUppercase(pwd):
        return False
    if not containsNumber(pwd):
        return False
    return True

senha = input("digite a senha: ")
if passwordValidator(senha):
    print("Senha válida!")
else:
    print("Senha inválida!")
    