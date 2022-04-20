
from distutils.command.build_scripts import first_line_re
import urllib
import Bio.PDB
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import string
import random
import os
from mpl_toolkits import mplot3d



# def download_pdb(pdb_from_list):

#     urllib.request.urlretrieve('https://files.rcsb.org/view/'+pdb_from_list+'.pdb', pdb_from_list+'.pdb')
#     pdb_filename = pdb_from_list+'.pdb'
#     return


# # -random letter generator-


# digits = string.digits
# digits_ = '123456789'
# all_chars = string.ascii_letters

# def get_rand_pdb(many):
#     list_pdb = []
#     list_pdb = many *[0]
#     count = 0

#     for item in range(len(list_pdb)):
#         rand_digits = random.choices(digits_)
#         rand_allchars = random.choices(digits_+string.ascii_letters,k=3)
#         rand_pdb = ''.join(rand_digits+rand_allchars)
        
#         if count < many:

#             list_pdb[item] = rand_pdb
#             y = list_pdb[item]

#             try:
#                 print("Downloading ",y)
#                 download_pdb(y)
#                 count += 1
#             except:
#                 print("Error: unable to download ",y)
#                 pass
#         else:
#             break

#     print("Done! Downloaded", count, "files")

#     return list_pdb

aa_list = ['ALA', 'ARG', 'ASN', 'ASP', 'AYA','CYS','GLN', 'GLN','GLU', 'GLY', 'HIS', 'ILE','LEU', 'LYS', 'MET', 'PHE', 'PRO','SER', 'THR', 'TRP', 'TYR', 'VAL']



def get_all_pdbs():
    
    all_pdb_files = []

    for x in os.listdir():
        if x.endswith(".pdb"):
            all_pdb_files.append(x)
            
    print("Done! Found ",len(all_pdb_files)," files")
    
    return all_pdb_files

def get_pdb_codes(allPDBfiles):
    
    all_codes = []

    for x in allPDBfiles:
        filename_ = x.split(".")
        code = filename_[0]
        all_codes.append(code)

    print("Done! Found ", len(all_codes),"files and stored in txt file")

    return all_codes

"Finding pdb files in directory and storing names..."

all_pdbs = get_all_pdbs() # stores all pdbs in the directory as an array
all_pdb_codes = get_pdb_codes(all_pdbs) # stores the parse filenames as a pdb codes


def get_name(pdb_code):
    pdb_filename = pdb_code+".pdb"
    structure = Bio.PDB.PDBParser(PERMISSIVE = True, QUIET = True).get_structure(pdb_code, pdb_filename)
    name = structure.header['name']
    
    return name

def get_header(pdb_code):
    pdb_filename = pdb_code+".pdb"
    structure = Bio.PDB.PDBParser(PERMISSIVE = True, QUIET = True).get_structure(pdb_code, pdb_filename)
    header = structure.header['keywords']
    
    return header

def set_label(ALLcodes):

    pool_labeled = {}
    count = 0

    for pdb in ALLcodes:

        try:
            pdb_headers = get_header(pdb)
            pdb_names = get_name(pdb)

            if 'channelrhodopsin' in pdb_headers:
                print(1, pdb)
                pool_labeled[pdb] = 1
                count += 1

            elif 'channelrhodopsin' in pdb_names:
                print(1, pdb)
                pool_labeled[pdb] = 1 
                count += 1

            elif 'rhodopsin' in pdb_names:
                print(1, pdb)
                pool_labeled[pdb] = 1  
                count += 1

            elif 'rhodopsin' in pdb_headers:
                print(1, pdb)
                pool_labeled[pdb] = 1      
                count += 1

            else:
        #         print(0, pdb)
                pool_labeled[pdb] = 0
        except:
            print('Error',pdb)
            continue

    df_Labeled = pd.DataFrame(pool_labeled, index=[0]).T
    df_Labeled.columns = ['Rhodopsin/ChR']
    df_Labeled.to_csv('pdb_labeled.csv')

    print("Done! Labeled ",len(pool_labeled), "pdbs and positive labels found =>", count)

    return pool_labeled

print('labeling data... ')

Labeled = set_label(all_pdb_codes) # build a dictionary of positive and negative labeled pdbs




def get_all_names(all_pdb_codes):

    all_names = {}

    for pdb in all_pdb_codes:
        
        try:
            print(pdb)
            all_names[pdb] = get_name(pdb)
        except:
            print(pdb,"Error unable to store name... continuing")
            continue

    df_names = pd.DataFrame(all_names, index=[0]).T
    df_names.columns = ['names']
    df_names.to_csv('pdb_names.csv')

    print("Done! Stored the names of",len(all_names), "pdbs in a csv file")
    return all_names
    
print("Starting annotation of stored pdbs... ")
Named = get_all_names(all_pdb_codes)

df_Named = pd.DataFrame(Named, index=[0]).T
df_Labeled = pd.DataFrame(Labeled, index=[0]).T

df_ALL_annot = pd.concat([df_Named, df_Labeled], axis=1, join='inner')
df_ALL_annot.columns = ['name','Rhodopsin/ChR']
df_ALL_annot.to_csv('pdb_names_labels.csv')










# store list of residues that are cleaned
def get_res(pdb_code):
    pdb_filename = pdb_code+".pdb"
    # print(pdb_filename)
    structure = Bio.PDB.PDBParser(PERMISSIVE = True, QUIET = True).get_structure(pdb_code, pdb_filename)
    model = structure[0]
    model = structure.get_models()
    models = list(model)
    chains = list(models[0].get_chains()) 
    residues = list(chains[0].get_residues()) 
    leng = len(residues)
    # print(leng)
    all_res = [] # this shows all the residues excluding non-amino acids
    
    for res in residues:
        try:
            resname = res.get_resname()
            if resname in aa_list:
                all_res.append(res)
            else:
                continue
        except:
            print("Error unable to get parse res name")
            continue 

    
    return all_res


