import socket

# Common proxy ports to check
ports = [7890, 1080, 2080, 80, 8888, 9999]
results = []

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect(('127.0.0.1', port))
        results.append(f"✅ Port {port} is OPEN (proxy may be running)")
        s.close()
    except Exception as e:
        results.append(f"❌ Port {port} is CLOSED: {e}")

print("\n".join(results))
