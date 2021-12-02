# Importing the necessary modules
import sys

from ipFileValid import ip_file_valid
from ipAdressValid import ip_addr_valid
from ipReach import ip_reach
from sshConnection import ssh_connection
from createThreads import create_threads

# Saving the list of IP addresses in ip.txt to a variable
ip_list = ip_file_valid()

# Verifying the validity of each IP address in the list
try:
    ip_addr_valid(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

# Verifying the reachability of each IP address in the list
try:
    ip_reach(ip_list)

except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

# Calling threads creation function for one or multiple SSH connections
create_threads(ip_list, ssh_connection)

# End of program
