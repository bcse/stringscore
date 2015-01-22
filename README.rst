===============================
String Score
===============================

.. image:: https://img.shields.io/pypi/v/stringscore.svg?style=flat-square
    :alt: PyPI version

.. image:: https://img.shields.io/travis/bcse/stringscore/master.svg?style=flat-square
    :alt: Build Status
    :target: https://travis-ci.org/bcse/stringscore

.. image:: https://img.shields.io/coveralls/bcse/stringscore/master.svg?style=flat-square
    :alt: Coverage Status
    :target: https://coveralls.io/r/bcse/stringscore

.. image:: https://img.shields.io/pypi/dm/stringscore.svg?style=flat-square
    :alt: Downloads

.. image:: https://img.shields.io/pypi/l/stringscore.svg?style=flat-square
    :alt: License


An algorithm provides scores between 0.0 (no match) to 1.0 (perfect match) for a comparison of two strings.

The algorithm is designed for auto-completion. For string similarity, please check `Levenshtein distance`_ (`Wagner–Fischer algorithm`_).

.. _Levenshtein distance: https://en.wikipedia.org/wiki/Levenshtein_distance
.. _Wagner–Fischer algorithm: https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm

Usage
-----

Include the library:

::

    from stringscore import liquidmetal


Score any string against an abbreviation:

::

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


Similar Works
-------------

* Quicksilver's scoreForAbbreviation_ algorithm by Alcor (Blacktree, Inc)
* LiquidMetal_ by Ryan McGeary
* string_score_ by Joshaven Potter
* `jQuery.fuzzyMatch`_ by Rapportive_

.. _scoreForAbbreviation: https://github.com/quicksilver/Quicksilver/blob/master/Quicksilver/Code-QuickStepFoundation/NSString_BLTRExtensions.m#L53
.. _LiquidMetal: https://github.com/rmm5t/liquidmetal
.. _string_score: https://github.com/joshaven/string_score
.. _jQuery.fuzzyMatch: https://github.com/rapportive-oss/jquery-fuzzymatch
.. _Rapportive: http://rapportive.com/

License
-------

String Score is released under the `MIT License`_.

.. _MIT License: http://opensource.org/licenses/MIT

Credits
-------

| Copyright © 2003 Blacktree, Inc (Original author of Quicksilver_)
| Copyright © 2009 Ryan McGeary (Author of LiquidMetal_)
| Copyright © 2013 Grey Lee

.. _Quicksilver: https://github.com/quicksilver/Quicksilver

.. image:: https://cruel-carlota.pagodabox.com/430816d5202dd8dcd04ffca1091894de
    :target: http://githalytics.com/bcse/stringscore

.. image:: https://d2weczhvl823v0.cloudfront.net/bcse/stringscore/trend.png
    :target: https://bitdeli.com/free
