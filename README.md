Converts WGS84 decimal coordiantes to c-squares

## Usage Example

```python
from csquares import to_csquare
to_csquare(-37.24, 1.0)
# returns "3300:371:120:140",
# (to the largest acuracy possible with the input )
```

## Background
CSquares are a neat way of storing Google Maps style longitude and latitude in an easy to way thats search using a normal database.

For example;

Melbourne central station has decimal coordinates of latitude = -37.8104
and longitude = 144.9607 to a precision of roughly 11m; Which is about as good as your phone's GPS can handle.

This gives a C-Square of '3314:374:489:216:100:247'

If you stored this in a text field on your favourite open source SQL database, you could do something like this:

```sql
SELECT * FROM locations WHERE csquare LIKE '3314:374:4%';
```

This would return most of the locations in your database in the Greater Melbourne area.  If you have set up your database correctly,  this should hit the index and be super fast. For me, this is what makes the system so interesting.

Read the CSIRO pages for all the details.

[Based on CSquares by Tony Rees of CSIRO](http://www.cmar.csiro.au/csquares/)

## Warning

This is currently just a hobby project, for now anyway.  There are better C-Square implementations out there!

I welcome your feedback and suggestions.
