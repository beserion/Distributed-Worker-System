.PHONY: all clean

CC = cc
CFLAGS = -O3 -march=native -pipe
SRC = src/heavy_compute.c
BIN_DIR = bin

all:
	mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) $(SRC) -o $(BIN_DIR)/heavy_compute

clean:
	rm -rf bin
