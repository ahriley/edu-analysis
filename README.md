# [TAMUHack](http://tamuhack.com/) 2018: Visualizing College Scorecard Data

Working with a group of 4 other Texas A&M employees (who were all first-time hackers), our project was to visualize [College Scorecard](https://catalog.data.gov/dataset/college-scorecard) data from [data.gov](https://www.data.gov/).  Now, [the website](https://collegescorecard.ed.gov/) for the dataset already makes some plots that we reproduce, but we were particularly interested in how demographics change *with time* (since this is a 20-year dataset, and most major universities have ~5 years of reporting these statistics), which the website does not do.

With an actual ~3 hours of work (a lot of time was spent exploring other projects and running into roadblocks), this was the result.
* cleandata.py does what it says on the tin (produced the "clean" files in /data)
* 2015plots.py makes pie-charts for race and income level
* timeseries.py showed how race breakdowns change with time

Results are shown in /plots.
