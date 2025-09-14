import pandas as pd
import json

class JuulFilter:

    def main(self):
        self.juulfilter()

    def check(self, line):
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

        string = string.lower()

        if 'juul' not in string:
            return True

    def juulfilter(self):
        with open('product_juul_filtered.json','w') as output:
            with open('new_filtered_promo_tweets.json','r') as src:
                for line in src:
                    temp= json.loads(line)
                    if self.check(temp):
                        output.write(line)
            src.close()
        output.close()



if __name__ == '__main__':
    JuulFilter().main()