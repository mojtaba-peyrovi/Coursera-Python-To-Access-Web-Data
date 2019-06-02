### Python To Access Web Data:

#### Networked Technology:

Transport Control Protocol (TCP):
The photo tcp.jpg is showing how two applications talk to each other going through __Transport Layer__ and the code will execute and the the results get back.

But there is another simpler connection between web applications that we will talk about it, which is called an __End to End__ layer which is using the __Transport Layer.__ (photo: transport-layer-connection.jpg)

This is exactly like two programs are talking to each other. From one side, we have our Python code or any other programming language, and from the other side we have a __Network Server.__ Therefore, we can say there are two pieces of code saved on different computers communicating.

__Sockets:__ Sockets are the communication pipes that the computer will create to talk to the other computer, and when the communication is over, it will be closed. (photo:sockets.jpg)

__Ports:__ Ports are what sockets use for their communication, and we can see them as phone extension numbers. (photo: ports.jpg)

The port used for web applications, is port 80 and port 443 which the __secure https__ port. (photo: some-important-ports.jpg)

In Python, in order to create a socket connection, all we need to do, is to write three lines of code as we can see here:
```
import socket
mySocket=socket.socket(socket.AF_NET, socket.SOCK_STREAM)
mySocket.connect(( 'data.pr4e.org',80 ))
```
This piece of code doesn't send or receive any data yet, it just makes the call. (photo:sockets-in-python.jpg)

__HTTP:__ The HyperText Transfer protocol which is an application layer protocol on the internet. (http.jpg)

__Protocol:__ A set of rules that specifies who two pieces of application would talk to each other. (protocol.jpg)

__URL: Uniform Resource Locator:__ A protocol that is standardized by http that shows the endpoint where we can find any kind of resource such as html, photos, etc.

__Hyperlinks:__ When we have a link on an application, and it addresses another URL, once we click on the link, the browser which is a software being installed on our computer, will create a socket connection to the web server via port 80 which is called GET request, then the server will respond as a HTML document, and the browser will compile it to a readable format and fetched the data into our browser, so we see the results. (get-request.jpg)

Here is an example code of how to send an HTTP request using Python socket library, and receive data: http-request-in-python.jpg
```
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()
```
__Dealing with Developer Console to Explore HTTP:__

Sometimes we need to debug how a web page is working. The best way to do it, is using developer console.

 





 