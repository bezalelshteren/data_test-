import pandas as pd
import json



class reader:
    def __init__(self):
        self.data =pd.read_csv("C:/Users/User/exe python/data_test/data/tweets_dataset.csv")
        self.data_table = pd.DataFrame(self.data)
        self.isnt_anti = None
        self.is_anti = None


    def split_by_biased(self):
        self.isnt_anti = self.data_table[self.data_table["Biased"] == 0]
        self.is_anti = self.data_table[self.data_table["Biased"] == 1]
        return self.data_table,self.isnt_anti ,self.is_anti


class tweetCleaner:
    def __init__(self, data_table):
        self.data_table = data_table
        self.last_data_table = None


    def remove_columns(self):
        self.last_data_table = self.data_table[["Text","Biased"]].copy()

    def clean_text(self):
       self.last_data_table["Text"] = self.last_data_table["Text"].apply(self.cleaner)

    def cleaner(self,data):
        text = str(data).lower()
        temp = ["!","@","#","$","%","^","&","*","(",")","_","-","+",'=','?','>','<','"',':',";"]
        text1 = " "
        for char in temp:
            text1 = text.replace(char," ")
        return text1

    def return_as_csv(self):
        self.last_data_table.to_csv("cleaned_dataset_tweets.csv")



class tweetAnalyzer:
    def __init__(self, data_table, is_anti, isnt_anti):
        self.data_table = data_table
        self.is_anti = is_anti
        self.isnt_anti = isnt_anti


    def return_the_sum_mess(self):
        len_of_all_data = len(self.data_table)
        len_of_isnt = len(self.isnt_anti)
        len_of_is =  len(self.is_anti)
        return {"len_of_all_data":len_of_all_data,"len_of_isnt":len_of_isnt ,"len_of_is":len_of_is}

    def return_avg_length(self,data):
        total_len = 0
        counter = 0
        for i, row in data.iterrows():
            msg_len = len(row["Text"])
            total_len += msg_len
            counter += 1
        avg = total_len / counter
        return {"avg":avg}

    def return_the_most_len_mess(self,data):
        results = []
        lengths = {}
        for i, row in data.iterrows():
            length = len(row["Text"].split())
            lengths[length] = row["Text"]
        for i in range(3):
            max_len = max(lengths)
            results.append(lengths[max_len])
            lengths.pop(max_len)
        return {"the tree most length":results}


    def return_the_most_common(self):
        max1 = []
        dict_of_common = {}
        op = self.data_table["Text"].to_string().split(" ")

        for i in op:
            if i not in dict_of_common:
                dict_of_common[i] = 1
            else:
                dict_of_common[i] += 1

        for _ in range(10):
            max_word = max(dict_of_common, key=dict_of_common.get)
            max1.append(max_word)
            dict_of_common.pop(max_word)

        return max1

    def sum_upper(self,data):
        sum = 0
        string_all = data.to_string().split()
        for word in string_all:
            if word.isupper():
                sum += 1
        return {"the sum":sum}


    def return_in_jison(self):
        data = {"the sum of len  " :self.return_the_sum_mess(),
                "the avg of words per tweet  ":[self.return_avg_length(self.data_table),self.return_avg_length(self.is_anti),self.return_avg_length(self.isnt_anti)],
                "return the 3 most len tweet":[self.return_the_most_len_mess(self.data_table),self.return_the_most_len_mess(self.is_anti),self.return_the_most_len_mess(self.isnt_anti)],
                "return the 10 most common":self.return_the_most_common(),
                "return the sum upper":[self.sum_upper(self.data_table),self.sum_upper(self.is_anti),self.sum_upper(self.isnt_anti)]
                }
        json_output = json.dumps(data)
        return json_output


read = reader()
data_table, is_anti, isnt_anti = read.split_by_biased()
analyzer = tweetAnalyzer(data_table, is_anti, isnt_anti)

print(analyzer.return_in_jison())
clean = tweetCleaner(data_table)
clean.remove_columns()
clean.clean_text()
clean.return_as_csv()