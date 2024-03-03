from protocol import protocol,vulnerability

protocol_http = protocol("HTTP", 80, "Hypertext Transfer Protocol")
print("The protocol is : ", protocol_http.name,"The port is : ", protocol_http.number, "The description is : " , protocol_http.description)

vulnerability_http = vulnerability("Apache HTTP Server 2.4.50", "CVE 2021-42013", "Path Traversal & Remote Code Execution (RCE)")
print("The vulnerability is : ", vulnerability_http.name,"The cve number is : ", vulnerability_http.cve, "The description is : " , vulnerability_http.description)
