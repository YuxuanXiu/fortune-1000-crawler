# Fortune 1000 crawler

## Description
Although there are existing repositories for obtaining [Fortune 1000](http://fortune.com/fortune500/) companies' data, such as [LegendL3n](https://github.com/LegendL3n)'s [fortune-grabber](https://github.com/ilyavorobiev/fortune-grabber), it seems that they are no longer being maintained. Besides, [Fortune 1000](http://fortune.com/fortune500/) has changed its API since 2015. [Roysoumya](https://github.com/roysoumya) has modified [LegendL3n](https://github.com/LegendL3n)'s project, but it can only obtained the data for 2017.
This repository is basically a modified version of [fortune-grabber](https://github.com/ilyavorobiev/fortune-grabber), that is able to crawl the annual data from 2002 to 2018. A method to obtain fortune 1000 API for the future years, such as 2019 and 2020, is also provided.

This repository needs Python 3.5.


## Usage

To obtain Fortune 1000 data from 2002 to 2014:
```terminal
python fortune_1000.py
```

To obtain Fortune 1000 data from 2005 to 2018:
```terminal
python fortune_1000_15_18.py
```

## Fortune 1000 API

The newest version of fortune 1000 API looks like this:

```
http://fortune.com/api/v2/list/{year_code}/expand/item/ranking/asc/{start_from}/{num_limit}/
```
{start_from} is the ranking in the list where we start to crawl.

{num_limit} is the number of companies in a single request, the maximum is 100.

{year_code} can be found in a HTTP request. An example to obtain this parameter with Chrome is shown as follows.

For 2015:

![2015](/images/2015.png)

For 2016:

![2016](/images/2016.png)

For 2017:

![2017](/images/2017.png)

For 2018:

![2018](/images/2018.png)

In this way, the corresponding code to each year can be obtained.

Append this dict to adjust to future years.

```python
dict_api_code = {'2015': '1141696', '2016': '1666518', '2017': '2013055', '2018': '2358051'}
```


## Prepared data
Just like [fortune-grabber](https://github.com/ilyavorobiev/fortune-grabber), the crawled data  can be found in [output folder](/output).
