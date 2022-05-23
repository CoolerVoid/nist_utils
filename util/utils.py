import requests
from termcolor import colored
import warnings
import json

warnings.simplefilter("ignore")


def risk_color(risk):
  if "LOW" in risk:
    return colored(risk,"green")
  if "MEDIUM" in risk:
    return colored(risk,"yellow")
  if "HIGH" in risk:
    return colored(risk,"red")
  if "CRITICAL" in risk:
    return colored(risk,"red",attrs=['blink'])

def banner_start():
    print(colored('Lib Diff Sec  v0.1 \n',"yellow")+' Tool to search public vulnerabilities in library\nby CoolerVoid\n')

def banner():
    print(colored('Lib Diff Sec v0.1 \n',"yellow")+' Tool to search public vulnerabilities in library\nby CoolerVoid')
    print("\nExample: \n\t$ python3 lib-sec-diff.py -s \"Openssl 1.2\" -l 10\n\t\n")

def parser_response_csv(pkg_name,content):
    data = json.loads(content)

    for vuln in data['result']['CVE_Items']:
        cve=vuln['cve']['CVE_data_meta']['ID']
        url="https://nvd.nist.gov/vuln/detail/"+cve
        date=vuln['publishedDate']
        description=vuln['cve']['description']['description_data'][0]['value']
        try:
            cvss2=vuln['impact']['baseMetricV2']['severity']
        except:
            cvss2="NULL"
        try:
            cvss3=vuln['impact']['baseMetricV3']['cvssV3']['baseSeverity']
        except:
            cvss3="NULL"
        # use pipes '|' because field description have ',' this can crash parsers
        row=pkg_name+"|"+date+"|"+cve+"|"+url+"|"+cvss2+"|"+cvss3+"|"+description
        name_file=pkg_name.replace(" ","_")
        name_file.replace(".","_")
        with open(name_file+'.csv', 'a+') as f:
            f.write(row+"\n")
        print(row)

    

def getCPE(cpe,limit):
    if cpe != 0:
        url = "https://services.nvd.nist.gov/rest/json/cves/1.0?keyword="+cpe+"&resultsPerPage="+str(limit)
        r = requests.get(url)

        if r.status_code == 200:
            return r.text
        else:
            return False
    return False

def search_nist(pkg_name,limit):
    result = getCPE(pkg_name,limit)
    if result:
        parser_response_csv(pkg_name,result)
