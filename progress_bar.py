from library import *

def progress_bar(text):
    import time
    for j in range(1,101):
            time.sleep(.003)
     
            downloading = colored(text, 'green', 'on_grey', attrs=['reverse'])
            percentage = colored(f"[{j}%]", 'blue')
            bar = colored('|' * j, "red")
            color = downloading + percentage + bar
     
            print(color, end="\r")
            
