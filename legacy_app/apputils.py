import os

# VARIABLES


# FUNCTIONS
# def process_results(servicename, job, code):
#     match code:
#         case 1:
#             return f'{servicename} has been successfully {job}ed.'
#         case -1:
#             return f'Error while {job}ing {servicename}. Error code = {code}'
#         case -2:
#             return f"{os.name} is not compatible with Legacy :("

def process_results(servicename, job, code):
    if code == 1:
        return f'{servicename} has been successfully {job}ed.'
    elif code == -1:
        return f'Error while {job}ing {servicename}. Error code = {code}'
    elif code == -2:
        return f"{os.name} is not compatible with Legacy :("
    else:
        return "huh?"