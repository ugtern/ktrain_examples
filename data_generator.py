import pandas as pd

data = ['привет', 'доброе утро', 'добрый день', 'здравствуйте',
        'пока', 'досвидания', 'хорошего дня']

labels = []
j = 0
while j < 20:
        for i in range(len(data)):
                labels.append('hi') if i <4 else labels.append('by')
        j += 1

print(labels)
data = data * 20

df = pd.DataFrame({'message': data, 'class': labels})
df.to_csv('train_data.csv')
