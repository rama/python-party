import re


def portfolio_cost(file_name):
    with open(file_name) as file:
        total_cost = 0
        for line in file:
            # line.split() splits on any number of whitespaces
            # but we like ours better! because we put in the EFFORT
            _, quantity, price = re.split(r"[ ]+", line)
            try:
                # str -> num conversions drop whitespace like \n
                quantity = int(quantity)
                price = float(price)
            except ValueError as e:
                print(f"Couldn't parse: {line}", end="")
                print(e)
                continue
            except Exception as e:
                print(e)
                continue
            total_cost += quantity * price
        return total_cost


# comma after colon for comma-separated numbers!
print(f"Total portfolio cost: ${portfolio_cost('Data/portfolio2.dat'):,.2f}")
# print(portfolio_cost("missing_portfolio.dat"))
