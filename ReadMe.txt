For Cleaning Tools
Some of the steps may not be necessary depending on the website. Also, depending on the website architecture, you will have to make adjustments. 
Stage 1: Header and Eclipses -- Here we identify headers and fix their capitalization. Also, change the Unicode Eclipses to ASCII.
Stage 2: Code Snippets -- Almost all of the scraped data has code-like junk that doesn't make sense. We will remove them here.
Stage 3: Remove Boiler in Top -- Repeating texts that don't add value to the context will be removed here (Top of the Article).
Stage 4: Remove Boiler in the bottom -- Repeating texts that don't add value to the context will be removed here (Bottom of the Article).
Stage 5: Remove non-English -- Some websites will have non-English texts which will degrade our english language model's output. So, we remove them here.
Stage 6: Decide what goes into the T5 -- We will convert the non-ASCII characters here if necessary. 
Stage 7: Last Stage Cleaning -- Any last changes (Depends on the website). 

For Scraping
Scraping is done in two steps so that we can avoid issues such as missing articles / degraded paragraph order etc. 

  Step One:
    What we do:
  Here we collect all the inner links of the website and write them into a text file.
    How to use it: 
  Goto Scrape Tools\Step One\twoSteps\spiders. 
  Then, open twoSteps.py.
  Change the following (Your website domain), 
      allowed_domains = ['thevaccinereaction.org']
      start_urls = ['https://thevaccinereaction.org/']
      base_url = 'https://thevaccinereaction.org/'
      Note that the format of the website you enter has to match up with above.
  Finally, open up the terminal and cd to "Scrape Tools\Step One".
  Then, type and enter following sytax: scrapy crawl twoSteps -o outputFileName.json
  
  Step Two:
    What we do:
  Now we scrape all the web pages in the text file called "webPageList.txt" we obtained from "Step One".
    How to use it: 
  Goto Scrape Tools\Step Two\stage2\stage2\stage2\spiders.
  Then, open stage2.py file.
  Change the following.
    Change the The directory of the file "webPageList.txt"
    Finally, open up the terminal and cd to Scrape Tools\Step Two\stage2\stage2
    Then, type and enter following sytax: scrapy crawl twoSteps -o outputFileName.json
    
