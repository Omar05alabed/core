def maze():

    with open("config.txt", "r") as config:
        try:
            for line in config:
                line = line.strip()
                if line == "":
                    continue
                if line[0] == "#":
                    continue
                key, value = line.split("=")
                if key == "WIDTH":
                    value = value.strip()
                    width = int(value)
                elif key == "HEIGHT":
                    value = value.strip()
                    height = int(value)
                elif key == "ENTRY":
                    value = value.strip()
                    first, second = value.split(",")
                    entry = int(first), int(second)
                elif key == "EXIT":
                    value = value.strip()
                    first, second = value.split(",")
                    exit = int(first), int(second)
                elif key == "OUTPUT_FILE":
                    value = value.strip()
                    output_file = value
                elif key == "PERFECT":
                    value = value.strip()
                    if value == "True":
                        state = True
                    elif value == "False":
                        state = False
        except Exception as e:
            print(e)
        if not (width and height and entry and exit and output_file):
            raise ("missing key value in your file")
        if state == False:
            print("your key values are invalid")
        if width <= 0:l 
            print("invalid width")
        if height <= 0:
            print("invalid height")


maze()
