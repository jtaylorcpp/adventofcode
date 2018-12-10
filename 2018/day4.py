def part_1():
    import numpy

    def parse_record(rec):
        import re
        import datetime

        timestampre = re.compile(r'\[([0-9\- :]+)\]')
        guardidre = re.compile(r'(#\d+)')

        ts = timestampre.search(rec).groups()[0]
        parsed_rec = [datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M')]

        if "shift" in rec:
            parsed_rec.append(guardidre.search(rec).groups()[0])

        elif "up" in rec:
            parsed_rec.append("up")
        else: # "asleep"
            parsed_rec.append("asleep")

        return tuple(parsed_rec)

    records = []

    with open("./day4_input.txt", "r") as file:
        for line in file:
            records.append(parse_record(line))

    records = sorted(records, key=lambda tup: tup[0])

    # sleep dict
    sleep_schedule = {}
    current_id = ""
    sleep_ts = None
    for rec in records:
        if "#" in rec[1]:
            # new id
            if rec[1] not in sleep_schedule:
                sleep_schedule[rec[1]] = {}
            current_id = rec[1]

        elif "asleep" in rec[1]:
            # start sleep clock
            sleep_ts = rec[0]
            mon = rec[0].timetuple().tm_mon
            day = rec[0].timetuple().tm_mday
            yr = rec[0].timetuple().tm_year
            if (yr, mon, day) not in sleep_schedule[current_id]:
                sleep_schedule[current_id][(yr, mon, day)] = numpy.zeros(shape=(60))

        elif "up" in rec[1]:
            ts_mon = sleep_ts.timetuple().tm_mon
            rec_mon = rec[0].timetuple().tm_mon
            ts_day = sleep_ts.timetuple().tm_mday
            rec_day = rec[0].timetuple().tm_mday
            ts_yr = sleep_ts.timetuple().tm_year

            if rec[0] > sleep_ts and ts_mon == rec_mon and ts_day == rec_day:
                for ts in range(sleep_ts.timetuple().tm_min, rec[0].timetuple().tm_min):
                    #fill in sleep time
                    sleep_schedule[current_id][(ts_yr, ts_mon, ts_day)][ts] = 1

                #print(sleep_ts, rec[0])
                #print(sleep_ts.timetuple().tm_min, rec[0].timetuple().tm_min)
                #print(sleep_schedule[current_id])

            else:
                print("ts error!!!!!")
                exit()


    minutes_sum = {}
    for k,v in sleep_schedule.items():
        minutes_sum[k] = 0
        for _,day in v.items():
            minutes_sum[k] += sum(day)

    max_sum = ("",0)
    for k,v in minutes_sum.items():
        if v > max_sum[1]:
            max_sum = (k,v)

    max_sleep_id = max_sum[0]

    max_sleep_minute = {}

    for k,v in sleep_schedule[max_sleep_id].items():
        for ts in range(60):
            if ts not in max_sleep_minute:
                max_sleep_minute[ts] = 0
            max_sleep_minute[ts] += v[ts]

    #print(sleep_schedule[max_sleep_id])
    #print(max_sleep_minute)

    max_min = (0,0)
    for k,v in max_sleep_minute.items():
        if v > max_min[1]:
            max_min = (k,v)

    print(max_sum[0], max_min, int(max_sum[0][1:]) * int(max_min[0]))




def part_2():
    import numpy

    def parse_record(rec):
        import re
        import datetime

        timestampre = re.compile(r'\[([0-9\- :]+)\]')
        guardidre = re.compile(r'(#\d+)')

        ts = timestampre.search(rec).groups()[0]
        parsed_rec = [datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M')]

        if "shift" in rec:
            parsed_rec.append(guardidre.search(rec).groups()[0])

        elif "up" in rec:
            parsed_rec.append("up")
        else: # "asleep"
            parsed_rec.append("asleep")

        return tuple(parsed_rec)

    records = []

    with open("./day4_input.txt", "r") as file:
        for line in file:
            records.append(parse_record(line))

    records = sorted(records, key=lambda tup: tup[0])

    # sleep dict
    sleep_schedule = {}
    current_id = ""
    sleep_ts = None
    for rec in records:
        if "#" in rec[1]:
            # new id
            if rec[1] not in sleep_schedule:
                sleep_schedule[rec[1]] = {}
            current_id = rec[1]

        elif "asleep" in rec[1]:
            # start sleep clock
            sleep_ts = rec[0]
            mon = rec[0].timetuple().tm_mon
            day = rec[0].timetuple().tm_mday
            yr = rec[0].timetuple().tm_year
            if (yr, mon, day) not in sleep_schedule[current_id]:
                sleep_schedule[current_id][(yr, mon, day)] = numpy.zeros(shape=(60))

        elif "up" in rec[1]:
            ts_mon = sleep_ts.timetuple().tm_mon
            rec_mon = rec[0].timetuple().tm_mon
            ts_day = sleep_ts.timetuple().tm_mday
            rec_day = rec[0].timetuple().tm_mday
            ts_yr = sleep_ts.timetuple().tm_year

            if rec[0] > sleep_ts and ts_mon == rec_mon and ts_day == rec_day:
                for ts in range(sleep_ts.timetuple().tm_min, rec[0].timetuple().tm_min):
                    #fill in sleep time
                    sleep_schedule[current_id][(ts_yr, ts_mon, ts_day)][ts] = 1

                #print(sleep_ts, rec[0])
                #print(sleep_ts.timetuple().tm_min, rec[0].timetuple().tm_min)
                #print(sleep_schedule[current_id])

            else:
                print("ts error!!!!!")
                exit()


    sleep_minutes = {}
    for k,v in sleep_schedule.items():
        sleep_minutes[k] = numpy.zeros(shape=(60))
        for _, sleep_array in v.items():
            for ts in range(60):
                sleep_minutes[k][ts] += sleep_array[ts]

    #print(sleep_minutes)

    max_sleep_minutes = ("", 0, 0)
    for id, sleep_array in sleep_minutes.items():
        for ts in range(60):
            if sleep_array[ts] > max_sleep_minutes[2]:
                max_sleep_minutes = (id, ts, sleep_array[ts])
    print(max_sleep_minutes, int(max_sleep_minutes[0][1:]) * max_sleep_minutes[1])



part_1()
part_2()
