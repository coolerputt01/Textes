#include <iostream>
#include <filesystem>

#include "libs/toml/toml.hpp"
#include "./config.hpp"

using namespace std::literals; 

auto config = toml::parse_file("./config.toml");
int main(void){
    std::string_view db_path = config["API"]["DB_PATH"].value_or(""sv);
    auto storage = dbInit(std::string(db_path));
    storage.sync_schema();
    return 0;
}