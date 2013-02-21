String Score
============

Port of [LiquidMetal](https://github.com/rmm5t/liquidmetal) from JavaScript to Python.

An algorithm provides scores between 0.0 (no match) to 1.0 (perfect match) for a comparison of two strings.

Usage
-----

Include the library:

```python
import stringscore
```

Score any string against an abbreviation:

```python
>>> stringscore.score('FooBar',  'foo')
0.95
>>> stringscore.score('FooBar',  'fb')
0.916666666667
>>> stringscore.score('Foo Bar', 'fb')
0.928571428571
>>> stringscore.score('Foo Bar', 'baz')
0.0
>>> stringscore.score('Foo Bar', '')
0.8
```

Similar Works
-------------

- Quicksilver's [scoreForAbbreviation](https://github.com/quicksilver/Quicksilver/blob/master/Quicksilver/Code-QuickStepFoundation/NSString_BLTRExtensions.m#L53) algorithm by Alcor
- [string_score](https://github.com/joshaven/string_score) by Joshaven Potter

License
-------

String Score is released under the [MIT License](http://opensource.org/licenses/MIT).

Credits
-------

Copyright © 2009 Ryan McGeary (Author of [LiquidMetal](https://github.com/rmm5t/liquidmetal))
Copyright © 2013 Grey Lee