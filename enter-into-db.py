import csv
import json

SITEMAP_FOLDER = './sitemaps-by-domain'

def process_entry(domain_link, search_domain):
    # Assume all are new additions
    if search_domain in domain_link['url']:
        return True
    
def build_entry(domain_link, topic):
    final_entry = {
        "url": domain_link['url'],
        "domain": domain_link['domain'],
        "topic": topic,
        "reads": 0,
        "recommends": 0
    }
    return final_entry
            
def write_to_db(topic_links):
    with open('db.json', 'w') as fout:
        json.dump(topic_links, fout)

# Will remove the http(s):// and everything after the first /
# e.g. https://www.google.com/maps becomes www.google.com
def strip_domain(domain):
    return domain.split('://')[1].split('/')[0]

def main():
    
    topic_links = []

    filename = 'doc_list.txt'
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:

            # Initialise the entries
            topic = row[0]
            search_domain = row[1]
            root_domain = strip_domain(search_domain)

            domain_links = []
            with open(SITEMAP_FOLDER + '/' + root_domain+".json", 'r') as fin:
                domain_links = json.load(fin)

            for domain_link in domain_links:
                if process_entry(domain_link, search_domain):
                    topic_links.append(build_entry(domain_link, topic))

    write_to_db(topic_links)

#
# Test function to test output
#
def query_db():
    with open('db.json', 'r') as fin:
        links = json.load(fin)
        return links

main()