#include "processing.hpp"

namespace proc{
	std::string sep1 = "(";
	std::string sep2 = ")";
}

//parse string by ',' character
std::tuple<std::string, std::string, std::string, std::string> parse_string(const std::string &s){
	std::string state_1, current_char, action, state_2;

	int i;

	for(i = 0; s[i] != ','; i++){	
		state_1 += s[i];
	}

	i++;
	current_char = s[i];
	i += 2;
	action = s[i];
	i += 2;
	for(; i != s.length(); i++){
		state_2 += s[i];
	}

	return std::make_tuple(state_1, current_char, action, state_2);
}

std::vector<std::string> convert(std::vector<std::string> &turing_commands){
	std::vector<std::string> markov_commands;

	for(int i = 0; i < turing_commands.size(); i++){
		std::string state_1, current_char, action, state_2;

		auto parsed_string = parse_string(turing_commands[i]);
		state_1 = std::get<0>(parsed_string);
		current_char = std::get<1>(parsed_string);
		action = std::get<2>(parsed_string);
		state_2 = std::get<3>(parsed_string);

		switch(action[0]){
			case '>':{
				//move right				
				markov_commands.push_back(std::string(current_char + proc::sep1 + state_1 + 
					proc::sep2 +"A->" + current_char + "A" + proc::sep1 + state_2 + proc::sep2));
				//add "space" in the end if there is no symbols
				markov_commands.push_back(std::string(current_char + proc::sep1 + state_1 + 
					proc::sep2 + "->" + current_char + "_" + proc::sep1 + state_2 + proc::sep2));
				break;
			}
			case '<':{
				//move left
				markov_commands.push_back(std::string(current_char + proc::sep1 + state_1 + 
					proc::sep2 + "->" + proc::sep1 + state_2 + proc::sep2 + current_char));
				break;
			}
			case '#':{
				//finish job
				markov_commands.push_back(std::string(current_char + proc::sep1 + state_1 + 
					proc::sep2 + "->." + current_char + proc::sep1 + state_2 + proc::sep2));
				break;
			}
			default:{
				//change symbol or/and state
				markov_commands.push_back(std::string(current_char + proc::sep1 + state_1 +  
					proc::sep2 + "->" + action + proc::sep1 + state_2 + proc::sep2));
				break;
			}
		}
	}

	return markov_commands;
}