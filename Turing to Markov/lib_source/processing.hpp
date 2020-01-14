#pragma once

#include <vector>
#include <string>
#include <tuple>

namespace proc{
	extern std::string sep1, sep2;
}

//parse string by ',' character
std::tuple<std::string, std::string, std::string, std::string> parse_string(const std::string &s);

//convert turing to markov
std::vector<std::string> convert(std::vector<std::string> &turing_commands);