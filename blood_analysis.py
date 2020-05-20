# blood_analysis

def interface():
    print("My Blood Analysis Calculator")
    keep_running = True
    while keep_running:
        print("Options:")
        print("9-quit")
        choice = input("Choose an option: ")
        if choice == '9':
            return

if __name__== "__main__":
    interface()
