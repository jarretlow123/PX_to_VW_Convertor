import json, re

HEADER = """
    ===========================================================================================
    |     PX to VW Convertor (Python)      |  By: Kah Xuan (https://github.com/jarretlow123)  |
    ===========================================================================================
"""

# color code
class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def main():
    # load content of config file
    try:
        with open('config.json', 'r') as file:
            CONFIG = json.load(file)
            print(HEADER)
            print(f"{colors.GREEN}[!] Loading config.json")
    except FileNotFoundError:
        print(f"{colors.RED}[X] File 'config.json' not found!")
        return
    except IOError:
        print(f"{colors.RED}[X] Error reading the file 'config.json'!")
        return
    
    # process the file 
    for file in CONFIG['files']:
        print(f"{colors.GREEN}[!] Start the process for the file '{file}'")
        
        # Read the target file
        try:
            f = open(file, "r")
            css = f.read()
        except FileNotFoundError:
            print(f"{colors.RED}[X] File '{file}' not found!")
            continue
        except IOError:
            print(f"{colors.RED}[X] Error reading the file {file}!")
            continue
        
        # regex pattern of (value)px
        PATTERN = r'(\b\d+\.?\d*)px\b'
        
        # Find all occurrences of values followed by "px"
        px_values = re.findall(PATTERN , css)
        
        # Calculate the value for vw
        for i in range(len(px_values)):
            px_values[i] = str(round((float(px_values[i])*100)/CONFIG['screen_width'],4))
            
        # Replace the calculated values back in the CSS
        css = re.sub(PATTERN, lambda x: f"{px_values.pop(0)}vw", css)
        
        # save the changes
        try:
            f = open(file, "w")
            f.write(css)
            f.close()     
            print(f"{colors.GREEN}[!] Completed processing the file '{file}'")
        except FileNotFoundError:
            print(f"{colors.RED}[X] File '{file}' not found!")
            continue
        except IOError:
            print(f"{colors.RED}[X] Error reading the file {file}!")
            continue
        
    print(f"{colors.YELLOW}[!] Done ...")
    print(colors.RESET)
    
if __name__ == "__main__":
    main()