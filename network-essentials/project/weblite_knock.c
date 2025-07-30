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

int wait_for_knock() {      //reusing code from xServer.c
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
        //create socket, taken from xServer.c
        server_s = socket(AF_INET, SOCK_DGRAM, 0);      
        if (server_s < 0) {
                printf("*** ERROR - socket() failed \n");
                exit(-1);
            }
        //fill in socket's address information
        memset(&server_addr, 0, sizeof(server_addr));       //initialize struct to 0
        server_addr.sin_family = AF_INET;                 // Address family to use
        server_addr.sin_port = htons(knock_seq[curr_knock]);           // Port number to use
        server_addr.sin_addr.s_addr = htonl(INADDR_ANY);  // Listen on any IP address
        retcode = bind(server_s, (struct sockaddr *)&server_addr,
        sizeof(server_addr));
        if (retcode < 0) {
            printf("*** ERROR - bind() failed \n");
            exit(-1);
            }

        // Wait to receive a message from client
        printf("Waiting for recvfrom() to complete... \n");
        addr_len = sizeof(client_addr);
        retcode = recvfrom(server_s, in_buf, sizeof(in_buf), 0,
            (struct sockaddr *)&client_addr, &addr_len);
        if (retcode < 0) {
            printf("*** ERROR - recvfrom() failed \n");
            close(server_s);       //deallocate memory location
            exit(-1);
        }

        //checking elapsed time
        time_t curr_time = time(NULL);      //initialize current time
    }
}