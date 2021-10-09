import pandas

df = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

fur_colors = ["Gray", "Cinnamon", "Black"]
counts = []

for color in fur_colors:
    counts.append(len(df[df["Primary Fur Color"] == color]))

squirrel_data = {
    "Fur Color": fur_colors,
    "Count": counts
}

data = pandas.DataFrame(squirrel_data)
data.to_csv('squirrel_count.csv')
