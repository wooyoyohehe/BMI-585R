# -*- coding: utf-8 -*
# 递推的核心是找到前一项和后一项的关系，比如爬楼梯问题就是

# Question 1
# If there are 10 stairs, you can go up two steps or step once, how many ways can you go up this stair?

def go_up_1(n):
    if n == 1:return 1
    if n == 2:return 2
    return go_up_1(n-1) + go_up_1(n-2)

def go_up_2(n):
    l = [1,2]
    for i in range(3,n):
        temp = l[1]
        l[1] = l[0] + l[1]
        l[0] = temp
    return l[0] + l[1]


# Question 2
# cutting-rod
# length = [1,2,3,4,5,6,7,8,9,10]
# price  = [1,5,8,9,10,17,17,20,24,30]
# 方法一：自底向上的动态规划
# 用小子问题的解去解决更大的问题;时间复杂度较好
def rod_cutting(price, length):
    solution = [0,0] * (length + 1)
    max_price = [0] * (length + 1)
    for i in range(1, length+1):
        for j in range(1, i+1):
            # max_price[i] =  max(max_price[i-j] + price[j], max_price[i]) 
            if max_price[i-j] + price[j] > max_price[i]:
                max_price[i] = max_price[i-j] + price[j]
                solution[i] = [i-j, j]
    return max_price, solution

length = [0,1,2,3,4,5,6,7,8,9,10]
price  = [0,1,5,8,9,10,17,17,20,24,30]
print rod_cutting(price, 10)


    


