import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mlt
from termcolor import colored
from pyfiglet import Figlet

f = Figlet(font='jazmine')
print(colored(f.renderText('traces'), 'green'))


print("\n \nWelcome to traces! \n \n***Please ensure your file is in this folder***\n ")


up1 = input('Is your file from the hPLC? (Y/n) \n') #because hPLC exports csv files with utf-16

up2 = input('Please enter file name: ')

if up1 =='Y' or up1 == 'y':

    df = pd.read_csv(up2, delimiter='\t',encoding='utf-16', header=None)

    up3 = input('\nPlease provide a label for the x-axis \n \n')

    up4 = input('\nPlease provide a label for the y-axis \n \n')

    df.columns = [up3, up4]
    
    user_title = input('\n  \nWhat would you like for a title? \n \n')

    print('\nBefore plotting let\'s decide on a color. \nHere are a few available colors: \n magenta = #ff00ff\n chrmison = #DC143C \n blue = #0000FF \n \n')

    up5 = input('Please provide a color using a hex RGB or RGBA string \n \n')

    print('Generating plot now...')

    font = {
        'color': 'black',
        'verticalalignment': 'baseline',
        'horizontalalignment': 'center'}

    sns.set_context("talk")
    sns.lineplot(data=df, x=up3, y=up4, color=up5)
    plt.title(user_title, fontdict=font
        )
    sns.set_theme(style='ticks')
    plt.show()
    

else:

    print('processing csv as a utf-8 encoded file...')

    df = pd.read_csv(up2, delimiter='\t',encoding='utf-16', header=None)

    up3 = input('\nPlease provide a label for the x-axis \n \n')

    up4 = input('\nPlease provide a label for the y-axis \n \n')

    df.columns = [up3, up4]
    
    user_title = input('\n  \nWhat would you like for a title? \n \n')

    print('\nBefore plotting let\'s decide on a color. \nHere are a few available colors: \n magenta = #ff00ff\n chrmison = #DC143C \n blue = #0000FF \n \n')

    up5 = input('Please provide a color using a hex RGB or RGBA string \n \n')

    print('Generating plot now...')

    font = {
        'color': 'black',
        'verticalalignment': 'baseline',
        'horizontalalignment': 'center'}

    sns.set_context("talk")
    sns.lineplot(data=df, x=up3, y=up4, color=up5)
    plt.title(user_title, fontdict=font
        )
    sns.set_theme(style='ticks')
    plt.show()
    