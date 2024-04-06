import calendar
print('Добро пожаловать в календарь\n')

year = int(input("Please enter a year: "))
month = int(input("Please enter a month: "))

print(calendar.month(year, month))

print('Всего хорошего')
