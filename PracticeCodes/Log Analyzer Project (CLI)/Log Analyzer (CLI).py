# Mini project: Log Analyzer (CLI)
def print_report(invalid, valid, info, warning, error, comp):
    print("--- LOG REPORT ---")
    print(f"{'Valid lines:':<16}{valid:<5}")
    print(f"{'Invalid lines:':<16}{invalid:<5}")
    print(f"{'INFO:':<16}{info:<5}")
    print(f"{'WARNING:':<16}{warning:<5}")
    print(f"{'ERROR:':<16}{error:<5}")
    print(f"{'Common comp:':<16}{comp:<5}")

#-----------------------------------------------
def most_common_comp(log_list, name_comp, name_comp_counter):

    for index in range(len(log_list)):
        line_read = log_list[index].split("|")
        if len(line_read) != 3:
            continue
        else:
            curr_comp = line_read[1].strip()
            if curr_comp not in name_comp:
                name_comp.append(curr_comp)
                name_comp_counter.append(1)
            else:
                find_comp = name_comp.index(curr_comp)
                name_comp_counter[find_comp] = name_comp_counter[find_comp] + 1

    most_counted = 0
    for i in range(1, len(name_comp_counter)):
        if name_comp_counter[i] > name_comp_counter[most_counted]:
            most_counted = i

    return name_comp[most_counted]
#-----------------------------------------------
def parse_log_build_reports(curr_element):

    invalid = 0
    valid = 0
    INFO = 0
    WARNING = 0
    ERROR = 0

    # Check length of curr_element if < 3
    if len(curr_element) != 3:
        invalid += 1
    else:
        valid += 1
        level = curr_element[0].strip().upper()

        if level == "INFO":
            INFO += 1
        elif level == "WARNING":
            WARNING += 1
        elif level == "ERROR":
            ERROR += 1

    return invalid, valid, INFO, WARNING, ERROR

#-----------------------------------------------
def get_logs(log_list):
    print("Enter log lines in this format:")
    print("LEVEL | component | notes")
    print("Type DONE to finish")
    log = input("Log> ")

    # Retrieve log until user inputs DONE
    while log.upper() != "DONE":
        log_list.append(log)
        log = input("Log> ")

    return log_list
#-----------------------------------------------
# --- MAIN ---
log_data = []   # List to contain user logs
components = [] # List to contain components
comp_counts = [] # Component common counter

invalid = 0
valid = 0
INFO = 0
WARNING = 0
ERROR = 0
common_comp = ""

# Get user logs
get_logs(log_data)

# Get each line of log_data and split
for line in range(len(log_data)):
    curr_line = log_data[line].split("|")
    inv, val, info, warning, error = parse_log_build_reports(curr_line)

    invalid += inv
    valid += val
    INFO += info
    WARNING += warning
    ERROR += error

found_comp = most_common_comp(log_data, components, comp_counts)

print_report(invalid, valid, INFO, WARNING, ERROR, found_comp)


