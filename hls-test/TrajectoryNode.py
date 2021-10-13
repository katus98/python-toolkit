class TrajectoryNode:
    def __init__(self, l_line):
        items = l_line.split(',')
        self.trajectory_id = int(items[0])
        self.timestamp = int(items[1])
        self.x = float(items[2])
        self.y = float(items[3])
        self.index_t = int(items[4])
        self.index_x = int(items[5])
        self.index_y = int(items[6])
        self.scaled_t = float(items[7])
        self.scaled_x = float(items[8])
        self.scaled_y = float(items[9])
        self.scaled_index_t = float(items[10])
        self.scaled_index_x = float(items[11])
        self.scaled_index_y = float(items[12])

    def __cmp__(self, other):
        if self.x < other.x:
            return -1
        elif self.x > other.x:
            return 1
        else:
            if self.timestamp < other.timestamp:
                return -1
            elif self.timestamp > other.timestamp:
                return 1
            else:
                return 0

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{},{},{},{},{}" \
            .format(self.trajectory_id, self.timestamp, self.x, self.y,
                    self.index_t, self.index_x, self.index_y,
                    self.scaled_t, self.scaled_x, self.scaled_y,
                    self.scaled_index_t, self.scaled_index_x, self.scaled_index_y)
