import time
import json
import dns.resolver
from datetime import date
import concurrent.futures
from tqdm import tqdm


def go(url):
    result = []
    ids = ['A', 'NS', 'SOA', 'MX', 'TXT']
    for a in ids:
        try:
            answers = dns.resolver.query(url, a)
            for rdata in answers:
                bb = a + ':' + rdata.to_text()
                result.append(bb)
        except:
            result = []

    refinal = json.dumps(result)
    final = refinal.replace("\'", "")
    print(url, final, '\n')


if __name__ == "__main__":
    start_time = time.time()

    urls = ['youtube.com', 'google.com']

    try:
        for url in urls:
            go(url)
    except Exception as e:
        print(e)
    print("--- %s seconds ---" % round(time.time() - start_time, 2))
