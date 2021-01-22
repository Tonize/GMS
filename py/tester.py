#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 20:50:17 2020

@author: root
"""

import pandas as pd
import numpy as np
import json 
import ast



labor_need = '''[{'day_of_week': 'Monday', 'labor_need': 2, 'hour': 8}, {'day_of_week': 'Monday', 'labor_need': 2, 'hour': 9}, {'day_of_week': 'Monday', 'labor_need': 3, 'hour': 10}, {'day_of_week': 'Monday', 'labor_need': 3, 'hour': 11}, {'day_of_week': 'Monday', 'labor_need': 3, 'hour': 12}, {'day_of_week': 'Monday', 'labor_need': 3, 'hour': 13}, {'day_of_week': 'Monday', 'labor_need': 4, 'hour': 14}, {'day_of_week': 'Monday', 'labor_need': 4, 'hour': 15}, {'day_of_week': 'Monday', 'labor_need': 2, 'hour': 16}, {'day_of_week': 'Monday', 'labor_need': 2, 'hour': 17}, {'day_of_week': 'Monday', 'labor_need': 1, 'hour': 18}, {'day_of_week': 'Monday', 'labor_need': 1, 'hour': 19}, {'day_of_week': 'Monday', 'labor_need': 1, 'hour': 20}, {'day_of_week': 'Tuesday', 'labor_need': 2, 'hour': 8}, {'day_of_week': 'Tuesday', 'labor_need': 2, 'hour': 9}, {'day_of_week': 'Tuesday', 'labor_need': 3, 'hour': 10}, {'day_of_week': 'Tuesday', 'labor_need': 3, 'hour': 11}, {'day_of_week': 'Tuesday', 'labor_need': 3, 'hour': 12}, {'day_of_week': 'Tuesday', 'labor_need': 3, 'hour': 13}, {'day_of_week': 'Tuesday', 'labor_need': 4, 'hour': 14}, {'day_of_week': 'Tuesday', 'labor_need': 4, 'hour': 15}, {'day_of_week': 'Tuesday', 'labor_need': 2, 'hour': 16}, {'day_of_week': 'Tuesday', 'labor_need': 2, 'hour': 17}, {'day_of_week': 'Tuesday', 'labor_need': 1, 'hour': 18}, {'day_of_week': 'Tuesday', 'labor_need': 1, 'hour': 19}, {'day_of_week': 'Tuesday', 'labor_need': 1, 'hour': 20}, {'day_of_week': 'Wednesday', 'labor_need': 2, 'hour': 8}, {'day_of_week': 'Wednesday', 'labor_need': 2, 'hour': 9}, {'day_of_week': 'Wednesday', 'labor_need': 3, 'hour': 10}, {'day_of_week': 'Wednesday', 'labor_need': 3, 'hour': 11}, {'day_of_week': 'Wednesday', 'labor_need': 3, 'hour': 12}, {'day_of_week': 'Wednesday', 'labor_need': 3, 'hour': 13}, {'day_of_week': 'Wednesday', 'labor_need': 4, 'hour': 14}, {'day_of_week': 'Wednesday', 'labor_need': 4, 'hour': 15}, {'day_of_week': 'Wednesday', 'labor_need': 2, 'hour': 16}, {'day_of_week': 'Wednesday', 'labor_need': 2, 'hour': 17}, {'day_of_week': 'Wednesday', 'labor_need': 1, 'hour': 18}, {'day_of_week': 'Wednesday', 'labor_need': 1, 'hour': 19}, {'day_of_week': 'Wednesday', 'labor_need': 1, 'hour': 20}, {'day_of_week': 'Thursday', 'labor_need': 2, 'hour': 8}, {'day_of_week': 'Thursday', 'labor_need': 2, 'hour': 9}, {'day_of_week': 'Thursday', 'labor_need': 3, 'hour': 10}, {'day_of_week': 'Thursday', 'labor_need': 3, 'hour': 11}, {'day_of_week': 'Thursday', 'labor_need': 3, 'hour': 12}, {'day_of_week': 'Thursday', 'labor_need': 3, 'hour': 13}, {'day_of_week': 'Thursday', 'labor_need': 4, 'hour': 14}, {'day_of_week': 'Thursday', 'labor_need': 4, 'hour': 15}, {'day_of_week': 'Thursday', 'labor_need': 2, 'hour': 16}, {'day_of_week': 'Thursday', 'labor_need': 2, 'hour': 17}, {'day_of_week': 'Thursday', 'labor_need': 1, 'hour': 18}, {'day_of_week': 'Thursday', 'labor_need': 1, 'hour': 19}, {'day_of_week': 'Thursday', 'labor_need': 1, 'hour': 20}, {'day_of_week': 'Friday', 'labor_need': 2, 'hour': 8}, {'day_of_week': 'Friday', 'labor_need': 2, 'hour': 9}, {'day_of_week': 'Friday', 'labor_need': 3, 'hour': 10}, {'day_of_week': 'Friday', 'labor_need': 3, 'hour': 11}, {'day_of_week': 'Friday', 'labor_need': 3, 'hour': 12}, {'day_of_week': 'Friday', 'labor_need': 3, 'hour': 13}, {'day_of_week': 'Friday', 'labor_need': 4, 'hour': 14}, {'day_of_week': 'Friday', 'labor_need': 4, 'hour': 15}, {'day_of_week': 'Friday', 'labor_need': 2, 'hour': 16}, {'day_of_week': 'Friday', 'labor_need': 2, 'hour': 17}, {'day_of_week': 'Friday', 'labor_need': 1, 'hour': 18}, {'day_of_week': 'Friday', 'labor_need': 1, 'hour': 19}, {'day_of_week': 'Friday', 'labor_need': 1, 'hour': 20}, {'day_of_week': 'Saturday', 'labor_need': 2, 'hour': 8}, {'day_of_week': 'Saturday', 'labor_need': 2, 'hour': 9}, {'day_of_week': 'Saturday', 'labor_need': 3, 'hour': 10}, {'day_of_week': 'Saturday', 'labor_need': 3, 'hour': 11}, {'day_of_week': 'Saturday', 'labor_need': 3, 'hour': 12}, {'day_of_week': 'Saturday', 'labor_need': 3, 'hour': 13}, {'day_of_week': 'Saturday', 'labor_need': 4, 'hour': 14}, {'day_of_week': 'Saturday', 'labor_need': 4, 'hour': 15}, {'day_of_week': 'Saturday', 'labor_need': 2, 'hour': 16}, {'day_of_week': 'Saturday', 'labor_need': 2, 'hour': 17}, {'day_of_week': 'Saturday', 'labor_need': 1, 'hour': 18}, {'day_of_week': 'Saturday', 'labor_need': 1, 'hour': 19}, {'day_of_week': 'Saturday', 'labor_need': 1, 'hour': 20}, {'day_of_week': 'Sunday', 'labor_need': 2, 'hour': 8}, {'day_of_week': 'Sunday', 'labor_need': 2, 'hour': 9}, {'day_of_week': 'Sunday', 'labor_need': 3, 'hour': 10}, {'day_of_week': 'Sunday', 'labor_need': 3, 'hour': 11}, {'day_of_week': 'Sunday', 'labor_need': 3, 'hour': 12}, {'day_of_week': 'Sunday', 'labor_need': 3, 'hour': 13}, {'day_of_week': 'Sunday', 'labor_need': 4, 'hour': 14}, {'day_of_week': 'Sunday', 'labor_need': 4, 'hour': 15}, {'day_of_week': 'Sunday', 'labor_need': 2, 'hour': 16}, {'day_of_week': 'Sunday', 'labor_need': 2, 'hour': 17}, {'day_of_week': 'Sunday', 'labor_need': 1, 'hour': 18}, {'day_of_week': 'Sunday', 'labor_need': 1, 'hour': 19}, {'day_of_week': 'Sunday', 'labor_need': 1, 'hour': 20}]'''

labor_need = ast.literal_eval(labor_need)
labor_need = pd.DataFrame.from_records(labor_need)



test = [{"shift": 15, "workers": "c", "employee_name": "c", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 15, "index": 389, "start": "2020-05-04 08:00:00", "end": "2020-05-04 16:00:00", "day_of_week": "Monday", "start_hour": 8, "end_hour": 16, "req": 2.0, "duration": 8, "shift_cost": 96}, {"shift": 15, "workers": "d", "employee_name": "d", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 15, "index": 389, "start": "2020-05-04 08:00:00", "end": "2020-05-04 16:00:00", "day_of_week": "Monday", "start_hour": 8, "end_hour": 16, "req": 2.0, "duration": 8, "shift_cost": 96}, {"shift": 16, "workers": "c", "employee_name": "c", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 16, "index": 395, "start": "2020-05-04 10:00:00", "end": "2020-05-04 18:00:00", "day_of_week": "Monday", "start_hour": 10, "end_hour": 18, "req": 1.0, "duration": 8, "shift_cost": 96}, {"shift": 17, "workers": "b", "employee_name": "b", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 10, "min_hours": 32, "max_hours": 60, "pos_index": 17, "index": 406, "start": "2020-05-04 14:00:00", "end": "2020-05-04 21:00:00", "day_of_week": "Monday", "start_hour": 14, "end_hour": 21, "req": 1.0, "duration": 7, "shift_cost": 70}, {"shift": 18, "workers": "a", "employee_name": "a", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 10, "min_hours": 32, "max_hours": 60, "pos_index": 18, "index": 461, "start": "2020-05-05 08:00:00", "end": "2020-05-05 16:00:00", "day_of_week": "Tuesday", "start_hour": 8, "end_hour": 16, "req": 2.0, "duration": 8, "shift_cost": 80}, {"shift": 18, "workers": "d", "employee_name": "d", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 18, "index": 461, "start": "2020-05-05 08:00:00", "end": "2020-05-05 16:00:00", "day_of_week": "Tuesday", "start_hour": 8, "end_hour": 16, "req": 2.0, "duration": 8, "shift_cost": 96}, {"shift": 19, "workers": "b", "employee_name": "b", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 10, "min_hours": 32, "max_hours": 60, "pos_index": 19, "index": 467, "start": "2020-05-05 10:00:00", "end": "2020-05-05 18:00:00", "day_of_week": "Tuesday", "start_hour": 10, "end_hour": 18, "req": 1.0, "duration": 8, "shift_cost": 80}, {"shift": 20, "workers": "b", "employee_name": "b", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 10, "min_hours": 32, "max_hours": 60, "pos_index": 20, "index": 478, "start": "2020-05-05 14:00:00", "end": "2020-05-05 21:00:00", "day_of_week": "Tuesday", "start_hour": 14, "end_hour": 21, "req": 1.0, "duration": 7, "shift_cost": 70}, {"shift": 1, "workers": "c", "employee_name": "c", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 1, "index": 32, "start": "2020-04-29 10:00:00", "end": "2020-04-29 18:00:00", "day_of_week": "Wednesday", "start_hour": 10, "end_hour": 18, "req": 1.0, "duration": 8, "shift_cost": 96}, {"shift": 2, "workers": "b", "employee_name": "b", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 10, "min_hours": 32, "max_hours": 60, "pos_index": 2, "index": 43, "start": "2020-04-29 14:00:00", "end": "2020-04-29 21:00:00", "day_of_week": "Wednesday", "start_hour": 14, "end_hour": 21, "req": 1.0, "duration": 7, "shift_cost": 70}, {"shift": 4, "workers": "a", "employee_name": "a", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 10, "min_hours": 32, "max_hours": 60, "pos_index": 4, "index": 107, "start": "2020-04-30 10:00:00", "end": "2020-04-30 18:00:00", "day_of_week": "Thursday", "start_hour": 10, "end_hour": 18, "req": 1.0, "duration": 8, "shift_cost": 80}, {"shift": 5, "workers": "d", "employee_name": "d", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 5, "index": 118, "start": "2020-04-30 14:00:00", "end": "2020-04-30 21:00:00", "day_of_week": "Thursday", "start_hour": 14, "end_hour": 21, "req": 1.0, "duration": 7, "shift_cost": 84}, {"shift": 6, "workers": "a", "employee_name": "a", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 10, "min_hours": 32, "max_hours": 60, "pos_index": 6, "index": 173, "start": "2020-05-01 08:00:00", "end": "2020-05-01 16:00:00", "day_of_week": "Friday", "start_hour": 8, "end_hour": 16, "req": 2.0, "duration": 8, "shift_cost": 80}, {"shift": 6, "workers": "b", "employee_name": "b", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 10, "min_hours": 32, "max_hours": 60, "pos_index": 6, "index": 173, "start": "2020-05-01 08:00:00", "end": "2020-05-01 16:00:00", "day_of_week": "Friday", "start_hour": 8, "end_hour": 16, "req": 2.0, "duration": 8, "shift_cost": 80}, {"shift": 7, "workers": "c", "employee_name": "c", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 7, "index": 179, "start": "2020-05-01 10:00:00", "end": "2020-05-01 18:00:00", "day_of_week": "Friday", "start_hour": 10, "end_hour": 18, "req": 1.0, "duration": 8, "shift_cost": 96}, {"shift": 8, "workers": "c", "employee_name": "c", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 8, "index": 190, "start": "2020-05-01 14:00:00", "end": "2020-05-01 21:00:00", "day_of_week": "Friday", "start_hour": 14, "end_hour": 21, "req": 1.0, "duration": 7, "shift_cost": 84}, {"shift": 9, "workers": "b", "employee_name": "b", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 10, "min_hours": 32, "max_hours": 60, "pos_index": 9, "index": 245, "start": "2020-05-02 08:00:00", "end": "2020-05-02 16:00:00", "day_of_week": "Saturday", "start_hour": 8, "end_hour": 16, "req": 2.0, "duration": 8, "shift_cost": 80}, {"shift": 9, "workers": "c", "employee_name": "c", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 9, "index": 245, "start": "2020-05-02 08:00:00", "end": "2020-05-02 16:00:00", "day_of_week": "Saturday", "start_hour": 8, "end_hour": 16, "req": 2.0, "duration": 8, "shift_cost": 96}, {"shift": 10, "workers": "a", "employee_name": "a", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 10, "min_hours": 32, "max_hours": 60, "pos_index": 10, "index": 251, "start": "2020-05-02 10:00:00", "end": "2020-05-02 18:00:00", "day_of_week": "Saturday", "start_hour": 10, "end_hour": 18, "req": 1.0, "duration": 8, "shift_cost": 80}, {"shift": 11, "workers": "d", "employee_name": "d", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 11, "index": 262, "start": "2020-05-02 14:00:00", "end": "2020-05-02 21:00:00", "day_of_week": "Saturday", "start_hour": 14, "end_hour": 21, "req": 1.0, "duration": 7, "shift_cost": 84}, {"shift": 12, "workers": "b", "employee_name": "b", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 10, "min_hours": 32, "max_hours": 60, "pos_index": 12, "index": 317, "start": "2020-05-03 08:00:00", "end": "2020-05-03 16:00:00", "day_of_week": "Sunday", "start_hour": 8, "end_hour": 16, "req": 2.0, "duration": 8, "shift_cost": 80}, {"shift": 12, "workers": "d", "employee_name": "d", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 12, "index": 317, "start": "2020-05-03 08:00:00", "end": "2020-05-03 16:00:00", "day_of_week": "Sunday", "start_hour": 8, "end_hour": 16, "req": 2.0, "duration": 8, "shift_cost": 96}, {"shift": 13, "workers": "c", "employee_name": "c", "employee_email": "alexjlamb93@gmail.com", "hourly_rate": 12, "min_hours": 32, "max_hours": 60, "pos_index": 13, "index": 323, "start": "2020-05-03 10:00:00", "end": "2020-05-03 18:00:00", "day_of_week": "Sunday", "start_hour": 10, "end_hour": 18, "req": 1.0, "duration": 8, "shift_cost": 96}]

df1 = pd.DataFrame.from_records(test).sort_values('start')
df = df1.groupby(['shift', 'req', 'day_of_week', 'start_hour', 'end_hour'])['employee_name'].nunique().reset_index()
df['key'] = 1
index = pd.DataFrame(list(range(1,25)), columns = ['hour'])
index['key'] = 1
df = df.merge(index, how = 'left', on = 'key' )
df = df[(df['hour'] < df['end_hour']) & (df['hour'] >= df['start_hour'])]
df = df.drop(['key', 'start_hour', 'end_hour'], axis = 1)
df = df.merge(df1[['shift', 'start']], how = 'left', on = 'shift')
df['start'] = df['start'].apply(lambda x: x[0:10]) 
df['start'] = df['start'] + ' ' + df['hour'].astype(str) + ':00'
df = df.drop_duplicates()

df['sort'] = pd.to_datetime(df['start'])
df = df.sort_values('sort')
df = df.groupby(['day_of_week', 'hour', 'req', 'start', 'sort'])['employee_name'].sum().reset_index()
df.drop('sort', axis = 1, inplace = True)







