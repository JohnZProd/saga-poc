# Saga - A Proof of Concept

This is a higher level overview for the Saga application, a CLI based web-service that allows you to learn a random topic by retrieving a random piece of documentation from the internet to you based on a topic that you specify

Currently, I have the following documentation topics available
* docker 
* kubernetes
* healthnavigator
* aws-knowledge-center
* devops.com

Upon selection of a topic, the app will recommend a random piece of documentation from the list of available documentation links and you will be able to answer Y or N if you would like to read it in full. If you select Y, the app will open that link in your browser.

The repository mainly holds the doc_list.txt file which sets out the list of available topics in the database.

## Terminology, Concepts, Architecture

The working version of the app is made up of services and sources of data

### Datasources

#### Database

A MongoDB database that holds all the valid links along with the associated topics. Note that links can be duplicated if they belong to multiple topics.

Links collection
```json
{
    "url":"string",
    "domain":"string",
    "topic": "string",
    "reads":"string",
    "recommends": "int"
}
```

Topics collection
```json
{
    "topic": "string",
    "filtered-url":"string",
    "last_updated": "timestamp",
    "currently_updating": "bool",
    "category": "string"
}
```

#### Knowledge repo

Lists the topic, domains to search, and the URL paths that pertain to that topic

```
kubernetes,https://kubernetes.io/docs,tech
docker,https://docs.docker.com,tech
healthnavigator,https://www.healthnavigator.org.nz,healthcare
aws-knowledge-centre,https://aws.amazon.com/premiumsupport/knowledge-center,tech
devops.com,https://devops.com/category/blogs,tech
```

### Services

#### New Topics

A job that takes in doc_list.txt (from the internet) and queries the topics table in the database. Inserts topics into the database if they are in doc_list.txt but not in the database, and removes topics from the database if they are not in doc_list.txt but existing in the database.

This job is triggered by a Github webhook whenever a change to doc_list.txt is detected in the master brance of this repo.

#### Sitemap Scraper

A job that queries the database for the least recently updated topic (from the last_updated field), and generates the sitemap for the corresponding domain of the topic (from filtered-url field) to grab all the URLs available for that domain. It then inserts all links matching the filtered-url field into the database's topics collection.

This job is executed by running the sitemap scraper script and the topic that it chooses to update can be overriden by specifying the --topic and --domain flags. For example:

```bash
python3 sitemap_scraper.py --topic docker --domain https://docs.docker.com
```

#### Recommender API

The API service that queries the database to provides functionality with the application.

The API listens on the following paths
* /api/recommend: To get the full list of available topics
* /api/recommend?<topic>: To get a random link from the list links available for that topic

#### Saga CLI

A local CLI application that interacts with the recommender API

### Architecture

Development is in progress for two different architectures of the application stack. You may read more and see their automation YAMLs in their respective Github repos.

#### saga-ra2

New topics, and sitemap scraper components are run as ECS tasks in AWS.

Recommender API and mongodb are run on EC2 instances in AWS.

#### saga-ra3

New topics, and sitemap scraper components are run as scheduled jobs in a Kubernetes cluster.

Recommender API and mongodb are run as Kubernetes services.

The end goal of this architecture is to be cloud agnostic.

## Usage

TBC

## Contributing to the knowledge repo

Fork the repo, add a topic in compliance with the predefined format, and submit a pull request. It will be manually validated by me at this point.

# Documentation

https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb

https://docs.mongodb.com/manual/tutorial/getting-started/

https://ianlondon.github.io/blog/mongodb-auth/

https://flaviocopes.com/go-nginx-reverse-proxy/
