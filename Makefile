all: libcmult.so

libcmult.so: cmult.o
	gcc cmult.o -shared -o libcmult.so

cmult.o: cmult.c
	gcc -c cmult.c