#pragma once

#include <chrono>
#include <string>
#include <format>

std::string dateNow(){
    auto now = std::chrono::system_clock::now();
    return std::format("{:%F %T}", now);
}