import numpy as np
import sympy as sp
import time
import os
import sys
import pickle
from math import pi, sin, cos

np.set_printoptions(threshold=sys.maxsize)

# Overvej at bruge numpys egen funktion til at gemme matricer i stedet for pickle: https://stackoverflow.com/questions/2848099/saving-and-loading-a-numpy-matrix-in-python

def safe_open(filepath, mode='r'):
    """
    Checks if file exists and gives a friendly error in case it doesn't.
    """
    if not os.path.isfile(filepath):
        print(f"File {filepath} not found. Current dir is {os.getcwd()}")
        sys.exit(1)
    return open(filepath, mode)

def store_sympy_expr(expr, file):
    with open(file, "wb") as f:
        pickle.dump(expr, f)

def load_sympy_expr(file):
    with safe_open(file, "rb") as f:
        return pickle.load(f)

def convert_to_numpy(data):
    d = np.array(data)
    print(f"Got data:\n{d}")
    print("\n\n")
    qdd2 = qdd1 = 3
    q2 = q1 = 1
    qd2 = qd1 = 2
    for i in d:
        for a in i:
            print(f"a : {str(a)}")
            print(eval(str(a)))
            print("\n")


def forloop_method(args_sym, args_num, reg_test):
    result_num_for_loop = []  # Initialization
    t0_for = time.time()
    for j in range(1):#range(reg_test.shape[0]):
        g_fun_j = sp.lambdify(args_sym, reg_test[j, :], 'numpy')
        result_num_j = np.zeros((args_num.shape[1], reg_test.shape[1]))
        for k in range(args_num.shape[1]):
            result_num_j[k, :] = g_fun_j(*args_num[:, k])
        result_num_for_loop.append(result_num_j)
    t_for = time.time() - t0_for
    print(f"Time, for-loop method: {t_for:.4f} s.")
    # with open("forloop.txt",'w') as f:
    #     f.write(str(result_num_for_loop))

    return t_for

def lamdify_method(args_sym, args_num, reg_test):
    result_num_function = []  # Initialization
    t0_fcn = time.time()
    for j in range(1):#range(reg_test.shape[0]):
        g_fun_j = sp.lambdify(args_sym, reg_test[j, :], 'numpy')
        result_num_j = g_fun_j(*args_num)
        result_num_function.append(result_num_j)
    t_fcn = time.time() - t0_fcn
    print(f"Time, lamdify method: {t_fcn:.4f} s.")
    return t_fcn

def comprehension_method(args_sym, args_num, reg_test):
    result_num_comprehension = []
    t0_com = time.time()
    for j in range(1):#range(reg_test.shape[0]):
        g_fun_j = sp.lambdify(args_sym, reg_test[j, :], 'numpy')
        result_num_j = [g_fun_j(*args_num[:, k]) for k in range(args_num.shape[1])]
        result_num_comprehension.append(result_num_j)
    t_com = time.time() - t0_com
    print(f"Time, comprehension method: {t_com:.4f} s.")
    return t_com


def numpy_eval_method(dict_args, reg_test):
    result_num_eval = []
    keyname = list(dict_args.keys())[0]
    list_of_dict = [{name: arr_val.pop(0) for name,arr_val in dict_args.items()} for n in dict_args[keyname]]
    t0_eval = time.time()
    sym_arr = np.array(reg_test).astype(str) # convert to string

    #sym_arr = np.array(reg_test)

    # for cur_dict in list_of_dict:
    #     m1 = np.array([[eval(elem, {'sin':sin, 'cos':cos, 'pi':pi}, cur_dict) for elem in elems] for elems in sym_arr ], dtype=np.float64)
    #     result_num_eval.append(m1)

    
    result_num_eval = [np.array([ [eval(elem, {'sin':sin, 'cos':cos, 'pi':pi}, cur_dict) for elem in elems] for elems in sym_arr], dtype=np.float64) for cur_dict in list_of_dict] # [eval(elem, {'sin':sin, 'cos':cos, 'pi':pi}, cur_dict) for elem in elems]


    t_eval = time.time() - t0_eval
    print(f"Time, numpy eval method: {t_eval:.4f} s.")
    
    # with open("numpy_eval.txt",'w') as f:
    #     f.write(str(result_num_eval))

    return t_eval


def test_lambdify_2():
    q1, q2, qd1, qd2, qdd1, qdd2 = sp.symbols('q1 q2 qd1 qd2 qdd1 qdd2')
    q = [q1, q2]
    qd = [qd1, qd2]
    qdd = [qdd1, qdd2]
    args_sym = q + qd + qdd
    n_samples = 100000
    q_num = np.ones((2, n_samples))
    qd_num = np.ones((2, n_samples))
    qdd_num = np.ones((2, n_samples))
    args_num = np.concatenate((q_num, qd_num, qdd_num))
    reg_test = load_sympy_expr('./reg_test.pickle')

    # q_num1 = np.arange(1, n_samples, 1)
    # q_num2 = np.arange(1, n_samples, 1)
    # qd_num1 = np.arange(1, n_samples, 1)
    # qd_num2 = np.arange(1, n_samples, 1)
    # qdd_num1 = np.arange(1, n_samples, 1)
    # qdd_num2 = np.arange(1, n_samples, 1)
    dict_args = {'q1': list(q_num[0]), 'q2': list(q_num[1]), 'qd1': list(qd_num[0]), 'qd2': list(qd_num[1]), 'qdd1': list(qdd_num[0]), 'qdd2': list(qdd_num[1])}
    t_eval = numpy_eval_method(dict_args, reg_test)


    # # for loop
    #t_for = forloop_method(args_sym, args_num, reg_test)
    # # comprehension
    # t_com = comprehension_method(args_sym, args_num, reg_test)
    # # lamdify
    # t_fcn = lamdify_method(args_sym, args_num, reg_test)
    
    # print(f"Relative speed-up: {100.0*(t_for-t_fcn)/t_for:.1f} %")





if __name__ == "__main__":
    test_lambdify_2()