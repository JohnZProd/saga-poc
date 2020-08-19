import webbrowser
import csv
import json
import random

DB_FILE = 'db.json'

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


def print_section_break():
    print("===========================")

def generate_random_number(upper):
    return random.randint(0, upper)

def query_db_file(topic_choice):
    links = []
    
    with open(DB_FILE, 'r') as fin:
        all_links = json.load(fin)

        for link in all_links:
            if link['topic'] == topic_choice:
                links.append(link)
        
    return links

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


def main():
    
    topic_choice, domain = get_choice()
    links = query_db_file(topic_choice)
    recommend(links)
    print_section_break()
    exit(0)  

main()