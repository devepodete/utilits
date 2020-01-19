set(EXECUTION_FILENAME nan.out)

cmake_minimum_required(VERSION 3.10)
project(markov_emulator)

set(CMAKE_CXX_STANDARD 11)

add_executable(${EXECUTION_FILENAME} main.cpp)