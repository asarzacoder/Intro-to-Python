# Mini project: Log Analyzer (CLI)

def print_report(valid_count, invalid_count, info_count, warn_count, error_count, top_component):
    print("----- LOG REPORT -----")
    print("Valid lines:", valid_count)
    print("Invalid lines:", invalid_count)
    print("INFO:", info_count)
    print("WARN:", warn_count)
    print("ERROR:", error_count)

    if top_component == "":
        print("Most common component: None")
    else:
        print("Most common component:", top_component)

    print("----------------------")

def most_common_component(components, component_counts):
    if len(components) == 0:
        return ""

    max_index = 0
    for i in range(1, len(component_counts)):
        if component_counts[i] > component_counts[max_index]:
            max_index = i
    return components[max_index]

def update_component_counts(component, components, component_counts):
    found = False
    for i in range(len(components)):
        if components[i] == component:
            component_counts[i] += 1
            found = True
    if not found:
        components.append(component)
        component_counts.append(1)

def build_report(logs):
    valid_count = 0
    invalid_count = 0
    info_count = 0
    warn_count = 0
    error_count = 0

    components = []
    component_counts = []

    for input_line in logs:
        level, component, message = parse_log(input_line)

        if level == "INVALID":
            invalid_count += 1
        else:
            valid_count += 1

            if level == "INFO":
                info_count += 1
            elif level == "WARN":
                warn_count += 1
            elif level == "ERROR":
                error_count += 1

            update_component_counts(component, components, component_counts)

    top_component = most_common_component(components, component_counts)

    return valid_count, invalid_count, info_count, warn_count, error_count, top_component

def parse_log(lines):
    parts = lines.split("|")

    # Checks length of single line input
    if len(parts) != 3:
        return "INVALID", "", ""

    # Grab each parts of line and insert into variables
    level = parts[0].strip()
    component = parts[1].strip()
    message = parts[2].strip()

    # invalid if any part is empty
    if level == "" or component == "" or message == "":
        return "INVALID", "", ""

    # CAPITALIZED LEVEL
    level = level.upper()

    return level, component, message

def get_logs():
    log_lines = []

    print("Enter log lines in this format:")
    print("LEVEL | component | message")
    print("Type DONE to finish")
    print("-" * 40)
    user_input = input("Log> ")

    while user_input.upper() != "DONE":
        log_lines.append(user_input)
        user_input = input("Log> ")

    return log_lines

# main

logs = get_logs()  # returns list of user line input
valid_count, invalid_count, info_count, warn_count, error_count, top_component = build_report(logs)
print_report(valid_count, invalid_count, info_count, warn_count, error_count, top_component)





