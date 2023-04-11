#!/usr/bin/env python3
'''Task 12's module.
'''

from pymongo import MongoClient

# Connect to the MongoDB database and collection
client = MongoClient()
db = client.logs
collection = db.nginx

# Count the total number of logs
total_logs = collection.count_documents({})

# Count the number of logs with each HTTP method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {}
for method in methods:
    method_counts[method] = collection.count_documents({"method": method})

# Count the number of logs with method=GET and path=/status
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

# Print the stats
print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"    method {method}: {count}")
print(f"{status_check_count} status check")

