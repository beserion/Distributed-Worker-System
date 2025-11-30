// simple heavy compute: multiply two n x n matrices and print checksum
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

double randf() {
    return (double)rand() / RAND_MAX;
}

int main(int argc, char **argv) {
    int n = 200;
    if (argc > 1) n = atoi(argv[1]);
    srand(12345);
    double *A = malloc(sizeof(double) * n * n);
    double *B = malloc(sizeof(double) * n * n);
    double *C = malloc(sizeof(double) * n * n);
    if (!A || !B || !C) {
        fprintf(stderr, "alloc_failed\n");
        return 2;
    }
    for (int i = 0; i < n * n; ++i) {
        A[i] = randf();
        B[i] = randf();
        C[i] = 0.0;
    }
    clock_t start = clock();
    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < n; ++k) {
            double rik = A[i*n + k];
            for (int j = 0; j < n; ++j) {
                C[i*n + j] += rik * B[k*n + j];
            }
        }
    }
    clock_t end = clock();
    double checksum = 0;
    for (int i = 0; i < n * n; ++i) checksum += C[i];
    double elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("n=%d checksum=%.6f time=%.3f\n", n, checksum, elapsed);
    free(A); free(B); free(C);
    return 0;
