error_types = {}

with open(logfile, "r") as f:
    for line in f:
        print(line)
        if program_name not in line:
            continue
        print(re.search(r'ERROR', line, re.IGNORECASE))
        error = re.search(r'ERROR (\w+.*) \(([\w]*)\)', line, re.IGNORECASE)[1]
        if error not in error_types:
            error_types[error] = 1
        else:
            error_types[error] += 1
f.close()
print(error_types)
return error_types
