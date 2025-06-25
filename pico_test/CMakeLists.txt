cmake_minimum_required(VERSION 3.13)

# Import pico-sdk
include(pico_sdk_import.cmake)

project(blink_test)

# Initialize the SDK
pico_sdk_init()

# Create executable
add_executable(blink
    blink.c
)

# Link libraries
target_link_libraries(blink pico_stdlib)

# Create map/bin/hex/uf2 files
pico_add_extra_outputs(blink)