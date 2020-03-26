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
