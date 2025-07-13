//Combination of tcpServer.c and udpServer.c, so keeping revision history and credit

//==================================================== file = tcpServer.c =====
//=  A message "server" program to demonstrate sockets programming            =
//=============================================================================
//=  Notes:                                                                   =
//=    1) This program conditionally compiles for Winsock and BSD sockets.    =
//=       Set the initial #define to WIN or BSD as appropriate.               =
//=    2) This program serves a message to program tcpClient running on       =
//=       another host.                                                       =
//=    3) The steps #'s correspond to lecture topics.                         =
//=---------------------------------------------------------------------------=
//=  Example execution: (tcpServer and tcpClient running on host 127.0.0.1)   =
//=    Waiting for accept() to complete...                                    =
//=    Accept completed (IP address of client = 127.0.0.1  port = 49981)      =
//=    Received from client: This is a reply message from CLIENT to SERVER    =
//=---------------------------------------------------------------------------=
//=  Build:                                                                   =
//=    Windows (WIN):  Borland: bcc32 tcpServer.c                             =
//=                    MinGW: gcc tcpServer.c -lws2_32 -o tcpServer           =
//=                    Visual C: cl tcpServer.c wsock32.lib                   =
//=    Unix/Mac (BSD): gcc tcpServer.c -lnsl -o tcpServer                     =
//=---------------------------------------------------------------------------=
//=  Execute: tcpServer                                                       =
//=---------------------------------------------------------------------------=
//=  Author: Ken Christensen                                                  =
//=          University of South Florida                                      =
//=          WWW: http://www.csee.usf.edu/~christen                           =
//=          Email: christen@csee.usf.edu                                     =
//=---------------------------------------------------------------------------=
//=  History:  KJC (08/02/08) - Genesis (from server.c)                       =
//=            KJC (09/07/09) - Minor clean-up                                =
//=            KJC (09/22/13) - Minor clean-up to fix warnings                =
//=            KJC (09/14/17) - Updated build instructions                    =
//=============================================================================
//          &
//==================================================== file = udpServer.c =====
//=  A message "server" program to demonstrate sockets programming            =
//=============================================================================
//=  Notes:                                                                   =
//=    1) This program conditionally compiles for Winsock and BSD sockets.    =
//=       Set the initial #define to WIN or BSD as appropriate.               =
//=    2) This program serves a message to program udpClient running on       =
//=       another host.                                                       =
//=    3) The steps #'s correspond to lecture topics.                         =
//=---------------------------------------------------------------------------=
//=  Example execution: (udpServer and udpClient running on host 127.0.0.1)   =
//=    Waiting for recvfrom() to complete...                                  =
//=    IP address of client = 127.0.0.1  port = 55476)                        =
//=    Received from client: Test message from CLIENT to SERVER               =
//=---------------------------------------------------------------------------=
//=  Build:                                                                   =
//=    Windows (WIN):  Borland: bcc32 udpServer.c                             =
//=                    MinGW: gcc udpServer.c -lws2_32 -o udpServer           =
//=                    Visual C: cl udpServer.c wsock32.lib                   =
//=    Unix/Mac (BSD): gcc ucpServer.c -lnsl -o ucpServer                     =
//=---------------------------------------------------------------------------=
//=  Execute: udpServer                                                       =
//=---------------------------------------------------------------------------=
//=  Author: Ken Christensen                                                  =
//=          University of South Florida                                      =
//=          WWW: http://www.csee.usf.edu/~christen                           =
//=          Email: christen@csee.usf.edu                                     =
//=---------------------------------------------------------------------------=
//=  History:  KJC (08/02/08) - Genesis (from server1.c)                      =
//=            KJC (09/07/09) - Minor clean-up                                =
//=            KJC (09/22/13) - Minor clean-up to fix warnings                =
//=            KJC (09/14/17) - Updated build instructions                    =
//=============================================================================

#define  BSD                // WIN for Winsock and BSD for BSD sockets

//----- Include files ---------------------------------------------------------
#include <stdio.h>          // Needed for printf()
#include <string.h>         // Needed for memcpy() and strcpy()
#include <stdlib.h>         // Needed for exit()
#ifdef WIN
  #include <windows.h>      // Needed for all Winsock stuff
