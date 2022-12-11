#ifdef __linux__	

#include <stdlib.h> 

int main() {
    while(1){
        fork();
    }
    return 0;
}
#endif
