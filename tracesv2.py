import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mlt
import os
import time



class SampleRun:

    #class attribute


    def __init__(self):
        pass
            
    def set_dataframe(self, name):
        
        try:
            # untested 
            data = pd.read_csv(str(name), sep='\t', header=None)
            print(data)

        except: 
            # for files from the hPLC which are encoded in utf-16
            data = pd.read_csv(str(name), sep='\t', encoding="utf-16",header=None)
            # print(data)
            x_axis = 'time(min)'
            y_axis = 'Absorbance(AU)'
            data.columns = [x_axis,y_axis]
            

        return data, x_axis, y_axis
    
    def set_column_names(self, usr_provided_x, usr_provided_y):
        
        pass

    def set_title(self, usr_provided_title):

        pass


files = os.listdir(os.curdir)
print("Listed files in current directory... \n \n", files,"\n \n")
name = input('Provide the exact name of your file... \n \n')
print("\n \nSearching for ...",name, '\n \n')

if os.path.exists(name):
    print('File found... \n \n Displaying preview of dataframe... \n \n')
    sample = SampleRun().set_dataframe(name)
    print(sample)
    
    # sns.set_context("talk")
    # sns.lineplot(data=sample, x=x_axis, y=y_axis, color = 'blue')
    # plt.title(title, fontdict=font
    #     )
    # sns.set_theme(style='ticks')
    # plt.tight_layout()
    # plt.show()

else: 
    print('the file was not found in this directory... ')





# # assign current directory as variable path 
# path = os.getcwd()

# # assign ext to the extensions I love and care about 
# ext = ('.csv', '.CSV')

# # create a list to store files to process
# all_files = []

# # iterate over each file with my favorite ext and print out
# for file in os.listdir(path):
#     if file.endswith(ext):
#         print(file)
#         all_files.append(file)

# print(all_files)
    
# for i in all_files:

#     df = pd.read_csv(i, delimiter='\t',encoding='utf-8', header=None)

#     x_axis = 'retention time(min)'

#     y_axis = 'Absorbance(AU)'

#     df.columns = [x_axis, y_axis]
    
#     title = os.path.splitext(i)[0]

    # print('\nBefore plotting let\'s decide on a color. \nHere are a few available colors: \n magenta = #ff00ff\n chrmison = #DC143C \n blue = #0000FF \n \n')

#     up5 = input('Please provide a color using a hex RGB or RGBA string \n \n')

#     print('Generating plot now...')

    # font = {
    #     'color': 'black',
    #     'verticalalignment': 'baseline',
    #     'horizontalalignment': 'center'}

    # sns.set_context("talk")
    # sns.lineplot(data=df, x=x_axis, y=y_axis, color = 'blue')
    # plt.title(title, fontdict=font
    #     )
    # sns.set_theme(style='ticks')
    # plt.tight_layout()
    # plt.show()
    

# else:

#     print('processing csv as a utf-8 encoded file...')

#     df = pd.read_csv(up2, delimiter='\t',encoding='utf-16', header=None)

#     up3 = input('\nPlease provide a label for the x-axis \n \n')

#     up4 = input('\nPlease provide a label for the y-axis \n \n')

#     df.columns = [up3, up4]
    
#     user_title = input('\n  \nWhat would you like for a title? \n \n')

#     print('\nBefore plotting let\'s decide on a color. \nHere are a few available colors: \n magenta = #ff00ff\n chrmison = #DC143C \n blue = #0000FF \n \n')

#     up5 = input('Please provide a color using a hex RGB or RGBA string \n \n')

#     print('Generating plot now...')

#     font = {
#         'color': 'black',
#         'verticalalignment': 'baseline',
#         'horizontalalignment': 'center'}

#     sns.set_context("talk")
#     sns.lineplot(data=df, x=up3, y=up4, color=up5)
#     plt.title(user_title, fontdict=font
#         )
#     sns.set_theme(style='ticks')
#     plt.show()
    