class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        result = f"{self.name.center(30, '*')}\n"
