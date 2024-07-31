def print_banner():
    banner = """
    ==============================================================
     _    _ _   _ _ _           _      ___ ___     _           
    | |  (_) | (_) (_)         | |    |_  / _ \\   | |          
    | | ___| |_ _| |_ _ __ __ _| |__    | | | |__| | ___ _ __  
    | |/ / | __| | | | '__/ _` | '_ \\   | | | / _` |/ _ \\ '_ \\ 
    |   <| | |_| | | | | | (_| | | | | / /| | | (_| |  __/ | | |
    |_|\_\_|\__|_|_|_|_|  \__,_|_| |_|/___|_|  \__,_|\___|_| |_|
    
                 By Vincent Chimaobi (CyberGhoxt)
    ===============================================================
    """
    print(banner)

def log_unique_ip(): #Defining a function for logging details 
    unique_ips = set() #Declaring an empty set for IP logs

    print_banner()  # Print the banner when the program starts

    while True: # Declaring a while condition to maintain the loop for all the logging provided it is true
        ip = input("Enter IP Address. (or 'done' to exit): ") # Accepting IPs for assessment and storage

        if ip.lower() == 'done': # If the user chooses to exit the program he/she will type "done" or "Done" or "DONE" which will be converted and accepted in lowercase
            break # Exits the program by breaking thye code.

        if ip not in unique_ips: # 
            unique_ips.add(ip)
            print(f"Logging IP: {ip}")  # Log the unique IP (print to console or write to a file)

        else:
            print(f"IP {ip} is already logged.")

    return unique_ips
# Log unique IPs
unique_ips = log_unique_ip()
print("The Logged IPs: \n", unique_ips)
        