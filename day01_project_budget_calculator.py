ACCOMMADATION_PRICE = {
    "东京":800,
    "大阪":700,
    "京都":650,
    "其他":500,
}
PLANE_PRICE = 4000


# 欢迎语句
print("欢迎使用日本旅行预算计算器")


#询问用户信息
user_name = input("请输入你的名字")
user_dirction = input("你的目的地是？")
user_time = input ("旅行时间多久？") #此处出现第一个问题，不知道如何设置input的类型
user_time = int(user_time)
user_jrpass = input("是否有日本铁路票？")

#判断住宿费用
living_fine = ACCOMMADATION_PRICE[user_dirction]

#判断交通费用
if user_jrpass == "是":
    trans_fine = 100
else:
    trans_fine = 200

#每日饮食
food_fine = 300

#总花销 机票固定4000元
total_fine = (food_fine + trans_fine + living_fine)*user_time + PLANE_PRICE

#打印用户预算
#此处出现第二个错误，加号只能连接两个字符串，我这里吧usertime转化为int以方便我运算了，导致我无法使用+

print("-------------------")
print(f"尊敬的{user_name},您好！")
print(f"您的目的地是{user_dirction} ")
print(f"您的旅游天数是{user_time}")
print("-------------------")
print(f"您的总花销为：{total_fine}")
print("其中：")
print(f"住宿费用是：每天{living_fine}元，{user_time}天共计{user_time*living_fine}元")
print(f"交通费用是：每天{trans_fine}元，{user_time}天共计{user_time*trans_fine}元")
print(f"饮食费用是：每天{food_fine}元，{user_time}天共计{user_time*food_fine}元")