# blood_analysis
def HDL_analysis(HDL_result):
    if HDL_result >= 60:
        return "Good"
    elif 40 <= HDL_result < 60:
        return "Borderline"
    else:
        return "Bad"

def LDL_analysis(LDL_result):
    if LDL_result < 130:
        return "Normal"
    elif 130 <= LDL_result < 159:
        return "Borderline High"
    elif 160 <= LDL_result < 189:
        return "High"
    else:
        return "Very High"

def HDL_interface():
    # Input should be HDL=66
    print("HDL Interface")
    print("Please input the result in the following format:")
    print("  HDL=## where ## is the numeric result")
    HDL_input = input("Result: ")
    HDL_result = HDL_input.split('=')
    HDL_status = HDL_analysis(int(HDL_result[1]))
    print("HDL status is {}".format(HDL_status))

def LDL_interface():
    # Input should be LDL=66
    print("LDL Interface")
    print("Please input the result in the following format:")
    print("  LDL=## where ## is the numeric result")
    LDL_input = input("Result: ")
    LDL_result = LDL_input.split('=')
    LDL_status = LDL_analysis(int(LDL_result[1]))
    print("HDL status is {}".format(LDL_status))

def interface():
    print("My Blood Analysis Calculator")
    keep_running = True
    while keep_running:
        print("\nOptions:")
        print("1-HDL Analysis")
        print("2-LDL Analysis")
        print("9-quit")
        choice = input("Choose an option: ")
        if choice == '9':
            return
        elif choice == '1':
            HDL_interface()
        elif choice == '2':
            LDL_interface()

def cholesterol_interface():
    print("Total Cholesterol Interface")
    print("Please input the result in the following format:")
    print("  TC=### where ### is the numeric result")
    TC_input = input("Result: ")
    TC_result = TC_input.split('=')
    TC_status = TC_analysis(int(TC_result[1]))
    print("Total Cholesterol status is {}".format(TC_status))

if __name__== "__main__":
    interface()
