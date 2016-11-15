import re
import os
import os.path
"""
\d 表示数字
\w表示字母 数字 下划线
\s 表示空格 tab 
？表示0或者1
+ 表示1 或者更多
* 表示0 或者更多
[] 表示一定范围的任意一个在[]，* + 会失效但\s \d \w 不会



"""
regu=re.compile(r'lo\w+')
regu1=re.compile(r'\w+.txt')
regu2=re.compile(r'\w+\s\w+')
currentWork=os.getcwd()
for root, dirs, files in os.walk(currentWork):
	for f in files:
		file=regu1.match(f)
		if file:
			print(str(file))
			os.unlink(os.path.join(currentWork,f))