import re
import os
import os.path
"""
\d ��ʾ����
\w��ʾ��ĸ ���� �»���
\s ��ʾ�ո� tab 
����ʾ0����1
+ ��ʾ1 ���߸���
* ��ʾ0 ���߸���
[] ��ʾһ����Χ������һ����[]��* + ��ʧЧ��\s \d \w ����



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