# Zomato Home Delivery Details Scraper

**Note**: Scraping (screen) data off a website is considered illegal in a lot of countries and also websites have their own copyright's to protect the same, with this thought in mind the code attached inside is only for educational purposes and NOT commercial purpose

The idea of this tool came in out of sheer laziness, I wanted a tool which given certain parameters mails me the best delivery outlets near me, hence came this tool :D

___

The tool takes in 3 commandline parameters:

1. **Location** - This has been tested in Delhi and NCR region (India)  <br>             
South Delhi: south-delhi  <br>
                    West Delhi: west-delhi  <br>
                    Gurgaon: gurgaon  <br>
                    Noida: noida  <br>
                    North Delhi: north-delhi  <br>
                    Ghaziabad: ghaziabad  <br>
                    East Delhi: east-delhi  <br>

2. **Cuisine** - The kind of cuisine you'll like to be delivered to you <br>             
Chinese: chinese <br>
                   North Indian: north-indian  <br>
                   Italian: italian  <br>
                   Continental: continental  <br>
                   Mughlai: mughlai  <br>
                   Cafe: cafe  <br>
                   Refer to zomato.com for more cuisines and use them accordingly  <br>

3. **Cost for two** -  <br>             
Less than 250: 0  <br>
                   250 - 500: 1  <br>
                   500 - 1000: 2  <br>
                   1000 - 1500: 3  <br>
                   1500-2000: 4  <br>

**To Run:** python zomato_scraper.py gurgaon chinese 3

And you'll receive an email :D

P.S. You'll have to enter your email ID and Password in the script before executing

**License**

The MIT License (MIT)

Copyright (c) 2016 Vaibhav Srivastav

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
