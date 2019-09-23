# NAME - Vanshika
# Section - A

from math import *
import copy
from matplotlib import pyplot as py

py.ion()  # makes interactive plot

shape = input()

if shape == 'disc':
    a,b,r = input("Enter dimensions : ").split(" ")
    a,b,r = float(a),float(b),float(r)
    rma=copy.deepcopy(r)
    rmi=copy.deepcopy(r)
    ANGLE = 0
    XN=[]
    YN=[]
    C=[a,b]
    while ANGLE<1000:
        ANGLE=float(ANGLE)
        XN.append(a+r*cos(ANGLE))
        YN.append(b+r*sin(ANGLE))
        ANGLE+=0.36
    MA=2*r
    MI=2*r

#   Plotting circle (special case of ellipse)
    fig,ax=py.subplots(subplot_kw={'aspect':'equal'})
    py.plot(XN,YN)
    py.pause(1)
    Check = True
    while Check:
        MD = [[a],[b],[1]]
        transform = input("Enter Transformation : ")
        if transform != 'quit':
            # Translating the ellipse
            if transform[0] == 'T':
                sss1,ssx21,ssy21 = transform.split()
                CM = [[C[0]],[C[1]],[1]]
                C[0],C[1],de = Functions.translate(float(ssx21),float(ssy21),CM)      
                for tr91 in range(len(XN)):
                    MS91 = [[XN[tr91]],[YN[tr91]],[1]]
                    XN[tr91],YN[tr91],wtl = Functions.translate(float(ssx21),float(ssy21),MS91)
                print(C,MA,MI)
                py.plot(XN,YN)
                py.pause(1)
            # Scaling the ellipse
            if transform[0] == 'S':
                ss1,sx21,sy21 = transform.split()
                CM1 = [[C[0]],[C[1]],[1]]
                C[0],C[1],de = Functions.scaling(float(sx21),float(sy21),CM1)
                MMA=[[MA],[MI],[1]]
                MA,MI,de1 = Functions.scaling(float(sx21),float(sy21),MMA)
                print(C,MA,MI)
                for tr1 in range(len(XN)):
                    MS11 = [[XN[tr1]],[YN[tr1]],[1]]
                    XN[tr1],YN[tr1],wt = Functions.scaling(float(sx21),float(sy21),MS11)
                py.plot(XN,YN)
                py.pause(1)
            # Rotating the ellipse
            if transform[0] == 'R':
                rr,Ang = transform.split()
                CM2 = [[C[0]],[C[1]],[1]]
                C[0],C[1],de = Functions.rotate(float(Ang),CM2)
                for tr1 in range(len(XN)):
                    MSp = [[XN[tr1]],[YN[tr1]],[1]]
                    XN[tr1],YN[tr1],wt0 = Functions.rotate(float(Ang),MSp)
                # printing in the following order :
                # [X-coordinate of center,Y-coordinate of center] Major axis length Minor axis length
                print(C,MA,MI)
                py.plot(XN,YN)
                py.pause(1)
        else:
            Check = False
            

if shape == 'polygon':
#   Taking space seperated numbers as input which are the coordinates of the
#   vertices of the polygon
    x=input("x : ")
    y=input("y : ")
    v=x.split()
    xi = list(map(float,v))
    xp = list(map(float,v))
    xp.append(xp[0])
    z=y.split()
    yi = list(map(float,z))
    yp = list(map(float,z))
    yp.append(yp[0])
    py.ion()
    # plotting the polygon
    fig,ax=py.subplots(subplot_kw={'aspect':'equal'})
    py.plot(xp,yp)
    py.pause(1)
    Check1 = True
    while Check1:
        # Input: transformation required
        trans = input("Enter Transformation : ")
        if trans != 'quit':
            for r in range(len(xi)):
                MP=[[xi[r]],[yi[r]],[1]]
                # Translating polygon
                if trans[0] == 'T':
                    tt,dxt,dyt = trans.split()
                    xi[r],yi[r],was = Functions.translate(float(dxt),float(dyt),MP)

                # Rotating polygon
                if trans[0] == 'R':
                    ra,angle = trans.split()
                    angle = float(angle)
                    xi[r],yi[r],was = Functions.rotate(angle,list(MP))

                # Scaling polygon
                if trans[0] == 'S':
                    sa,sxs,sys = trans.split()
                    xi[r],yi[r],was = Functions.scaling(float(sxs),float(sys),MP)
            Xp = copy.deepcopy(xi)
            Xp.append(Xp[0])
            Yp = copy.deepcopy(yi)
            Yp.append(Yp[0])
            ansx = str(round(xi[0], ndigits = 2))        
            for g in range(1,len(xi)):
                ansx = ansx + " " + str(round(xi[g],ndigits = 2))
            ansy = str(round(yi[0], ndigits = 2))
            for g1 in range(1,len(yi)):
                ansy = ansy + " " + str(round(yi[g1],ndigits = 2))
            print(ansx)
            print(ansy)
            py.plot(Xp,Yp)
            py.pause(1)

        else :
            Check1 = False
                
    
    
    
        
    
