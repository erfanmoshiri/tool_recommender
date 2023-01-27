import os

import numpy as np
import pandas as pd

from tools.models import Feature


# user_features = []


# while(True):
#     user_feature = input('Enter feature: ')
#     user_features.append(user_feature)
#     if user_feature == '':
#         user_features.pop()
#         break

def edit_csv():
    curr_dir = os.getcwd()
    here_dir = os.path.join(curr_dir, 'tools', 'utils', 'dataset.csv')
    dataset = pd.read_csv(here_dir)

    feat = Feature.objects.filter(id=66).values_list('name', flat=True)
    for name in feat:
        max = -1
        max_i = -1
        for i in range(0, 10):
            cell = dataset._get_value(i, name)
            if cell > max:
                max = cell
                max_i = i
        col_max = dataset._get_value(max_i, name)
        for j in range(0, 10):
            c = dataset._get_value(j, name)
            c = c / col_max
            dataset.loc[j, name] = c

    dataset.to_csv(here_dir, index=False)


def get_top(user_features):
    curr_dir = os.getcwd()
    here_dir = os.path.join(curr_dir, 'tools', 'utils', 'dataset.csv')
    dataset = pd.read_csv(here_dir)

    i = 0
    n_tools = 10
    curr_tool_sum = 0
    sum_feature_values = []

    while (i < n_tools):
        for user_feature in user_features:
            curr_tool_sum += dataset._get_value(i, user_feature)
        sum_feature_values.append(curr_tool_sum)
        curr_tool_sum = 0
        i += 1

    tops_index = []
    for i in range(5):
        max_sum_row = np.argmax(sum_feature_values)
        tops_index.append(max_sum_row)
        sum_feature_values[max_sum_row] = -1

    res = []
    for i in tops_index:
        res.append(dataset._get_value(i, 'TOOL'))
        # print(dataset._get_value(i, 'TOOL'))
    return res
