# PLOTS FOR THE PAPER (Line chart comparing 2 datasets)

import pandas as pd
import matplotlib.pyplot as plt
import json


def load_and_process(file):
    tweet_data = []
    with open(file, 'r') as f:
        for line in f:
            tweet_data.append(json.loads(line))
    df = pd.DataFrame(tweet_data)
    df['created_at'] = pd.to_datetime(df['created_at'], format='%a %b %d %H:%M:%S %z %Y')
    df['month_year'] = df['created_at'].dt.to_period('M')
    monthly_tweets = df.groupby('month_year').size()

    labels = monthly_tweets.index.strftime('%Y-%m').tolist()
    x = list(range(len(labels)))
    y = monthly_tweets.values.tolist()

    return x, y, labels


# Load and process the first dataset
x1, y1, labels1 = load_and_process('overall_dataset.json')

# Load and process the second dataset
x2, y2, labels2 = load_and_process('merged_cal_tweets.json')

# Plotting the data
plt.figure(figsize=(9, 6))

# Plotting the first dataset
plt.plot(x1, y1, label='US', color='#1f77b4')

# Plotting the second dataset
plt.plot(x2, y2, label='California', color='#ff7f0e')

plt.xlabel('Date', fontsize=12, fontweight='bold')
plt.ylabel('Number of tweets per month', fontsize=12, fontweight='bold')
plt.xticks(x1, labels1, rotation=45)
plt.yticks(fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.legend()
plt.tight_layout()

plt.savefig('US_tweets.pdf', format='pdf')
plt.show()



# Bar chart for one dataset
# import pandas as pd
# import matplotlib.pyplot as plt
# import json
#
# # Load the JSON file into a DataFrame
# tweet_data=[]
# with open('merged_cal_tweets.json', 'r') as file:
#     for line in file:
#         tweet_data.append(json.loads(line))
# df = pd.DataFrame(tweet_data)
#
# # For overall dataset
# # df = pd.read_csv('Data_File.csv')
# # df['Time'] = pd.to_datetime(df['Time'],format='%a %b %d %H:%M:%S %z %Y')
# # df['month_year'] = df['Time'].dt.to_period('M')
#
# # Convert the 'created_at' column to datetime format
# df['created_at'] = pd.to_datetime(df['created_at'],format='%a %b %d %H:%M:%S %z %Y')
#
# # Extract the month and year from the 'created_at' column
# df['month_year'] = df['created_at'].dt.to_period('M')
#
# # Group by month_year and count the number of tweets in each group
# monthly_tweets = df.groupby('month_year').size()
# print(monthly_tweets.head())
#
# # Plotting the data
# plt.figure(figsize=(10, 6))
# monthly_tweets.plot(kind='bar', color='red')  # Adjust colors as desired
# plt.xlabel('Month-Year', fontsize=12, fontweight='bold')
# plt.ylabel('Number of Tweets', fontsize=12, fontweight='bold')
# plt.title('Monthly Tweets', fontsize=14, fontweight='bold')
# plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotating and aligning x ticks
# plt.yticks(fontsize=10)
# plt.grid(axis='y', linestyle='--', alpha=0.7)  # Adding grid lines
# plt.tight_layout()
# plt.show()
