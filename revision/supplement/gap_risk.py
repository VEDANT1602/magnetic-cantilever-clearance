"""Uniform-grid decision loss and Tikhonov regularization of two-zone compliance."""
import csv
from functools import lru_cache
from itertools import product
from pathlib import Path
import numpy as np
from clearance_sensitivity import PROFILES, slopes, height, GAPS, ALTERNATE_GAPS, save

ROOT=Path(__file__).resolve().parent
A=np.array([[7/8,1/8],[3/4,1/4]])  # maps P,D to 3d and 2t; equal scales for a uniform beam
C=np.array([[1.,-1.],[-1.,1.]])
BOUND=(.12,4.)


def fit(d,t,lam):
    """Box constrained ridge. Check interior optimum and minimizers on four edges."""
    target=np.array([3*d,2*t])
    matrix=A.T@A + lam*C
    v=A.T@target
    unconstrained=np.linalg.solve(matrix,v)
    if np.all((unconstrained>=BOUND[0]) & (unconstrained<=BOUND[1])):
        return unconstrained
    candidates=[]
    for k,j in [(0,1),(1,0)]:
        for bound in BOUND:
            z=np.empty(2);z[k]=bound;z[j]=np.clip((v[j]-matrix[j,k]*bound)/matrix[j,j],*BOUND)
            candidates.append(z)
    return min(candidates,key=lambda z:np.sum((A@z-target)**2)+lam*(z[0]-z[1])**2)


def main():
    cached=lru_cache(maxsize=None)(height)
    records=[]
    for (name,base),scale,L,field in product(PROFILES.items(), [.65,1,1.5], [.85,1.15], [.4,1,2,3.6]):
        j=tuple(np.array(base)*scale);q=L**2*field
        d,t=slopes(j)
        true=cached(j,q)
        for de,te in [(0,0),(.015,.005),(.015,.015),(.015,.03),(.05,.05)]:
            for s1,s2 in product([-1,1],repeat=2):
                y=d*(1+s1*de);ang=t*(1+s2*te)
                u=np.linalg.solve(A,[3*y,2*ang])
                shapes={'repeat':np.repeat(1.5*(y+d*(1+s2*de)),2),'inverse_clip':np.clip(u,*BOUND)}
                for lam in (0,.001,.01,.1):
                    shapes[f"ridge_{lam}"]=fit(y,ang,lam)
                for method,(p,z) in shapes.items():
                    pred=cached((p,p,z,z),q)
                    # Continuous uniform threshold probability from clipped interval lengths.
                    continuous=abs(np.clip(pred,.10,.70)-np.clip(true,.10,.70))/.60
                    records.append(dict(profile=name,scale=scale,length=L,field=field,sign1=s1,sign2=s2,
                       displacement_error=de,angle_error=te,model=method,mae=abs(pred-true),
                       wrong4=int(np.count_nonzero((pred>=GAPS)!=(true>=GAPS))),
                       wrong61=int(np.count_nonzero((pred>=ALTERNATE_GAPS)!=(true>=ALTERNATE_GAPS))),
                       uniform_risk=continuous,true=true,pred=pred,clipped=bool(any(x in BOUND for x in (p,z)))))
    groups={}
    for x in records:groups.setdefault((x['displacement_error'],x['angle_error'],x['model']),[]).append(x)
    summaries=[]
    for (de,te,m),grp in groups.items():
        summaries.append(dict(displacement_error=de,angle_error=te,model=m,n=len(grp),
          mean_abs_height_error=np.mean([x['mae'] for x in grp]),
          wrong4=sum(x['wrong4'] for x in grp),wrong61=sum(x['wrong61'] for x in grp),
          mean_continuous_uniform_risk=np.mean([x['uniform_risk'] for x in grp]),
          on_bound=sum(x['clipped'] for x in grp)))
    save('decision_risk.csv',summaries)
    fields=['profile','scale','length','field','sign1','sign2']
    low=[r for r in groups[.015,.005,'inverse_clip']]
    high={tuple(x[k] for k in fields):x for x in groups[.015,.03,'inverse_clip']}
    movements=[]
    for a in low:
        idx=tuple(a[k] for k in fields);b=high[idx]
        for gap in GAPS:
            wa=(a['true']>=gap)!=(a['pred']>=gap);wb=(b['true']>=gap)!=(b['pred']>=gap)
            if wa!=wb:
                movements.append(dict(**{k:a[k] for k in fields},gap=gap,true=a['true'],
                   weak_angle_error_prediction=a['pred'],strong_angle_error_prediction=b['pred'],
                   low_wrong=bool(wa),high_wrong=bool(wb),high_on_bound=b['clipped']))
    save('threshold_crossings.csv',movements)
    for x in summaries:
        if x['displacement_error']==x['angle_error']:print(x)
    print('repaired / new',sum(x['low_wrong'] for x in movements),sum(x['high_wrong'] for x in movements))


if __name__=='__main__':
    main()
