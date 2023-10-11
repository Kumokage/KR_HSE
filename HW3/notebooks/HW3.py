import nltk
import numpy as np


read_expr = nltk. sem. Expression.fromstring
exprs = []
exprs.append(read_expr('B(v,m,d,r)'))
exprs.append(read_expr('Se(m,v,d,r)'))
exprs.append(read_expr('P(v,m,d,r)'))
exprs.append(read_expr ('C(v,m,r,d)'))
exprs.append(read_expr('exists x exists y (B(v,x,d,y)) '))
exprs.append(read_expr('exists x (Se(m,v,d,x))'))
exprs.append(read_expr('exists x (Ge(v, d))'))
exprs.append(read_expr('exists x (Ge(m,x) & M(x))'))
exprs.append(read_expr('exists x exists y (P(v,x,y,r))'))
exprs.append(read_expr('exists x (Gi(v,m,x) & M(x))'))
exprs.append(read_expr('Gi(m,v,d)'))
exprs.append(read_expr('exists x (C(v,x,r,d))'))
exprs.append(read_expr('exists x exists y (C(x,m,d,y) & M(y))'))

addones = []
addones.append(read_expr('M(r)'))
addones.append(read_expr('all x all y all z all w (B(x,y,z,w) <-> Se(y,x,z,w))'))
addones.append(read_expr('all x all y all z all w (B(x,y,z,w) <-> P(x,y,z,w))'))
addones.append(read_expr('all x all y all z all w (B(x,y,z,w) <-> C(x,y,w,z))'))
addones.append(read_expr('Ge(m, r)'))
addones.append(read_expr('Gi(v, m, r)'))
addones.append(read_expr('all x all y all z all w (B(x,y,z,w) <-> Ge(x, z) & Ge(y, w))'))
addones.append(read_expr('all x all y all z all w (B(x,y,z,w) <-> Gi(x, y, z) & Gi(y, x, w))'))

proofs = []
for i, expr in enumerate(exprs [:4]):
    assumptions = [expr] + addones
    proofs.append([])
    for j, goal in enumerate (exprs):
        prover = nltk. Prover9 ()
        prover.config_prover9('C:\\Program Files (x86)\\Prover9-Mace4\\bin-win32')
        proofs[i].append(int(prover.prove (goal, assumptions)))

for i in proofs:
    for j in i:
        print(j, end=" ")
    print('\n')
 