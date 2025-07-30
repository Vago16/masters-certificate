#include "weblite.c"        //for ease of readability, import code instead of putting it all in one file

#define  UDP_1_PORT          1100
#define  UDP_2_PORT          1200
#define  UDP_3_PORT          1300
#define  KNOCK_TIMING        5        // max amount of seconds allowed between each knock
#define  IP_ADDR    "127.0.0.1"       // IP address as defined in project specifications

int wait_for_knock();      //prototype for knock function

int main() {
    printf("Waiting for knock sequence...\n");
    run_server();
    return 0;
}

int wait_for_knock() {      //reusing some code from xServer.c
    int                  server_s;        // Server socket descriptor
    struct sockaddr_in   server_addr;     // Server Internet address
    struct sockaddr_in   client_addr;     // Client Internet address
    int                  addr_len;        // Internet address length
    char                 out_buf[4096];   // Output buffer for data
    char                 in_buf[4096];    // Input buffer for data
    int                  retcode;         // Return code

    int knock_seq[3] = {UDP_1_PORT, UDP_2_PORT, UDP_3_PORT};     //array of ports to knock   
    int curr_knock = 0;     //for use in socket creation loop
    time_t last_knock_time = 0;

    while (curr_knock < 3) {
        
    }
}