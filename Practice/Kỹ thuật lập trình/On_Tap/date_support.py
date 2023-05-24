import time
def thoi_gian():
    timec = time.localtime()
    timex = time.strftime("%d/%m/%Y")
    timey = time.ctime()
    x = timec.tm_wday
    def thu(x):
        if x == 0:
            return ("Monday")
        elif x == 1:
            return ("Tuesday")
        elif x == 2:
            return ("Wednesday")
        elif x == 3:
            return ("Thurday")
        elif x == 4:
            return ("Friday")
        elif x == 5:
            return ("Saturday")
        else:
            return ("Sunday")
    return(f'''Ngay hien tai la: {timec.tm_mday}
Thang hien tai la: {timec.tm_mon}
Nam hien tai la: {timec.tm_year}
Ngay thang nam hien tai la: {timex}
Hom nay la {thu(x)}''')