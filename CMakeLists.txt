set(PCL_DIR "/opt/pcl/release" )
cmake_minimum_required(VERSION 2.8)

cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(library)

find_package(PCL 1.2 REQUIRED)
find_package( OpenCV REQUIRED )
#set(PCL_DIR "/opt/pcl/release" CACHE PATH "")
# directories
set (LIBELAS_SRC_DIR src)

# use sse3 instruction set for LIBELAS
SET(CMAKE_CXX_FLAGS "-msse3")

# sources for LIBELAS
FILE(GLOB LIBELAS_SRC_FILES "src/*.cpp")



# make release version
set(CMAKE_BUILD_TYPE Release)


include_directories(${PCL_INCLUDE_DIRS})

include_directories("${LIBELAS_SRC_DIR}")  

link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable (library library.C ${LIBELAS_SRC_FILES})

#add_executable(elas ${LIBELAS_SRC_FILES})
target_link_libraries (library ${PCL_LIBRARIES})

target_link_libraries( library ${OpenCV_LIBS} )
