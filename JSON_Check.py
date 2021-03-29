"""
Ваше приложение использует API, которое всякий раз отправляет Вам невалидный json, заменить API Вы
не в силах, поэому приходиться работать с тем,что есть.
Ваша задача написать код,который проверит является ли json валидным.

Типичные ошибки API:
- пропушенная кавычка,
- пропущенная скобка.
Внутри ключа и значения могут быть только строки.
"""

json1 = """{
  "support": {
    "message": "Контакты технической поддержки",
    "general": {
      "startWeekDay": Понедельник",
      "endWeekDay": "Суббота"
    }
  }
}"""

json1_valid = """{
  "support": {
    "message": "Контакты технической поддержки",
    "general": {
      "startWeekDay": "Понедельник",
      "endWeekDay": "Суббота"
    }
  }
}"""

json2 = """{
"support": {
"message": Контакты технической поддержки ООО Маяк",
"responsibleUsers": [
"Иванов Иван",
"Смирнова Ольга",
"Петрова Александра"
}
}"""

json2_valid = """{
"support": {
"message": "Контакты технической поддержки ООО Маяк",
"responsibleUsers": [
"Иванов Иван",
"Смирнова Ольга",
"Петрова Александра" ]
}
}"""

def json_validator(json):
    openbrackets = 0
    closebrackets = 0
    openquadbrackets = 0
    closequadbrackets = 0
    quotes = 0
    for i in json:
            if i == '{':
                    openbrackets += 1
            if i == '}':
                    closebrackets += 1
            if i == '[':
                    openquadbrackets += 1
            if i == ']':
                    closequadbrackets += 1
            if i == '"':
                    quotes += 1
    if openbrackets == closebrackets and openquadbrackets == closequadbrackets and quotes % 2 == 0:
        print('JSON-Scheme is valid')
    else:
        print('Invalid JSON-Scheme')

if __name__ == '__main__':

    json_validator(json1)
    json_validator(json1_valid)
    json_validator(json2)
    json_validator(json2_valid)
