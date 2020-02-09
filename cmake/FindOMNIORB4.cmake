#
# Find the omniORB libraries and include dir
#
find_package(PkgConfig REQUIRED)
pkg_search_module(OMNIORB4 REQUIRED omniORB4>=4.1.2)
pkg_search_module(OMNIDYNAMIC4 REQUIRED omniDynamic4>=4.1.2)

find_program(OMNIORB4_IDL_COMPILER
    NAMES omniidl
    PATHS ${OMNIORB4_PREFIX}/bin
    DOC "What is the path where omniidl (the idl compiler) can be found")

# OMNIORB4_OMNIIDL_BCXX SOURCE_DIR FILENAME DESTINATION_DIR
# -------------------------------------------------------------
#
# Generate stubs from an IDL file.
# An include directory can also be specified.
#
# SOURCE_DIR : path part of IDL file location
# FILENAME : IDL filename without the extension
# DESTINATION_DIR : where will be stored the generated CPP files
# IDL_CC : a variable to store the names of the generated .cc files
# IDL_HH : a variable to store the name of the generated header file
#
macro(OMNIORB4_OMNIIDL_BCXX SOURCE_DIR FILENAME DESTINATION_DIR IDL_CC IDL_HH)

    set(${IDL_CC} ${DESTINATION_DIR}/${FILENAME}SK.cc ${DESTINATION_DIR}/${FILENAME}DynSK.cc)
    set(${IDL_HH} ${DESTINATION_DIR}/${FILENAME}.hh)
    add_custom_command(
        OUTPUT ${${IDL_CC}} ${${IDL_HH}}
        COMMAND ${OMNIORB4_IDL_COMPILER}
        ARGS -bcxx -Wba -Wbh=.hh -Wbs=SK.cc -Wbd=DynSK.cc -Wbuse_quotes -C${DESTINATION_DIR} ${FILENAME}.idl
        MAIN_DEPENDENCY ${SOURCE_DIR}/${FILENAME}.idl
        WORKING_DIRECTORY ${SOURCE_DIR}
    )

    # Clean generated files.
    set_property(
        DIRECTORY APPEND PROPERTY
        ADDITIONAL_MAKE_CLEAN_FILES
        ${${IDL_CC}}
        ${${IDL_HH}})

endmacro()


# OMNIORB4_IDL_TO_CPP FROM FILENAMES
# --------------------------------------
#
# IDL_SOURCE_DIR : path part of IDL files location
# IDL_DESTINATION_DIR : where will be stored the generated C++ files
# IDL_CC : a variable to store the names of the generated .cc files
# IDL_HH : a variable to store the names of the generated header files
# ARGN : IDL filenames without the path part
#
macro(OMNIORB4_IDL_TO_CPP IDL_SOURCE_DIR IDL_DESTINATION_DIR IDL_CC IDL_HH)

    if(NOT EXISTS "${IDL_DESTINATION_DIR}")
        file(MAKE_DIRECTORY "${IDL_DESTINATION_DIR}")
    endif()
    set(${IDL_CC} "")
    set(${IDL_HH} "")
    foreach(_idl_file ${ARGN})
        GET_FILENAME_COMPONENT(_filename ${_idl_file} NAME_WE)
        OMNIORB4_OMNIIDL_BCXX(${IDL_SOURCE_DIR} ${_filename} ${IDL_DESTINATION_DIR} _idl_cc _idl_hh)
        set(${IDL_CC} ${${IDL_CC}} ${_idl_cc})
        set(${IDL_HH} ${${IDL_HH}} ${_idl_hh})
    endforeach()

endmacro()
