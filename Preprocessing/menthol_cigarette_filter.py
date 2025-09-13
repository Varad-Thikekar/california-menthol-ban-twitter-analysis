import ujson
import pandas as pd
import nltk
import json

class ecigFiltering:
    # keywords1 = set(['menthol', 'mentholated', 'menthols', 'methol', 'methols', 'cigarette', 'cigarettes', 'cig'])
    keywords1 = set(['menthol', 'mentholated', 'menthols', 'methol', 'methols'])
    keywords2 = set(['cigarette', 'cigarettes', 'cig'])

    def main(self):
        self.filter_ecig()

    def contains(self, line):  # detect whether those ecig-related keywords are in the Twitter contenct
        string = ""
        if "delete" not in line:
            is_retweet = True if (line["text"].startswith("RT @")) else False

            if "retweeted_status" in line:
                if is_retweet:
                    return False

                else:
                    string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]
            else:
                string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]

        string = string.lower()  # make the tweets in lower case
        # string = word_tokenize(string)  # tokienize the tweets by space

        for keyword1 in self.keywords1:
            if keyword1 in string:
                for keyword2 in self.keywords2:
                    if keyword2 in string:
                        return True

        return False

    def filter_ecig(self):
        # with open("menthol_cigarette_tweets.json", 'w') as output:
        with open("both_filters.json", 'w') as output:# Output filename changed to .txt
            # with open("new_filtered_promo_tweets.json", 'r') as src:  # Input filename changed to .txt
            with open("filtered_tweets.json", 'r') as src:
                for line in src:
                    # print(line)
                    temp = json.loads(line)
                    if self.contains(temp):

                        output.write(line)
            src.close()
            output.close()



if __name__ == '__main__':
    ecigFiltering().main()
