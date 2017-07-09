# personal weibo lottery purpose
# @hewhosawthedeep along with weibo user ID=5604614868. Thanks!

import numpy as np

flag = 0
tmp = ''
IDlist = []

with open('raw_from_wap.txt', 'r') as file:
    for line in file:  # filter out irrelevant strings
        if line[0] not in '0123456789':
            flag = 1
            tmp = line.strip()
            if '@' in line:
                mylist = [_.split(':')[0] for _ in line.split('@')[1:]]
                mylist = [_.strip().split(' ')[0].split('：')[0].replace('/', '') for _ in mylist]
                IDlist.extend(mylist)
        else:
            if flag:
                flag = 0
                IDlist.append(tmp)
                tmp = ''
            else:  # find @ sign
                flag = 0
                if '@' in line:
                    mylist = [_.split(':')[0] for _ in line.split('@')[1:]]
                    mylist = [_.strip().split(' ')[0].split('：')[0].replace('/', '') for _ in mylist]
                    IDlist.extend(mylist)
IDlist = list(set(IDlist))
IDlist.sort()  # seems `set()` may introduce uncontrollable randomness so give a sort here and shuffle it up later
print(len(IDlist))  
# The printed number should be less than repost count(~2174) showed at webUI
# because some of the users were reposting privately (i.e.friend circle only)
# if you have any doubt with this method, feel free to contact us.

np.random.seed(201707080)
np.random.shuffle(IDlist)  # to make sure we are blind from results

# arbitrarily this is for 100RMB/person part:
np.random.seed(201707081)
print('100x3 prize:', np.random.choice(IDlist, 3))
np.random.seed(201707082)
# and for 50/person:
print('50x3 prize:', np.random.choice(IDlist, 3))
