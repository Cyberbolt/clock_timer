clock_timer 是 Python 下的时间库，用于时间字符串处理，可在 Web 开发、数据分析 等领域使用。该库 80% 基于 datetime ，使用该库，您能更人性化地处理时间字符串，而无需每次查询 datetime 繁琐的接口。

clock_timer 主要用于时间加减计算、获取时间对应的周数和星座、获取当前时间、获取时间戳、时间戳和时间字符串的转换 等功能。后期仍会不断优化，欢迎留言。


### 安装方法

1.进入命令窗口，创建虚拟环境，依次输入以下命令

Linux 和 macOS :

```
python3 -m venv venv #创建虚拟环境
. venv/bin/activate #激活虚拟环境
```

Windows:

```
python -m venv venv #创建虚拟环境
venv\Scripts\activate #激活虚拟环境
```

2.安装 clock_timer 库，依次输入

```
pip install --upgrade pip
pip install clock_timer
```




### 简易功能概述

**一、可以对标准格式的时间字符串（如：2021-07-26 19:52:06）进行处理。**

1.加上 几 天

```
from clock_timer import timer


def main():
    time_start = '2021-07-26 19:52:06' #时间字符串
	#加上3天
    time_end = timer.add_days(time_start=time_start, days=3) 
    '''
        返回 time_start 时间加上 days 天 的时间
        time_start: 起始时间，格式如 2021-07-26 19:52:06
        days: 增加的天数，类型为 int
    '''    
    
    print(' 起始时间:', time_start, '\n', '修改时间:', time_end)


if __name__ == '__main__':
    main()

'''
终端输出:
 起始时间: 2021-07-26 19:52:06 
 修改时间: 2021-07-29 19:52:06
'''
```

2.减去 几 天
```
from clock_timer import timer


def main():
    time_start = '2021-07-26 19:52:06' #时间字符串
    #减去3天
    time_end = timer.sub_days(time_start=time_start, days=3) 
    '''
        返回 time_start 时间减去 days 天 的时间
        time_start: 起始时间，格式如 2021-07-26 19:52:06
        days: 减去的天数，类型为 int
    '''
    
    print(' 起始时间:', time_start, '\n', '修改时间:', time_end)


if __name__ == '__main__':
    main()

'''
终端输出:
 起始时间: 2021-07-26 19:52:06 
 修改时间: 2021-07-23 19:52:06
'''
```

3.加上 几 年
```
from clock_timer import timer


def main():
    time_start = '2021-07-26 19:52:06' #时间字符串
    #加上3年
    time_end = timer.add_years(time_start=time_start, years=3) 
    '''
        返回 time_start 时间加上 years 年 的时间
        time_start: 起始时间，格式如 2021-07-26 19:52:06
        years: 增加的年数，类型为 int
    '''
    
    print(' 起始时间:', time_start, '\n', '修改时间:', time_end)


if __name__ == '__main__':
    main()

'''
终端输出:
 起始时间: 2021-07-26 19:52:06 
 修改时间: 2024-07-26 19:52:06
'''
```

4.减去 几 年
```
from clock_timer import timer


def main():
    time_start = '2021-07-26 19:52:06' #时间字符串
    #减去3年
    time_end = timer.sub_years(time_start=time_start, years=3) 
    '''
        返回 time_start 时间减去 years 年 的时间
        time_start: 起始时间，格式如 2021-07-26 19:52:06
        years: 减去的年数，类型为 int
    '''
    
    print(' 起始时间:', time_start, '\n', '修改时间:', time_end)


if __name__ == '__main__':
    main()

'''
终端输出:
 起始时间: 2021-07-26 19:52:06 
 修改时间: 2018-07-26 19:52:06
'''
```

5.转换为 星期制
```
from clock_timer import timer


def main():
    time_day = '2021-07-26 19:52:06' #时间字符串
    #返回该时间是星期几
    time_end = timer.to_weekday(time_day=time_day) 
    '''
        返回 time_day 是星期几(0 到 6 分别代表 星期日 到 星期六)
        time_day: 时间，格式如 2021-07-26 19:52:06
    '''
    
    print(' 输入时间:', time_day, '\n', '星期:', time_end + 1)


if __name__ == '__main__':
    main()

'''
终端输出:
 输入时间: 2021-07-26 19:52:06 
 星期: 1
'''
```

