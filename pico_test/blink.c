#include "pico/stdlib.h"

int main() {
    // Initialize standard library
    stdio_init_all();
    
    // Initialize GPIO pin for LED (pin 25 is built-in LED)
    gpio_init(25);
    gpio_set_dir(25, GPIO_OUT);
    
    // Blink forever
    while (true) {
        gpio_put(25, 1);  // Turn LED on
        sleep_ms(500);    // Wait 500ms
        gpio_put(25, 0);  // Turn LED off
        sleep_ms(500);    // Wait 500ms
    }
    
    return 0;
}