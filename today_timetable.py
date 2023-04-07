import datetime

def today_timetable():
    # 建立課表資料庫，格式為 {星期幾: [課程1, 課程2, ...]}
    timetable = {
        0: ['公民', '英語', '數位科技進階','彈性學習時間','中國小說選讀','數學應用','商業溝通'],
        1: ['運算思維', '運算思維', '體育','會計實務','取為英文閱讀','經濟學進階','生涯規劃'],
        2: ['數位科技進階', '數位科技進階','商業經營管理', '趣味英文選讀','團體活動時間','團體活動時間','數學應用'],
        3: ['會計實務', '英語文', '體育','商業經營管理','經濟學進階','國語文','彈性學習時間'],
        4: ['資料庫應用', '資料庫應用', '會計實務','經濟學進階','國語文','數學應用','數位科技進階']}
        # 其他星期幾的課表資料
    
    # 取得現在時間
    now = datetime.datetime.now()

    # 調整時間增加8小時1.5分鐘
    adtime=datetime.timedelta(hours=8,minutes=1.5)
    now=now-adtime

    # 取得今天星期幾，0 為星期一，6 為星期日
    weekday = now.weekday()

    # 將現在時間格式改為 'HH:MM'
    current_time = now.strftime('%H:%M')

    next_class = None
    # 查詢接下來的課程
    if weekday in timetable:
        # 取得今天的課表
        today_timetable = timetable[weekday]
    return '\n'.join(today_timetable)