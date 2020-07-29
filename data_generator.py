import pandas as pd

data = ['привет', 'доброе утро', 'добрый день', 'おはようございます', 'здравствуйте',
        'пока', 'досвидания', 'хорошего дня', 'じゃあまた']

labels = []
for i in range(len(data)):
        labels.append('hi') if i <5 else labels.append('by')

print(labels)

df = pd.DataFrame({'message': [data], 'class': [labels]})
df.to_csv('train_data.csv')
