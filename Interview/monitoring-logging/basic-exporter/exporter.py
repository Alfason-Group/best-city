#!/usr/bin/env python3
"""
Ultra-simple Prometheus exporter - minimal dependencies
"""

import time
import random
from prometheus_client import start_http_server, Counter, Gauge, Histogram

# Initialize metrics
requests_total = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint'])
cpu_usage = Gauge('cpu_usage_percent', 'Current CPU usage percent')
memory_usage = Gauge('memory_usage_percent', 'Current memory usage percent')
response_time = Histogram('http_response_time_seconds', 'HTTP response time')

# Simulate metrics updates
def update_metrics():
    while True:
        # Simulate some requests
        for _ in range(random.randint(1, 10)):
            method = random.choice(['GET', 'POST'])
            endpoint = random.choice(['/api', '/home', '/users'])
            requests_total.labels(method=method, endpoint=endpoint).inc()
            
            # Simulate response time
            latency = random.uniform(0.05, 2.0)
            response_time.observe(latency)
        
        # Update system metrics (simulated)
        cpu_usage.set(random.uniform(0.0, 100.0))
        memory_usage.set(random.uniform(20.0, 90.0))
        
        time.sleep(5)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    print("Metrics exporter running on http://localhost:8000/metrics")
    
    # Start background updates
    update_metrics()