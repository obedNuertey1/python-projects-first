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
