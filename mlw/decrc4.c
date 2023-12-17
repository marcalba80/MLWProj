#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(unsigned char *s, int i, int j) {
    unsigned char temp = s[i];
    s[i] = s[j];
    s[j] = temp;
}

void rc4_crypt(unsigned char *key, unsigned char *data, size_t data_len) {
    unsigned char s[256];
    int i, j = 0, k;
    size_t keylen = strlen(key);

    for (i = 0; i < 256; i++) {
        s[i] = i;
    }

    for (i = 0; i < 256; i++) {
        j = (j + s[i] + key[i % keylen]) % 256;
        swap(s, i, j);
    }

    i = j = 0;
    for (size_t n = 0; n < data_len; n++) {
        i = (i + 1) % 256;
        j = (j + s[i]) % 256;
        swap(s, i, j);
        k = s[(s[i] + s[j]) % 256];
        data[n] ^= k;
    }
}

int main() {
    unsigned char key[] = "SecretKey"; // Replace with your key
    unsigned char data[] = {0x12, 0x34, 0x56, 0x78, 0x90}; // Replace with your encrypted data
    size_t data_len = sizeof(data) / sizeof(data[0]);

    printf("Encrypted data: ");
    for (size_t i = 0; i < data_len; i++) {
        printf("%02X ", data[i]);
    }
    printf("\n");

    rc4_crypt(key, data, data_len);

    printf("Decrypted data: ");
    for (size_t i = 0; i < data_len; i++) {
        printf("%c", data[i]);
    }
    printf("\n");

    return 0;
}