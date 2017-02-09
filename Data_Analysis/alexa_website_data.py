__author__ = 'saipc'

from total_unique_domains import get_domains_from_list
import requests
import xml.etree.ElementTree as ET


def get_alexa_data(url):
  constructed_url = 'http://data.alexa.com/data?cli=10&url=' + url
  print('querying', constructed_url)
  r = requests.get(constructed_url)
  parsed_xml = get_xml(r.text)
  get_ranks(parsed_xml)

def get_xml(xml_string):
  print('obtained XML')
  return ET.fromstring(xml_string)

def get_ranks(xml_data):
  print('getting rank')
  interested_attrs = ['POPULARITY', 'COUNTRY']
  # data is always inside the first tag, if present
  if (len(xml_data) > 0):
    sd_data = xml_data[0]
    for child in sd_data:
      # we are interested only in the popularity and country stats
      if child.tag in interested_attrs:
        print(child.tag, child.attrib)

if __name__ == '__main__':
  with open('domains_list', 'r') as domains_file:
    domains = [domain.strip() for domain in domains_file]
    unique_domains = get_domains_from_list(domains)
    for domain in unique_domains:
      get_alexa_data(domain)
