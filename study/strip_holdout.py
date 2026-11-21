"""Calibrate on low-load readings; predict disjoint physical height measurements."""
import argparse,csv,hashlib
from pathlib import Path
import numpy as np
from scipy.integrate import solve_bvp,simpson
from scipy.optimize import least_squares
HERE=Path(__file__).resolve().parent
SHA="d815d7567a2d42e5b0436125203211d2a3f970270000721e0be1b0a1cc880361"
G=12*2010*9.81*.0132**3/(1.16e6*.00050**2)
def observations(path):
    import fitz
    assert hashlib.sha256(path.read_bytes()).hexdigest()==SHA
    with fitz.open(path) as doc:
        strokes=doc[11].get_drawings()
    for specimen,h0,a0 in [('s1-1',190,442),('s1-2',234,464),('s1-3',146,420)]:
        def center(stroke):
            if specimen=='s1-2': return np.mean([tuple(i[1]) for i in stroke['items']],axis=0)
            r=stroke['rect'];return (r.x0+r.x1)/2,(r.y0+r.y1)/2
        points=[]
        for i in reversed(range(22)):
            x,y=center(strokes[h0+i]);u,v=center(strokes[a0+i])
            q=(x-152.672)/(136.049/45)
            assert abs(q-(u-326.506)/(136.050/45))<.001
            points.append((q,(162.650-y)/103.866,np.radians((162.428-v)*90/(162.428-64.029))))
        yield specimen,np.asarray(points)
def forward(params,loads):
    jp,jd=params
    s=np.linspace(0,.5,21);init=np.zeros((4,len(s)));last=0;out=[]
    for q in loads:
        for val in np.linspace(last,q,max(1,int(np.ceil(abs(q-last)/2)))+1)[1:]:
            def ode(s,y):
                a,m,b,n=y
                return np.vstack((jp*m,-val*np.cos(a)+G*(1-s)*np.sin(a),
                                  jd*n,-val*np.cos(b)+G*(.5-s)*np.sin(b)))
            def bc(l,r): return [l[0],r[0]-l[2],r[1]-l[3],r[3]]
            sol=solve_bvp(ode,bc,s,init,tol=3e-6)
            if not sol.success: raise RuntimeError(sol.message)
            init=sol.sol(s)
        v=np.linspace(0,.5,101);z=sol.sol(v)
        out.append((simpson(np.sin(z[0])+np.sin(z[2]),x=v),z[2,-1]))
        last=q
    return np.asarray(out)
def estimate(training,kind,structure,lam):
    q,h,a=training.T
    def errors(x):
        pred=forward([x[0],x[-1]],q)
        if kind=='two heights': return [*(3*(pred[:,0]-h)/q),np.sqrt(lam)*(x[0]-x[-1])]
        return [3*(pred[0,0]-h[0])/q[0],2*(pred[0,1]-a[0])/q[0],np.sqrt(lam)*(x[0]-x[-1])]
    # The homogeneous comparator has one compliance parameter and no spatial penalty.
    x=least_squares(errors,np.ones(1 if structure=='uniform' else 2),bounds=(.12,4),ftol=1e-10,xtol=1e-10,gtol=1e-10).x
    return [x[0],x[-1]]
def write(name,rows):
    with (HERE/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main(path):
    rows=[]
    for label,obs in observations(path):
        for train_indices in [(1,2),(1,3),(2,3)]:
            tr=obs[list(train_indices)]
            # Same 18 test loads for every split; neither test values nor gaps inform fits.
            held=obs[4:]; qs,h,_=held.T
            for kind,structure,lam in [('nominal','uniform',0)]+[(k,'uniform',0) for k in ['two heights','height + angle']]+[(k,'two zone',v) for k in ['two heights','height + angle'] for v in (0,.001,.01,.1)]:
                p=[1.,1.] if kind=='nominal' else estimate(tr,kind,structure,lam)
                pred=forward(p,qs)[:,0]
                err=pred-h
                r=dict(specimen=label,training_indices='/'.join(map(str,train_indices)),method=kind,
                      structure=structure,penalty=lam,heldout_count=len(h),proximal=p[0],distal=p[1],
                      mean_bias=np.mean(err),mae_over_length=np.mean(np.abs(err)),
                      uniform_0_1_risk=np.mean(np.abs(np.clip(pred,0,1)-np.clip(h,0,1))),
                      uniform_010_070_risk=np.mean(np.abs(np.clip(pred,.1,.7)-np.clip(h,.1,.7)))/.6,
                      max_abs_error=np.max(np.abs(err)))
                rows.append(r)
    write('strip_results.csv',rows)
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('source_pdf',type=Path);main(parser.parse_args().source_pdf)
