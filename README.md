# Saga - A Proof of Concept

This is a proof-of-concept for the Saga application. A CLI based web-service that allows you to learn a random topic by recommending a random piece of documentation to you given a topic.

Currently, I have the following documentation domains available
* docker 
* kubernetes
* healthnavigator
* aws-knowledge-center
* devops.com

Upon selection, the app will recommend a random piece of documentation from the domain and you will be able to answer Y or N if you would like to read it in full.

Once again, please note that this is merely a proof of concept and is not intended as anything close to the final working version of the app.

## Terminology, Concepts, Architecture

The working version of the app is made up of services and sources of data

### Services

#### Sitemap Scraper

Given a list of domains (from knowledge-repo), will provide a full list of available links (i.e. sitemap) available on the domain for each domain

Given a list of topic (from knowledge-repo), will filter out the invalid links before inserting valid links into the Link Database

#### Recommender API

Given a user input of topics (from knowledge-repo), will query the Database for links that match the topic and recommend random ones to the user

### Datasources

#### Link Database

Holds all the valid links along with the associated topics. Note that links can be duplicated if they belong to multiple topics

This requires an additional step by the sitemaps by domain function

Links table
```json
{
    "url":"string",
    "domain":"string",
    "topic": "string",
    "reads":"string",
    "recommends": int
}
```

Topics table
```json
{
    "topic": "string",
    "search_domain":"string",
    "last_updated": "timestamp",
    "currently_updating" bool,
    "category": "string"
}
```

In future releases, this is a mongodb data source rather than a file

#### Knowledge repo

Lists the topics, domains to search, and the URL paths that pertain to that topic

```
kubernetes,https://kubernetes.io/docs
docker,https://docs.docker.com,
healthnavigator,https://www.healthnavigator.org.nz
aws-knowledge-centre,https://aws.amazon.com/premiumsupport/knowledge-center
devops.com,https://devops.com/category/blogs,tech
```

## Usage

To use the POC, execute the setup script, then the three services sequentially

```bash
sh setup.sh

python3 generate-sitemap.py

python3 enter-into-db.py

python3 recommend-from-db.py
```

## Ideas

* Get a way for people to store custom topics

# Documentation

https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb

https://docs.mongodb.com/manual/tutorial/getting-started/

https://ianlondon.github.io/blog/mongodb-auth/

https://flaviocopes.com/go-nginx-reverse-proxy/
