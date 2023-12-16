with open("inputs/day16.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

columns_len = len(lines[0])
rows_len = len(lines)


# define class for beam of lights
class Beam:
    def __init__(self, x, y, direction=(0, 1)):
        self.x = x
        self.y = y
        self.direction = direction
        self.is_moving = True
        self.locations = [(self.x, self.y)]

    def __repr__(self):
        return f"BEAM: ({self.x}, {self.y}) A:{self.is_moving}, D:{self.direction}"

    def __str__(self):
        return f"BEAM: ({self.x}, {self.y}) A:{self.is_moving}, D:{self.direction}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_coord(self):
        return (self.x, self.y)

    def get_is_moving(self):
        return self.is_moving

    def stop_moving(self):
        self.is_moving = False

    def get_direction(self):
        return self.direction

    def set_new_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.is_moving:
            self.x += self.direction[0]
            self.y += self.direction[1]
            self.locations.append((self.x, self.y))
            if self.x < 0 or self.x >= columns_len or self.y < 0 or self.y >= rows_len:
                self.is_moving = False

    def any_beams_moving(beams):
        for beam in beams:
            if beam.get_is_moving():
                return True
        return False

    def move_beams(beams):
        for beam in beams:
            beam.move()
        return beams

    def get_moving_beam_locations(beams):
        locations = []
        for beam in beams:
            if beam.get_is_moving():
                locations.append(beam.get_coord())
        return locations

    def get_locations(beams, columns_len, rows_len):
        locations_set = set()
        for beam in beams:
            for location in beam.locations:
                if not (
                    location[0] < 0
                    or location[0] >= columns_len
                    or location[1] < 0
                    or location[1] >= rows_len
                ):
                    locations_set.add(location)
        return locations_set

    def __hash__(self):
        return hash(
            (self.x, self.y, self.direction, self.is_moving)
        )  # Replace attr1, attr2 with the attributes that uniquely identify a Beam object


# define class for mirros that deflect the beam
class Mirror:
    def __init__(self, x, y, shape="/"):
        self.x = x
        self.y = y
        self.shape = shape

    def __repr__(self):
        return f"({self.x}, {self.y}) --> {self.shape}"

    def __str__(self):
        return f"({self.x}, {self.y}) --> {self.direction}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_shape(self):
        return self.shape

    def get_new_direction(self, direction):
        if direction == (0, 1):
            if self.shape == "/":
                return (-1, 0)
            else:
                return (1, 0)
        elif direction == (0, -1):
            if self.shape == "/":
                return (1, 0)
            else:
                return (-1, 0)
        elif direction == (1, 0):
            if self.shape == "/":
                return (0, -1)
            else:
                return (0, 1)
        elif direction == (-1, 0):
            if self.shape == "/":
                return (0, 1)
            else:
                return (0, -1)
        else:
            print("Error: invalid direction")
            return None


"""defin class for spliter that splits the beam
If the beam encounters the pointy end of a splitter (| or -), the beam passes through the splitter as if the splitter were empty space. For instance, a rightward-moving beam that encounters a - splitter would continue in the same direction.
If the beam encounters the flat side of a splitter (| or -), the beam is split into two beams going in each of the two directions the splitter's pointy ends are pointing. For instance, a rightward-moving beam that encounters a | splitter would split into two beams: one that continues upward from the splitter's column and one that continues downward from the splitter's column.
"""


class Splitter:
    def __init__(self, x, y, shape="|"):
        self.x = x
        self.y = y
        self.shape = shape

    def __repr__(self):
        return f"({self.x}, {self.y}) --> {self.shape}"

    def __str__(self):
        return f"({self.x}, {self.y}) --> {self.shape}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_shape(self):
        return self.shape

    def get_refraction(self, beam: Beam, beams):
        if self.shape == "|":
            if beam.get_direction() == (1, 0) or beam.get_direction() == (-1, 0):
                pass
            elif beam.get_direction() == (0, 1) or beam.get_direction() == (0, -1):
                beam.stop_moving()
                beam1 = Beam(self.x, self.y, (1, 0))
                beam2 = Beam(self.x, self.y, (-1, 0))
                beams.append(beam1)
                beams.append(beam2)
        elif self.shape == "-":
            if beam.get_direction() == (0, 1) or beam.get_direction() == (0, -1):
                pass
            elif beam.get_direction() == (1, 0) or beam.get_direction() == (-1, 0):
                beam.stop_moving()
                beam1 = Beam(self.x, self.y, (0, -1))
                beam2 = Beam(self.x, self.y, (0, 1))
                beams.append(beam1)
                beams.append(beam2)
        return beams


def read_board(lines):
    mirrors = {}
    splitters = {}

    for row in range(rows_len):
        for col in range(columns_len):
            if lines[row][col] == "/" or lines[row][col] == "\\":
                mirrors[(row, col)] = Mirror(row, col, lines[row][col])
            elif lines[row][col] == "|" or lines[row][col] == "-":
                splitters[(row, col)] = Splitter(row, col, lines[row][col])

    return mirrors, splitters


def print_board(mirrors, splitters, beams):
    for row in range(rows_len):
        for col in range(columns_len):
            if (row, col) in Beam.get_moving_beam_locations(beams):
                print("B", end="")
            elif (row, col) in mirrors:
                print(mirrors[(row, col)].get_shape(), end="")
            elif (row, col) in splitters:
                print(splitters[(row, col)].get_shape(), end="")
            else:
                print(".", end="")
        print()


mirrors, splitters = read_board(lines)


def run_beam(start_location, direction):
    b = Beam(start_location[0], start_location[1], direction)
    beams = [b]
    x = 0
    same_count = 0
    previous_length = None
    master_locations = set()
    while Beam.any_beams_moving(beams):
        for beam in beams:
            if not beam.get_is_moving():
                continue
            if beam.get_coord() in mirrors:
                beam.set_new_direction(
                    mirrors[beam.get_coord()].get_new_direction(beam.get_direction())
                )
            elif beam.get_coord() in splitters:
                beams = splitters[beam.get_coord()].get_refraction(beam, beams)
        beams = Beam.move_beams(beams)

        if x == 5000:  # dont really need
            break
        x += 1

        # energized = len(Beam.get_locations(beams ,columns_len, rows_len))
        master_locations.update(Beam.get_locations(beams, columns_len, rows_len))
        energized = len(master_locations)
        if previous_length == energized:
            same_count += 1
        else:
            same_count = 0

        previous_length = energized

        if same_count == 10:
            break

        # prune beams
        beams = [beam for beam in beams if beam.get_is_moving()]
        # dedupe beams
        beams = list(set(beams))

    print(len(master_locations))
    return len(master_locations)


print(run_beam((0, 0), (0, 1)))


### PART 2

all_beam_lengths = []
for row in range(rows_len):
    all_beam_lengths.append(run_beam((row, 0), (0, 1)))
    all_beam_lengths.append(run_beam((row, columns_len - 1), (0, -1)))

for col in range(columns_len):
    all_beam_lengths.append(run_beam((0, col), (1, 0)))
    all_beam_lengths.append(run_beam((rows_len - 1, col), (-1, 0)))

print(max(all_beam_lengths))
