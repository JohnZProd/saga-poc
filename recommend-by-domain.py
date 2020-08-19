#
# CLI code
# Note that the POC will combine both the CLI with the web-service
#


import webbrowser
import csv
import json
import random

SITEMAP_FOLDER = './sitemaps-by-domain'

def main():

  topic_choice, domain = get_choice()

  link_file = strip_domain(domain) + '.json'

  #print(link_file)
  
  links = load_link_file(link_file)
  links = remove_invalid_links(links, domain)

  recommend(links)

  print_section_break()
  exit(0)  

def get_choice(filename='doc_list.txt'):
  topics = []

  with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      topics.append(row)
    
    #You may sort the topics list here

    print("Select a topic out of: ")
    for topic_num in range(0, len(topics)):
      print("["+str(topic_num)+"]: "+topics[topic_num][0])
    selection = input()
    print_section_break()

    return topics[int(selection)]

def strip_domain(domain):
  return domain.split('://')[1].split('/')[0]

def load_link_file(filename):
  links = []

  with open(SITEMAP_FOLDER + '/' + filename, 'r') as fin:
    links = json.load(fin)

  return links

def generate_random_number(upper):
  return random.randint(0, upper)

def print_section_break():
  print("===========================")

def remove_invalid_links(links, domain):
  valid_links = []
  #Logic evaluates the path and whether the path ends with /
  #
  # Evaluation for which links are valid could improve
  #

  for link in links:
    if domain in link['url'] and link['url'][-1] == '/':
      valid_links.append(link)
  
  return valid_links

def recommend(links):
  random_int = generate_random_number(len(links))

  print("Would you like to read")
  link_url = links[random_int]['url']
  print(link_url)
  print("(Y/N):")
  selection = input()

  #Maybe do Y, N or other here
  if selection.upper() == "Y":
    webbrowser.open(link_url,new=2)
  else:
    print_section_break()
    recommend(links)

main()
