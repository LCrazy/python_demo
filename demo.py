import time,datetime
from math import sqrt
from functools import reduce

# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
def demo_01():
    arrNumbers = [ ]
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if(i!=j) and (j!=k) and (i!=k):
                    number = str(i) + str(j) + str(k)
                    arrNumbers.append(number)
    return arrNumbers

# 业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
def demo_02(profit):
    try:
        bonus = 0
        profitArr = [0,100000,200000,400000,600000,1000000]
        profitNum = [0.1,0.075,0.05,0.03,0.015,0.01]
        for i in range(0,6):
            if profit > profitArr[i]:
                bonus += ( profit - profitArr[i]) * profitNum[i]
    except ValueError:
        print('value error')
    return bonus

# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# x + 100 = n*n
# x + 100 + 168 = m*m
# m*m -n*n = 168
def demo_03 ():
    numbers = []
    for i in range(1,85):
        if 168 % i == 0:
            j = 168 / i
        if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
            m = (i + j) / 2
            y = m*m - 268
            n = (i - j) / 2
            x = n * n - 100
            if x == y :
                numbers.append(x)
    return numbers

# 输入某年某月某日，判断这一天是这一年的第几天？
def demo_04 (year, month, day):
    days = 0
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    try:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: #闰年
            dur = 1
        for i in range(1,len(months)+1):
            if i == month:
                if i ==2 :
                    days += day
                else:
                    days += day + dur
                break
            else:
                days += months[i-1]
    except ValueError:
        print('input value is error')
    return days

# 输入三个整数x,y,z，请把这三个数由小到大输出。
def demo_05(x, y, z):
    numbers = [x,y,z]
    numbers.sort()
    return numbers

# 斐波那契数列 0、1、1、2、3、5、8、13、21、34、
def demo_06(number):
    golden_sections = []
    for n in range(0,number):
        if n == 0 or n == 1:
            golden_section = n
        elif  n == 2:
            golden_section = 1
        else:
            golden_section = (golden_sections[n-1]+golden_sections[n-2])
        golden_sections.append(golden_section)
    return golden_sections

# 将一个列表的数据复制到另一个列表中
def demo_07(listData):
    return listData[:]

# 输出 9*9 乘法口诀表
def demo_08():
    for i in range(1,10):
        for j in range(1,i+1):
           print(f' {i} * {j} = {i*j}',end=' ')
           if i == j:
               print('')
               break

# 暂停一秒输出
def demo_09(args):
    time.sleep(1)
    print(f'time.sleep(1) 输出结果：{args}')

# 暂停一秒输出，并格式化当前时间
def demo_10(args):
    input_time = time.localtime(time.time())
    time.sleep(1)
    sleep_time = time.localtime(time.time())
    # 2020-03-24 15:06:26
    input_time = time.strftime('%Y-%m-%d %H:%M:%S',input_time)
    # Tue Mar 24 15:07:37 2020
    sleep_time = time.strftime('%a %b %d %H:%M:%S %Y',sleep_time)
    print(f'输入时间：{input_time}  输入内容：{args}')
    print(f'输出时间：{sleep_time}')

    # 将格式字符串转换为时间戳
    # a = "Sat Mar 28 22:24:24 2016"
    # time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
    # time.struct_time(tm_year=2020, tm_mon=3, tm_mday=24, tm_hour=15, tm_min=10, tm_sec=16, tm_wday=1, tm_yday=84, tm_isdst=0)
    # time.localtime(time.time())

# 有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
# 第几个月   有几对兔子 
#   1          1 
#   2          1
#   3          2
#   4          3
#   5          5
#   6          8
# 斐波那契数列
def demo_11(months):
    rabbit_numbers = []
    try:
        for month in range(1,months+1):
            if month == 1 or month == 2:
                rabbit_num = 1
            else:
                rabbit_num = rabbit_numbers[month-2] + rabbit_numbers[month-3]
            rabbit_numbers.append(rabbit_num)
    except IndexError :
        print('请输入正确月份')
    finally:
        return rabbit_numbers

