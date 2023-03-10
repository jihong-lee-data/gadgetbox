import json
import os
import re
from pathlib import Path

def load_json(path): 
    return json.load(open(path, "r"))

def save_json(file, path): 
    json.dump(file, open(path, "w"))

def mk_dir(path):
    if not os.path.isdir(path):
        os.makedirs(path)

    
def rm_spcl_char(text):
    # remove special characters
    text = re.sub(r'[!@#$(),，\n"%^*?？:;~`0-9&\[\]\。\/\.\=\-]', ' ', text)
    text = re.sub(r'[\s]{2,}', ' ', text.strip())
    text = text.lower().strip()
    return text

class ISO():
    def __init__(self):
        self.dict_path= Path('resource/iso.json')
        self.iso_dict= load_json(str(self.dict_path))
        self.code_dict= dict(zip(['e', 'k', '1', '2'], ['English', 'Korean', 'ISO 639-1 Code', 'ISO 639-2 Code']))
        
    def __call__(self, query, tol= 2):
        return self._search(query, tol)

    def _search(self, query, code:str =None, tol = 2):
        results = []
        for row in self.iso_dict:
            if code:
                target= ' '.join([row.get(i) for i in row if i in [self.code_dict.get(c) for c in list(code)]])
            else:
                target= ' '.join(row.values())
            if self._word_validation(query, target, tol):
                results.append(row)
        return results
    
    def convert(self, query, src_code=None, dst_code=None):
        search_result= self._search(query, code= src_code, tol= 1)
        if not search_result:
            raise ValueError('Input query is case-insensitive but must be fully matched to a target.')
        else:
            result= search_result.pop(0)

        if dst_code:
            return [result.get(self.code_dict.get(d)) for d in list(dst_code)]
        else:
            return list(result.values())
        
    def _word_validation(self, test:str, target:str, tol = 2):
        if tol == 0: # completely-matched
            return test in target.split()
        elif tol == 1: # case-insensitive
            return test.lower() in target.lower().split()
        elif tol == 2: # character-included
            return test.lower() in target.lower()
            
        