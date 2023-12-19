"""Code for day nineteen of advent of code 2023."""
import numpy as np
from copy import deepcopy


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
    Convert input to list of dicts of parts, and dict of rules.
    """
    sep_ind = raw_lines.index("")
    rules = raw_lines[:sep_ind]
    parts = raw_lines[sep_ind + 1 :]

    # Parts - place in list of dicts where keys are letter and values are val
    parts_dicts = [
        {att[0]: int(att[2:]) for att in p_line[1:-1].split(",")} for p_line in parts
    ]

    # Rules - place in dict where keys are name and vals are list of rules as dict
    rules_dict = {}
    for rule in rules:
        name = rule.split("{")[0]

        rules_dict[name] = [
            {
                "att": wf[0],
                "op": wf[1],
                "val": int(wf.split(":")[0][2:]),
                "res": wf.split(":")[1],
            }
            if ":" in wf
            else {"att": None, "op": None, "val": None, "res": wf}
            for wf in rule.split("{")[1][:-1].split(",")
        ]

    return parts_dicts, rules_dict


def run_workflow(pt, wf):
    """
    Run a single workflow on a part and return where to go next/result.
    """
    # print(f"running on part {pt}")
    for rule in wf:
        # print(f"running rule {rule}")
        if not rule["att"]:
            return rule["res"]
        else:
            att_val = pt[rule["att"]]
            match rule["op"]:
                case "<":
                    if att_val < rule["val"]:
                        return rule["res"]
                case ">":
                    if att_val > rule["val"]:
                        return rule["res"]
                case _:
                    raise ValueError(f"Unrecognised operation {rule['att']}")


def split_rule(pt, wfs, wf_name):
    """
    Take part ranges, recursively apply a workflow, and sum number of parts accepted.
    """
    n_acc = 0

    for rule in wfs[wf_name]:
        # if at the end of rule
        if not rule["att"]:
            if rule["res"] == "A":
                n_acc += n_parts(pt)
            elif rule["res"] == "R":
                n_acc += 0
            else:
                n_acc += split_rule(pt, wfs, rule["res"])

        else:
            match rule["op"]:
                case "<":
                    # Apply next rule to lower and continue processing upper
                    pt_l = deepcopy(pt)
                    pt_l[rule["att"]] = range(pt_l[rule["att"]][0], rule["val"])
                    pt[rule["att"]] = range(rule["val"], pt[rule["att"]][-1] + 1)
                    if rule["res"] == "A":
                        n_acc += n_parts(pt_l)
                    elif rule["res"] == "R":
                        n_acc += 0
                    else:
                        n_acc += split_rule(pt_l, wfs, rule["res"])

                case ">":
                    # Apply next rule to lower and continue processing upper
                    pt_u = deepcopy(pt)
                    pt[rule["att"]] = range(pt[rule["att"]][0], rule["val"] + 1)
                    pt_u[rule["att"]] = range(
                        rule["val"] + 1, pt_u[rule["att"]][-1] + 1
                    )

                    if rule["res"] == "A":
                        n_acc += n_parts(pt_u)
                    elif rule["res"] == "R":
                        n_acc += 0
                    else:
                        n_acc += split_rule(pt_u, wfs, rule["res"])

                case _:
                    raise ValueError(f"Unrecognised operation {rule['att']}")

    return n_acc


def n_parts(pt):
    """
    Sum number of passing parts for a part defined with ranges.
    """
    return len(pt["x"]) * len(pt["m"]) * len(pt["a"]) * len(pt["s"])


if __name__ == "__main__":
    # Get inputs
    parts, workflows = process_input(read_file("data/day19.dat"))
    # parts, workflows = process_input(read_file("data/day19.test"))

    # Part 1
    ans_one = 0
    for part in parts:
        ended = False
        wf_name = "in"
        while not ended:
            wf_name = run_workflow(part, workflows[wf_name])

            if wf_name == "R":
                # Reject
                ended = True
            elif wf_name == "A":
                # Accept
                ended = True
                ans_one += part["x"] + part["m"] + part["a"] + part["s"]

    print(f"Part one answer is {ans_one}")

    # Part 2
    ans_two = 0

    # Track through workflows splitting on each option.
    my_part = {
        "x": range(1, 4001),
        "m": range(1, 4001),
        "a": range(1, 4001),
        "s": range(1, 4001),
    }

    ans_two = split_rule(my_part, workflows, "in")

    print(f"Part two answer is {ans_two}")
