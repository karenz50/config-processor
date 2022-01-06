import yaml
import json
import configparser as ConfigParser
import io
from bs4 import BeautifulSoup

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

"""def process_ini( file_name ):
    in_file = open(file_name)
    sample_config = in_file.read()
    config = ConfigParser.RawConfigParser(allow_no_value=True)
    config.readfp(io.BytesIO(sample_config))

    # List all contents
    print("List all contents")
    for section in config.sections():
        print("Section: %s" % section)
        for options in config.options(section):
            print(
                "x %s:::%s:::%s"
                % (options, config.get(section, options), str(type(options)))
            )

    # Print some contents
    print("\nPrint some contents")
    print(config.get("other", "use_anonymous"))  # Just get the value
    print(config.getboolean("other", "use_anonymous"))"""

def process_xml( file_name ):
    in_file = open(file_name)
    my_config = in_file.read()
    my_result = BeautifulSoup(my_config, "lxml")
    print(my_result)

if __name__ == "__main__":

    #process_yaml("config_files/test1.yml")
    #process_json("config_files/test2.json")
    #process_ini("config_files/test3.ini")
    process_xml("config_files/test4.xml")