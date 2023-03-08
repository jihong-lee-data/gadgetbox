import pandas as pd
from glob import glob
import requests
from tqdm import tqdm
import os

def download(url, filepath):
    r = requests.get(url)
    f = open(filepath, 'wb')
    f.write(r.content)
    f.close()



for lang in tqdm(lang_list):
    url = f"https://opus.nlpl.eu/download.php?f=TED2020/v1/raw/{lang}.zip"
    file_path = f"/Users/jihonglee/xlent/{lang}.zip"
    if not os.path.exists(f"/Users/jihonglee/xlent/{lang}.zip"):
        download(url, file_path)
    