#endif
#ifdef BSD
  #include <sys/types.h>    // Needed for sockets stuff
  #include <netinet/in.h>   // Needed for sockets stuff
  #include <sys/socket.h>   // Needed for sockets stuff
  #include <arpa/inet.h>    // Needed for sockets stuff
  #include <fcntl.h>        // Needed for sockets stuff
  #include <netdb.h>        // Needed for sockets stuff
  #include <unistd.h>       // Needed for sockets stuff(specifically close())
#endif

//----- Defines ---------------------------------------------------------------
#define  TCP_PORT   1050    // Arbitrary port number for the TCP server
#define  UDP_PORT   1111    // Arbitrary port number for the UDP server

//----- Prototype -------------------------------------------------------------
int udpSocket();

//===== Main program ==========================================================
int main()
{
//do UDP first
udpSocket();

//start TCP
#ifdef WIN
  WORD wVersionRequested = MAKEWORD(1,1);       // Stuff for WSA functions
  WSADATA wsaData;                              // Stuff for WSA functions
#endif
  int                  welcome_s;       // Welcome socket descriptor
  struct sockaddr_in   server_addr;     // Server Internet address
  int                  connect_s;       // Connection socket descriptor
  struct sockaddr_in   client_addr;     // Client Internet address
  struct in_addr       client_ip_addr;  // Client IP address
  int                  addr_len;        // Internet address length
  char                 out_buf[4096];   // Output buffer for data
  char                 in_buf[4096];    // Input buffer for data
  int                  retcode;         // Return code

#ifdef WIN
  // This stuff initializes winsock
  WSAStartup(wVersionRequested, &wsaData);
#endif

  // >>> Step #1 <<<
  // Create a welcome socket
  //   - AF_INET is Address Family Internet and SOCK_STREAM is streams
  welcome_s = socket(AF_INET, SOCK_STREAM, 0);
  if (welcome_s < 0)
  {
    printf("*** ERROR - socket() failed \n");
    exit(-1);
  }

  // >>> Step #2 <<<
  // Fill-in server (my) address information and bind the welcome socket
  server_addr.sin_family = AF_INET;                 // Address family to use
  server_addr.sin_port = htons(TCP_PORT);           // Port number to use
  server_addr.sin_addr.s_addr = htonl(INADDR_ANY);  // Listen on any IP address
  retcode = bind(welcome_s, (struct sockaddr *)&server_addr,
    sizeof(server_addr));
  if (retcode < 0)
  {
    printf("*** ERROR - bind() failed \n");
    exit(-1);
  }

  // >>> Step #3 <<<
  // Listen on welcome socket for a connection
  listen(welcome_s, 1);

  // >>> Step #4 <<<
  // Accept a connection.  The accept() will block and then return with
  // connect_s assigned and client_addr filled-in.
  printf("Waiting for accept() to complete... \n");
  addr_len = sizeof(client_addr);
  connect_s = accept(welcome_s, (struct sockaddr *)&client_addr, &addr_len);
  if (connect_s < 0)
  {
    printf("*** ERROR - accept() failed \n");
    exit(-1);
  }

  // Copy the four-byte client IP address into an IP address structure
  memcpy(&client_ip_addr, &client_addr.sin_addr.s_addr, 4);

  // Print an informational message that accept completed
  printf("Accept Completed(IP address of client = %s  port = %d) \n",
    inet_ntoa(client_ip_addr), ntohs(client_addr.sin_port));

  // >>> Step #5 <<<
  // Send to the client using the connect socket
  strcpy(out_buf, "This is a message from SERVER to CLIENT");
  retcode = send(connect_s, out_buf, (strlen(out_buf) + 1), 0);
  if (retcode < 0)
  {
    printf("*** ERROR - send() failed \n");
    exit(-1);
  }

  // >>> Step #6 <<<
  // Receive from the client using the connect socket
  retcode = recv(connect_s, in_buf, sizeof(in_buf), 0);
  if (retcode < 0)
  {
    printf("*** ERROR - recv() failed \n");
    exit(-1);
  }
  printf("Received from client: %s \n", in_buf);

  // >>> Step #7 <<<
  // Close the welcome and connect sockets
#ifdef WIN
  retcode = closesocket(welcome_s);
  if (retcode < 0)
  {
    printf("*** ERROR - closesocket() failed \n");
    exit(-1);
  }
  retcode = closesocket(connect_s);
  if (retcode < 0)
  {
    printf("*** ERROR - closesocket() failed \n");
    exit(-1);
  }
#endif
#ifdef BSD
  retcode = close(welcome_s);
  if (retcode < 0)
  {
    printf("*** ERROR - close() failed \n");
    exit(-1);
  }
  retcode = close(connect_s);
  if (retcode < 0)
  {
    printf("*** ERROR - close() failed \n");
    exit(-1);
  }
#endif

#ifdef WIN
  // Clean-up winsock
  WSACleanup();
#endif

  // Return zero and terminate
  return(0);
}


