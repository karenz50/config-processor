import json

"""def process_yaml( file_name ):
    yaml_file = open(file_name, "r") 
    my_config = yaml.load(yaml_file)

    for section in my_config:
        print(section)
    print(my_config["mysql"])
    print(my_config["other"])"""

def process_json( file_name ):
    json_file = open(file_name)
    my_config = json.load(json_file)
    print(my_config)

if __name__ == "__main__":

    #process_yaml("config_files/test1.yml")
    process_json("config_files/test2.json")