import csv
import json
import os


def process_and_write_tweets(src_file, filter_name, location_name, writer, recorded_tweets):
    """
    Processes tweets from a single JSON file and writes them to a CSV,
    avoiding duplicates.
    """
    try:
        with open(src_file, 'r') as src:
            for tweet_line in src:
                try:
                    line = json.loads(tweet_line)
                    tweet_id = line['id']

                    if tweet_id not in recorded_tweets:
                        recorded_tweets.add(tweet_id)

                        time = line['created_at']
                        user_id = line['user']['id']
                        string = ""

                        if "delete" not in line:
                            is_retweet = True if (line.get("text", "").startswith("RT @")) else False
                            if "retweeted_status" in line:
                                if is_retweet:
                                    continue
                                else:
                                    string = line.get("extended_tweet", {}).get("full_text", line.get("text", ""))
                            else:
                                string = line.get("extended_tweet", {}).get("full_text", line.get("text", ""))

                        string = string.lower()
                        writer.writerow([tweet_id, time, user_id, string, filter_name, location_name])

                except json.JSONDecodeError:
                    print(f"Skipping a malformed line in {src_file}.")
                except KeyError as e:
                    print(f"Skipping tweet in {src_file} due to missing key: {e}")

    except FileNotFoundError:
        print(f"Error: The file {src_file} was not found.")


def create_combined_tweet_file():
    """
    Combining tweets from multiple source files.
    """
    files_to_process = [
        ('tempcal.json', 'Paper keywords', 'California'),
        ('tempcal2.json', 'Product keywords', 'California'),
        ('temp.json', 'Paper keywords', 'US'),
        ('temp2.json', 'Product keywords', 'US'),
    ]

    with open('Data_File.csv', 'w', newline='', encoding='utf-8') as output:
        writer = csv.writer(output)
        writer.writerow(['ID', 'Time', 'User', 'Text', 'Filter', 'Location'])
        recorded_tweets = set()

        for src_file, filter_name, location_name in files_to_process:
            process_and_write_tweets(src_file, filter_name, location_name, writer, recorded_tweets)

    print("Successfully created 'Data_File.csv' with all unique tweets.")


if __name__ == "__main__":
    create_combined_tweet_file()