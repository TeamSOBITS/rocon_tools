##############################################################################
# CMake
##############################################################################

cmake_minimum_required(VERSION 3.0.2)
project(rocon_ebnf)

##############################################################################
# Catkin
##############################################################################

find_package(catkin REQUIRED)
catkin_package()

catkin_python_setup()

##############################################################################
# Installs
##############################################################################

#install(
#    PROGRAMS 
#        scripts/rospair
#    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#    )

##############################################################################
# Unit Tests
##############################################################################

if (CATKIN_ENABLE_TESTING)
  catkin_add_nosetests(tests)
endif()