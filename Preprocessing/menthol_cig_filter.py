# import ujson
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import json


class ecigFiltering:

    keywords = ['menthol', 'mentholated', 'menthols', 'methol', 'methols', 'cigarette', 'cigarettes', 'cig']
    # count=0

    def main(self):
        self.filter_ecig()

    def contains(self, line):  #detect whether those ecig-related keywords are in the Twitter contenct
        string = ""
        if "delete" not in line:
            try: is_retweet = True if (line["text"].startswith("RT @")) else False
            except:
                # self.count+=1
                return False
            if "retweeted_status" in line:
                if is_retweet:
                    return False

                    # Removing retweets since they have the same content as the original tweet
                    # if "extended_tweet" in line["retweeted_status"]:
                    #     string = line["retweeted_status"]["extended_tweet"]["full_text"]
                    # else:
                    #     string = line["retweeted_status"]["text"]
                else:
                    string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]
            else:
                string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]
        
        string = string.lower()   #make the tweets in lower case
        # string = word_tokenize(string)   #tokienize the tweets by space
        
        # if any(s == string[i] for s in self.keywords for i in range(len(string))):
        #     return True
        for s in self.keywords:
            if s in string:
                return True
        return False

    def filter_ecig(self):
        with open("filtered_tweets.json", 'w') as output:  # Output filename changed to .txt
            with open("cig_iqos_twitter_crawl_20211212_20230314.txt", 'r') as src:  # Input filename changed to .txt
                for line in src:
                    # print(line)
                    temp = json.loads(line)
                    if self.contains(temp):
                        # print('yes')
                        output.write(line)

    # TO CHECK THE NUMBER OF FAULTY TWEETS WITH NO LINE['TEXT']
    # def filter_ecig(self):
    #     # with open("filtered_tweets.json", 'w') as output:  # Output filename changed to .txt
    #     with open("cig_iqos_twitter_crawl_20211212_20230314.txt", 'r') as src:  # Input filename changed to .txt
    #         for line in src:
    #             # print(line)
    #             temp = json.loads(line)
    #             self.contains(temp)
    #     print(self.count) OUTPUT = 2



if __name__ == '__main__':
    ecigFiltering().main()
