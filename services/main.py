# #include <iostream>
# #include <filesystem>

# #include "libs/toml/toml.hpp"
# #include "./config.hpp"

# using namespace std::literals; 

# auto config = toml::parse_file("./config.toml");
# int main(void){
#     std::string_view db_path = config["API"]["DB_PATH"].value_or(""sv);
#     auto storage = dbInit(std::string(db_path));
#     storage.sync_schema();
#     return 0;
# }

import tomllib
from .db_handler import db_init

data = None

with open("./config.toml", "rb") as f:
    data = tomllib.load(f)

def main():
    db_path = data["API"]["DB_PATH"]
    db_init(db_path)