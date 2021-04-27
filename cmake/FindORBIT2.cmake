#
# Find the ORBIT2 libraries and include dir
#
find_package(PkgConfig REQUIRED)
pkg_search_module(ORBIT2 REQUIRED ORBit-2.0>=2.14.19)

find_program(ORBIT2_IDL_COMPILER
    NAMES orbit-idl-2
    PATHS ${ORBIT2_PREFIX}/bin
    DOC "What is the path where orbit-idl-2 (the idl compiler) can be found")

# ORBIT2_IDL_2 SOURCE_DIR FILENAME DESTINATION_DIR
# -------------------------------------------------------------
#
# Generate stubs from an IDL file.
# An include directory can also be specified.
#
# SOURCE_DIR : path part of IDL file location
# FILENAME : IDL filename without the extension
# DESTINATION_DIR : where will be stored the generated C files
# IDL_C : a variable to store the names of the generated .c files
# IDL_H : a variable to store the name of the generated header file
#
macro(ORBIT2_IDL_2 SOURCE_DIR FILENAME DESTINATION_DIR IDL_C IDL_H)

    set(${IDL_C} "${DESTINATION_DIR}/${FILENAME}-common.c" "${DESTINATION_DIR}/${FILENAME}-stubs.c")
    set(${IDL_H} "${DESTINATION_DIR}/${FILENAME}.h")
    message(STATUS "${FILENAME}-common.c ${FILENAME}-stubs.c ${FILENAME}.h: ${FILENAME}.idl")
    add_custom_command(
        OUTPUT ${${IDL_C}} ${${IDL_H}}
        COMMAND "${ORBIT2_IDL_COMPILER}" > /dev/null
        ARGS --onlytop --noskels "${SOURCE_DIR}/${FILENAME}.idl"
        MAIN_DEPENDENCY "${SOURCE_DIR}/${FILENAME}.idl"
        WORKING_DIRECTORY "${DESTINATION_DIR}"
    )

    # Clean generated files.
    set_property(
        DIRECTORY APPEND PROPERTY
        ADDITIONAL_MAKE_CLEAN_FILES
        ${${IDL_C}}
        ${${IDL_H}})

endmacro()


# ORBIT2_IDL_TO_C FROM FILENAMES
# --------------------------------------
#
# IDL_SOURCE_DIR : path part of IDL files location
# IDL_DESTINATION_DIR : where will be stored the generated C files
# IDL_C : a variable to store the names of the generated .c files
# IDL_H : a variable to store the names of the generated header files
# ARGN : IDL filenames without the path part
#
macro(ORBIT2_IDL_TO_C IDL_SOURCE_DIR IDL_DESTINATION_DIR IDL_C IDL_H)

    if(NOT EXISTS "${IDL_DESTINATION_DIR}")
        file(MAKE_DIRECTORY "${IDL_DESTINATION_DIR}")
    endif()
    set(${IDL_C} "")
    set(${IDL_H} "")
    foreach(_idl_file ${ARGN})
        GET_FILENAME_COMPONENT(_filename ${_idl_file} NAME_WE)
        ORBIT2_IDL_2(${IDL_SOURCE_DIR} ${_filename} ${IDL_DESTINATION_DIR} _idl_c _idl_h)
        set(${IDL_C} ${${IDL_C}} ${_idl_c})
        set(${IDL_H} ${${IDL_H}} ${_idl_h})
    endforeach()

endmacro()
