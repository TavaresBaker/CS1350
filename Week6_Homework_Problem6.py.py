def problem6():
    log_data = """192.168.1.1 - - [15/Mar/2024:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 5234
    192.168.1.2 - - [15/Mar/2024:10:30:46 +0000] "POST /api/login HTTP/1.1" 401 234
    192.168.1.1 - - [15/Mar/2024:10:30:47 +0000] "GET /images/logo.png HTTP/1.1" 304 0
    192.168.1.3 - - [15/Mar/2024:10:30:48 +0000] "GET /admin/dashboard HTTP/1.1" 403 0
    192.168.1.2 - - [15/Mar/2024:10:30:49 +0000] "POST /api/login HTTP/1.1" 200 1234
    192.168.1.4 - - [15/Mar/2024:10:30:50 +0000] "GET /products HTTP/1.1" 200 15234
    192.168.1.1 - - [15/Mar/2024:10:30:51 +0000] "GET /contact HTTP/1.1" 404 0"""

    log_pattern = r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\w+) (?P<path>[^\s]+) [^"]+" (?P<status>\d{3}) (?P<size>\d+)'
    parsed_logs = [m.groupdict() for m in re.finditer(log_pattern, log_data)]

    total_requests = len(parsed_logs)
    unique_ips = list({entry['ip'] for entry in parsed_logs})
    error_count = sum(1 for entry in parsed_logs if 400 <= int(entry['status']) < 600)
    total_bytes = sum(int(entry['size']) for entry in parsed_logs)
    paths = [entry['path'] for entry in parsed_logs]
    most_requested_path = Counter(paths).most_common(1)[0][0] if paths else ''
    methods_used = list({entry['method'] for entry in parsed_logs})

    analysis = {
        'total_requests': total_requests,
        'unique_ips': unique_ips,
        'error_count': error_count,
        'total_bytes': total_bytes,
        'most_requested_path': most_requested_path,
        'methods_used': methods_used
    }

    return {'parsed_logs': parsed_logs, 'analysis': analysis}


