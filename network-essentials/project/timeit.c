//===================================================== file = timeit.c =====
//=  Program to time program execution using standard timers                =
//===========================================================================
//=  Notes:                                                                 =
//=    1) This program conditionally compiles for Windows and UNIX.         =
//=       Set the initial #define to WIN or UNIX as appropriate.            =
//=    2) Input is prompted from user (to enter their name)                 =
//=    3) Output is to stdout                                               =
//=    4) The accuracy of this program is dependent on the platform.        =
//=       but is approximately 1 millisecond.                               =
//=    5) The timeb structure in ftime.h keeps track of the number of       =
//=       seconds and milliseconds since January 1, 1970.                   =
//=    6) The timeb structure is supported in UNIX and Windows systems,     =
//=       but is not ANSI C.  The ANSI C way (but, not supported on         =
//=       UNIX!) is to use clock() and the clock_t type in time.h           =
//=-------------------------------------------------------------------------=
//= Example execution:                                                      =
//=                                                                         =
//=  ----------------------------------------------- timeit.c -----         =
//=    Enter your full name =====> Ken C.                                   =
//=    Your name is Ken C. and it took 1.966 seconds to execute             =
//=  ---------------------------------------------------------------        =
//=-------------------------------------------------------------------------=
//=  Build: gcc timeit.c, bcc32 timeit.c, cl timeit.c                       =
//=-------------------------------------------------------------------------=
//=  Execute: timeit                                                        =
//=-------------------------------------------------------------------------=
//=  Author: Ken Christensen                                                =
//=          University of South Florida                                    =
//=          WWW: http://www.csee.usf.edu/~christen                         =
//=          Email: christen@csee.usf.edu                                   =
//=          Chi-ming Chao                                                  =
//=          http://www.csee.usf.edu/~cchao                                 =
//=          E-mail: cchao@csee.usf.edu                                     =
//=-------------------------------------------------------------------------=
//=  History: KJC (03/02/99) - Genesis                                      =
//=           CMC (04/01/99) - Made it portable to UNIX system              =
//=           KJC (02/13/14) - Minor clean-up                               =
//===========================================================================
#define  UNIX                // WIN for Windows and UNIX for Unix

//----- Include files -------------------------------------------------------
#include <stdio.h>          // Needed for printf()
#ifdef WIN
#include <sys\timeb.h>      // Needed for ftime() and timeb structure
#endif
#ifdef UNIX
#include <sys/timeb.h>      // Needed for ftime() and timeb structure
#endif

//===========================================================================
//=  Main program                                                           =
//===========================================================================
void main(void)
{
  char         name[255];   // String for name
  struct timeb start, stop; // Start and stop times structures
  double       elapsed;     // Elapsed time in seconds

  // Output a banner
  printf("----------------------------------------------- timeit.c -----\n");

  // Start timing
  ftime(&start);

  // Prompt for user input while timing
  printf("  Enter your full name =====> ");
  gets(name);
  printf("\n");

  // Stop timing and compute elapsed time
  ftime(&stop);
  elapsed=((double) stop.time + ((double) stop.millitm * 0.001)) -
          ((double) start.time + ((double) start.millitm * 0.001));

  // Output name and elapsed time
  printf("  Your name is %s and it took %f seconds to execute \n",
    name, elapsed);
  printf("---------------------------------------------------------------\n");
}