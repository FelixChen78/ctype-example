#include <stdio.h>
#include "c_file.h"
// 1.) Run in command line to create so file: cc -fPIC -shared -o fileName.so fileName.c
int square(int num) {
    return num * num;
}

int factorial(int num) {
    if (num == 1) {
        return num;
    }
    else {
        return num * factorial(num - 1);
    }
}

double slope(int x1, int x2, int y1, int y2) {
    return ((double)(y2 - y1) / (double)(x2 - x1));
}

double probability(int target, int total) {
    return (double) target / (double) total;
    // return target / total;
}

double printDb(double num) {
    return num;
}

//driver code
int main () {
    printf("%d \n", square(10));
    printf("%d \n", factorial(5));
    printf("%f \n", slope(3,4,1,5));
    printf("%f \n", slope(1,4,1,5));
    printf("%f \n", probability(5,10));
    printf("%f", printDb(3.0));
    return 0;
}


