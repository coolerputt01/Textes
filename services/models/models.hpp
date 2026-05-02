#pragma once
#include <string>

enum class SESSION : int {
    LOGGED_IN=0,
    LOGGED_OUT=1
};
struct Profile {
    int id;
    std::string username;
    std::string bio;
    SESSION session;
    std::string join_date;

    void setSession(int sxn){
        session = static_cast<SESSION>(sxn);
    }
    int getSession(){
        return static_cast<int>(session);
    }
};


struct Friend : public Profile {
    int profile_id;
    std::string tag;
};