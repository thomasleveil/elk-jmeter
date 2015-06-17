#!/usr/bin/python -u

# telnet program example
import socket, select, string, sys, os
 
#main function
if __name__ == "__main__":
     
    if(len(sys.argv) < 5) :
        print 'Usage : %s hostname port interval metrics' % os.path.basename(sys.argv[0])
        sys.exit(1)
    
    host = sys.argv[1]
    port = int(sys.argv[2])
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit(2)

    s.send("interval:%s\n" % sys.argv[3])
    s.send("%s\n" % sys.argv[4])

    try:
        while 1:
            socket_list = [s]
             
            # Get the list sockets which are readable
            read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [], 1)
             
            for sock in read_sockets:
                #incoming message from remote server
                if sock == s:
                    data = sock.recv(4096)
                    if not data :
                        print 'Connection closed'
                        sys.exit()
                    else :
                        #print data
                        sys.stdout.write(data)
    except KeyboardInterrupt:
        pass