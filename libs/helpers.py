from datetime import timedelta


def get_file_lines(self, file_name, lines_to_read):
    found_lines = []
    with open(file_name, "r") as file:
        for position, line in enumerate(file):
            if position in lines_to_read:
                found_lines.append(line.replace("\"", "").rstrip("\n"))
    return found_lines


def str_time_prop(self, start, end, prop):
    """
        Get a time at a proportion of a range of two formatted times.

        start and end should be strings specifying times formated in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
    """
    delta = end - start
    ptime = start + timedelta(seconds=prop * delta.total_seconds())

    return ptime