# 判断101-200之间有多少个素数，并输出所有素数
# 素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数
def demo_12():
    prime_numbers = []
    flag = 0
    for num in range(101,201):
        sqrt_num = int(sqrt(num))
        for n in range(2,sqrt_num + 1):
             if num % n == 0:
                 flag = 1
                 break
        if flag == 0:
            prime_numbers.append(num)
        flag = 0
    return prime_numbers

# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身
def demo_13():
    numbers = []
    for number in range(100,1000):
        i = number // 100
        j = number // 10 % 10
        k = number % 10
        add_sum = i ** 3 + j ** 3 + k ** 3
        if add_sum == number:
            numbers.append(number)
    return numbers

# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5
def demo_14(input_num):
    reslut = '{} ='.format(input_num)
    if input_num <= 0 :
        input_num = int(input('请输入一个正确的数 : ' ))
        demo_14(input_num)
    elif input_num == 1:
        reslut = '{} = '.format(input_num)
    else:
        while input_num != 1:
            for i in range(2, input_num+1):
                if input_num % i == 0:
                    input_num //= i
                    if input_num == 1:
                        reslut +='{}'.format(i)
                    else:
                       reslut += '{} * '.format(i)
                    break
    return reslut

    
# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
def demo_15(input_score):
    if isinstance(input_score,float):
        # reslut = (input_score >= 90) ? 'A': ((input_score >= 60) ? 'B': 'C')
        if input_score >= 90:
            reslut = 'A'
        elif input_score >= 60:
            reslut = 'B'
        else:
            reslut = 'C'
    else:
        input_score = int(input('请输入一个正确的分数 : ' ))
        demo_15(input_score)
    return reslut

# 输出指定格式的日期。datetime
def demo_16():
   dateT  = datetime.date.today().strftime('%d/%m/%Y')
   reslut = '今天日期：{}\n\r'.format(dateT)
   creatT = datetime.date(1949,10,1)
   reslut += '创建日期: {}\n\r'.format(creatT.strftime('%d/%m/%Y'))
   next_date = creatT+ datetime.timedelta(days=1)
   reslut += '创建日期的下一天: {}\n\r'.format(next_date.strftime('%d/%m/%Y'))
   replce_date = creatT.replace(year = creatT.year + 10)
   reslut += '日期替换: {} \n\r'.format(replce_date.strftime('%d/%m/%Y'))
   return reslut

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
def demo_17(args):
    length_abc = 0
    length_space = 0
    length_dig = 0
    length_other = 0
    for s in args:
        if s.isalpha(): # 字母
            length_abc += 1
        elif s.isspace(): # 空格
            length_space += 1
        elif s.isdigit(): # 数字
            length_dig += 1
        else: #其他字符
            length_other += 1
    return '字母个数:{}\n\r空格个数:{}\n\r数字个数:{}\n\r其他字符个数:{}\n\r'.format(length_abc,length_space,length_dig,length_other)  

# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制
def demo_18(n,a):
    num = 0
    add_num = []
    for i in range(n):
        num +=a
        a *= 10
        add_num.append(num)
    num_sum = reduce(lambda x,y : x + y, add_num )
    print(f'相加数集合{add_num}')
    return num_sum

# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
def demo_19():
    reslut = []
    for num in range(2,1001):
        k = []
        flag = num
        for i in range(1,num):
            if num % i == 0 : # 因子 
                flag -= i
                k.append(i)
        if flag == 0:
            print(f'{num}的因子集合:{k}')
            reslut.append(num)
    return reslut

# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def demo_20():
    height = 100.0
    times = 10
    sum_height = 0
    for i in range(times):
        if i == 0:
            sum_height = height
        else:
            sum_height += height*2
        height /= 2
    print(f'第十次高度 = {height}米,共经过 = {sum_height}米')


