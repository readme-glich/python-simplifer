#the comments will be repeated but in different languages (my github:readme-glich, my email:readmegod4321@gmail.com)
#в комментарии будут повторяться но на разных языках (мой github:readme-glich,моя почта:readmegod4321@gmail.com)
from datetime import datetime

today = datetime.now()
#calculates how many days are left until something, if the "year" value is empty, then the current year is taken
#считает сколько дней осталось до чего-то, если значение "year" пустое то берётся год на данный момент
def days_until(day,month,year):
    target = datetime(today.year, month, day)
    if year ==None:
        target = datetime(today.year, month, day)
    else:
        target = datetime(year, month, day)

    if target < today:
        # Если дата уже прошла в этом году, берем следующий год
        target = datetime(today.year + 1, month, day)
    delta = target - today
    return delta.days+1
#does it count a leap year
#считает високосный ли год 
def leap_year(year):
    leap = False
    if year % 4 ==0 :
        leap = True
    if year % 100==0:
        leap= False
    if year %400 ==0:
        leap = True
    return leap
#difference
#разница
def difference(num1,num2):
    if num1>num2:
        return num1-num2
    elif num1<num2:
        return num2-num1
    elif num1==num2:
        return 0
#counts the percentages
#считает проценты
def percentage_num(numerator,denominator):return numerator/denominator*100