6.转换为 时间对应的星座
```
from clock_timer import timer


def main():
    time_day = '2021-07-26 19:52:06' #时间字符串
    #返回该时间对应的星座
    time_end = timer.to_constellation(time_day=time_day) 
    '''
        返回 time_day 是哪个星座(星座使用中文名)
        time_day: 时间，格式如 2021-07-26 19:52:06
    '''
    
    print(' 输入时间:', time_day, '\n', '星座:', time_end)


if __name__ == '__main__':
    main()

'''
终端输出:
 输入时间: 2021-07-26 19:52:06 
 星座: 狮子座
'''
```

7.转换为 对应的年份的第几周
```
from clock_timer import timer


def main():
    time_day = '2021-07-26 19:52:06' #时间字符串
    #返回该时间是对应年份的第几周
    time_end = timer.how_many_weeks(time_day=time_day) 
    '''
        返回 time_day 是该年的第几周
        time_day: 时间，格式如 2021-07-26 19:52:06
    '''   
    
    print(' 输入时间:', time_day, '\n', '第', time_end, '周')


if __name__ == '__main__':
    main()

'''
终端输出:
 输入时间: 2021-07-26 19:52:06 
 第 30 周
'''
```


**二、自动获取当前时间点及其处理**

1.获取当前时间
```
from clock_timer import timer


def main():
    #获取当前时间
    result = timer.get_current_time() 
    '''
        获取当前时间
        格式如: 2021-07-26 19:52:06
    '''
    
    print(result)


if __name__ == '__main__':
    main()

'''
终端输出:
2021-08-14 23:05:00
'''
```

2.获取昨年的这个时刻
```
from clock_timer import timer


def main():
    #获取昨年的这个时刻
    result = timer.last_year() 
    '''
        获取当前时间一年前的时间点
    '''
    
    print(result)


if __name__ == '__main__':
    main()

'''
终端输出:
2020-08-14 23:07:07
'''
```

3.获取半年前的这个时刻
```
from clock_timer import timer


def main():
    #获取半年前的这个时刻
    result = timer.last_half_year() 
    '''
        获取当前时间半年前的时间点
    '''
    
    print(result)


if __name__ == '__main__':
    main()

'''
终端输出:
2021-02-12 23:08:25
'''
```

4.获取上个月的这个时刻
```
from clock_timer import timer


def main():
    #获取上个月的的这个时刻
    result = timer.last_month() 
    '''
        获取当前时间一月前的时间点
    '''
    
    print(result)


if __name__ == '__main__':
    main()

'''
终端输出:
2021-07-15 23:09:56
'''
```


**三、时间戳 和 标准时间字符串 的转换**

1.获取秒级时间戳
```
from clock_timer import timer


def main():
    #获取获取秒级时间戳
    result = timer.get_current_timestamp() 
    '''
        获取秒级时间戳
    '''
    
    print(result)


if __name__ == '__main__':
    main()

'''
终端输出:
1628953892
'''
```

2.时间戳 转 时间字符串
```
from clock_timer import timer


def main():
    #时间戳 转 时间字符串
    time_int = timer.get_current_timestamp() #获取妙级时间戳
    time_str = timer.int_to_str(time_int) #时间戳转字符串
    
    print(' 时间戳原格式:', time_int, '\n 转换后的格式:', time_str)


if __name__ == '__main__':
    main()

'''
终端输出:
 时间戳原格式: 1628954144 
 转换后的格式: 2021-08-14 23:15:44
'''
```

3.时间字符串 转 时间戳
```
from clock_timer import timer


def main():
    #时间戳 转 时间字符串
    time_str = '2021-07-26 19:52:06'
    time_int = timer.str_to_int(time_str) #时间字符串 转 时间戳
    
    print(' 时间字符串原格式:', time_str, '\n 转换后的格式:', time_int)


if __name__ == '__main__':
    main()

'''
终端输出:
 时间字符串原格式: 2021-07-26 19:52:06 
 转换后的格式: 1627300326
'''
```




