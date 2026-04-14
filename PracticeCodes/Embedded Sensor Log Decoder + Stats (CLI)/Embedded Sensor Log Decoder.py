def print_report(stats):
    print("-- SENSOR REPORT --")
    print(f"Total Packets: {stats['packet_counter']}")
    print(f"Valid Packets: {stats['valid_counter']}")
    print(f"Invalid Packets: {stats['invalid_counter']}")
    print()
    print("Status Counts: ")
    print(f"OK: {stats['status_counts']['OK']}")
    print(f"LOW_BATT: {stats['status_counts']['LOW_BATT']}")
    print(f"OVERHEAT: {stats['status_counts']['OVERHEAT']}")
    print(f"SENSOR_FAIL: {stats['status_counts']['SENSOR_FAIL']}")
    print()
    print("Per-Device Data: ")
    for key in stats["devices"]:
        temp_sum = stats["devices"][key]["temp_sum"]
        count = stats["devices"][key]["count"]
        min_volt = stats["devices"][key]["min_volt"]

        avg_temp = temp_sum / count

        print(f"{key} -> "
              f"count={count} "
              f"avg_temp={avg_temp:.2f} "
              f"min_volt={min_volt:.2f}"
        )

def update_stats(packet, stats_dict):

    # Check status and update stats
    if packet["STATUS"] == "OK":
        stats_dict["status_counts"]["OK"] += 1
    elif packet["STATUS"] == "LOW_BATT":
        stats_dict["status_counts"]["LOW_BATT"] += 1
    elif packet["STATUS"] == "OVERHEAT":
        stats_dict["status_counts"]["OVERHEAT"] += 1
    else:
        stats_dict["status_counts"]["SENSOR_FAIL"] += 1

    # Per-device data-check
    # packet not found, add stats
    if packet["ID"] not in stats_dict["devices"]:
        stats_dict["devices"][packet["ID"]] = {
            "count": 1,
            "temp_sum": packet["TEMP_C"],
            "min_volt": packet["VOLT_V"]
        }
    else:
        # packet is found, update stats
        stats_dict["devices"][packet["ID"]]["count"] += 1
        stats_dict["devices"][packet["ID"]]["temp_sum"] += packet["TEMP_C"]

        # compare for lowest volt seen
        lowest_volt = packet["VOLT_V"]
        if lowest_volt < stats_dict["devices"][packet["ID"]]["min_volt"]:
            stats_dict["devices"][packet["ID"]]["min_volt"] = lowest_volt

def parse_packet(line):

    # split line data's by comma separator
    line_parts = line.split(",")

    # validate if line is valid with four parts
    if len(line_parts) != 4:
        return None

    # parse each parts into data
    packets_id = line_parts[0]
    temp_c = float(line_parts[1])
    volt_v = float(line_parts[2])
    status = line_parts[3]

    # create dictionary containing key-values of data and inputs
    packet = {
        "ID": packets_id,
        "TEMP_C": temp_c,
        "VOLT_V": volt_v,
        "STATUS": status
    }

    return packet

def get_packets():

    # declare empty list variable for storing user input lines
    packets = []

    # get user input(s) until done
    user_input = input("Packet> ")
    while user_input != "DONE":
        packets.append(user_input)
        user_input = input("Packet> ")

    return packets

def main():

    # Dictionary for updating stats
    stats = {
        "packet_counter": 0,
        "valid_counter": 0,
        "invalid_counter": 0,
        "status_counts": {
            "OK": 0,
            "LOW_BATT": 0,
            "OVERHEAT": 0,
            "SENSOR_FAIL": 0
        },
        # this is where to append valid packets with additional independent devices data
        "devices": { }
    }

    # call get_packets to retrieve raw input data lines from user
    packets = get_packets()

    # loop through "packet list" and parse each line inputted
    for line in packets:
        # increment total packet counter
        stats["packet_counter"] += 1

        # call parse_packet function and get dictionary line back
        parsed_packet = parse_packet(line)

        # validate if parsed_packet is None, update invalid count here
        if parsed_packet is None:
            stats["invalid_counter"] += 1
        else:
            stats["valid_counter"] += 1
            update_stats(parsed_packet, stats)

    # Print
    print_report(stats)

if __name__ == "__main__":
    main()