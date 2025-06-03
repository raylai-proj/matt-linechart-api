import pandas as pd
import matplotlib.pyplot as plt
import tkinter as Tk
from tkinter import filedialog
from utility.color import COLOR
TIME = ["time/mn", "charge time (min)"]
YAXIS = [""]
EXCELNAME = "sheet1.xlsx"
OPENFILEFOLDEREMOJI = "\U0001F4C2"
# EXCELNAME = "3Ah cell data sheet-SOC_vs_time_111023.xlsx"

def select_file():
    return filedialog.askopenfilename(title="Open "+OPENFILEFOLDEREMOJI, filetypes=[("Excel File",".xlsx xls")])

def check_valid_col(cols):
    # find valid columns for plot
    idxs = []
    for idx, val in enumerate(cols):
        if any(word in str.lower(val) for word in TIME):
            idxs += [idx]
    return idxs
    

def remove_suffix(val):
    # correct unit by remove suffix when having duplicated unit
    return val[:-2] if val[-2] == "." else val

file_path = select_file()
print("file_path:",file_path)

dfs = pd.read_excel(file_path, sheet_name=None)
for key, value in dfs.items():
    cur_df = value.copy()
    start_index = []
    cur_col = list(cur_df.columns)
    valid_cols = check_valid_col(cur_col)
    y_label_dict = dict()
    all_ylabel = dict()
    fig, ax = plt.subplots()
    fig.subplots_adjust(right=0.75)

    for idx, col in enumerate(valid_cols):
        x_label = cur_col[col]
        y_label = cur_col[col+1]
        cur_x = cur_df[x_label]
        cur_y = cur_df[y_label]

        # cor_x_label = remove_suffix(cur_col[col])
        cor_y_label = remove_suffix(cur_col[col+1])
        if idx == 0:
            ax.plot(cur_x, cur_y, color=COLOR[idx])
            ax.set_ylabel(cor_y_label, color=COLOR[idx])
            # ax.spines["right"].set_color(COLOR[idx])
            all_ylabel[cor_y_label] = True
            left_ylabel = cor_y_label
            ax.yaxis.set_tick_params()
            print(ax.yaxis.get_tick_params("major"))
            # y_label_dict[cor_y_label] = True
        elif cor_y_label == left_ylabel:
            ax.plot(cur_x, cur_y, color=COLOR[idx])
        else:
            par = ax.twinx()
            par.plot(cur_x, cur_y, color=COLOR[idx])
            if not cor_y_label in all_ylabel:
                par.set_ylabel(cor_y_label, color=COLOR[idx])            
                if y_label_dict:
                    par.spines["right"].set_position(("axes", 1.2))    
                # else:
                    # par.set_yticks(range(min(cur_x.astype(int)), max(cur_y.astype(int))+1))    
                    # par.spines["right"].set_color(COLOR[idx])
                # par.spines["right"].set_position(("axes", 1.1))
                y_label_dict[cor_y_label] = True
                all_ylabel[cor_y_label] = True
            # else:
            #     par.spines


    # for idx, val in enumerate(cur_col):
    #     if any(word in str.lower(val) for word in TIME):
    #         x_label = remove_suffix(val)
    #         y_label = remove_suffix(cur_col[idx+1])
    #         ax.set_ylabel(y_label)
    #         ax.plot(cur_df[x_label], cur_df[y_label])
            # plt.plot(cur_df[x_label], cur_df[y_label])
            # plt.ylabel(y_label)
            # print(x_label, y_label)

    
    plt.xlabel(TIME[0])
    plt.title(key)
    plt.show()

    # for idx in start_index:
    #     x_idx, y_idx = idx, idx+1
    #     x_label = cur_col[x_idx]
    #     y_label = cur_col[y_idx]
    #     x_col = cur_df.iloc[: , x_idx]
    #     y_col = cur_df.iloc[: , y_idx]
    #     print(x_label, y_label)


    # print(cur_col)
# cols = dfs.columns
# dfs = pd.read_excel("3Ah cell data sheet-SOC_vs_time_111023.xlsx", sheet_name=None, header=None)
# # print(dfs)
# for key, value in dfs.items():
#     # print(value.iloc[:,0])
#     title = value.iloc[:,0].dropna().astype("str").str.cat(sep=" ")
#     x_label = value.iloc[0, 1]
#     y_label = value.iloc[0, 2]
#     x_col = value.iloc[1:, 1]
#     y_col = value.iloc[1:, 2]
#     print(x_label, y_label)
#     print(x_col)
#     print(y_col)
#     print(title)
# print(dfs.keys())
# print("test")