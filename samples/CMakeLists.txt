set(PCL_DIR "/opt/pcl/release" )
cmake_minimum_required(VERSION 2.8)

cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(populate)

find_package(PCL 1.2 REQUIRED)
find_package( OpenCV REQUIRED )
#set(PCL_DIR "/opt/pcl/release" CACHE PATH "")


include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable (populate populate.C)
target_link_libraries (populate ${PCL_LIBRARIES})

target_link_libraries( populate ${OpenCV_LIBS} )
