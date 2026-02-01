#      program: p2.py
#         date: 1-29-26
#       author: Mason Reeves
#  description: Calculates miles walked from steps and stride length,
#               and reports how far over or under 10,000 steps.
#               Demonsrates use of return functions.

# functions

def get_steps():
    
    print("Enter number of steps")
    steps = int(input())
    
    return steps


def get_stride_inches():
    
    print("Enter stride distance in inches")
    stride_inches = int(input())
    
    
    return stride_inches


def calculate_miles(steps, stride_inches):
    
    miles = steps * stride_inches/63360
    
    
    return miles


def additional_steps_needed(steps):    
    if steps < 10000:
        return 10000 - steps
    elif steps > 10000:
        return steps - 10000:
    else: 
        return 0

def miles_output_line(steps, miles):
    msg = f"You walked {steps:,} steps which is {miles} miles"
    return msg

def steps_output_line(additional):
    msg = f"You need {additional:,} more steps to reach 10,000"
    
    return msg

# +------ do not modify this section ----------+
def main():

    # input
    steps = get_steps()
    stride_inches = get_stride_inches()

    # processing
    miles = calculate_miles(steps, stride_inches)
    additional = additional_steps_needed(steps)

    # output
    print( miles_output_line(steps, miles) )
    print( steps_output_line(additional) )

if __name__ == "__main__":
    main()

# +------ do not modify this section ----------+ 
