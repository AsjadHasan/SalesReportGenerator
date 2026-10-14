def generate_sales_report():
    sales_totals = {}
    units_sold = {}

    number_of_sales = int(input("Number of sales: "))

    for i in range(number_of_sales):
        salesperson = input("Salesperson: ")
        product = input("Product: ")
        amount = int(input("Amount: "))

        # Calculate total sales for each salesperson
        if salesperson in sales_totals:
            sales_totals[salesperson] += amount
        else:
            sales_totals[salesperson] = amount

        # Count units sold for each product
        if product in units_sold:
            units_sold[product] += 1
        else:
            units_sold[product] = 1

    # Find the top performer
    top_performer = max(sales_totals, key=sales_totals.get)
    top_sales = sales_totals[top_performer]

    print("\nSales totals:", sales_totals)
    print("Units sold:", units_sold)
    print(f"Top performer: {top_performer} ({top_sales})")


generate_sales_report()