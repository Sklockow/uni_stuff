import pandas as pd
from IPython.display import display, HTML

file ='companies.csv'

blue = 'rgb(168, 185, 255)'
yellow = 'rgb(253, 255, 135)'
green = 'rgb(181, 255, 199)'
red = 'rgb(255, 79, 79)'

HEADER={
    'net profit / equity': green
    ,'net profit / total assets': green 
    ,'earnings before interest and taxes / total assets': green
    ,'earnings before deprecation, interest and taxes / total assets': green
    ,'current assets / current liabilities': blue
    ,'working capital / total assets': blue
    ,'working capital / sales': blue
    ,'accounts receivable / sales': yellow
    ,'accounts payable / sales': yellow
    ,'inventory / sales': yellow
    ,'sales / total assets': yellow
    ,'net profit / sales': yellow
    ,'earnings before deprecation, interest and taxes / sales': yellow
    ,'earnings before interest and taxes / sales': yellow
    ,'added value / total assets': yellow
    ,'added value / fixed assets': yellow
    ,'equity / total assets': red
    ,'cash flow / total debt': red
    ,'retained earnings / total assets': red
    ,'earnings before interest and taxes / interest': red
    ,'bankrupt': 'white'
}
    
def show_data():

    df = build_frame()
    return df.hide_index()

def build_frame():

    df = pd.read_csv(
        file,
        header=0,
        names=HEADER,
        index_col=False,
        sep=';',
        low_memory=True)
    df =  change_order(df)
    df = df.sample(frac=1).reset_index(drop=True).head()

    return df.style.apply(color_cols, colordict=HEADER)

def change_order(df):
    cols = df.columns.tolist()
    cols.insert(0, cols.pop(cols.index('bankrupt')))
    return df.reindex(columns= cols)

def color_cols(s, colordict):
    if s.name in colordict.keys():
        return ['background-color: {}'.format(colordict[s.name])] * len(s)
    return [''] * len(s)

if __name__ == '__main__':
    data = show_data()
    display(data)
