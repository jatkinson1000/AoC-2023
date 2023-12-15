"""Code for day fifteen of advent of code 2023."""


def read_file(fname: str) -> list[str]:
    """
    Read data from file and strip each line of '\n'.
    """
    with open(fname) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines


def process_input(raw_line):
    """
    Process raw lines from the input file to lists of ints.
    """
    s = raw_line[0].split(",")

    return s


def hash_line(l):
    """
    Perform hash operation on a single string.
    """
    val = 0
    for ch in l:
        val += ord(ch)
        val *= 17
        val = val % 256

    return val


def hash_seq(s):
    """
    Perform hash operation on a sequence of strings and return the sum.
    """
    sum = 0
    for l in s:
        sum += hash_line(l)
    return sum


def sort_lenses(s):
    """
    Sort lenses into boxes as described by the problem. Use ordered dicts!
    """
    boxes = [{} for _ in range(256)]

    for l in s:
        lens_n = l.replace("-", "=").split("=")[0]
        lens_id = l.replace("-", "=").split("=")[1]
        if "=" in l:
            # Using dict, so no need to worry if lens is already in box or not.
            boxes[hash_line(lens_n)][lens_n] = lens_id

        elif "-" in l and lens_n in boxes[hash_line(lens_n)]:
            boxes[hash_line(lens_n)].pop(lens_n)

    return boxes


def get_power(boxes):
    """
    Get the focussing power of the sorted lenses in boxes as described.
    """
    sum = 0
    for i, box in enumerate(boxes):
        for j, l in enumerate(box):
            sum += (i + 1) * (j + 1) * int(box[l])
    return sum


if __name__ == "__main__":
    # Get inputs
    seq = process_input(read_file("data/day15.dat"))
    # seq = process_input(["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"])

    # Tests
    assert hash_line("HASH") == 52
    assert hash_line("rn=1") == 30
    assert hash_line("pc-") == 48

    # Part 1
    ans_one = hash_seq(seq)
    print(f"Part one answer is {ans_one}")

    # Part 2
    boxed = sort_lenses(seq)
    ans_two = get_power(boxed)
    print(f"Part two answer is {ans_two}")
