import yaml
import json

def process_yaml( file_name ):
    yaml_file = open(file_name, "r") 
    my_config = yaml.safe_load(yaml_file)

    for section in my_config:
        print(section)
    print(my_config["oracle"])
    print(my_config["connections"])

def process_json( file_name ):
    json_file = open(file_name)
    my_config = json.load(json_file)
    print(my_config)

#def process_

if __name__ == "__main__":

    process_yaml("config_files/test1.yml")
    #process_json("config_files/test2.json")
    #process_