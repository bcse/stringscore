String Score [![Build Status](https://travis-ci.org/bcse/stringscore.png?branch=master)](https://travis-ci.org/bcse/stringscore)
============

An algorithm provides scores between 0.0 (no match) to 1.0 (perfect match) for a comparison of two strings.

The algorithm is designed for auto-completion. For string similarity, please check [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) ([Wagner–Fischer algorithm](https://en.wikipedia.org/wiki/Wagner-Fischer_algorithm)).

Usage
-----

Include the library:

```python
from stringscore import liquidmetal
```

Score any string against an abbreviation:

```python
>>> liquidmetal.score('FooBar', 'foo')
0.95
>>> liquidmetal.score('FooBar', 'fb')
0.916666666667
>>> liquidmetal.score('Foo Bar', 'fb')
0.928571428571
>>> liquidmetal.score('Foo Bar', 'baz')
0.0
>>> liquidmetal.score('Foo Bar', '')
0.8
```

Similar Works
-------------

- Quicksilver's [scoreForAbbreviation](https://github.com/quicksilver/Quicksilver/blob/master/Quicksilver/Code-QuickStepFoundation/NSString_BLTRExtensions.m#L53) algorithm by Alcor (Blacktree, Inc)
- [LiquidMetal](https://github.com/rmm5t/liquidmetal) by Ryan McGeary
- [string_score](https://github.com/joshaven/string_score) by Joshaven Potter
- [jQuery.fuzzyMatch](https://github.com/rapportive-oss/jquery-fuzzymatch) by [Rapportive](http://rapportive.com/)

License
-------

String Score is released under the [MIT License](http://opensource.org/licenses/MIT).

Credits
-------

Copyright © 2003 Blacktree, Inc (Original author of [Quicksilver](https://github.com/quicksilver/Quicksilver))  
Copyright © 2009 Ryan McGeary (Author of [LiquidMetal](https://github.com/rmm5t/liquidmetal))  
Copyright © 2013 Grey Lee
