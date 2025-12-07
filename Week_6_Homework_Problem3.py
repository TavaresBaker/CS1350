def problem3():
    log_text = """ [2024-03-15 10:30:45] INFO: Server started on port 8080
    [2024-03-15 10:31:02] ERROR: Connection failed to database
    [2024-03-15 10:31:15] WARNING: High memory usage detected (85%)
    [2024-03-15 10:32:00] INFO: User admin logged in from 192.168.1.100
    [2024-03-15 10:32:30] ERROR: File not found: config.yml """

    pattern_timestamp = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]'
    timestamps = re.findall(pattern_timestamp, log_text)

    pattern_log = r'\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\] (\w+): (.+)'
    log_entries = re.findall(pattern_log, log_text)

    pattern_ip = r'\b\d{1,3}(?:\.\d{1,3}){3}\b'
    ip_addresses = [{'ip': m.group(), 'start': m.start(), 'end': m.end()} for m in re.finditer(pattern_ip, log_text)]

    def highlight_errors(text):
        return re.sub(r'(ERROR: .+)', r'**\1**', text)

    highlighted_log = highlight_errors(log_text)

    return {
        'timestamps': timestamps,
        'log_entries': log_entries,
        'ip_addresses': ip_addresses,
        'highlighted_log': highlighted_log
    }
