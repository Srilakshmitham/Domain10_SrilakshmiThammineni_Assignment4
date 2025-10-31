from collections import Counter

def analyze_log_file(file_path):
    ip_count = Counter()
    url_count = Counter()
    response_count = Counter()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) < 9:
                    continue 
                ip = parts[0]
                url = parts[6]
                response = parts[8]

                ip_count[ip] += 1
                url_count[url] += 1
                response_count[response] += 1

        print("\n--- Log Analysis Summary ---")
        print("Top 5 IP Addresses:")
        for ip, count in ip_count.most_common(5):
            print(f"{ip} -> {count} times")

        print("\nTop 5 URLs:")
        for url, count in url_count.most_common(5):
            print(f"{url} -> {count} times")

        print("\nResponse Code Summary:")
        for code, count in response_count.items():
            print(f"{code}: {count} times")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("Error:", e)
