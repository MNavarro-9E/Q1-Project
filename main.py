from pyscript import display # pyright: ignore[reportMissingImports]


restaurant_name = "Rumiyeon's " #string
owner_name = "Sofia Navarro" #string
year_established = 2025 #int
popular_item_price = 200 #int
has_delivery = True #boolean
product_names = ['Spicy Buldak', 'Carbonara Buldak', 'Cheese Buldak', 'Spicy Jin Ramen', 'Mild Jin Ramen'] #list
business_hours = 'Open 10:00 - 22:00 ;)' #string
menu_prices = {
    'Spicy Buldak' : 200,
    'Carbonara Buldak' : 185,
    'Cheese Buldak' : 180,
    'Spicy Jin Ramen' : 85,
    'Mild Jin Ramen' : 80
}
common_allergens = ("wheat", "egg", "fish") #3 common allergens
tax_rate = 0.08 #float
#resto header display
display(restaurant_name, target="restaurant-name")
display(f'Owner Name: {owner_name}', target="owner-name")
display(f'Since {year_established}', target="year-established")

#displaying the product names & prices
display(product_names[0], target="row1col1") #product
display(f'Php {menu_prices["Spicy Buldak"]}', target="row1col2") #price

display(product_names[1], target="row2col1")
display(f'Php {menu_prices["Carbonara Buldak"]}', target="row2col2")

display(product_names[2], target="row3col1")
display(f'Php {menu_prices["Cheese Buldak"]}', target="row3col2")

display(product_names[3], target="row4col1")
display(f'Php {menu_prices["Spicy Jin Ramen"]}', target="row4col2")

display(product_names[4], target="row5col1")
display(f'Php {menu_prices["Mild Jin Ramen"]}', target="row5col2")

#restaurant hours
display(business_hours, target="resto-hours")