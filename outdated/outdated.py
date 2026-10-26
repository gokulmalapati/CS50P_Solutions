while True:
    date = input("What is the date? ").strip()

    try :
        month,day,year= date.split("/")
        if 0 < int(month)<13 and 0< int(day)<32:
            print(f"{year}-{int(month):02}-{int(day):02}", end=(" "))
            break
        else:
            continue

    except ValueError:
        try:
            month_day,year1= date.split(",")
            month1,day1 = month_day.split(" ")
            match month1 :
                case "January":
                    month1 = 1
                case "February":
                    month1 = 2
                case "March":
                    month1 = 3
                case "April":
                    month1 = 4
                case "May":
                    month1 = 5
                case "June":
                    month1 = 6
                case "July":
                    month1 = 7
                case "August":
                    month1 = 8
                case "September":
                    month1 = 9
                case "October":
                    month1 = 10
                case "November":
                    month1 = 11
                case "December":
                    month1 = 12
                case _ :
                    continue
            if 0 < int(month1)<13 and 0< int(day1)<32:
                print(f"{year1}-{int(month1):02}-{int(day1):02}", end=(" "))
                break
            else:
                continue
        except ValueError:
            continue

    except ValueError:
        pass

