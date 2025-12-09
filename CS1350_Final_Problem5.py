def analyze_sales(sales_data):
    """
    Analyze sales data using map, filter, and lambda functions.
    """

    with_revenue = list(map(lambda item: {
        **item,
        'revenue': item['quantity'] * item['price']
    }, sales_data))

    total_revenue = sum(item['revenue'] for item in with_revenue)

    high_value_items = list(filter(lambda item: item['revenue'] > 100, with_revenue))

    low_stock_items = list(filter(lambda item: item['quantity'] < 10, with_revenue))

    average_price = sum(map(lambda item: item['price'], with_revenue)) / len(with_revenue) if with_revenue else 0

    return {
        'total_revenue': total_revenue,
        'high_value': [item['product'] for item in high_value_items],
        'low_stock': [item['product'] for item in low_stock_items],
        'average_price': round(average_price, 2)
    }
