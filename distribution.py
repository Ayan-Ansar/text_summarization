import matplotlib.pyplot as plt 
from datapreprocessing import CleanData
import pandas as pd 
import numpy as np

if __name__ == "__main__":
    CD = CleanData()
    df = CD.getData()

    text_word_count = []
    summary_word_count = []

    # populate the lists with sentence lengths
    for i in df['cleaned_text']:
        text_word_count.append(len(i.split()))

    for i in df['cleaned_summary']:
        summary_word_count.append(len(i.split()))

    fig, ax = plt.subplots()
    length_df = pd.DataFrame({'text':text_word_count, 'summary':summary_word_count})
    length_df.hist(bins = 30, ax=ax)
    fig.suptitle(f'length of text: {round(np.quantile((np.array(text_word_count)), 0.95))} , length of summary: {round(np.quantile((np.array(summary_word_count)), 0.95))}')
    fig.savefig('AvgLength.png')


