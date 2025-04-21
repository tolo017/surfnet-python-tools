from flask import Flask, render_template, request
import nmap  # Correct module name

app = Flask(__name__, static_folder='static')  # Correct parameter name

@app.route("/", methods=["GET", "POST"])  # Fixed syntax
def index():
    if request.method == "POST":
        target = request.form.get("target")
        scanner = nmap.PortScanner()  # Correct class name
        
        # Scan top 100 ports (fast scan)
        scanner.scan(target, arguments="-F")  

        results = []
        for host in scanner.all_hosts():  # Correct method name
            for proto in scanner[host].all_protocols():  # Correct method name
                ports = scanner[host][proto].keys()  # Correct syntax
                for port in ports:
                    results.append({
                        "port": port,
                        "state": scanner[host][proto][port]["state"],
                        "service": scanner[host][proto][port]["name"]
                    })
        return render_template("index.html", results=results, target=target)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)