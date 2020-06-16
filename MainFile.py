import datetime
import calendar
import tkinter as tk
import tkinter.ttk as ttk
from datetime import date, timedelta
from exchange import MoneyRates, PaintingRates
from tkcalendar import Calendar

class Window:
    def __init__(self, width, height, title='Change rates', resizable=(False, False), icon=None):
        self.root =tk.Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+200+50')
        self.root.resizable(resizable[0], resizable[1])

    def run(self):
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # create widgets of main window
        self.start_date_label = tk.Label(self.root, text='Start date: ').grid(row = 0, column = 1, columnspan=2)
        self.start_date_label = tk.Label(self.root, text='End date: ').grid(row=0, column=3, columnspan=2)
        self.start_date = Calendar(self.root, font="Arial 8", selectmode='day', year=2000, month=1, day=1,
                                   mindate=datetime.date(2000, 1, 1), maxdate=datetime.date.today())
        self.end_date = Calendar(self.root, font="Arial 8", selectmode='day', year=2000, month=1, day=2,
                                 mindate=datetime.date(2000, 1, 2), maxdate=datetime.date.today())
        self.end_date.bind("<<CalendarSelected>>", self.DateCheck)
        self.start_date.bind("<<CalendarSelected>>", self.DateCheck)
        self.start_date.grid(column=1, row=1, padx=10, pady=10, columnspan=2)
        self.end_date.grid(column=3, row=1, padx=10, pady=10, columnspan=2)
        self.step = tk.Label(self.root, text='Step ').grid(row=2, column=1)
        # years = self.setTimeInterval(start_year, end_year)
        # self.yy1 = ttk.Combobox(self.root, values=years, height =10, width=5)
        # self.yy1.set(years[0])
        # self.yy1.grid(row=1, column=2)
        # self.yy1['state'] = 'readonly'
        # self.yy1.bind("<<ComboboxSelected>>", self.YearCheck)
        #
        # months = self.setTimeInterval(1, 12)
        # self.mm1 = ttk.Combobox(self.root, values=months, height =12, width=3)
        # self.mm1.set(months[0])
        # self.mm1.grid(row=1, column=3)
        # self.mm1['state'] = 'readonly'
        # self.mm1.bind("<<ComboboxSelected>>", self.CheckMonth)
        #
        # daysInMonth = calendar.monthrange(int(self.yy1.get()), int(self.mm1.get()))[1]
        # self.days = self.setTimeInterval(1, daysInMonth)
        # self.dd1 = ttk.Combobox(self.root, values = self.days, height =10, width=3)
        # self.dd1.set(self.days[0])
        # self.dd1.grid(row=1, column=4)
        # self.dd1.bind("<<ComboboxSelected>>", self.DayValidate)
        # self.dd1['state'] = 'readonly'
        #
        # self.yy2 = ttk.Combobox(self.root, values=years, height =10, width=5)
        # self.yy2.set(years[0])
        # self.yy2.grid(row=2, column=2)
        # self.yy2.bind("<<ComboboxSelected>>", self.YearCheck)
        # self.yy2['state'] = 'readonly'
        #
        # self.mm2 = ttk.Combobox(self.root, values=months, height =12, width=3)
        # self.mm2.set(months[0])
        # self.mm2.grid(row=2, column=3)
        # self.mm2.bind("<<ComboboxSelected>>", self.CheckMonth)
        # self.mm2['state'] = 'readonly'
        #
        # self.dd2 = ttk.Combobox(self.root, values=self.days, height=10, width=3)
        # self.dd2.set(self.days[0])
        # self.dd2.grid(row=2, column=4)
        # self.dd2.bind("<<ComboboxSelected>>", self.DayValidate)
        # self.dd2['state'] = 'readonly'
        self.interval = tk.Scale(self.root, orient='horizontal', length=300, from_=1, to=365, tickinterval=50, resolution=1)
        self.interval.grid(row=2, column=2, columnspan=4)
        self.check_dates = tk.Button(self.root, text='Get list of money', command= self.createMoneyList)
        self.check_dates.grid(row=4, column=2, columnspan=2, pady=10)
        self.quit = tk.Button(self.root, text="QUIT", fg="red",
                              command=self.root.destroy).grid(row=4, column=4, columnspan=1, pady=10)
    # def setTimeInterval(self, start, end):
    #     interval = []
    #     for i in range(int(start), int(end)+1):
    #         interval.append(i)
    #     return interval
    #
    # def YearCheck(self, event):
    #     if int(self.yy1.get())>int(self.yy2.get()):
    #         self.yy2.set(self.yy1.get())
    #     self.DayValidate()
    #
    # def CheckMonth(self, event):
    #     if int(self.yy1.get())==int(self.yy2.get()) and int(self.mm1.get())>int(self.mm2.get()):
    #         self.mm2.set(self.mm1.get())
    #     self.DayValidate()
    #
    # def DayValidate(self):
    #     daysInMonth1 = calendar.monthrange(int(self.yy1.get()), int(self.mm1.get()))[1]
    #     daysInMonth2 = calendar.monthrange(int(self.yy2.get()), int(self.mm2.get()))[1]
    #     if len(self.dd1['value']) != daysInMonth1:
    #         days = self.setTimeInterval(1, daysInMonth1)
    #         self.dd1['value'] = days
    #     elif len(self.dd2['value']) != daysInMonth2:
    #         days = self.setTimeInterval(1, daysInMonth2)
    #         self.dd2['value'] = days
    #     else:
    #         pass
    #     if int(self.dd1.get()) > daysInMonth1:
    #         self.dd1.set(daysInMonth1)
    #     elif int(self.dd2.get()) > daysInMonth2:
    #         self.dd2.set(daysInMonth2)
    #     if int(self.yy1.get()) == int(self.yy2.get()) and int(self.mm1.get()) == int(self.mm2.get()) and\
    #             int(self.dd1.get()) == int(self.dd2.get()) and int(self.dd1.get())<daysInMonth1:
    #         self.dd2.set(int(self.dd2.get())+1)
    #     elif int(self.yy1.get()) == int(self.yy2.get()) and int(self.mm1.get()) == int(self.mm2.get()) and \
    #             int(self.dd1.get()) >= int(self.dd2.get()):
    #         if int(self.mm2.get()) < 12:
    #             self.mm2.set(int(self.mm2.get()) + 1)
    #             self.dd2.set(1)
    #         else:
    #             self.yy2.set(int(self.yy2.get())+1)
    #             self.mm2.set(1)
    #             self.dd2.set(1)

    def DateCheck(self, event):
        # Function validating of Calendar
        delta = timedelta(days=1)
        if self.start_date.selection_get()==datetime.date.today():
            self.start_date.selection_set(self.start_date.selection_get()-delta)
        if self.start_date.selection_get()>=self.end_date.selection_get():
            self.end_date.selection_set(self.start_date.selection_get()+delta)

    def createMoneyList(self):
        # Function to create child window
        moneyList = ChildWindow(self.root, 500, 350, 'money list')
        start_date = self.start_date.selection_get()
        end_date = self.end_date.selection_get()
        step=timedelta(days=self.interval.get())
        moneyList.run(start_date, end_date, step)


