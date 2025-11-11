#%%
def has_adjacent_duplicate(L):
    for i in range(len(L) -1):
        if L[i]== L[i+1]:
            return True
        else:
            pass
    return False
#Example
print(has_adjacent_duplicate([2,4,4,5,5,6]))  
#%%  
    
   
