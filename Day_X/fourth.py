# coding=gbk

import random

#初始化需要的数值
workers = list(range(300))
first_reward = 3
second_reward = 6
third_reward = 30


#抽奖过程
#三等奖
third_reward_peo = random.sample(workers,30)
print('抽到三等奖的人是： '+ str(third_reward_peo))
for x in third_reward_peo:
    workers.remove(x)

#二等奖
second_reward_peo = random.sample(workers,6)
print('抽到二等奖的人是: '+ str(second_reward_peo))
for y in second_reward_peo:
    workers.remove(y)

#三等奖
third_reward_peo = random.sample(workers,3)
print('抽到三等奖的人是： '+ str(third_reward_peo))
for z in third_reward_peo:
    workers.remove(z)


