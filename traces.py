import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mlt

print("Welcome to traces! \n Please ensure your file is in this folder\n ")
up1 = input('Please enter file name: ')

up2 = input('Is your file from the hPLC? (Y/n) \n') #because hPLC exports csv files with utf-16

if up2 =='Y' or 'y':

    df = pd.read_csv(up1, delimiter='\t',encoding='utf-16', header=None)

    df.columns = ['Time (min)', 'GFP Signal (AU)']

    user_title = input('What would you like for a title? \n')

    # up3 = input('Would you like to subtract baseline value? (Y/n)')

    palette = sns.color_palette('rocket_r')

    font = {
        'color': 'black',
        'verticalalignment': 'baseline',
        'horizontalalignment': 'center'}

    sns.set_context("talk")
    sns.lineplot(data=df, x='Time (min)', y='GFP Signal (AU)', color='g',palette=palette)
    plt.title(user_title, fontdict=font
        )
    sns.set_theme(style='ticks')
    plt.show()
    plt.tight_layout()



else :

    print('Assuming UTF-8... under construction')
