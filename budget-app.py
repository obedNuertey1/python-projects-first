class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        result = f"{self.name.center(30, '*')}\n"
        for item in self.ledger:
            amount = "{:.2f}".format(item['amount'])
            description = item['description'][:23]
            result += f"{description:<23}{amount:>7}\n"
        total = self.get_balance()
        result += f"Total: {total:.2f}"
        return result

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.name}")
            budget_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount


def create_spend_chart(categories):
    total_spent = 0
    category_spent = []

    # Calculate spending per category
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        category_spent.append((category.name, spent))
        total_spent += spent

    # Calculate percentages
    percentages = [(name, int((spent / total_spent) * 100)) for name, spent in category_spent]

    # Build the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for _, percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    # Add horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Add category names
    max_name_length = max(len(name) for name, _ in percentages)
    category_names = [name.ljust(max_name_length) for name, _ in percentages]
    for i in range(max_name_length):
        chart += "     "  # Padding
        for name in category_names:
            chart += f"{name[i]}  "
        if i < max_name_length - 1:
            chart += "\n"

    return chart


# Example usage
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.55, 'new shoes')
clothing.withdraw(100, 'jacket')
entertainment = Category('Entertainment')
entertainment.deposit(1000, 'initial deposit')
entertainment.withdraw(150, 'concert tickets')

print(food)
print(create_spend_chart([food, clothing, entertainment]))
