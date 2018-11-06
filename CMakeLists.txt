cmake_minimum_required(VERSION 3.5)

find_program(IDL_PROGRAM omniidl)
find_program(GIT_PROGRAM git)

set(program_name fred-idl)
project(${program_name} NONE)

macro(set_default variable_name variable_value)
    if(NOT ${variable_name})
        set(${variable_name} ${variable_value})
    endif()
endmacro()

set_default(TARBALL_FILE_NAME fred-idl)
set_default(PYTHON python)

if(NOT VERSION)
    execute_process(COMMAND "git" "describe" "--tags"
                    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
                    OUTPUT_VARIABLE RAWVERSION)
    string(REGEX REPLACE "-.*\n" "" VERSION ${RAWVERSION})
endif()

function(compile_idl_files)
    message(STATUS "Compiling idl...")
    if(NOT IDL_PROGRAM)
        message(FATAL_ERROR "omniidl not found")
    endif()
    execute_process(
        COMMAND mkdir fred_idl
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR})
    foreach(idl_name ${ARGN})
        execute_process(
            COMMAND ${IDL_PROGRAM} -bpython -Wbmodules=fred_idl -Wbstubs=fred_idl._stubs ${CMAKE_SOURCE_DIR}/idl/${idl_name}.idl
            WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/fred_idl
            OUTPUT_VARIABLE OMNIIDL_MESSAGE${idl_name})
        message(STATUS ${OMNIIDL_MESSAGE}${idl_name})
    endforeach()
    execute_process(
        COMMAND find fred_idl -name \*.py -exec ${PYTHON} -mcompileall {} \;
        WORKING_DIRECTORY ${CMAKE_BINARY_DIR})
    message(STATUS "...done")
endfunction()

compile_idl_files(
    Accounting
    AdminContactVerification
    Admin
    AdministrativeBlocking
    AutomaticKeysetManagement
    Buffer
    ccReg
    ContactVerification
    _dataTypes
    DateTime
    DomainBrowser
    EPP
    FileManager
    Filters
    IsoDate
    IsoDateTime
    Logger
    Mailer
    Messages
    MojeID
    Notification
    NullableIsoDate
    NullableIsoDateTime
    NullableTypes
    PublicRequest
    RecordStatement
    Registry
    TechCheck
    Whois2
    Whois
    ZoneGenerator
    Zone)

execute_process(COMMAND ${PYTHON} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(True, False, '${CMAKE_INSTALL_PREFIX}'))"
    OUTPUT_VARIABLE PKGPYTHONDIR)
string(REGEX REPLACE "\n" "" PKGPYTHONDIR "${PKGPYTHONDIR}")

install(DIRECTORY ${CMAKE_BINARY_DIR}/fred_idl/ DESTINATION "${PKGPYTHONDIR}")
install(DIRECTORY ${CMAKE_BINARY_DIR}/idl/ DESTINATION "${CMAKE_INSTALL_PREFIX}/share/idl/fred/" FILES_MATCHING PATTERN "*.idl")
add_custom_target(uninstall_python_idl COMMAND rm -rf "${PKGPYTHONDIR}/fred_idl")
add_custom_target(uninstall COMMAND rm -rf "${CMAKE_INSTALL_PREFIX}/share/idl/fred/" DEPENDS uninstall_python_idl)

if(EXISTS ${CMAKE_SOURCE_DIR}/.git AND GIT_PROGRAM)
    if(NOT TARGET dist)
        add_custom_target(dist
            COMMAND ${GIT_PROGRAM} archive --format=tar.gz --prefix=${TARBALL_FILE_NAME}/ HEAD -o ${CMAKE_BINARY_DIR}/${TARBALL_FILE_NAME}.tar.gz
            WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
    endif()

    if(NOT TARGET distcheck)
        set(DISTCHECK_BUILD_DIR "_build")
        set(DISTCHECK_INSTALL_DIR "_inst")
        if(${CMAKE_GENERATOR} STREQUAL "Ninja")
            set(DISTCHECK_BUILD_CMD "ninja")
            set(DISTCHECK_MAKEFLAGS "")
        else()
            set(DISTCHECK_BUILD_CMD "make")
            execute_process(COMMAND "grep" "-c" "model name" "/proc/cpuinfo"
                WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
                OUTPUT_VARIABLE NOCPUS)
            string(REGEX REPLACE "\n" "" NOCPUS ${NOCPUS})
            set(DISTCHECK_MAKEFLAGS "MAKEFLAGS=-j${NOCPUS}")
        endif()
        add_custom_target(distcheck
            COMMAND
            rm -rf ${DISTCHECK_BUILD_DIR} ${DISTCHECK_INSTALL_DIR} ${TARBALL_FILE_NAME}
            && mkdir ${DISTCHECK_BUILD_DIR} ${DISTCHECK_INSTALL_DIR}
            && (tar xzf ${TARBALL_FILE_NAME}.tar.gz
                || (echo 'Error: failed to unpack the archive' 2>&1\; false))
            && (cd ${DISTCHECK_BUILD_DIR}
                && (cmake -G${CMAKE_GENERATOR} -DCMAKE_INSTALL_PREFIX=../${DISTCHECK_INSTALL_DIR} ../${TARBALL_FILE_NAME}
                    || (echo 'Error: failed to configure the archive' 2>&1\; false))
                && (${DISTCHECK_BUILD_CMD} install
                    || (echo 'Error: the install target failed' 2>&1\; false))
                && (${DISTCHECK_BUILD_CMD} uninstall
                    || (echo 'Error: the uninstall target failed' 2>&1\; false))
                && (${DISTCHECK_BUILD_CMD} clean
                    || (echo 'Error: the clean target failed' 2>&1\; false)))
            && rm -rf ${DISTCHECK_BUILD_DIR} ${DISTCHECK_INSTALL_DIR} ${TARBALL_FILE_NAME}
            && echo 'PASS: ' ${TARBALL_FILE_NAME}.tar.gz 'is ready for distribution.'
            WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
            COMMENT "Checking the distribution archive...")
        add_dependencies(distcheck dist)
    endif()
else()
    message(STATUS "no git -- not including dist and distcheck targets")
endif()
