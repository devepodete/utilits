set(EXECUTION_FILENAME tm_converter.out)

cmake_minimum_required(VERSION 3.10)
project(turing_markov_converter)

set(CMAKE_CXX_STANDARD 11)
add_library(full_library STATIC processing.cpp output.cpp)

add_executable(${EXECUTION_FILENAME} turing-markov.cpp)

target_link_libraries(${EXECUTION_FILENAME} full_library)