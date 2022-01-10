cmake_minimum_required(VERSION 3.0)
set(CMAKE_BUILD_TYPE "Release")

project(main)

include_directories(
	${PROJECT_SOURCE_DIR}\\inc
)

link_directories(
	${PROJECT_SOURCE_DIR}\\lib
)

add_executable(main main.cpp)
