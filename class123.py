import datetime

def class123():
    # 建立課表資料庫，格式為 {星期幾: [課程1, 課程2, ...]}
    timetable = {
        0: ['公民', '英語', '數位科技進階','彈性學習時間','中國小說選讀','數學應用','商業溝通'],
        1: ['運算思維', '運算思維', '體育','會計實務','取為英文閱讀','經濟學進階','生涯規劃'],
        2: ['數位科技進階', '數位科技進階','商業經營管理', '趣味英文選讀','團體活動時間','團體活動時間','數學應用'],
        3: ['會計實務', '英語文', '體育','商業經營管理','經濟學進階','國語文','彈性學習時間'],
        4: ['資料庫應用', '資料庫應用', '會計實務','經濟學進階','國語文','數學應用','數位科技進階']}
        # 其他星期幾的課表資料
    

    # 定義函式 get_class_time，用來取得指定課程的上課時間
    def get_class_time(index, timetable):
        # 定義課程時間，格式為 'HH:MM-HH:MM'
        class_times = [
            '08:00-08:50',
            '09:00-09:50',
            '10:00-10:50',
            '11:00-11:50',
            '13:00-13:50',
            '14:00-14:50',
            '15:00-15:50',
            '16:00-16:50']
        return class_times[index]

    # 取得現在時間
    now = datetime.datetime.now()

    # 取得今天星期幾，0 為星期一，6 為星期日
    weekday = now.weekday()

    # 取得現在時間，格式為 'HH:MM'
    current_time = now.strftime('%H:%M')

    next_class = None

    # 查詢接下來的課程
    if weekday in timetable:
        # 取得今天的課表
        today_timetable = timetable[weekday]
        
        for i in range(len(today_timetable)):
            # 取得課程時間，格式為 'HH:MM-HH:MM'
            class_time = get_class_time(i, today_timetable)
            
            # 判斷現在時間是否在課程時間之前
            if current_time < class_time.split('-')[0]:
                next_class = today_timetable[i]
                break

    if next_class:
        return '下一節課是：%s'%next_class
    else:
        return '今天已經沒有課了...'
