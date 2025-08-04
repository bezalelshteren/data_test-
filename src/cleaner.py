from os.path import split

import pandas as pd
import numpy as np

class clean_the_data:
    def __init__(self):
        data_table =pd.read_csv("C:/Users/User/exe python/data_test/data/tweets_dataset.csv")
        self.data_table = pd.DataFrame(data_table)
        self.isnt_anti = None
        self.is_anti = None


    def split_the_data_by_biased(self):
        # since = ["@", "!", "#", "$", "?", ":", ",", ".","/","_"]
        # self.data_table = self.data_table.replace(since, " ")
        self.isnt_anti = self.data_table[self.data_table["Biased"]==0]
        self.is_anti =self.data_table[self.data_table["Biased"]==1]
        # print(self.isnt_anti)
        # print(self.is_anti)
        return self.isnt_anti,self.is_anti


    def return_the_sum_mess(self):
        len_of_all_messeges = len(self.data_table)
        len_of_sum_messeges_is_antisemic = len(self.isnt_anti)
        len_of_sum_messeges_isnt_antisemic = len(self.is_anti)
        return len_of_all_messeges,len_of_sum_messeges_is_antisemic,len_of_sum_messeges_isnt_antisemic


    def return_the_average_of_len_mess_in_isnot(self):
        len_of_all_messeges_in_isnot = 0
        counter = 0
        the_most_len = ""
        for i,t in self.isnt_anti.iterrows():
            if len(t) > len(the_most_len):
                the_most_len = t

            len_of_all_messeges_in_isnot += len(t["Text"])
            print(len_of_all_messeges_in_isnot)
            counter +=1
            print(counter)
        print("--------------------")
        print(len_of_all_messeges_in_isnot/counter)
        print(the_most_len["Text"])


    def return_the_average_of_len_mess_in_is(self):
        len_of_all_messeges_in_is = 0
        counter = 0
        the_most_len = ""
        for i, t in self.is_anti.iterrows():
            if len(t) > len(the_most_len):
                the_most_len = t

            len_of_all_messeges_in_is += len(t["Text"])
            # print(len_of_all_messeges_in_is)
            counter += 1
            # print(counter)
        print("--------------------")
        print(len_of_all_messeges_in_is / counter)
        print(the_most_len["Text"])



    def return_the_most_len_mess(self):
        y = [self.data_table,self.is_anti,self.isnt_anti]
        oppo = []
        for i in y:
            count = 0
            len1 = 0
            the_lengest =[]
            dict_to_check = {}
            for idx, tweet in enumerate(i["Text"]):
                count += len(tweet.split())
                length = len([word for word in tweet])
                len1+=length
                dict_to_check[length] = tweet
            for i in range(3):
                max_len = max(dict_to_check)
                the_lengest.append(dict_to_check[max_len])
                dict_to_check.pop(max_len)
            rt = len1/count
            oppo.append(the_lengest)
            oppo.append("==============================================================")
            oppo.append(rt)
        return oppo



    def return_the_most_common(self):
        max1 = []
        t = 0
        dict_of_common = {}
        dict_of_upper = {}
        op = self.data_table["Text"].to_string().split(" ")
        for i in op:
            iii = op.is_lower().sum()
            t+= iii
            if i not in dict_of_common:
                dict_of_common[i] = 1
            elif i in dict_of_common:
                dict_of_common[i] += 1
        for i in range(10):
            pp = max(dict_of_common.values())
            max1.append(dict_of_common[pp])
            # dict_of_common.pop(pp)
        print(t)
        return max1

    # def chainge_to_json(self):
    #     with open("cleaned_dataset_tweets.csv","W")as file:


    # def return_bisike_info(self):
    #     print(self.data_table.value_counts("Biased"))


c = clean_the_data()

c.split_the_data_by_biased()
print(c.return_the_most_len_mess())
print(c.return_the_most_common())
# print(c.chainge_to_json())

