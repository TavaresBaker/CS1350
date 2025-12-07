class Pizza:
    price_list = {'small': 10, 'medium': 15, 'large': 20}
    topping_price = 2

    def __init__(self, size, toppings):
        if not self.validate_size(size):
            raise ValueError("Invalid size")
        self.size = size
        self.toppings = toppings

    def calculate_price(self):
        return self.price_list[self.size] + len(self.toppings) * self.topping_price

    def __str__(self):
        return f"{self.size} pizza with {len(self.toppings)} toppings"

    @classmethod
    def create_margherita(cls, size):
        return cls(size, ['cheese', 'tomato', 'basil'])

    @classmethod
    def create_pepperoni(cls, size):
        return cls(size, ['cheese', 'pepperoni'])

    @classmethod
    def create_veggie(cls, size):
        return cls(size, ['cheese', 'mushrooms', 'peppers', 'onions'])

    @staticmethod
    def validate_size(size):
        return size in ['small', 'medium', 'large']


class PizzaOrder:
    total_orders = 0

    def __init__(self):
        PizzaOrder.total_orders += 1
        self.order_id = f"ORDER_{PizzaOrder.total_orders:03}"
        self.pizzas = []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_total(self):
        return sum(p.calculate_price() for p in self.pizzas)

    def __str__(self):
        return f"Order {self.order_id} - Total: ${self.get_total()}"

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders


class OrderManager:
    @staticmethod
    def create_order_from_string(order_string):
        order = PizzaOrder()
        for item in order_string.split(','):
            parts = item.strip().split()
            size = parts[0]
            type_ = parts[1].lower()
            if type_ == "margherita":
                order.add_pizza(Pizza.create_margherita(size))
            elif type_ == "pepperoni":
                order.add_pizza(Pizza.create_pepperoni(size))
            elif type_ == "veggie":
                order.add_pizza(Pizza.create_veggie(size))
        return order

    @staticmethod
    def format_receipt(order):
        lines = ["=== RECEIPT ===", f"Order: {order.order_id}", "Items:"]
        for p in order.pizzas:
            lines.append(f"{p} - ${p.calculate_price()}")
        lines.append(f"Total: {order.get_total()}")
        lines.append("="*14)
        return '\n'.join(lines)


if __name__ == "__main__":
    pizza1 = Pizza.create_margherita("large")
    pizza2 = Pizza.create_pepperoni("medium")
    pizza3 = Pizza.create_veggie("small")

    print("Individual Pizzas:")
    for pizza in [pizza1, pizza2, pizza3]:
        print(f" {pizza} - ${pizza.calculate_price()}")

    order1 = PizzaOrder()
    order1.add_pizza(pizza1)
    order1.add_pizza(pizza2)
    print(f"\n{order1}")

    print("\nOrder from string:")
    order2 = OrderManager.create_order_from_string(
        "large pepperoni, small margherita, medium veggie"
    )
    print(OrderManager.format_receipt(order2))

    print(f"\nTotal orders created: {PizzaOrder.get_total_orders()}")
