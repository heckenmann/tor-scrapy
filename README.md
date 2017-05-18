# tor-scrapy
webcrawler using a tor-proxy, elasticsearch and scrapy

## What you need
- docker
- docker-compose
- internet connection :\

## How to create and run
You can set the entrypoint for the crawler in the docker-compose.yml under scrapy / urls. Many urls are comma separated.
```
docker-compose up -d
```
The crawler starts its work automatically.

## How to stop / start
```
docker-compose stop
docker-compose start
```

## How to delete
```
docker-compose down
```

## Use
To find something in your index, you can use kibana. You have to know the ip of the kibana container:
```
docker inspect torcrawler_kibana_1 | jq '.[] | .NetworkSettings.Networks.torcrawler_default.IPAddress'
```
Open the address in your browser:
```
http://KIBANA_ADDRESS:5601
```
As index pattern set __"crawler"__. Timefield name is __"timestamp"__.

Then click on "discover" on the left side to see all found pages.
To search for an entry, type the keywords into the kibana-search-bar on the top.
To get an kibana introduction, you can go to this site: https://www.elastic.co/guide/en/kibana/current/introduction.html
