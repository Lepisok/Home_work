from requests import get


def save_log(url, file_name):
    """ сохраняет контент url в file_name. Пишет байты. Читает по 10мб
    """
    response = get(url, stream=True)
    if response.status_code == 200:
        with open(file_name, 'bw') as f:
            for chunk in response.iter_content(chunk_size=10 * 1024 * 1024):
                f.write(chunk)


def parse_log(file_name, req_counters):
    """возвращает список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
        [
            ...
            ('141.138.90.60', 'GET', '/downloads/product_2'),
            ('141.138.90.60', 'GET', '/downloads/product_2'),
            ('173.255.199.22', 'GET', '/downloads/product_2'),
            ...
        ]
    и словарь с подсчетом вызовов от каждого IP:
        {
            ...
            '1.2.3.4': 9000
            ...
        }
    """
    parsed_data = []
    with open(file_name) as f:
        for line in f:
            first_quote = line.find('"') + 1
            parsed_data.append((line[:line.find(' ')], *line[first_quote:line.find('"', first_quote)].split()[:2]))
            req_counters.setdefault(parsed_data[-1][0], 0)
            req_counters[parsed_data[-1][0]] += 1
    return parsed_data


if __name__ == '__main__':
    log_name = 'nginx_logs.txt'
    request_counters = dict()
    if False:
        save_log('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs', log_name)

    parse_log(log_name, request_counters)

    max_req_key = max(request_counters, key=request_counters.get)
    print(f'{max_req_key}: {request_counters[max_req_key]}')

    max_req_value = max(request_counters.values())
    print([f'{k}: {v}' for k, v in request_counters.items() if v == max_req_value])
