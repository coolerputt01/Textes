#include "./libs/orm/sqlite_orm.h"
#include "./models/models.hpp"

using namespace sqlite_orm;

inline auto dbInit(std::string path){
    auto storage = make_storage(path,
    make_table("profile",
        make_column("id",&Profile::id,primary_key().autoincrement()),
        make_column("username",&Profile::username),
        make_column("bio",&Profile::bio),
        make_column("session",&Profile::getSession,&Profile::setSession),
        make_column("join_date",&Profile::join_date)
    ),
    make_table("friends",
        make_column("id",&Friend::id,primary_key().autoincrement()),
        make_column("username",&Friend::username),
        make_column("bio",&Friend::bio),
        make_column("session",&Friend::getSession,&Friend::setSession),
        make_column("join_date",&Friend::join_date),
        make_column("profile_id",&Friend::profile_id),
        make_column("tag",&Friend::tag)
    ));

    return storage;
}