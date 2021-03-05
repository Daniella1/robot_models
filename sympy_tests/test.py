import numpy as np
from numpy import sin, cos, pi



symbolic_array = np.array([[0, 1, 'a'], [2,3, 'sin(b)']])

def cm(arr, dict_args):
    matrices = []
    keyname = list(dict_args.keys())[0]
    list_of_dict = [{name: arr_val.pop(0) for name,arr_val in dict_args.items()} for n in dict_args[keyname]]
    print(list_of_dict)
    for cur_dict in list_of_dict:
        m1 = [[eval(elem, {'sin':sin, 'cos':cos, 'pi':pi}, cur_dict) for elem in elems] for elems in arr ]
        matrices.append(m1)
    return matrices


a = [10,20]
b = [30,40]

dict_args = {'a':a, 'b':b}
print(f"Symbolic: {symbolic_array}")
print(f"Evaled: {cm(symbolic_array, dict_args)}")


    # first_dict = list_of_dict.pop(0)
    # m1 = np.array([[eval(elem, {'sin':sin, 'cos':cos, 'pi':pi}, cur_dict) for elem in elems] for elems in sym_arr ])


    # newsym = compile(sym_arr, "string", "eval")
    # eval(newsym,{'sin':sin, 'cos':cos, 'pi':pi}, list_of_dict)
    # with open("symbolic_arr.txt",'w') as f:
    #     f.write(str(sym_arr))
