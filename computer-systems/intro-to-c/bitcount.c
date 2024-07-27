#include <assert.h>
#include <stdio.h>

int bitcount(unsigned int num) {
    int count = 0;
    for (; num > 0; num >>= 1) {
        if (num & 0b1) count++;
    }

    return count;
}

int bitcount2(unsigned int num) {
    int count = 0;
    for (; num > 0; num >>= 1) {
        count += num & 0b1;
    }

    return count;
}

// Idea: x &= x-1 is a faster way of deleting the low-order bit
int bitcount3(unsigned int num) {
    int count = 0;
    for (; num > 0; num &= num - 1) {
        count += num ^ (num - 1);
    }

    return count;
}
// It works because
//   0b111    0b1000
// & 0b110  & 0b0111
// = 0b110  = 0b0000

int main() {
    assert(bitcount3(0) == 0); // 0b0
    assert(bitcount3(1) == 1); // 0b1
    assert(bitcount3(3) == 2); // 0b11
    assert(bitcount3(8) == 1); // 0b100

    assert(bitcount3(0xffffffff) == 32);

    printf("passed!\n");

    return 0;
}