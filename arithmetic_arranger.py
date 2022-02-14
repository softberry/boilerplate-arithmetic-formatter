import re


def valid_operand(str):
    return str == "+" or str == "-"


def only_digits(nums):
    return len(re.findall('\d', str(nums))) == len(str(nums))

def calculate(entry,should_print=False):
    if should_print == False:
        return ""
    f=int(entry[0])
    o=entry[1]
    s=int(entry[2])

    if o =="+":
        return str(f+s)
    else:
        return str(f-s)

def arithmetic_arranger(list_calc, should_print=False):
    result = {"first_op": [], "second_op": [], "line": [],"total_sum":[]}


    if len(list_calc) == 0:
        return

    if len(list_calc) > 5 :
        return "Error: Too many problems."

    for idx,entry in enumerate(list_calc):

        space ="    "
        if (idx==len(list_calc)-1):
            space=""

        list_from_entry = entry.split(" ")

        if (len(list_from_entry) != 3):
            continue

        if (not only_digits(list_from_entry[0])):
            return "Error: Numbers must only contain digits."

        if (not only_digits(list_from_entry[2])):
            return "Error: Numbers must only contain digits."

        if (len(list_from_entry[0]) > 4):
            return "Error: Numbers cannot be more than four digits."

        if (len(list_from_entry[2]) > 4):
            return "Error: Numbers cannot be more than four digits."

        if not valid_operand( list_from_entry[1]):
            return "Error: Operator must be '+' or '-'."

        
        len_of_nums = max(len(list_from_entry[0]), len(list_from_entry[2])) + 2
        first_op = list_from_entry[0].rjust(len_of_nums)
        second_op = list_from_entry[1] + " " + list_from_entry[2].rjust(
            len_of_nums - 2)
        line = "".rjust(len_of_nums, "-")
        total_sum=calculate(list_from_entry,should_print).rjust(len_of_nums)
        
        result["first_op"].append(first_op + space)
        result["second_op"].append(second_op + space)
        result["line"].append(line + space)
        result["total_sum"].append(total_sum + space)
        
    
    str_results = r"".join(result["first_op"]) + "\n" + "".join(
        result["second_op"]) + "\n" + "".join(result["line"])

    if should_print:
        str_results =  str_results + "\n" + "".join(result["total_sum"])
        
    return str_results