

class Calculate:
    def __init__(self, amount, period, intrate):
        self.amount  = int(amount)
        self.period = int(period)
        self.intrate = int(intrate)


    def loan_pars(self):

        per_month = self.amount/self.period

        balance = []
        for _ in range(self.period):
            self.amount -= per_month
            balance.append(self.amount)

        interest = []

        for x in balance:
            x = x + per_month
            intr = x  * self.intrate
            intr = intr / per_month
            intr = intr / 12
            interest.append(intr)

        total = []

        for x in interest:
            tot = per_month + x
            total.append(tot)

        per_month_table = [per_month for i in range(self.period)]
        month = [i+1 for i in range(self.period)]

        loan_pars = {'Month': month,'per_month':per_month_table, 'balance_p_month': balance, 'interest_p_month':interest, 'total_p_month':total}

        return loan_pars, [month, per_month_table, balance, interest, total]




