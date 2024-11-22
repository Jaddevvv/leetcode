# https://www.deep-ml.com/problem/Reshape%20Matrix


def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    nb_cols = new_shape[1]
    final_list = []

    counter=0
    draft_list=[]
    for line in a:
        for value in line:
            draft_list.append(value)
            counter+=1
            if counter == nb_cols:
                final_list.append(draft_list)
                draft_list=[]
                counter=0
            
        
    return final_list



print(reshape_matrix([[1,2,3],[4,5,6]], (3, 2)))
print(reshape_matrix([[1,2,3,4],[5,6,7,8]], (2, 4)))
