cmake_minimum_required(VERSION 3.10)
project(turing_markov_converter)

set(CMAKE_CXX_STANDARD 11)
add_executable(tm_converter.out turing-markov.cpp)

include_directories(lib)
include_directories(lib_source)

#add_library(output_library STATIC output.cpp)
#add_library(processing_library STATIC processing.cpp)

find_library(FULL_LIBRARY full_lib lib)

target_link_libraries(tm_converter.out LINK_PUBLIC ${FULL_LIBRARY})
