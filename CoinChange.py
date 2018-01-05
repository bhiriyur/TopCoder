class CoinChange:
    def __init__(self):
        self.denominations = (1, 5, 10, 25, 100)
        self.coins = ('penny', 'nickel', 'dime', 'quarter', 'dollar')
        pass

    def find_change(self, val):
        N = len(self.denominations)
        remainder = val
        result = ''
        num_coins = 0
        for i in range(N, 0, -1):
            denom = self.denominations[i-1]
            num_denom, remainder = self.find_change_denom(remainder, denom)
            num_coins += num_denom
            if num_denom > 0:
                result += " {} {}".format(num_denom, self.coins[i-1])
            if remainder == 0:
                break

        result += " | TOTAL = {}".format(num_coins)
        return result


    def find_change_denom(self, val, denom):
        return int(val/denom), val%denom


M = CoinChange()
value = 17
print(value, " ANSWER = ", M.find_change(value))