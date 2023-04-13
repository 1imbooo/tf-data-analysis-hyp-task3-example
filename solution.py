import pandas as pd
import numpy as np
from scipy import stats


chat_id = 661128504 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.09
    t_stat, p_value = stats.ttest_ind(y, x, equal_var=False, alternative="greater")
    
    # Сравнение с критическим значением
    t_crit = stats.t.ppf(1-alpha/2, len(x)+len(y)-2)   
    
    if t_stat > t_crit and p_value < alpha:
        return True
    else:
        return False
