import pandas as pd
import math

def mid_point(lst):
  x1 = (float(lst[0]) + float(lst[6])) / 2
  y1 = (float(lst[1]) + float(lst[3])) / 2
  x2 = (float(lst[2]) + float(lst[4])) / 2
  y2 = (float(lst[7]) + float(lst[5])) / 2
  mid_x = (x1 + x2) / 2
  mid_y = (y1 + y2) / 2
  length = x2 - x1
  height = y2 - y1
  return (mid_x, mid_y, length, height)

l = ['BPL-Ultima-PrimeD-A', 'BPL-EliteView-EV100-C', 'BPL-EliteView-EV10-B_Meditec-England-A', 'Nihon-Kohden-lifescope-A']

for n in l:

    df = pd.read_csv(f'./data/classification/{n}.csv')

    for i in df.index:

        with open(f'data/classification/{n}/' + f'{df["image_name"][i]}'[:-4] + 'txt', "w") as f:
            tt = df.iloc[i]
            for j in range(1,10):

                # if(t )
                if(type(tt[j]) == float):
                    continue

                t = (tt[j])[1:-1].replace(' ','').split(',')

                x,y,w,h = t
                f.write(f'{i} {x} {y} {w} {h}\n')
