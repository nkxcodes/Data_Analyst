
def calculate_average(list):
    return sum(list) / len(list)

def check_result(marks):
    if marks >= 40 and marks <= 100:
        return 'Passed.'
    else:
        return 'Failed'