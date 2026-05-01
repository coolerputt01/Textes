#pragma once

#include <string>

#include "../libs/http/httplib.h"
#include "models/models.hpp"
#include "libs/utils/date.hpp"

int createUser(auto &storage,std::string username,std::string bio){
    if(username.empty()){
        return 1;
    }
    User user;
    user.username = username;
    user.bio = bio;
    user.join_date = dateNow();

    storage.insert(user);
    return 0;
}