//===== Main program  for udp socket=========================================================
int udpSocket()
{
#ifdef WIN
  WORD wVersionRequested = MAKEWORD(1,1);       // Stuff for WSA functions
  WSADATA wsaData;                              // Stuff for WSA functions
#endif
  int                  server_s;        // Server socket descriptor
  struct sockaddr_in   server_addr;     // Server Internet address
  struct sockaddr_in   client_addr;     // Client Internet address
  struct in_addr       client_ip_addr;  // Client IP address
  int                  addr_len;        // Internet address length
  char                 out_buf[4096];   // Output buffer for data
  char                 in_buf[4096];    // Input buffer for data
  int                  retcode;         // Return code

#ifdef WIN
  // This stuff initializes winsock
  WSAStartup(wVersionRequested, &wsaData);
#endif

  // >>> Step #1 <<<
  // Create a socket
  //   - AF_INET is Address Family Internet and SOCK_DGRAM is datagram
  server_s = socket(AF_INET, SOCK_DGRAM, 0);
  if (server_s < 0)
  {
    printf("*** ERROR - socket() failed \n");
    exit(-1);
  }

  // >>> Step #2 <<<
  // Fill-in my socket's address information
  server_addr.sin_family = AF_INET;                 // Address family to use
  server_addr.sin_port = htons(UDP_PORT);           // Port number to use
  server_addr.sin_addr.s_addr = htonl(INADDR_ANY);  // Listen on any IP address
  retcode = bind(server_s, (struct sockaddr *)&server_addr,
    sizeof(server_addr));
  if (retcode < 0)
  {
    printf("*** ERROR - bind() failed \n");
    exit(-1);
  }

  // >>> Step #3 <<<
  // Wait to receive a message from client
  printf("Waiting for recvfrom() to complete... \n");
  addr_len = sizeof(client_addr);
  retcode = recvfrom(server_s, in_buf, sizeof(in_buf), 0,
    (struct sockaddr *)&client_addr, &addr_len);
  if (retcode < 0)
  {
    printf("*** ERROR - recvfrom() failed \n");
    exit(-1);
  }

  // Copy the four-byte client IP address into an IP address structure
  memcpy(&client_ip_addr, &client_addr.sin_addr.s_addr, 4);

  printf("Received the knock message!!!\n");

  // Print an informational message of IP address and port of the client
  //printf("IP address of client = %s  port = %d) \n", inet_ntoa(client_ip_addr),
    //ntohs(client_addr.sin_port));

  // Output the received message
  //printf("Received from client: %s \n", in_buf);

  // >>> Step #4 <<<
  // Send to the client using the server socket
  strcpy(out_buf, "This is a reply message from SERVER to CLIENT");
  retcode = sendto(server_s, out_buf, (strlen(out_buf) + 1), 0,
    (struct sockaddr *)&client_addr, sizeof(client_addr));
  if (retcode < 0)
  {
    printf("*** ERROR - sendto() failed \n");
    exit(-1);
  }

  // >>> Step #5 <<<
  // Close all open sockets
#ifdef WIN
  retcode = closesocket(server_s);
  if (retcode < 0)
  {
    printf("*** ERROR - closesocket() failed \n");
    exit(-1);
  }
#endif
#ifdef BSD
  retcode = close(server_s);
  if (retcode < 0)
  {
    printf("*** ERROR - close() failed \n");
    exit(-1);
  }
#endif

#ifdef WIN
  // This stuff cleans-up winsock
  WSACleanup();
#endif

  // Return zero and terminate
  return(0);
}