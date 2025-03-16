import webbrowser, sys, os  

VIDEO_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
error_count = 0

def input_math():
    global error_count
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            if user_input == "1": 
                open_video()
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                error_count += 1 
    except:
        error_count -= 1
        pass 

def open_video():
    os.system("echo 'Rickroll incoming...'")
    webbrowser.open(VIDEO_URL)

input_math()