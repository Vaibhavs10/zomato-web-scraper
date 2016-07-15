# Zomato delivery details scraper

**Note**: Scraping (screen) data off a website is considered illegel in a lot of countries and also websites have their own copyright's to protect the same, with this thought in mind the code attavhed inside is only for educational purposes and NOT commercial purpose

The idea of this tool came in out of sheer laziness, I wanted a tool which given certain parameters mails me the best delivery outlets near me, hence came this tool :D

The tool takes in 3 commandline parameters:

1. **Location** - This has been tested in Delhi and NCR region (India)
             List: South Delhi: south-delhi
                    West Delhi: west-delhi
                    Gurgaon: gurgaon
                    Noida: noida
                    North Delhi: north-delhi
                    Ghaziabad: ghaziabad
                    East Delhi: east-delhi

2. **Cuisine** - The kind of cuisine you'll like to be delivered to you
             List: Chinese: chinese
                   North Indian: north-indian
                   Italian: italian
                   Continental: continental
                   Mughlai: mughlai
                   Cafe: cafe
                   Refer to zomato.com for more cuisines and use them accordingly

3. **Cost for two** -
             List: Less than 250: 0
                   250 - 500: 1
                   500 - 1000: 2
                   1000 - 1500: 3
                   1500-2000: 4
