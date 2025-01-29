import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('streaming_data.csv')

# Display summary statistics
print("\nYour Year in Music Summary:")
print('\nAverage Completion Rate:')
completion_rate = df['completion_rate'].mean()
print(completion_rate)
print("\nTotal Listening Time (seconds):")
total_time = df['duration_seconds'].sum()
print(total_time)
print("\nTop Artists:")
top_artists = df['artist'].value_counts().head(5)
print(top_artists)
print("\nTop Songs:")
top_songs = df['song'].value_counts().head(10)
print(top_songs)
print("\nTop Genres:")
top_genres = df['genre'].value_counts()
print(top_genres)

print('\n Month and Day of Week Analysis')
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
day_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# Convert month and day columns to Categorical with custom ordering
df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=day_order, ordered=True)
days = df['day_of_week'].value_counts().sort_index()
months = df['month'].value_counts().sort_index()
print(days)
print(months)

plt.figure(figsize=(8, 5)) 

days.plot(kind='bar')
plt.title('Amount of Songs by Day')
plt.xlabel('Day of Week')
plt.ylabel('Count')
plt.savefig("bar_chart.png")

plt.figure()
months.plot(kind='line')
plt.title('Amount of Songs by Day')
plt.xlabel('Month')
plt.ylabel('Count')
plt.savefig("line_graph.png")

plt.figure()
plt.hist(df['duration_seconds'], color='skyblue', edgecolor='black')
plt.title('Frequency of Song Duration')
plt.xlabel('Bin')
plt.ylabel('Count')
plt.savefig('histogram.png')