import sys
import io
import csv
import pprint
import pandas as pd

if(len(sys.argv) <= 1):
    print('For example: only_common.py a.csv b.csv shift-jis')
    sys.exit()

sys.argv[0] = 'a.csv'
sys.argv[1] = 'b.csv'
sys.argv[2] = 'shift-jis'
print('sys.argv[0]:', sys.argv[0])
print('sys.argv[1]:', sys.argv[1])
print('sys.argv[2]:', sys.argv[2])

df_a = pd.read_csv(sys.argv[0], encoding=sys.argv[2], header=None)
list_a = []
list_a = list(df_a.loc[0][0])

df_b = pd.read_csv(sys.argv[1], encoding=sys.argv[2], header=None)
list_b = []
list_b = list(df_b.loc[0][0])

after_content = ""
def deplicate_delete_csv(content, content2, after_content):
    for i in range(len(content)):
        if content[i] != content2[i]:
            for num in range(len(content) - i):
                if content2[i] == content[i+num]:
                    after_content = content[:i] + content[(i+num):]
                    return after_content
    return content


while list_a != list_b:
    if(len(list_a) > len(list_b)):
        list_a_old = list_a
        list_a = deplicate_delete_csv(list_a, list_b, after_content)
        if list_a_old == list_a:
            break
    elif(len(list_a) < len(list_b)):
        list_b_old = list_b
        list_b = deplicate_delete_csv(list_b, list_a, after_content)
        if list_b_old == list_b:
            break
    else:
        list_a_old = list_a
        list_a = deplicate_delete_csv(list_a, list_b, after_content) 
        list_b_old = list_b
        list_b = deplicate_delete_csv(list_b, list_a, after_content)
        if list_b_old == list_b:
            break

StrA = "".join(list_a)
print('Only common parts:', StrA)
sys.exit

