Name:only_common

Explanation:Please use it when you want to extract only the common part of two csv.

For example)

>only_common.py a.csv b.csv utf-8

a,csv  abdefg
b.csv  abcdhi

Common is abd.

License)
MIT license

Using method:  
pip install only_common  
import only_common as oc  
oc.excommon('a.csv', 'b.csv', 'shift-jis')  
>あいこかきこさ  
