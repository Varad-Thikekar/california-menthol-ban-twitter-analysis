

import ujson

class Duplicate_Removal:

    unique_values = set()
    def main(self):
        self.remove()

    def check(self,line):
        # string = ""
        # if "delete" not in line:
        #     is_retweet = True if (line["text"].startswith("RT @")) else False
        #     if "retweeted_status" in line:
        #         if is_retweet:
        #             return False
        #             # if "extended_tweet" in line["retweeted_status"]:
        #             #     string = line["retweeted_status"]["extended_tweet"]["full_text"]
        #             # else:
        #             #     string = line["retweeted_status"]["text"]
        #         else:
        #             string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]
        #     else:
        #         string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]
        #
        # string = string.lower()
        # if string in self.unique_values:
        #     return False
        # else:
        #     self.unique_values.add(string)
        #     return True

        tweet_id = line['id']
        if tweet_id in self.unique_values:
            return False
        else:
            self.unique_values.add(tweet_id)
            return True


    def remove(self):


        # with open("new_filtered_promo_tweets.json", 'w') as output:  # Output filename changed to .txt
        #     with open("filtered_promo_tweets.json", 'r') as src:

        with open("new_filtered_promo_tweets.json", 'w') as output:  # Output filename changed to .txt
            with open("filtered_promo_tweets.json", 'r') as src:

                for line in src:
                    parsedJsonRecord = ujson.decode(line)
                    if self.check(parsedJsonRecord):
                        output.write(ujson.dumps(parsedJsonRecord) + '\n')
        output.close()
        src.close()


if __name__ == '__main__':
    Duplicate_Removal().main()