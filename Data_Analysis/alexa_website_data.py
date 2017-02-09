__author__ = 'saipc'

from total_unique_domains import get_domains_from_list
import requests
import xml.etree.ElementTree as ET


def get_alexa_data(url):
  constructed_url = 'http://data.alexa.com/data?cli=10&url=' + url
  print('querying', constructed_url)
  r = requests.get(constructed_url)
  parsed_xml = get_xml(r.text)
  return get_ranks(parsed_xml)

def get_xml(xml_string):
  # print('obtained XML')
  try:
    return ET.fromstring(xml_string)
  except Exception as e:
    print("Was not able to parse this one", xml_string)
    return []

def get_ranks(xml_data):
  # print('getting rank')
  # data is always inside the first tag, if present
  if (len(xml_data) > 0):
    sd_data = xml_data[0]
    # we are interested only in the popularity and country stats
    url =''
    world_pop = ''
    country_name = ''
    country_rank = ''
    for child in sd_data:
      child_tag_attr = child.attrib
      if child.tag == 'POPULARITY':
        url = child_tag_attr['URL']
        world_pop = child_tag_attr['TEXT']
      elif child.tag == 'COUNTRY':
        country_name = child_tag_attr['NAME']
        country_rank = child_tag_attr['RANK']
    print(url, world_pop, country_name, country_rank)
    return (url, world_pop, country_name, country_rank)

if __name__ == '__main__':
  with open('domains_list', 'r') as domains_file:
    domains = [domain.strip() for domain in domains_file]
    unique_domains = get_domains_from_list(domains)
    ranks_list = []
    for domain in unique_domains:
      ranks_list.append(get_alexa_data(domain))
    ranks_list = filter(None, ranks_list)
    print(len(ranks_list))
    with open('output_alexa_domains_list', 'w') as op_file:
      op_file.write(",\n".join(ranks_list))
