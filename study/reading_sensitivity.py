"""Stress low-field picking uncertainty; export aggregate endpoint changes only."""
import argparse
from itertools import product
from pathlib import Path
import numpy as np
from strip_holdout import observations,estimate,forward,write
def main(path):
    sources=list(observations(path))
    rows=[]
    for h1,h2,a1 in product([-1,1],repeat=3):
        loss={'height + angle':[],'two heights':[]}
        for name,obs in sources:
            tr=obs[[1,2]].copy();tr[0,1]+=h1*.002;tr[1,1]+=h2*.002;tr[0,2]+=a1*np.radians(.25)
            for method,values in loss.items():
                p=estimate(tr,method,'uniform',0)
                y=forward(p,obs[4:,0])[:,0]
                values.append(np.mean(np.abs(y-obs[4:,1])))
        rows.append(dict(height1_sign=h1,height2_sign=h2,angle1_sign=a1,dual_uniform=np.mean(loss['height + angle']),
                        height_uniform=np.mean(loss['two heights']),dual_minus_height=np.mean(loss['height + angle'])-np.mean(loss['two heights'])))
    write('reading_sensitivity.csv',rows)
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('source_pdf',type=Path);main(parser.parse_args().source_pdf)
