import pandas as pd
import numpy as np
from scipy import stats


chat_id = 661128504 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.09
    t_stat, p_value = stats.ttest_ind(x, y)
    t_crit = stats.t.ppf(1-alpha/2, len(x)+len(y)-2)
    
    if abs(t_stat) > t_crit:
        return False
    else:
        return True

