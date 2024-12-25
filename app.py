import pandas as pd

df = pd.read_csv('diamonds.csv')
colors = []

def high_price():
    high_price = 0
    for price in df['price'].values:
        if price > high_price:
            high_price = price
    return high_price

def Average_price():
    Average_price = 0
    for price in df['price'].values:
        Average_price += price
    return (Average_price / len(df['price']))

def ideal_counter():
    ideal_counter = 0
    for cut in df['cut'].values:
        if cut == 'Ideal':
            ideal_counter += 1
    return ideal_counter

def colors_name():
    global colors
    for item in df['color'].values:
        if item not in colors:
            colors.append(item)
    colors_sum()
    return

def colors_sum():
    global colors
    sum_colors = [0,0,0,0,0,0,0]
    for index, color in enumerate(colors):
        for name_of_color in df['color'].values:
            if name_of_color == color:
                sum_colors[index] += 1
        print(f"ther are {sum_colors[index]} from the color {color}")
    return


if __name__=="__main__":
    
    print(f"1. the high price is {high_price()}")
    print(f"2. the Average price is {Average_price()}")
    print(f"3. the sum of the ideal is {ideal_counter()}")
    print("4. ")
    colors_name()
    
