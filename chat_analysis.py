import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
import datetime as dt

# Obtain df from cleaning.py file
df = pd.read_csv('df.csv')

chats_df = df[df['interaction_type'] == 'chats'].copy()

chat_body_rows = []

for df_index, info in chats_df.iterrows():
    id = info['id']
    chat_body_time = info['details']

# Will have multiple rows for each id if >1 chat sent.
    for chat in chat_body_time: 
        body = chat.get('body','')
        time = chat.get('timestamp','')
        chat_body_rows.append({'id': id, 'chat_body': body, 'timestamp': time})

chats_df = pd.DataFrame(chat_body_rows)

# Creating word cloud
stopwords = [INSERT_STOP_WORDS] # Depends on words you tend to use a lot but hold little meaning, for example "like" or "and"

text = " ".join(chats_df['chat_body']) # strings
words = text.split() # list of words split at spaces
long_words = [word for word in words if len(word) > 1]
cleaned_text = " ".join(long_words)

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',
    prefer_horizontal = 1,
    stopwords = stopwords,
).generate(cleaned_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# Creating dataframe to see how many times a day a message is sent
chats_df['timestamp'] = pd.to_datetime(chats_df['timestamp'])
chats_df['date'] = chats_df['timestamp'].dt.date

count_by_date = chats_df['date'].value_counts()
chats_dates_df = count_by_date.reset_index()

chats_dates_df.columns = ['date', 'count']
chats_dates_df = chats_dates_df.sort_values(by = 'date', ascending = True)

# Plotting date vs number of outgoing messages. Can also use seaborn
plt.figure(figsize = (12,5))
plt.plot(chats_dates_df['date'], chats_dates_df['count']);

plt.xticks(rotation=45);
plt.minorticks_on()
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Outgoing messages per day');
plt.xlim([dt.date([YEAR, MONTH, DATE]) dt.date([YEAR, MONTH, DATE]) # Not necessary, but I liked how it looked visually with x-axis boundaries

# Adding to dataframe to explore the time of day messages are sent
chats_df['time'] = chats_df['timestamp'].dt.time # Set to proper date-time format for Python to read

# I categorized late night as 10PM-4:59AM, morning as 5AM-10:59AM, Afternoon as 11AM-4:59PM, and evening as 5PM-9:59PM
time_period = []

for index, info in chats_df.iterrows():
    if dt.time(22, 0, 0) <= info['time'] and info['time'] <= dt.time(23, 59, 59):
        time_period.append('late night')
    if dt.time(0, 0, 0) <= info['time'] and info['time'] <= dt.time(4, 59, 59):
        time_period.append('late night')
    if dt.time(5, 0, 0) <= info['time'] and info['time'] <= dt.time(10, 59, 59):
        time_period.append('morning')
    if dt.time(11, 0, 0) <= info['time'] and info['time'] <= dt.time(16, 59, 59):
        time_period.append('afternoon')
    if dt.time(17, 0, 0) <= info['time'] and info['time'] <= dt.time(21, 59, 59):
        time_period.append('evening')
chats_df['time_period'] = time_period

# Creating a time period vs count dataframe for visualization
time_period_dict = {
    'late_night': 0,
    'morning': 0,
    'afternoon': 0,
    'evening': 0
}

for index, info in chats_df.iterrows():
    if info['time_period'] == 'late night':
        time_period_dict['late_night'] += 1
    if info['time_period'] == 'morning':
        time_period_dict['morning'] += 1
    if info['time_period'] == 'afternoon':
        time_period_dict['afternoon'] += 1
    if info['time_period'] == 'evening':
        time_period_dict['evening'] +=1

time_period_df = pd.DataFrame.from_dict(time_period_dict, orient = 'index').reset_index()
time_period_df.rename({'index': 'time_period', 0: 'count'}, axis = 1, inplace = True)

# Plotting time period vs count
plt.figure(figsize = (10,5))
plt.bar(
    x = 'time_period',
    height = 'count',
    data = time_period_df,
    width = 0.6,
    color = 'pink',
    edgecolor = 'black',
    tick_label = ['Late night (10PM-4:59AM)', 'Morning (5AM-10:59AM)', 'Afternoon (11AM-4:59PM)', 'Evening (5PM - 10:59PM)']);

plt.xlabel('Time Period')
plt.ylabel('Count')
plt.title ('Messages sent per time frame');
