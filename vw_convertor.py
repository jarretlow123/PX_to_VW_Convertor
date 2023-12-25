import json

def main():
    # load content of config file
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        print("File 'config.json' not found!")
        return
    except IOError:
        print("Error reading the file!")
        return
    

if __name__ == "__main__":
    main()