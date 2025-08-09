import pandas as pd
import cleaner
import string


class reader:
    def __init__(self):
        self.data =pd.read_csv("C:/Users/User/exe python/data_test/data/tweets_dataset.csv")
        self.data_table = pd.DataFrame(self.data)

    def return_data(self):
        return self.data_table


class tweetCleaner:
    def __init__(self, data_table):
        self.data_table = data_table
        self.isnt_anti = None
        self.is_anti = None

    def clean_text(self, text):
        text = str(text).lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text

    def split_by_biased(self):
        self.data_table["Text"] = self.data_table["Text"].apply(self.clean_text)
        self.isnt_anti = self.data_table[self.data_table["Biased"] == 0]
        self.is_anti = self.data_table[self.data_table["Biased"] == 1]


class TweetAnalyzer:  # מחלקה לניתוח סטטיסטי של הציוצים
    def __init__(self, data_table, is_anti, isnt_anti):
        self.data_table = data_table
        self.is_anti = is_anti
        self.isnt_anti = isnt_anti

    def return_the_sum_mess(self):
        len_of_all_data = len(self.data_table)
        return len_of_all_data, len(self.isnt_anti), len(self.is_anti)

    def return_avg_length(self,):
        df = [self.data_table,self.is_anti,self.isnt_anti]
        avg_lis = []
        for data in df:
            total_len = 0
            counter = 0

            for i, row in data.iterrows():
                msg_len = len(row["Text"])
                total_len += msg_len
                counter += 1
            avg = total_len / counter
            avg_lis.append(avg)
            return avg_lis

    def return_the_most_len_mess(self):
        sections = [
             self.data_table ,self.is_anti, self.isnt_anti
        ]
        results = []
        for  df in sections:
            lengths = {}
            for i, row in df.iterrows():
                length = len(row["Text"].split())
                lengths[length] = row["Text"]
            for i in range(3):
                max_len = max(lengths)
                results.append(dict_to_check[max_len])
                lengths.pop(max_len)


        return results


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

    def sum_upper(self):
        sum = 0
        string_all = self.data_table.to_string().split()
        for word in string_all:
            if word.is_upper():
                sum += 1
        return sum


read = reader()
data_table = read.return_data()

clean = tweetCleaner(data_table)


analyzer = TweetAnalyzer(clean.data_table, is_anti, isnt_anti)
print(analyzer.return_the_sum_mess())
# print(analyzer.return_avg_length(is_anti))
# print(analyzer.return_avg_length(isnt_anti))
# print(analyzer.return_the_most_len_mess())
# print(analyzer.return_the_most_common())
