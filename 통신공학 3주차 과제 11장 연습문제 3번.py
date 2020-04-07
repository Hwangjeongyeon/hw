#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 연습문제 11장 3번
# hint : 텍스트 파일이므로 open(filename,"r")과 같이 파일을 연다. 파일 안의 각 줄은 
# 다음과 같이 읽을 수 있다. 각 줄 안의 문자들은 다시 for 루프를 이용하면 된다.
# for line in infile :
# for ch in line :
# ....read


# In[1]:


from tkinter import * 
sentence={}
infile=open("C:\\HumptyDumpty.txt","r")
a=infile.read()
infile.close()

for line in a:
    for ch in line:
        if ch in sentence:
            sentence[ch] +=1
        else:
            sentence[ch]=1
print(sentence)


# In[ ]:




