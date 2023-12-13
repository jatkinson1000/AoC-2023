"""Code for day thirteen of advent of code 2023."""


def read_file(fname: str) -> list[str]:
    """
    Read data from file and strip each line of '\n'.
    """
    with open(fname) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines


def process_input(raw_lines):
    """
    Process raw lines from the input file to lists of ints.
    """
    blocks = []
    block = []
    for line in raw_lines:
        if line == "":
            blocks.append(block)
            block = []
        else:
            block.append(line)

    blocks.append(block)

    return blocks


def reflect_horiz(b, ival=None, tval=None):
    """
    Check for horizontal lines of reflection.
    """
    # Point to end
    ref_cols = []
    for i in range(len(b[0]) - 1):
        # find reflection points of line 1
        if b[0][i:] == b[0][i:][::-1] and len(b[0][i:]) % 2 == 0:
            ref_cols.append((i, i + len(b[0][i:]) // 2))

    # Check rest of lines
    for ref in ref_cols:
        check = [r[ref[0] :] == r[ref[0] :][::-1] for r in b]
        if all(check):
            # print(f"reflect H: {b[0]} col {ref[0] + len(b[0][ref[0]:])//2} {ref[0]} {len(b[0][ref[0]:])//2}")
            if ival != ref[0] or tval != "H0":
                return ref[1], ref[0], "H0"

    # Start to point
    ref_cols = []
    for i in range(1, len(b[0])):
        # find reflection points of line 1
        if b[0][0 : i + 1] == b[0][0 : i + 1][::-1] and len(b[0][0 : i + 1]) % 2 == 0:
            ref_cols.append((i, len(b[0][0 : i + 1]) // 2))

    # Check rest of lines
    for ref in ref_cols:
        check = [r[0 : ref[0] + 1] == r[0 : ref[0] + 1][::-1] for r in b]
        if all(check):
            print(f"reflect H2: {b[0]} col {ref[1]//2} {ref[1]}")
            if ival != ref[0] or tval != "H1":
                return ref[1], ref[0], "H1"
    return 0, 0, "X"


def reflect_vert(b, ival=None, tval=None):
    """
    Check for vertical lines of reflection.
    """
    # row to end
    for i in range(len(b) - 1):
        # find reflection points
        if b[i:] == b[i:][::-1] and len(b[i:]) % 2 == 0:
            # print(f"reflect V: {b} row {i + len(b[i:])//2} {i} {len(b[i:])//2}")
            if ival != i or tval != "V0":
                return 100 * (i + len(b[i:]) // 2), i, "V0"

    # Top to row
    for i in range(1, len(b)):
        # find reflection points
        if b[:i] == b[:i][::-1] and len(b[:i]) % 2 == 0:
            # print(f"reflect V2: {b} row {i + len(b[i:])//2} {i} {len(b[i:])//2}")
            if ival != i or tval != "V1":
                return 100 * (len(b[:i]) // 2), i, "V1"

    return 0, 0, "X"


def get_reflection(b):
    """
    Check mirror for any reflection.
    """
    href, i, t = reflect_horiz(b)
    if href > 0:
        return href, i, t
    vref, i, t = reflect_vert(b)
    if vref > 0:
        return vref, i, t
    raise ValueError("Oh No! No reflection found.")


def fix_smudge(b, ival, tval, val):
    """
    Fix smudges everywhere until reflection found.
    """
    for j in range(len(b)):
        for i in range(len(b[0])):
            # print(i, j)
            b_c = b.copy()
            if b[j][i] == ".":
                b_c[j] = b_c[j][:i] + "#" + b_c[j][i + 1 :]
            else:
                b_c[j] = b_c[j][:i] + "." + b_c[j][i + 1 :]

            href, _, _ = reflect_horiz(b_c, ival, tval)
            if href > 0:
                # print(f"href = {href}")
                return href

            vref, _, _ = reflect_vert(b_c, ival, tval)
            if vref > 0:
                # print(f"vref = {vref}")
                return vref
    raise ValueError("Oh No! No reflection found.")


if __name__ == "__main__":
    # Get inputs
    # blocks = process_input(read_file("data/day13.dat"))
    blocks = process_input(read_file("data/day13.test"))
    # blocks = process_input(read_file("data/day13.test_2"))

    # Part 1
    ans_one = 0
    p1_i = []
    p1_t = []
    vals = []
    for j, block in enumerate(blocks):
        # print("\n")
        # print(f"block {j}")
        val, i, t = get_reflection(block)
        ans_one += val
        p1_i.append(i)
        p1_t.append(t)
        vals.append(val)
    print(f"Part one answer is {ans_one}")

    # Part 2
    ans_two = 0
    for j, block in enumerate(blocks):
        # print("\n")
        # print(f"block {j}")
        ans_two += fix_smudge(block, p1_i[j], p1_t[j], vals[j])
    print(f"Part two answer is {ans_two}")
