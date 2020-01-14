#include <iostream>
#include <vector>
#include <string>

#include "processing.hpp"
#include "output.hpp"

int main(int argc, char *argv[]){
	if(argc == 3){
		proc::sep1 = argv[1];
		proc::sep2 = argv[2];
		std::cout << "Default state separator set by \'" << 
			proc::sep1 << "\' and \'" << proc::sep2 << "\'" << std::endl;
	}else if(argc == 1){
		std::cout << "Default state separator set by \'(\' and \')\'" << std::endl;
	}else if(argc != 1){
		std::cout << "Usage: ./PROGRAM_NAME [STATE_SEPARATOR_1] [STATE_SEPARATOR_2]" << std::endl;
		return 0;
	}

	std::vector<std::string> turing_commands;

	std::string turing_command = "";
	while(std::cin >> turing_command){
		turing_commands.push_back(turing_command);
	}

	std::vector<std::string> markov_commands = convert(turing_commands);

	for(int i = 0; i < markov_commands.size(); i++){
		std::cout << markov_commands[i] << std::endl;
	}

	return 0;
}