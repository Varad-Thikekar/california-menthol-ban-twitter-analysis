# import ujson
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
import json


class ecigFiltering:
    # keywords = ['menthol', 'mentholated', 'menthols', 'methol', 'methols', 'cigarette', 'cigarettes', 'cig']
    keywords = [['ban','menthol'],['ban','menthols'],['banned','menthols'],['banned','menthol'],
                ['ban','mentholcigarette'],['ban','mentholcigarettes'],['banned','mentholcigarettes'],['banned','mentholcigarette'],
                ['prohibit','menthol'],['prohibit','menthols'],['prohibited','menthols'],['prohibited','menthol'],
                ['prohibit','mentholcigarette'],['prohibit','mentholcigarettes'],['prohibited','mentholcigarettes'],['prohibited','mentholcigarette'],
                ['get rid of','menthol'],['get rid of','menthols'],['got rid of','menthols'],['got rid of','menthol'],
                ['get rid of','mentholcigarette'],['get rid of','mentholcigarettes'],['got rid of','mentholcigarettes'],['got rid of','mentholcigarette'],
                ['fda','ban'],['fda','banned'],['food and drug administration','ban'],['food and drug administration','banned'],['food & drug administration','ban'],['food & drug administration','banned'],
                ['fda','prohibit'],['fda','prohibited'],['food and drug administration','prohibit'],['food and drug administration','prohibited'],['food & drug administration','prohibit'],['food & drug administration','prohibited'],
                ['fda','get rid of'],['fda','got rid of'],['food and drug administration','get rid of'],['food and drug administration','got rid of'],['food & drug administration','get rid of'],['food & drug administration','got rid of'],
                ['fda','rule'],['fda','ruled'],['food and drug administration','rule'],['food and drug administration','ruled'],['food & drug administration','rule'],['food & drug administration','ruled'],
                ['fda','policy'],['fda','policies'],['food and drug administration','policy'],['food and drug administration','policies'],['food & drug administration','policy'],['food & drug administration','policies']]
    # count=0

    def main(self):
        self.filter_ecig()

    def contains(self, line):  # detect whether those ecig-related keywords are in the Twitter contenct
        string = ""
        if "delete" not in line:
            try:
                is_retweet = True if (line["text"].startswith("RT @")) else False
            except:
                # self.count+=1
                return False
            if "retweeted_status" in line:
                if is_retweet:
                    return False

                else:
                    string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]
            else:
                string = line["extended_tweet"]["full_text"] if "extended_tweet" in line else line["text"]

        string = string.lower()  # make the tweets in lower case
        # string = word_tokenize(string)   #tokienize the tweets by space

        for k1,k2 in self.keywords:
            if k1 in string and k2 in string:
                return True
        return False

    def filter_ecig(self):
        with open("paper_filter_tweets.json", 'w') as output:  # Output filename changed to .txt
            with open("cig_iqos_twitter_crawl_20211212_20230314.txt", 'r') as src:  # Input filename changed to .txt
                for line in src:
                    # print(line)
                    temp = json.loads(line)
                    if self.contains(temp):
                        # print('yes')
                        output.write(line)



if __name__ == '__main__':
    ecigFiltering().main()
