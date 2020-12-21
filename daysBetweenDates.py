def month_to_day(m):
    if m < 2:
        return m * 31
    if m%2 == 1:
        return int(round((m * 30 + (m/2) * 1 - 2), 0))
    else:
        return int(round((m * 30 + (m/2) * 1 - 1), 0))

# print(month_to_day(1))
# print(month_to_day(11))
# print(month_to_day(6))

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    total1 = year1 * 365
    total2 = year2 * 365
    
    total1 += day1
    total2 += day2
    
    total1 += month_to_day(month1)
    total2 += month_to_day(month2)
    
    out = total2 - total1

    # print(out)
    return out

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30, 2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29, 2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
testDaysBetweenDates()