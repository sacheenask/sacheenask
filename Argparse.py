import os
abc=os.path.dirname(os.path.abspath(__file__))
defg = os.path.basename(__file__)
a=os.path.join(abc, '../..')
ww= os.path.relpath('..\..')

print(f'Directory Name: {abc} & file name {defg} & {ww}')
