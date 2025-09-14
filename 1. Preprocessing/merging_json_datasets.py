import ujson

unique_tweets = set()
with open('overall_dataset.json', 'w') as output:
    with open ('merged_us_tweets.json', 'r') as src:
        for temp in src:
            line = ujson.loads(temp)
            # string = ""
            # if "delete" not in line:
            #     is_retweet = True if (line["text"].startswith("RT @")) else False
            #     if "retweeted_status" in line:
            #         if is_retweet:
            #            continue
            #         else:
            #             string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]
            #     else:
            #         string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]
            #
            # string = string.lower()
            # unique_tweets.add(string)
            unique_tweets.add(line['id'])
            output.write(temp)

with open('overall_dataset.json', 'a') as output:
    with open('merged_cal_tweets.json', 'r') as src:
        for temp in src:
            line = ujson.loads(temp)
            # string = ""
            # if "delete" not in line:
            #     is_retweet = True if (line["text"].startswith("RT @")) else False
            #     if "retweeted_status" in line:
            #         if is_retweet:
            #            continue
            #         else:
            #             string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]
            #     else:
            #         string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]
            #
            # string = string.lower()
            # if string not in unique_tweets:
            #     unique_tweets.add(string)
            #     output.write(temp)

            tweet_id = line['id']
            if tweet_id not in unique_tweets:
                unique_tweets.add(tweet_id)
                output.write(temp)



