__author__ = 'saipc'

from total_unique_domains import get_domains_from_list
import requests
import xml.etree.ElementTree as ET


def get_alexa_data(url):
  constructed_url = 'http://data.alexa.com/data?cli=10&url=' + url
  r = requests.get(constructed_url)
  parsed_xml = get_xml(r.text)
  get_ranks(parsed_xml)

def get_xml(xml_string):
  return ET.fromstring(xml_string)

def get_ranks(xml_data):
  print(xml_data.tag)
  print(xml_data.attrib)

if __name__ == '__main__':
  with open('domains_list', 'r') as domains_file:
    domains = [domain.strip() for domain in domains_file]
    unique_domains = get_domains_from_list(domains)
    # for domain in unique_domains:
    get_alexa_data(unique_domains.pop())
