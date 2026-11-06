cmake_minimum_required(VERSION 3.16)

project(vezba03_calculators VERSION 1.0 LANGUAGES CXX)

# Enables editor tools (e.g. clangd) that read build/compile_commands.json.
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# Do not add "solutions" here: both source files intentionally contain bugs.
add_executable(simple_calculator
    SimpleCalculator/calculator02buggy.cpp
    SimpleCalculator/std_lib_facilities.h
)

add_executable(advanced_calculator
    AdvancedCalculator/calculator08buggy.cpp
    AdvancedCalculator/std_lib_facilities.h
)

foreach(target IN ITEMS simple_calculator advanced_calculator)
    target_compile_features(${target} PRIVATE cxx_std_17)
    set_target_properties(${target} PROPERTIES
        CXX_STANDARD_REQUIRED YES
        CXX_EXTENSIONS NO
    )
    if(MSVC)
        target_compile_options(${target} PRIVATE /W3)
    else()
        target_compile_options(${target} PRIVATE -Wall -Wextra -Wpedantic)
    endif()
endforeach()
