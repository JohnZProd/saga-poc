from usp.tree import sitemap_tree_for_homepage
import json
import csv

#
# Will generate one file per DOMAIN (not topic)
#

# The sitemap folder will act as the NoSQL 'database' with each domain acting as its own table
SITEMAP_FOLDER = './sitemaps-by-domain'

def generate_sitemap(domain):

  # Generate the sitemap
  tree = sitemap_tree_for_homepage(domain)

  # Initialise the list of links
  links = []

  # Iterate through all URLs found by the sitemap generator
  for page in tree.all_pages():
    url = page.url

    # Some sites will not have the domain name in front of URL == add this in
    if url[0] == '/':
      url = domain + url

    # This is the structure of the db
    # Needs work to improve search functionality
    link_entry = {
      'url': url,
      'domain': 'https://'+strip_domain(domain) #TODO: Optimise this to call the function only once
    }

    #Add this to the list of links needing to be appended
    links.append(link_entry)
  
  # Write the links to a file (one for each domain) 
  write_to_file(domain, links)

# Will remove the http(s):// and everything after the first /
# e.g. https://www.google.com/maps becomes www.google.com
def strip_domain(domain):
  return domain.split('://')[1].split('/')[0]

# Write the list of links to a file
def write_to_file(domain, links):

  # Will only put the domain name without protocol and paths to filename
  filename = domain.split('://')[1].split('/')[0] + '.json'

  # Open the file for writing
  with open(SITEMAP_FOLDER + '/' + filename, 'w') as fout:
    json.dump(links, fout)

###################################################
# MAIN BELOW
###################################################

def main():
  # Open the list of topics needing to be processes
  filename = 'doc_list.txt'
  with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)

    # TODO: Implement functionality for non-unique domains across different topics
    # e.g. cloudformation and elasticbeanstalk

    for row in reader:
      generate_sitemap(row[1])

main()