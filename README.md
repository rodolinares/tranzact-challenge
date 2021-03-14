# tranzact-challenge

Application developed for the code challenge proposed by TRANZACT.

## Challenge

The Wikimedia Foundation provides all pageviews for Wikipedia site since 2015 in machine-readable format. The pageviews can be downloaded in gzip format and are aggregated per hour per page. Each hourly dump is approximately 50MB in gzipped text file and is somewhere between 100MB and 250MB in size unzipped.

### Technical documentation of the service

https://wikitech.wikimedia.org/wiki/Analytics/Data_Lake/Traffic/Pageviews

### Sample link

https://dumps.wikimedia.org/other/pageviews/2015/2015-05/pageviews-20150501-010000.gz

![Explanation of file structure](https://i.imgur.com/7pEhqpV.png 'Explanation of file structure')

Please create a command line application. Your code should get data for last 5 hours and provide the following counts in file (grouped by hours):

1. Language & Domain trailing part - display the max viewed count for language & domain combination (see https://wikitech.wikimedia.org/wiki/Analytics/Data_Lake/Traffic/Pageviews for domain)

2. Page title with max count of views per page (should include all languages)

Result of your execution should be printed in console like this: 

![Output sample](https://i.imgur.com/wPyr3cP.png 'Output sample')
