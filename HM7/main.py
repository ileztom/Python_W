import pandas as pd
def main():
    price_list = pd.Series({'Вода': 40, 'Молоко': 90, 'Мука': 140, 'Масло':100 })
    data = {
        'product': ['Вода', 'Молоко', 'Мука', 'Масло'],
        'price': [price_list['Вода'], price_list['Молоко'], price_list['Мука'], price_list['Масло']],
        'number': [5, 2, 1, 2],
    }
    df = pd.DataFrame(data)
    df['cost'] = df['price'] * df['number']
    print(df)
main()