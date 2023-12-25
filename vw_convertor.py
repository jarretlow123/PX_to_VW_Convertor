import json

HEADER = """
    =========================================================================================
    |          PX to VW Convertor (Python) |    By: https://github.com/jarretlow123         |
    =========================================================================================
"""

def main():
    # load content of config file
    try:
        with open('config.json', 'r') as file:
            CONFIG = json.load(file)
            print(HEADER)
            print("[!] Loading config.json")
    except FileNotFoundError:
        print("[X] File 'config.json' not found!")
        return
    except IOError:
        print("[X] Error reading the file!")
        return
    
    # process the file 
    for file in CONFIG['files']:
        print(f"[!] Start the process for the file '{file}'")
        
        print(f"[!] Completed processing the file '{file}'")
    
if __name__ == "__main__":
    main()