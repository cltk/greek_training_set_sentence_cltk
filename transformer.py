import os
import re

root = os.path.abspath('./')
originals = os.path.join(root,'originals/')

'''
try:
    os.remove('../training_sentences.txt')
except:
    pass
'''

with open('models/xen_anab_1.txt') as f:
    read = f.read()
rm_brackets = re.sub(r'\[\d+?\]', '', read)
rm_nums = re.sub(r'\d+?\.', '', rm_brackets)
rm_two_spaces = re.sub(r'\s{2}', ' ', rm_nums)
one_sigma = re.sub('ς', 'σ', rm_two_spaces)
rm_junk = re.sub('†', '', one_sigma)
rm_breaks = re.sub(r'\n', ' ', rm_junk)
add_punct_breaks = re.sub(r'(\.|;) ', r'\1\n', rm_breaks)
print(add_punct_breaks)


with open('models/training_sentences_anab1.txt', 'w') as f:
    f.write(add_punct_breaks)
