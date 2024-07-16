
shopping_list = {
    'salad': {'lettuce': '1 head', 'tomatoes': '2 large', 'cucumbers': '1 large', 'red onion': '1 small', 'carrot': '2 medium'},
    'burger': {'ground beef': '1kg', 'burger buns': '4 buns', 'cheese slices': '4 slices', 'mustard': '1 bottle'},
    'waffle ice cream': {'waffle mix': '1 box', 'milk': '1 carton', 'ice cream': '1 pint', 'whipped cream': '1 can'}
}

for dish,ingredient in shopping_list.items():
    print(f"{dish} --> ingredients:")
    for item,quantity in ingredient.items():
        print(f"{item} - {quantity}")

