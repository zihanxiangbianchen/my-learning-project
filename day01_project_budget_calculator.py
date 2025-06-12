# 欢迎语句
print("欢迎使用日本旅行预算计算器")

#询问用户信息
user_name = input("请输入你的名字")
user_dirction = input("你的目的地是？")
user_time = input ("旅行时间多久？") #此处出现第一个问题，不知道如何设置input的类型
user_time = int(user_time)
user_jrpass = input("是否有日本铁路票？")

#判断住宿费用
if user_dirction == "东京":
    living_fine = 800
elif user_dirction == "大阪":
    living_fine = 700
elif user_dirction == "京都":
    living_fine = 650
else:
    living_fine = 500

#判断交通费用
if user_jrpass == "是":
    trans_fine = 100
else:
    trans_fine = 200

#每日饮食
food_fine = 300

#总花销 机票固定4000元
total_fine = (food_fine + trans_fine + living_fine)*user_time + 4000

#打印用户预算
#此处出现第二个错误，加号只能连接两个字符串，我这里吧usertime转化为int以方便我运算了，导致我无法使用+
print("您的名字是 " + user_name)
print("您的目的地是 " + user_dirction)
print("您的旅游天数是 " + str(user_time))
print("-------------------")
print("您的总花销为：" + str(total_fine))
print("其中：")
print("住宿费用是：" + str(living_fine) + "每天，*" + str(user_time) + " = " +str(living_fine*user_time))
print("交通费用是：" + str(trans_fine) + "每天，*" + str(user_time) + " = " +str(trans_fine*user_time))
print("餐饮费用是：" + str(food_fine) + "每天，*" + str(user_time) + " = " +str(food_fine*user_time))
