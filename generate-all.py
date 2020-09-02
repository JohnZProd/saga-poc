from generate_sitemap import *

def get_existing_sitemaps():
  sitemaps = []
  for f in listdir(SITEMAP_FOLDER):
    sitemaps.append(f.split('.json')[0])
  return sitemaps

def main():
    # Open the list of topics needing to be processes
    filename = 'doc_list.txt'
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        domains_generated = ['']

        # TODO: Condition to see if the --all flag is NOT SET
        if True:
            domains_generated = get_existing_sitemaps()

        # Will not generate duplicate sitemaps
        for row in reader:
            if strip_domain(row[1]) not in domains_generated:
                generate_sitemap(row[1])
                domains_generated.append(strip_domain(row[1]))

if __name__ == "__main__":
    main()