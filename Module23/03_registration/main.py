def validate_data(registrations_line):
    fields = registrations_line.split()
    if len(fields) < 3:
        raise IndexError("НЕ присутствуют все три поля.")
    name, email, age = fields
    if not name.isalpha():
        raise NameError("Поле «Имя» содержит НЕ только буквы.")
    elif email.count('@') != 1 or email.count('.') != 1:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку.")
    elif not age.isdigit() or not (10 <= int(age) <= 99):
        raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99.")


with (open("registrations.txt", encoding='utf-8') as in_file,
      open("registrations_good.log", "w", encoding='utf-8') as good_file,
      open("registrations_bad.log", "w", encoding='utf-8') as bad_file):
    for line in in_file:
        try:
            data = validate_data(line)
            good_file.write(line.strip() + "\n")
        except (IndexError, NameError, SyntaxError, ValueError) as exe:
            bad_file.write(line.strip() + "     " + str(exe) + "\n")




