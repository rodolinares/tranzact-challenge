# tranzact-challenge

Application developed for the code challenge proposed by TRANZACT.

## Table of contents

- [Challenge](#challenge)
- [Technologies](#technologies)
- [Usage](#usage)

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

## Technologies

### Python 3.8.5

![Python](https://www.python.org/static/img/python-logo.png 'Python')

Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

## Usage

### Prerequisites

- [Python](https://www.python.org/downloads/) - Be sure to install Python (this was tested with v3.8.5) or the script won't work!

- [Git](https://git-scm.com/downloads) - We're using git to clone the repository to your machine.

### Download and execution

Clone the repository using the following command:

```sh
git clone https://github.com/rodolinares/tranzact-challenge.git
```

Then enter the directory that was just downloaded:

```sh
cd tranzact-challenge
```

To execute the script, use this:

```sh
python3 app.py
```

It will take a while to download the necessary data and process it, but after a while you should have an output like this:

```
Period              Language            Domain              ViewCount           
6PM                 en                  wikipedia           217508              
7PM                 en                  wikipedia           211812              
8PM                 en                  wikipedia           209527              
9PM                 en                  wikipedia           205066              
10PM                en                  wikipedia           195176              


Period              Page                ViewCount           
6PM                 Main_Page           343454              
7PM                 Main_Page           340759              
8PM                 Main_Page           334941              
9PM                 Main_Page           318441              
10PM                Main_Page           299938  
```