#!/usr/bin/env python3

import sys
import re
import csv

#modify these values for your own purpose or use sys.argv[1] and sys.argv[2]
logfile = "syslog.log"
program_name = "ticky"




def count_error_types(logfile, program_name):
    error_types = {}

    with open(logfile, "r") as f:
        file = f.readlines()
        for line in file:
            error = re.search(r': ERROR', line)
            info = re.search(r': INFO', line)
            if program_name not in line:
                continue
            if "INFO" in line:
                continue
            if error is not None:
                error = re.search(r'ERROR ([\w ]*)', line)[1].strip()
                if error not in error_types:
                    error_types[error] = 1
                else:
                    error_types[error] += 1

    f.close()
    print(error_types)
    return error_types

def sort_errors(error_dic):
    return sorted(error_dic.items(), key=lambda x: x[1], reverse=True)

def sort_by_user(user_dic):
    return sorted(user_dic.items())

def user_stats(logfile, program_name):
    user_info = {}
    with open(logfile, "r") as f:
        for line in f:
            if program_name not in line:
                continue
            username = re.search(r'\(([\w. ]*)\)', line)[1]
            error = re.search(r': ERROR', line)
            info = re.search(r': INFO', line)

            # username = re.search(r'[\w]* ([\w+.]*) (\[[#][\d]*\])? \(([\w]*)\)', line, re.IGNORECASE)[3]
            if username not in user_info:
                user_info[username] = {}
                user_info[username]["error"] = 0
                user_info[username]["info"] = 0
            if error is None:
                user_info[username]["info"] += 1
            else:
                user_info[username]["error"] += 1
            # if "error" in line.lower():
            #     user_info[username]["error"] += 1
            # if "info" in line.lower():
            #     user_info[username]["info"] += 1
    f.close()
    print(user_info)
    return user_info

def type_of_errors_csv_generator(sorted_dict_of_errors):
    fields = ['Error', 'Count']
    filename = "error_message.csv"
    with open(filename, "w") as f:
        csvwriter = csv.writer(f)

        csvwriter.writerow(fields)

        csvwriter.writerows(sorted_dict_of_errors)
    f.close()
    return None

def user_stats_csv_generator(sorted_dict_of_user_stats):
    fields = ['Username', 'ERROR', 'INFO']
    filename = "user_statistics.csv"
    with open(filename, "w") as f:
        csvwriter = csv.writer(f)

        csvwriter.writerow(fields)
        for user in sorted_dict_of_user_stats:
            username = user[0]
            error = user[1]["error"]
            info = user[1]["info"]
            csvwriter.writerow([username, error, info])
    f.close()
    return None

if __name__ == "__main__":
    errors = count_error_types(logfile, program_name)
    errors = sort_errors(errors)
    per_user = user_stats(logfile, program_name)
    per_user = sort_by_user(per_user)
    type_of_errors_csv_generator(errors)
    user_stats_csv_generator(per_user)
