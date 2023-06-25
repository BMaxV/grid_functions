class GridHandler:
    def __init__(self):
        self.grid = {}
    
    def make_grid(self,x,y,fill=None):
        grid={}
        xc=0
        while xc < x:
            yc=0
            while yc < y:
                grid[(xc,yc)]=fill
                yc+=1
            xc+=1
        return grid
    
    def paint_area(self,startx,starty,x,y,value):
        xc=0
        while xc < x:
            yc=0
            while yc < y:
                self.grid[(startx+xc,starty+yc)] = value
                yc+=1
            xc+=1

def get_three_by_three_environment(x_y_cell_key,diff):
    x,y=x_y_cell_key
    l=[
    (x+diff,y),
    (x+diff,y+diff),
    (x+diff,y-diff),
    #(x,y),
    (x,y+diff),
    (x,y-diff),
    (x-diff,y),
    (x-diff,y+diff),
    (x-diff,y-diff),
    ]
    return l
    
    

def threebythree_y_flip(my_dict):
    new_dict = {}
    new_dict[(0,0)] = my_dict[(0,0)]
    
    new_dict[(1,1)] = my_dict[(1,-1)]
    new_dict[(1,-1)] = my_dict[(1,1)]
    new_dict[(-1,1)] = my_dict[(-1,-1)]
    new_dict[(-1,-1)] = my_dict[(-1,1)]
    
    new_dict[(1,0)] = my_dict[(1,0)]
    new_dict[(-1,0)] = my_dict[(-1,0)]
    new_dict[(0,1)] = my_dict[(0,-1)]
    new_dict[(0,-1)] = my_dict[(0,1)]
    
    return new_dict

def threebythree_x_flip(my_dict):
    new_dict={}
    new_dict[(0,0)]=my_dict[(0,0)]
    
    new_dict[(1,1)] = my_dict[(-1,1)]
    new_dict[(1,-1)] = my_dict[(-1,-1)]
    new_dict[(-1,1)] = my_dict[(1,1)]
    new_dict[(-1,-1)] = my_dict[(1,-1)]
    
    new_dict[(1,0)] = my_dict[(-1,0)]
    new_dict[(-1,0)] = my_dict[(1,0)]
    new_dict[(0,1)] = my_dict[(0,1)]
    new_dict[(0,-1)] = my_dict[(0,-1)]
    return new_dict


def single_rotation(my_dict):
    new_dict={}
    new_dict[(0,0)]=my_dict[(0,0)]
    
    new_dict[(1,-1)] = my_dict[(-1,-1)]
    new_dict[(1,1)] = my_dict[(1,-1)]
    new_dict[(-1,1)] = my_dict[(1,1)]
    new_dict[(-1,-1)] = my_dict[(-1,1)]
    
    new_dict[(1,0)] = my_dict[(0,-1)]
    new_dict[(0,1)] = my_dict[(1,0)]
    new_dict[(-1,0)] = my_dict[(0,1)]
    new_dict[(0,-1)] = my_dict[(-1,0)]
    return new_dict


def permutations(R,my_p):
    """this is only using flips, but on 3x3 that's the same thing
    as rotation..."""
    new_dict={}
    
    my_f1 = single_rotation(my_p)
    my_f2 = single_rotation(my_f1)
    my_f3 = single_rotation(my_f2)
    
    r = [my_p, my_f1, my_f2, my_f3]
    
    nl = []
    for x in r:
        f1 = threebythree_x_flip(x)
        f2 = threebythree_y_flip(x)
        nl.append(f1)
        nl.append(f2)
    
    r += nl
    
    return r
