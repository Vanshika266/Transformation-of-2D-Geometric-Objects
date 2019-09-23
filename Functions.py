# NAME - Vanshika
# Section - A

from math import *

def Multiply(M1,M2):
    """
    Multiplies two matrices M1 and M2

    Args:
        M1: matrix of the dimensions -> m rows and n columns (m X n)
        M2: matrix of the dimensions -> n rows and r columns (n X r)

    Returns:
        Nested List, denoting multiplied matrix
    """
    M3=[]
    w=0
    while w<len(M2[0]):
        tap=[]
        t=0
        while t<len(M2):
            tap.append(M2[t][w])
            t=t+1
        M3.append(tap)
        w=w+1
    M=[]
    # Multiplying matrices
    k=0
    sums=0
    while k<len(M1):
        j=0
        mpy=[]
        while j<len(M3):
            p=0
            sums=0
            while p<len(M3[j]):
                temp = (M1[k][p])*(M3[j][p])
                sums=sums+temp
                p=p+1
            mpy.append(sums)
            j=j+1
        M.append(mpy)
        k=k+1
    return M

def scaling(sx,sy,Mat):
    """
    Scale a point by a factor of sx along x axis and sy along y axis

    Args:
        sx: magnitude to be scaled along x axis
        sy: magnitude to be scaled along y axis
        Mat: A nested list, denoting a Matrix with elements as points

    Returns:
        This python functions returns the Transformed points x,y
    """
    # SM is the Scaling Matrix ( 3 X 3 )
    SM = [[sx,0,0],[0,sy,0],[0,0,1]]
    Scaled = Multiply(SM,Mat)
    # Scaled[0][0] is the updated x coordinate
    # Scaled[1][0] is the updated y coordinate
    return Scaled[0][0],Scaled[1][0],Scaled[2][0]

    
def rotate(Y,Mat):
    """
    This python function rotates a point by angle Y (0 <= Y <= 360) in the
    counter-clockwise direction about the origin

    Args:
        Y: angle of rotation (in degrees)
        Mat: Matrix of point to be transformed (in form of nested list)

    Returns:
        Updated/Transformed point x and y
    """
    # Converting angle into radians 
    Y = radians(Y)
    # RM is the Rotation Matrix (3 X 3)
    RM=[[cos(Y),-sin(Y),0],[sin(Y),cos(Y),0],[0,0,1]]
    Rotate_Matrix = Multiply(RM,Mat)
    # Rotate_Matrix[0][0] is the updated x coordinate
    # Rotate_Matrix[1][0] is the updated y coordinate
    return Rotate_Matrix[0][0],Rotate_Matrix[1][0],Rotate_Matrix[2][0]

def translate(dx,dy,Mat):
    """
    This python function translates a point by dx units along x-axis and dy units
    along y-axis

    Args:
        dx: Magnitude of translation along x-axis
        dy: Magnitude of translation along y-axis
        Mat: A nested list, denoting Matrix of points to be translated

    Returns:
        Translated points x and y
    """
    # MT is the Translation (3 X 3) Matrix
    MT=[[1,0,dx],[0,1,dy],[0,0,1]]
    Translated= Multiply(MT,Mat)
    # Translated[0][0] is the updated x coordinate
    # Translated[1][0] is the updated y coordinate
    return Translated[0][0],Translated[1][0],Translated[2][0]
    

            
    
