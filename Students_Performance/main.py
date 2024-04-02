import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Students_Performance.csv')

#1
print(data.iloc[61:77])

#2
senior_school_reading = data[(data['parental level of education'] == 'high school') & (data['test preparation course'] == 'completed')].head(5)
print(senior_school_reading)

#3
preparatory_passed = data[data['test preparation course'] == 'completed'].groupby('race/ethnicity').size()
print(preparatory_passed)

#4
min_writing_score = data['writing score'].min()
max_writing_score = data['writing score'].max()
print("Минимальный балл за письмо:", min_writing_score)
print("Максимальный балл за письмо:", max_writing_score)

#5
plt.hist(data['reading score'], bins=10, edgecolor='black')
plt.xlabel('Баллы за чтение')
plt.ylabel('Количество студентов')
plt.title('Распределение баллов за чтение')
plt.show()

#6
plt.hist(data['writing score'], bins=10, edgecolor='black')
plt.xlabel('Баллы за письмо')
plt.ylabel('Количество студентов')
plt.title('Распределение баллов за письмо')
plt.show()