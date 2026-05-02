#pragma once
#include <string>

//#include "../libs/http/httplib.h"
#include "../models/models.hpp"
#include "../config.hpp"
#include "../libs/utils/date.hpp"
#include "../libs/pybind11/pybind11.h"
#include "../libs/pybind11/stl.h"

using namespace sqlite_orm;
namespace py = pybind11;

int createUser(auto &storage,std::string username,std::string bio){

    if(username.empty()){
        return 1;
    }

    auto existing_profiles = storage.template get_all<Profile>(where(c(&Profile::username) == username));
    if(!existing_profiles.empty()){
        return 1;
    }
    Profile profile;
    profile.username = username;
    profile.bio = bio;
    profile.session = SESSION::LOGGED_IN;
    profile.join_date = dateNow();

    storage.insert(profile);
    return 0;
}


PYBIND11_MODULE(services, mobj){
    using Storage = decltype(dbInit(""));

    py::class_<Storage>(mobj, "Storage");
    mobj.def("dbInit", &dbInit);

    py::class_<Profile>(mobj,"Profile")
    .def(py::init<>())
    .def_readwrite("id",&Profile::id)
    .def_readwrite("username",&Profile::username)
    .def_readwrite("bio",&Profile::bio)
    .def_readwrite("join_date",&Profile::join_date)
    .def("getSession",&Profile::getSession)
    .def("setSession",&Profile::setSession);

    mobj.def("createUser", [](Storage &storage, std::string username, std::string bio) {
        return createUser(storage, username, bio);
    });
} 