#include "./libs/orm/sqlite_orm.h"
#include "./models/models.hpp"

using namespace sqlite_orm;

auto dbInit(std::string path){
    auto storage = make_storage(path,
    make_table("users",
        make_column("id",&User::id,primary_key()),
        make_column("username",&User::username),
        make_column("bio",&User::bio),
        make_column("join_date",&User::join_date)
    ));

    return storage;
}