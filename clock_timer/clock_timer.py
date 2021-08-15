'''
    此模块用于处理时间，如 时间、时间戳获取，时间加减法
    如 一年前，半年前 等，格式如 2021-07-26 19:52:06
'''
import time
import datetime
from dateutil.relativedelta import relativedelta


def add_days(time_start: str, days: int) -> str:
    '''
        返回 time_start 时间加上 days 天 的时间
        time_start: 起始时间，格式如 2021-07-26 19:52:06
        days: 增加的天数，类型为 int
    '''
    time_start = datetime.datetime.strptime(time_start, '%Y-%m-%d %H:%M:%S')
    time_end = (time_start + datetime.timedelta(days=days)).strftime('%Y-%m-%d %H:%M:%S')
    return time_end

def sub_days(time_start: str, days: int) -> str:
    '''
        返回 time_start 时间减去 days 天 的时间
        time_start: 起始时间，格式如 2021-07-26 19:52:06
        days: 减去的天数，类型为 int
    '''
    time_start = datetime.datetime.strptime(time_start, '%Y-%m-%d %H:%M:%S')
    time_end = (time_start + datetime.timedelta(days=-days)).strftime('%Y-%m-%d %H:%M:%S')
    return time_end

def add_years(time_start: str, years: int) -> str:
    '''
        返回 time_start 时间加上 years 年 的时间
        time_start: 起始时间，格式如 2021-07-26 19:52:06
        years: 增加的年数，类型为 int
    '''
    time_start = datetime.datetime.strptime(time_start, '%Y-%m-%d %H:%M:%S')
    time_end = (time_start + relativedelta(years=years)).strftime('%Y-%m-%d %H:%M:%S')
    return time_end

def sub_years(time_start: str, years: int) -> str:
    '''
        返回 time_start 时间减去 years 年 的时间
        time_start: 起始时间，格式如 2021-07-26 19:52:06
        years: 减去的年数，类型为 int
    '''
    time_start = datetime.datetime.strptime(time_start, '%Y-%m-%d %H:%M:%S')
    time_end = (time_start + relativedelta(years=-years)).strftime('%Y-%m-%d %H:%M:%S')
    return time_end

def to_weekday(time_day: str) -> int:
    '''
        返回 time_day 是星期几(0 到 6 分别代表 星期日 到 星期六)
        time_day: 时间，格式如 2021-07-26 19:52:06
    '''
    time_day = datetime.datetime.strptime(time_day, '%Y-%m-%d %H:%M:%S')
    return time_day.weekday()

def to_constellation(time_day: str) -> str:
    '''
        返回 time_day 是哪个星座(星座使用中文名)
        time_day: 时间，格式如 2021-07-26 19:52:06
    '''
    md = time_day.split('-', 1)[1] #提取 月 和 日
    if md >= '12-22' or md <= '01-19':
        return '摩羯座'
    elif '01-20' <= md <= '02-18':
        return '水瓶座'
    elif '02-19' <= md <= '03-20':
        return '双鱼座'
    elif '03-21' <= md <= '04-19':
        return '白羊座'
    elif '04-20' <= md <= '05-20':
        return '金牛座'
    elif '05-21' <= md <= '06-21':
        return '双子座'
    elif '06-22' <= md <= '07-22':
        return '巨蟹座'
    elif '07-23' <= md <= '08-22':
        return '狮子座'
    elif '08-23' <= md <= '09-22':
        return '处女座'
    elif '09-23' <= md <= '10-23':
        return '天秤座'
    elif '10-23' <= md <= '11-22':
        return '天蝎座'
    elif '11-23' <= md <= '12-21':
        return '射手座'

def how_many_weeks(time_day: str) -> int:
    '''
        返回 time_day 是该年的第几周
        time_day: 时间，格式如 2021-07-26 19:52:06
    '''    
    time_day = datetime.datetime.strptime(time_day, '%Y-%m-%d %H:%M:%S')
    return time_day.isocalendar()[1]


def get_current_time() -> str:
    '''
        获取当前时间
        格式如: 2021-07-26 19:52:06
    '''
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def last_year() -> str:
    '''
        获取当前时间一年前的时间点
    '''
    return (datetime.datetime.now() + relativedelta(years=-1)).strftime('%Y-%m-%d %H:%M:%S')

def last_half_year() -> str:
    '''
        获取当前时间半年前的时间点
    '''
    return (datetime.datetime.now() + datetime.timedelta(days=-183)).strftime('%Y-%m-%d %H:%M:%S')
    
def last_month() -> str:
    '''
        获取当前时间一月前的时间点
    '''
    return (datetime.datetime.now() + datetime.timedelta(days=-30)).strftime('%Y-%m-%d %H:%M:%S')


def get_current_timestamp() -> int:
    '''
        获取秒级时间戳
    '''
    return int(time.time())

def int_to_str(t: int) -> str:
    '''
        时间戳 转 时间字符串
    '''
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

def str_to_int(t: str) -> int:
    '''
        时间字符串 转 时间戳\n
        时间字符串格式如 2021-07-26 19:52:06
    '''
    return int(time.mktime(time.strptime(t, "%Y-%m-%d %H:%M:%S")))
