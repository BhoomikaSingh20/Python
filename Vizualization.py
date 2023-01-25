from visualization import *

def show_curve():
    curve(x=arange(100), y=arange(100)**0.5, color=color.red)
def show_sphere():
    ball = sphere(pos=(1,2,1), radius=0.5)
def show_arrow():
    pointer=arrow(pos=(0, 2, 1), axis=(5, 0, 0), shaftwidth=1)
def show_rings():
    ring(pos=(1, 1, 1), axis=(0, 1, 0), radius=0.5, thickness=0.1)
def show_cylinder():
    rod= cylinder(pos=(0, 2, 1), axis=(5, 0, 0), radius=1)

ch= 'y'
while(ch=='y'):
    print('1. Curve')
    print('2. Sphere')
    print('3. Cone')
    print('4. Arrow')
    print('5. Rings')
    print('6. Cylinder')

    choice = int(input('Enter choice..'))
    if(choice == 1):
        show_curve()
    elif(choice == 2):
        show_sphere()
    elif(choice == 3):
        show_cone()
    elif(choice == 4):
        show_arrow()
    elif(choice == 5):
        show_rings()
    elif(choice == 6):
        show_cylinder()
    else:
        print('Wrong choice')
    ch= input('Do you want to continue (y/n)...')