class ChildWindow:
    def __init__(self, parent,  width, height, title='Change rates', resizable=(False, False), icon=None):
        self.root = tk.Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+200+50')
        self.root.resizable(resizable[0], resizable[1])
        self.root.grab_set()

    def run(self, start, end, delta):
        self.start, self.end, self.delta = start, end, delta
        self.creareList()

    def creareList(self):
        #Function to choose valutes in choosen time interval
        # valute list depend from  date
        self.check, self.money = self.showValutes()
        okBut = tk.Button(self.root, text='Go', fg='blue', command=self.onClickCheckBtn)
        okBut.grid(column=2, row=30, pady=10)
        self.quit = tk.Button(self.root, text="Get back to dates", fg="red",
                              command=self.root.destroy).grid(column=3, columnspan=2, row=30, pady=10)

    def showValutes(self):
        # This function is drawing checkboxes of valutes and add that objects in the same dictionaky as nomeylist
        start_date = self.start
        self.moneyRate = MoneyRates()
        money, nameMoney = self.moneyRate.make_money_list(start_date)
        moneyRes = money.copy()
        row=1
        col=1
        for i, key  in enumerate(money):
            variable = tk.BooleanVar()
            variable.set(0)
            label = '{} : {}'.format(key, nameMoney[key])
            checkMoney = tk.Checkbutton(self.root, variable=variable, text=label)
            checkMoney.grid(row=row, column=col, sticky='W')
            moneyRes.update({key:variable})
            if (i+1)%3==0:
                row+=1
                col=1
            else:
                col+=1
        return moneyRes, money

    def onClickCheckBtn(self):
        # This function find all rates of choosen valutes and draw it
        money = self.money.copy()
        for key in self.check:
            val = self.check.get(key)
            if val.get()==True:
                pass
            elif val.get()==False:
                money.pop(key)
            else:pass
        rates, dates = self.moneyRate.find_all_rates(self.start, self.end, money, self.delta)
        paint = PaintingRates()
        paint.painting(rates, dates)



if __name__ == '__main__':
    app = Window(width=500, height=330)
    app.run()