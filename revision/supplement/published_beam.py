"""Uniform-strip forward check against the experimental markers in Yan et al., Fig. 6."""
from pathlib import Path
import csv, hashlib, argparse
import numpy as np
from scipy.integrate import solve_bvp, simpson
from clearance_sensitivity import save,GAPS,ALTERNATE_GAPS
HERE=Path(__file__).resolve().parent
SOURCE_SHA="d815d7567a2d42e5b0436125203211d2a3f970270000721e0be1b0a1cc880361"
G=12*2010*9.81*.0132**3/(1.16e6*.00050**2)


def extract(path):
    import fitz
    assert hashlib.sha256(path.read_bytes()).hexdigest()==SOURCE_SHA
    doc=fitz.open(path)
    paths=doc[11].get_drawings()
    rows=[]
    # These stroke ranges contain the 22 experimental tip-height and tip-angle
    # markers in respectively panels a and b, excluding analytical/FEM symbols.
    for name,height_start,angle_start in [('s1-1',190,442),('s1-2',234,464),('s1-3',146,420)]:
        for j in range(21,-1,-1):
            def center(draw):
                r=draw['rect']
                if name=='s1-2':
                    points=np.array([tuple(item[1]) for item in draw['items']])
                    return points.mean(axis=0)   # centroid of inverted triangle
                return np.array([(r.x0+r.x1)/2,(r.y0+r.y1)/2])
            x,y=center(paths[height_start+j]);u,v=center(paths[angle_start+j])
            q=(x-152.672)/(136.049/45)
            q2=(u-326.506)/(136.050/45)
            assert abs(q-q2)<.001
            rows.append(dict(specimen=name,q=max(0,q),measured_height=(162.650-y)/103.866,
                             measured_angle_deg=(162.428-v)*90/(162.428-64.029)))
    save('yan_fig6_observations.csv',rows)


def predict(q,gravity):
    s=np.linspace(0,1,100)
    def bc(a,b):return np.array([a[0],b[1]])
    # Continuation selects the branch connected to the unforced straight strip.
    states=np.zeros((2,len(s)))
    for load in np.linspace(0,q,int(np.ceil(q/2))+1)[1:] if q>0 else [0.]:
        def ode(x,y):
            return np.vstack((y[1],-load*np.cos(y[0])+gravity*(1-x)*np.sin(y[0])))
        sol=solve_bvp(ode,bc,s,states,tol=1e-8)
        assert sol.success
        states=sol.sol(s)
    dense=np.linspace(0,1,401)
    theta=sol.sol(dense)[0]
    return simpson(np.sin(theta),x=dense),np.degrees(theta[-1])


def main():
    p=argparse.ArgumentParser();p.add_argument('--extract',type=Path)
    args=p.parse_args()
    if args.extract:extract(args.extract)
    rows=[]
    with (HERE/'yan_fig6_observations.csv').open() as fi:
        for r in csv.DictReader(fi):
            q=float(r['q'])
            if not .01<q<=4.761:continue # same dimensionless loading range as the main grid; omit origins
            for label,g in [('original_no_self_weight',0),('gravity_adjusted',G)]:
                h,ang=predict(q,g);obs=float(r['measured_height'])
                rows.append(dict(**r,model=label,gravity=g,height=h,angle_deg=ang,
                   abs_height=abs(h-obs),abs_angle_deg=abs(ang-float(r['measured_angle_deg'])),
                   wrong4=np.count_nonzero((h>=GAPS)!=(obs>=GAPS)),
                   wrong61=np.count_nonzero((h>=ALTERNATE_GAPS)!=(obs>=ALTERNATE_GAPS))))
    save('yan_forward_check.csv',rows)
    for typ in ['original_no_self_weight','gravity_adjusted']:
        sample=[r for r in rows if r['model']==typ]
        print(typ,len(sample),[(k,np.mean([r[k] for r in sample])) for k in ['abs_height','abs_angle_deg']],sum(r['wrong61'] for r in sample),sum(r['wrong4'] for r in sample),G)


if __name__=='__main__':
    main()
