from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
    <title>TOP SOFTWARE COMAPANIES</title>
</head>
<body>
     <div aling="centre">
    <h2>TOP 5 SOFTWARE COMPANIES IN INDIA</h2>
    <table border="5">
        <tr>
            <th>RANK</th>
            <th>COMPANY NAME</th>
            <th>COUNTRY</th>
            <th>SALES</th>
            <th>MARKET VALUE</th>
            
        </tr>
       
        <tr>
            <td>01</td>
            <td>TCS.</td>
            <td>INDIA</td>
            <td>164177</td>
            <td>$2.6</td>

        </tr>
        <tr>
           <td>02</td>
            <td>INFOSYS</td>
            <td>INDIA</td>
            <td>100472</td>
            <td>$1.6</td>
        </tr>
        <tr>
            <td>03</td>
            <td>WIPRO</td>
            <td>INDIA</td>
            <td>61935</td>
            <td>$2.1</td>
        </tr>
        <tr>
            <td>04</td>
            <td>HCL</td>
            <td>INDIA</td>
            <td>75379</td>
            <td>$367.3</td>
        </tr>
        <tr>
            <td>05</td>
            <td>TECH MAHINDRA</td>
            <td>INDIA</td>
            <td>37855</td>
            <td>$414.3</td>
        </tr>
       
    </table>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