# store a dictionary of pdbs with a complete list of residues
def get_ALL_res(listOfPDBcodes):
    
    ALL_res = {}

    for i in listOfPDBcodes:
        try:
            ALL_res[i] = get_res(i)
            print(i)
        
        except:
            print("Error unable to get residues for ",i)
            pass
    
    my_dict = ALL_res
    with open('pdb_residues.csv', 'w') as f:
        for key in my_dict.keys():
            f.write("%s,%s\n"%(key,my_dict[key]))
    print("Done! Stored a dictionary the residues of ", len(ALL_res), "pdbs as a csv")
    
    return ALL_res

print('Building dictionary of residues for all pdbs list')
all_residues = get_ALL_res(all_pdb_codes)




# make a function that returns the distance between reside 1 and 2
def calc_residue_dist_test(residue_A, residue_B):
    diff_vector  = residue_A["CA"].coord - residue_B["CA"].coord
    distance = np.sqrt(np.sum(diff_vector * diff_vector))
    return distance

# calculate the distance matrix
def calc_dist_matrix_test(chain_one, chain_two) :
     answer = np.zeros((len(chain_one), len(chain_two)), np.float64)
     for row, residue_A in enumerate(chain_one):
         try:
            for col, residue_B in enumerate(chain_two):
                try:
                    answer[row, col] = calc_residue_dist_test(residue_A, residue_B)
                except KeyError:
                    break
         except KeyError:
             break
#      print(answer)
     return answer


def dist_matrix(x,y):
    
    distogram = calc_dist_matrix_test(y, y)
    contact_map = distogram < 10 
    
    mean = np.mean(distogram)
    std = np.std(distogram)
    variance = np.var(distogram)
    
    print("\n",x,"\nMean: ", mean,"\nstd: ",std,"\nvariance: ",variance,"\n\n")

    return distogram # contact_map, mean, std, variance


def get_all_matrices(All_residues):

    all_matrices = {}

    for x,y in All_residues.items():
        check_ = y
        lc_=len(check_)
        if lc_ == 0:
            print(x," will be omitted")
            pass

        else:
            try:

                all_matrices[x] = dist_matrix(x,y)
            
            except:

                print(x, "Error unable to calculate matrix")
                continue
    
    my_dict = {}

    for x,y in all_matrices.items():
        mean = np.mean(y)
        std = np.std(y)
        variance = np.var(y)
        
        my_dict[x] = mean, std, variance

        
    df_stats = pd.DataFrame(my_dict).T
    df_stats.columns = ['mean','std','variance']
    df_stats.to_csv('pdb_disto_stats.csv')    
    


    print("Done!", len(all_matrices)," matrices were calculated and stored in csv as well as their stats")
    return all_matrices


"Creating a dictionary of distograms \n"
"\nCalculating matrices... and storing stats in csv file: pdb_matrices_stats.csv"
all_matrices = get_all_matrices(all_residues)



print('generating dataframes of stats and annotated data...')
df_disto_stats = pd.read_csv('pdb_disto_stats.csv',index_col=0)

print(df_disto_stats)

df_complete = pd.concat([df_ALL_annot, df_disto_stats], axis=1, join='inner')
print("Combined dataframes...")
print(df_complete)
print("writing to a csv file...")
df_complete.to_csv('combined_annotated_stats.csv')


print('Plotting... stats of labeled rhodopsins in the data')




z = df_complete['variance'].to_numpy()
y = df_complete['mean'].to_numpy()
x = df_complete['std'].to_numpy()


alphas = (df_complete['Rhodopsin/ChR'])

save_results_to = 'charts/'

fig, (ax1,ax2) = plt.subplots(ncols=2, nrows=1, figsize=(10,4))

df_complete.plot(x ='std',
                 y='mean',
                 kind = 'scatter',
                 c='Rhodopsin/ChR',
                 cmap='viridis',
                 alpha=0.6,
#                  s=15,
                 xlabel='standard deviation',
                 ylabel='means',
                 title='all data',
                 ax=ax1)

df_complete.plot(x ='std',
                 y='mean',
                 kind = 'scatter',
                 c='Rhodopsin/ChR',
                 alpha=alphas,
                 s=15,
                 xlabel='standard deviation',
                 ylabel='means',
                 title='ChRs and Rhodopsins',
                 ax=ax2
                )
plt.savefig(save_results_to +'scatter_combined'+'.png', dpi = 300)

plt.show()


ax3 = plt.axes(projection='3d')


zdata = z
xdata = x
ydata = y
ax3.scatter(xdata, ydata, zdata, c=alphas, cmap='viridis', alpha=.6, linewidths=0.4)
ax3.set_xlabel("std")
ax3.set_ylabel("mean")
ax3.set_zlabel("variance")
ax3.view_init(40, 220)
plt.figure()
plt.savefig(save_results_to +'scatter_combined__3D'+'.png', dpi = 300)

ax4 = plt.axes(projection='3d')


zdata = z
xdata = x
ydata = y
ax4.scatter(xdata, ydata, zdata, c="black", cmap=alphas, alpha=alphas, linewidths=0.4)
ax4.set_xlabel("std")
ax4.set_ylabel("mean")
ax4.set_zlabel("variance")
ax4.view_init(40, 220)
plt.figure()
plt.savefig(save_results_to +'scatter_posi__3D'+'.png', dpi = 300)

