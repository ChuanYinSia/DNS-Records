import time
import json
import dns.resolver

def go(url):
    result = []
    ids = ['NONE', 'A', 'NS', 'MD', 'MF', 'CNAME', 'SOA', 'MB', 'MG', 'MR', 'NULL', 'WKS', 'PTR', 'HINFO', 'MINFO', 'MX', 'TXT', 'RP', 'AFSDB', 'X25', 'ISDN', 'RT', 'NSAP', 'NSAP-PTR', 'SIG', 'KEY', 'PX', 'GPOS', 'AAAA', 'LOC', 'NXT', 'SRV', 'NAPTR', 'KX', 'CERT', 'A6',
           'DNAME', 'OPT', 'APL', 'DS', 'SSHFP', 'IPSECKEY', 'RRSIG', 'NSEC', 'DNSKEY', 'DHCID', 'NSEC3', 'NSEC3PARAM', 'TLSA', 'HIP', 'CDS', 'CDNSKEY', 'CSYNC', 'SPF', 'UNSPEC', 'EUI48', 'EUI64', 'TKEY', 'TSIG', 'IXFR', 'AXFR', 'MAILB', 'MAILA', 'ANY', 'URI', 'CAA', 'TA', 'DLV']
    for a in ids:
        try:
            answers = dns.resolver.query(url, a)
            for ans in answers:
                bb = a + ':' + ans.to_text()
                result.append(bb)
        except:
            pass

    refinal = json.dumps(result)
    final = refinal.replace("\\", "")
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
