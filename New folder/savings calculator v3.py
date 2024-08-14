ja=31
feb=28
march=31
mar=31
apr=30
may=31
jun=30
jul=31
aug=31
sept=30
oct=31
nov=30
dec=31
jan=0
goal=40000 # how much money you want 
hours=8 #how many hours a day you work
wages=26.54#an hour 
days=5 #working days
costsw=453.21 #any weekly expenses
debtpercent=.85 #what percentage of your money you put toward debt, the rest goes to your goal
Int=.05 #how much interest is on your debt
month=mar
day=0 #334 is the number it likes 
#These are the variables that control the entire calculator
if month==jan:
    daysinyear=day
if month==feb:
    daysinyear=ja+day
    ja+day==daysinyear
if month==march:
    daysinyear=ja+feb+day
    ja+feb+day==daysinyear
if month==apr:
    daysinyear=ja+feb+mar+day
    ja+feb+mar+day==daysinyear
if month ==may:
    daysinyear=ja+feb+mar+apr+day
    ja+feb+mar+apr+day==daysinyear
if month==jun:
    daysinyear=ja+feb+mar+apr+may+day
    ja+feb+mar+apr+may+day==daysinyear
if month==jul:
    daysinyear=ja+feb+mar+apr+may+jun+day
    ja+feb+mar+apr+may+jun+day==daysinyear
if month==aug:
    daysinyear=ja+feb+mar+apr+may+jun+jul+day
    ja+feb+mar+apr+may+jun+jul+day==daysinyear
if month==sept:
    daysinyear=ja+feb+mar+apr+may+jun+jul+aug+day
    ja+feb+mar+apr+may+jun+jul+aug+day==daysinyear
if month==oct:
    daysinyear=ja+feb+mar+apr+may+jun+jul+aug+sept+day
    ja+feb+mar+apr+may+jun+jul+aug+sept+day==daysinyear
if month ==nov:
    daysinyear=ja+feb+mar+apr+may+jun+jul+aug+sept+oct+day
    ja+feb+mar+apr+may+jun+jul+aug+sept+oct+day==daysinyear
if month ==dec:
    daysinyear=ja+feb+mar+apr+may+jun+jul+aug+sept+oct+nov+day
    ja+feb+mar+apr+may+jun+jul+aug+sept+oct+nov+day==daysinyear
debtpaydays=(31,59)
print(daysinyear,"days into the year")



print(goal,"is the goal")
print(hours,"hours a day")
print(wages,"dollars an hour")
daily=wages*hours
daily==wages*hours
print(daily,"dollars made per day")
weekly=daily*days
weekly==daily*days
print(weekly,"per dollars made per week")
cashw=weekly-costsw #cashw is the total free money in a week
cashw==weekly-costsw
goalmoneyw=cashw*debtpercent
print(costsw,"in expenses per week")
print(cashw,"dollars of profit a week")
weekstogoal=goal/goalmoneyw
weekstogoal==goal/goalmoneyw
print(weekstogoal,"weeks to goal")
daystogoal=weekstogoal*7
daystogoal==weekstogoal*7
print(daystogoal,"more days")
hourstogoal=goal/wages
hourstogoal==goal/wages
print(hourstogoal,"more hours (not including expenses)")
yearstogoal=daystogoal/365
yearstogoal==daystogoal/365
print(yearstogoal,"years left")
monthstogoal=yearstogoal*12
monthstogoal==yearstogoal*12
print(monthstogoal,"months to goal")

debt= 3000
print(debt,"this is your original debt")
debtpaymentsw=cashw*debtpercent
print(debtpaymentsw,"weekly debt payment")
debtw=debt-debtpaymentsw
debt-debtpaymentsw==debtw
print(debtw,"this is your debt before interest")
weekcalculator=daysinyear/7
daysinyear/7==weekcalculator

print(weekcalculator,"Is it week")
print(type(weekcalculator))
moneydue=weekcalculator*debtpaymentsw
weekcalculator*debtpaymentsw==moneydue

print(debtpaymentsw,"Weekly debt payments")
debtInt=(debtw*Int)+debtw
debtInt==(debtw*Int)+debtw
print(debtInt,"this is your debt after interest and payments")
if debtInt>debt:
    print("The interest on your debt is greater than your payments.")
print(debtpaymentsw,"how much debt you pay in a week")
losses=debtpaymentsw+costsw
debtpaymentsw+costsw==losses


print("rounded output") #rounding all of the numbers to the second decimal
print("these are your hourly wages:")
print(round(wages,2))
print("this is how much you make in a day:")
print(round(daily,2))
print("this is how much you make in a week:")
print(round(weekly,2))
print("this is how much you pay per week total")
print(round(losses,2))
print("this is how much you pay in a week (not including debts):")
print(round(costsw,2))
print("this is how much you have left over per week, this is put into the goal:")
print(round(goalmoneyw,2))
print("This shows how many weeks are left before you reach the goal:")
print(round(weekstogoal,2))
print("this shows how many days are left before you reach the goal:")
print(round(daystogoal,2))
print("this shows how many hours you will have to work to complete the goal:")
print(round(hourstogoal,2))
print("this shows how many years you have to work before you reach your goal:")
print(round(yearstogoal,2))
print("this shows how many months are left before you reach the goal:")
print(round(monthstogoal,2))
