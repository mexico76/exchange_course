from forex_python.converter import CurrencyRates, CurrencyCodes
import matplotlib.pyplot as plt

class MoneyRates():
    c = CurrencyRates()
    cc = CurrencyCodes()
    dates = []
    def make_money_list(self, start_date):
        # Get names of the money
        valute = self.c.get_rates('USD', start_date)
        valuteNames = valute.copy()
        # Make clear dict with keys is list
        for key in valute:
            valuteNames[key] = self.cc.get_currency_name(key)
            valute[key]=[]
        return valute, valuteNames

    def find_all_rates(self, start_date, end_date, valute, step):
        # Fill course_all_time data
        dates=[]
        while start_date<=end_date:
            dates.append(start_date) #.strftime('%d.%m.%Y'))
            course = self.c.get_rates('USD', start_date)
            for key in valute:
                try:
                    valute.get(key).append(course.get(key))
                except AttributeError:
                    valute.get(key).append(0)
            start_date += step
        return valute, dates


# Writing with matplotlib
class PaintingRates():
    def painting(self, rates, dates):
        fig, ax1 = plt.subplots(1, 1, figsize=(16,8), facecolor='white', dpi= 80)
        for key in rates:
            value = rates.get(key)
            lines = ax1.plot(dates, value, label=key)
            plt.setp(lines, linewidth=2)
        ax1.set_xlabel('Dates')
        ax1.set_ylabel('Exchange rates')
        ax1.set_title('Exchange rates to USD')
        ax1.legend()
        ax1.grid(which='both')
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()