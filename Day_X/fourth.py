# coding=gbk

import random

#��ʼ����Ҫ����ֵ
workers = list(range(300))
first_reward = 3
second_reward = 6
third_reward = 30


#�齱����
#���Ƚ�
third_reward_peo = random.sample(workers,30)
print('�鵽���Ƚ������ǣ� '+ str(third_reward_peo))
for x in third_reward_peo:
    workers.remove(x)

#���Ƚ�
second_reward_peo = random.sample(workers,6)
print('�鵽���Ƚ�������: '+ str(second_reward_peo))
for y in second_reward_peo:
    workers.remove(y)

#���Ƚ�
third_reward_peo = random.sample(workers,3)
print('�鵽���Ƚ������ǣ� '+ str(third_reward_peo))
for z in third_reward_peo:
    workers.remove(z)


