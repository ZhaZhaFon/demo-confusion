
import os
import argparse
import soundfile as sf
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--fold", default=None, required=True, type=str, help="# Path of the fold to be processed #")

args = parser.parse_args()
filelist = os.listdir(args.fold)

print('# Processing files...')
for file in filelist:
    path = os.path.join(args.fold, file)
    print(f'   {path}')
    wav, fs = sf.read(path)
    
    