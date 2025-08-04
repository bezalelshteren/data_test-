import pandas as pd
import cleaner


class cleaner1:
    def __init__(self):
        self.data_table = self.data_table

    def cl(self):
        since = ["@", "!", "#", "$", "?", ":", ",", ".", "/", "_"]
        self.data_table = self.data_table.replace(since, " ")