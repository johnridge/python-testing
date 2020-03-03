with open(indata) as k:
    portfolio_data = list(k.read().splitlines())
for i in range(len(portfolio_data)):
    portfolio_data[i] = list(portfolio_data[i])