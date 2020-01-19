#include <iostream>
#include <string>
#include <vector>
#include <tuple>
#include <fstream>

namespace cmd_type{
	using type = int;
	enum{terminate, usual};
}

void print_usage(){
	std::cout << "Usage: ./mam [-m] file_name" << std::endl;
	std::cout << "Key -m is not necessary and using for metasymbols" << std::endl;
}

std::vector<std::tuple<std::string, std::string, cmd_type::type>> parse_file(std::ifstream &ifs){
	std::vector<std::tuple<std::string, std::string, cmd_type::type>> result;

	std::string str, str1, str2;
	while(ifs >> str){
		str1 = str2 = "";
		std::string::size_type arrow_pos;
		cmd_type::type command_type = cmd_type::usual;

		arrow_pos = str.rfind("->");
		if(arrow_pos == std::string::npos){
			std::cerr << "Error: some of commands has wrong format" << std::endl;
			throw int();
		}
		
		str1 = str.substr(0, arrow_pos);
		
		if(arrow_pos + 2 < str.length()){
			if(str[arrow_pos+2] == '.'){
				command_type = cmd_type::terminate;
			}
		}
		
		if(command_type == cmd_type::usual){
			//abc->def
			str2 = str.substr(arrow_pos+2, str.length());
		}else{
			//abc->.def
			str2 = str.substr(arrow_pos+3, str.length());
		}

		result.push_back(std::make_tuple(str1, str2, command_type));
	}

	return result;
}

void run(std::string &str, const std::vector<std::tuple<std::string, std::string, cmd_type::type>> &parsed_commands){
	bool work = true;

	std::cout << str;
	while(work){
		work = false;
		getchar();
		std::cout << '\r';
		for(int i = 0; i < parsed_commands.size(); i++){
			std::string to_find = std::get<0>(parsed_commands[i]);
			if(to_find.empty()){
				str.insert(0, std::get<1>(parsed_commands[i]));
				if(std::get<2>(parsed_commands[i]) != cmd_type::terminate){
					work = true;
				}
				break;
			}else{
				std::string::size_type pos = str.find(to_find);
				if(pos != std::string::npos){
					if(std::get<2>(parsed_commands[i]) != cmd_type::terminate){
						work = true;
					}
					str.replace(pos, std::get<0>(parsed_commands[i]).length(), std::get<1>(parsed_commands[i]));
					break;
				}
			}
		}
		std::cout << str;
	}
}

int main(int argc, char *argv[]){
	bool use_metasymbols = false;
	
	std::ifstream input_file;

	if(argc == 2){
		input_file.open(argv[1], std::ios_base::in);
	}else if(argc == 3){
		std::string second_key = std::string(argv[2], std::ios_base::in);
		if(second_key == "-m"){
			use_metasymbols = true;
			input_file.open(argv[2]);
		}else{
			std::cerr << "Wrong key" << std::endl;
			print_usage();
			return 1;
		}
	}else if(argc <= 1 || argc > 3){
		print_usage();
		return 1;
	}
	
	if(!input_file.is_open()){
		std::cerr << "Error: can not open file" << std::endl;
		return 1;
	}

	std::vector<std::tuple<std::string, std::string, cmd_type::type>> parsed;

	try{
		parsed = parse_file(input_file);
	}catch(...){
		std::cout << "Some erros were occured while file parsing." << std::endl;
		input_file.close();
		return 1;
	}

	std::cout << "Input string: ";
	std::string initial_string;
	std::cin >> initial_string;
	getchar();

	run(initial_string, parsed);

	return 0;
}
