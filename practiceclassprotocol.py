from protocol import protocol
protocol_http = protocol("HTTP", 80, "Hypertext Transfer Protocol")
print("The protocol is : ", protocol_http.name,"The port is : ", protocol_http.number, "The description iis : " , protocol_http.description)
