import cPickle as pickle

def find_classes_at_timings(current_sem, current_weekday,current_time):
    course_db = pickle.load(open("courses_database.pkl","r"))
    filtered_course = []

    for course in course_db:
        if len(course[4])==2 or current_sem == course[4]:
            timings = course[8][0]
            # print timings
            i = 0
            flag = 'F'
            for times in timings:
                i = i+1
                if len(times)>0:
                    try:
                        index_t = times.index(current_weekday)
                        if index_t!=-1:
                            flag = 'T'
                            break
                    except:
                        continue
            if flag=='T':
                class_time = course[8][1]
                mer_time = course[8][2]
                l_class_time = len(class_time)
                for j in range(0,l_class_time):
                    if len(class_time[j])==4:
                        if mer_time[j][0]=="PM":
                            start_t = (((int(class_time[j][0])%12)+12)*100)+ int(class_time[j][1])
                        else:
                            start_t = (int(class_time[j][0])*100) + int(class_time[j][1])
                        if mer_time[j][1]=="PM":
                            end_t = (((int(class_time[j][2])%12)+12)*100)+ int(class_time[j][3])
                        else:
                            end_t = (int(class_time[j][2])  *100) + int(class_time[j][3])
                        if (current_time)>start_t and current_time<end_t:
                            filtered_course.append(course)

    return filtered_course

# print find_classes_at_timings(curr_sem, curr_weekday,curr_time)
