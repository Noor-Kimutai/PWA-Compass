"""Custom HTTP server that adds Permissions-Policy headers for mobile sensor access."""
import http.server
import sys

class SensorPolicyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Allow all sensor APIs required for compass functionality
        self.send_header('Permissions-Policy', 
            'accelerometer=*, gyroscope=*, magnetometer=*')
        # Also set the older Feature-Policy for broader compatibility
        self.send_header('Feature-Policy',
            'accelerometer *; gyroscope *; magnetometer *')
        # Prevent caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        super().end_headers()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    server = http.server.HTTPServer(('127.0.0.1', port), SensorPolicyHandler)
    print(f"Serving on http://127.0.0.1:{port} with sensor Permissions-Policy headers")
    server.serve_forever()
