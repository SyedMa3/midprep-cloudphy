import pandas as pd


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

df = pd.read_csv('./data/segmentation/labels.csv')

for i in df.index:

    t = (df['points'][i])[1:-1].replace(' ','').split(',')

    x,y,w,h = mid_point(t)

    x = x/1280
    y = y/720
    w = w/1280
    h = h/720


    with open('data/segmentation/labels/' + f'{df["image_name"][i]}'[:-4] + 'txt', "w") as f:
        f.write(f'0 {x} {y} {w} {h}')