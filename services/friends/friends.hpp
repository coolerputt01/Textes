#pragma once
#include <string>
#include <vector>

#include "../models/models.hpp"

using namespace sqlite_orm;

int addFriend(std::string tag,string username,auto& storage,int profile_id){

    if(username.empty()){
        return 1;
    }

    auto profile = storage.template get_all<Profile>(where(c(&Profile::username) == username));

    if(tag.empty()){
        tag = "";
    }

    if(!profile.empty()){
        Friend user_friend = profile.front();
        user_friend.tag = tag;
        user_friend.profile_id = profile_id;
        storage.insert(user_friend);
    }

    return 0;

}

std::vector listFriends(auto& storage,int profile_id){
    std::vector<Friend> friends = storage.template get_all<&Friend>(where(c(&Friend::profile_id) == profile_id));

    return friends;
}