import pandas as pd

# Создание DataFrame исходных данных
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

print(data)

# Создание one hot encoding для столбца 'whoAmI' без использования get_dummies
categories = data['whoAmI'].unique()
for category in categories:
    data[category] = (data['whoAmI'] == category).astype(int)

# Удаление столбца 'whoAmI'
data = data.drop('whoAmI', axis=1)

# Вывод преобразованного DataFrame
print(data)