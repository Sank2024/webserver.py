# import socket module
from socket import *
# In order to terminate the program
import sys



def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  
  #Prepare a server socket
  serverSocket.bind(("", port))
  
  #Fill in start
  serverSocket.listen(1)
  #Fill in end

  while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start -are you accepting connections?     #Fill in end
    
    try:
      message = connectionSocket.recv(1024).decode()
      filename = message.split()[1]

      # Open the requested file
      with open(filename[1:], 'rb') as f:
        content = f.read()

      # Create the HTTP response headers
      headers = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nServer: MyWebServer\r\nConnection: close\r\n\r\n"

      # Send the headers followed by the file content
      connectionSocket.sendall(headers.encode() + content)

      # Close the connection socket
      connectionSocket.close()

    except FileNotFoundError:
      # File not found, send a 404 response
      not_found_response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nServer: MyWebServer\r\nConnection: close\r\n\r\n404 Not Found\r\n"
      connectionSocket.sendall(not_found_response.encode())
      connectionSocket.close()

    except Exception as e:
      print("Error:", e)
      connectionSocket.close()

  #Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
  #serverSocket.close()
  #sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)
