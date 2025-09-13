def analyze_user_activity(log_file_path: str) -> dict:
    dict_ac = {}
    dict_activity = {}
    
    count_row = 0
    store = []
    temporary = []
    
    time_total = []
    username = []
    
    with open(log_file_path,"r") as file:
        log_line = file.readlines()
        
        for i in range(len(log_line)):
            log_split = str(log_line[i]).split()
            store.append(log_split)
        
        # แก้ไข: เปลี่ยนเงื่อนไขจาก len(log_split) <= 4 เป็น len(store[i]) >= 4
        for i in range(len(log_line)):
            count_row += 1
            dict_ac = {}
            if len(store[i]) >= 4:  # เปลี่ยนเงื่อนไข: ต้องมีอย่างน้อย 4 elements
                dict_ac["Record"] = i+1
                dict_ac["Date"] = store[i][0]
                dict_ac["User"] = store[i][1]
                dict_ac["Activity"] = store[i][2]
                dict_ac["Time"] = store[i][3]
                temporary.append(dict_ac)
    
    # แก้ไข: ใช้ len(temporary) แทน len(log_line) เพราะบางบรรทัดอาจถูก skip
    # หา ผู้ใช้ซ้ำ
    for i in range(len(temporary)):
        if temporary[i]["User"] not in username:
            username.append(temporary[i]["User"])
    
    # จำนวนuser
    count_user = len(username)
    
    # นับจำนวน Activity ที่ซ้ำ
    for i in range(len(temporary)):
        if temporary[i]["Activity"] not in dict_activity:
            dict_activity[temporary[i]["Activity"]] = 1
        else:
            dict_activity[temporary[i]["Activity"]] += 1
                
    # หาเวลาแต่ละ user ,เปรียบเทียบเวลา ,รวมเวลาของทุกคน
    dict_user_time = {}
    for i in range(len(temporary)):
        if temporary[i]["User"] not in dict_user_time:
            time_total.append(temporary[i]["Time"])
            dict_user_time[temporary[i]["User"]] = int(temporary[i]["Time"]) 
        else:
            dict_user_time[temporary[i]["User"]] += int(temporary[i]["Time"]) 
    
    # แก้ไข: ตรวจสอบว่า dict_user_time ไม่ว่างก่อนเรียก max()
    if dict_user_time:
        user_max_session = max(dict_user_time, key=dict_user_time.get)  # แก้ไข: ใช้ key parameter
    else:
        user_max_session = None
    
    # หาค่าเฉลี่ย login
    if len(username) > 0:  # แก้ไข: ตรวจสอบหารศูนย์
        time_sum = 0
        for i in time_total:
            time_sum += int(i)
        average_time = time_sum / len(username)
    else:
        average_time = 0.0
        
    # แก้ไข: เปลี่ยนชื่อ key ให้ตรงกับที่ test ต้องการ
    return {
        "total_users": count_user,           # เปลี่ยนจาก total_user เป็น total_users
        "action_counts": dict_activity,      # เปลี่ยนจาก action_count เป็น action_counts
        "most_active_user": user_max_session,
        "average_session_time": average_time
    }

if __name__ == "__main__":
    result = analyze_user_activity("activity.log")
    from pprint import pprint
    pprint(result)