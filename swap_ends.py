def swap_ends(L, k):
    if k <= 0 or len(L) == 0 or k > len(L) // 2:
        return (L.copy(), 0)
    
    new_list = L.copy()
    
    new_list[:k], new_list[-k:] = L[-k:], L[:k]
    
    return (new_list, k)

print(swap_ends([9,8,7,6,5,4,3],2))

  
