def countInRows(l, thing):
    #loop over each row of the 2D list and count the occurences of 'thing' in list 'l'
    #append count for each row in 'row_count' list and return it
    row_count=[]
    return row_count

def countInCols(l, thing):
    #loop over each column of the 2D list and count the occurences of 'thing' in list 'l'. 
    #append count for each column in 'col_count' list and return it
    col_count=[]
    return col_count

def countIn2x2Grids(l, thing):
    #For a given grid with even number of rows and columns, this function should loop through each 2x2 grid.
    #call function countInGrid for each possible 2x2 grid in this function inside a nested for-loop
    #pass the starting row and column for each grid
    #append count values for each grid in count_grids list
    count_grids =[]
    return count_grids
        
def countInGrid(l, thing, start_i, start_j):
    #should return count of 'thing' in given grid. Should be a number not a list
    c = 0
    return c

def main():
    l = [ ["A", 1 , 2 , 3 , 4 , 5],
          ["A","A", 2 , 3 , 4 , 5],
          [ 1 , 2 , 3 , 4 , 5 , 5 ],
          ["A","A","A","A","A","A"],
          ["A", 3 ,"A", 4 ,"A","A"],
          [ 1 , 3 , 5 ,"A", 5 ,"A"] 
        ]
    print(countInRows(l,"A"))
    print(countInCols(l, "A"))
    print(countIn2x2Grids(l, "A"))
    
if __name__ == "__main__":
    main()