def time_format(timestamp: int, format='std') -> str:
    '''
    格式化输出剩余时间信息。

    参数：
    - `timestamp: int`：时间戳。

    关键字参数：
    - `format: str`：格式名称，可用的格式名称有：
        * `std`：标准格式，以冒号分隔日、时、分、秒，例如 `05:04:03:02`；
        * `zh`：中文格式，例如 `5天4小时3分2秒`。
      默认值为 `std`。

    返回：
    - `str`：格式化的时间信息
    '''
    days = abs(timestamp) // 86400
    hours = (abs(timestamp) - days * 86400) // 3600
    minutes = (abs(timestamp) - days * 86400 - hours * 3600) // 60
    seconds = abs(timestamp) - days * 86400 - hours * 3600 - minutes * 60

    if format == 'std':
        return (f'{str(days).zfill(2)}:{str(hours).zfill(2)}:'
                f'{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
    elif format == 'zh':
        result = []
        if days:
            result.append(f'{days}天')
        if hours:
            result.append(f'{hours}小时')
        if minutes:
            result.append(f'{minutes}分')
        if seconds or (not days and not hours and not minutes):
            result.append(f'{seconds}秒')

        return ''.join(result)