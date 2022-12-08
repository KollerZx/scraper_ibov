import pandas as pd
# import wget
# from zipfile import ZipFile
import os
url_base = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/'

files_zip = []

base_path = os.getcwd() + 'scrap/src/data/'
downloads_path = base_path + 'downloads/'
zip_path = base_path + 'CVM'

for year in range(2011, 2023):
  files_zip.append(f'itr_cia_aberta_{year}.zip')

# for file in files_zip:
#   wget.download(url_base+file, downloads_path)

# for file in files_zip:
#   ZipFile(downloads_path + file, 'r').extractall(zip_path)

tags = ["BPA_con", "BPA_ind", "BPP_con", "BPP_ind", "DFC_MD_con", "DFC_MD_ind", "DFC_MI_con", "DFC_MI_ind", "DMPL_con", "DMPL_ind", "DRA_con", "DRA_ind", "DRE_con", "DRE_ind", "DVA_con", "DVA_ind"]

for tag in tags:
  file = pd.DataFrame()
  
  for year in range(2011, 2023):
    file = pd.concat([file, pd.read_csv(f'{zip_path}/itr_cia_aberta_{tag}_{year}.csv', sep=";", decimal=",", encoding="ISO-8859-1")])
  
  file.to_csv(f'{base_path}Compile/itr_cia_aberta_{tag}_2011-2022.csv', index=False)


