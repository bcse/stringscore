"""
String Score
~~~~~~~~~~~~

Port of [LiquidMetal](https://github.com/rmm5t/liquidmetal) from JavaScript to Python.

An algorithm provides scores between 0.0 (no match) to 1.0 (perfect match) for a comparison of two strings.

:copyright: (c) 2013 by Grey Lee.
:license: MIT License.
"""

__version__ = '1.2.1'
__author__ = 'Grey Lee <bcse@bcse.tw>'


SCORE_NO_MATCH = 0.0
SCORE_MATCH = 1.0
SCORE_TRAILING = 0.8
SCORE_TRAILING_BUT_STARTED = 0.9
SCORE_BUFFER = 0.85
WORD_SEPARATORS = ' \t_-'


def score(string, abbrev):
    # short circuits
    if len(string) < len(abbrev):
        # string, abbrev = abbrev, string
        return SCORE_NO_MATCH

    if len(abbrev) == 0:
        return SCORE_TRAILING

    # match & score all
    all_scores = _score_all(string, string.lower(), abbrev.lower())

    # complete miss
    if len(all_scores) == 0:
        return SCORE_NO_MATCH

    # sum per-character scores into overall scores,
    # selecting the maximum score
    max_score = 0.0
    for i in range(len(all_scores)):
        scores = all_scores[i]
        score_sum = sum(scores)
        if score_sum > max_score:
            max_score = score_sum

    # normalize max score by string length
    # s. t. the perfect match score = 1
    max_score /= len(string)

    # record maximum score & score array, return
    return max_score


def _score_all(string, search, abbrev):
    all_scores = []  # collection of scores for complete matches
    scores = [None] * len(string)  # per-char scores, for accumulating complete scores

    # initialize the search for the first char at the beginning
    # abbr_indices: index of the abbrev char to match
    # search_indices: starting index for search string match
    # fill_indices: index from which to fill-in score updates
    match_abbr_indices = [0]
    match_search_indices = [-1]
    match_fill_indices = [0]

    # match & score all sequences of the abbrev chars
    while (len(match_abbr_indices) > 0):
        abbr_index = match_abbr_indices.pop()
        search_index = match_search_indices.pop()
        fill = match_fill_indices.pop()

        # cancel match if char is missing
        try:
            index = search.index(abbrev[abbr_index], search_index + 1)
        except ValueError:
            continue

        # score this match according to context
        if is_new_word(string, index):
            if index > 0:
                scores[index - 1] = SCORE_MATCH
                fill_array(scores, SCORE_BUFFER, fill, index - 1)
        elif is_upper_case(string, index):
            fill_array(scores, SCORE_BUFFER, fill, index)
        else:
            fill_array(scores, SCORE_NO_MATCH, fill, index)
        scores[index] = SCORE_MATCH

        # queue up next search for this char
        match_abbr_indices.append(abbr_index)
        match_search_indices.append(index)
        match_fill_indices.append(fill)

        # continue search or complete match and score
        if abbr_index != len(abbrev) - 1:
            # continue search, advancing to next abbrev char
            match_abbr_indices.append(abbr_index + 1)
            match_search_indices.append(index)
            match_fill_indices.append(index + 1)
        else:
            # all abbrev chars have been matched, complete score and record
            # add trailing score for the remainder of the match
            started = (search[0] == abbrev[0])
            trail_score = SCORE_TRAILING_BUT_STARTED if started else SCORE_TRAILING
            if None in scores:
                begin = scores.index(None)
                end = len(scores) - scores[::-1].index(None)
                fill_array(scores, trail_score, begin, end)
            # save score clone (since reference is persisted in scores)
            all_scores.append(scores[:])

    return all_scores


def is_upper_case(string, index):
    c = string[index]
    return 'A' <= c <= 'Z'


def is_new_word(string, index):
    c = string[index - 1] if index > 0 else ''
    return c in WORD_SEPARATORS


def fill_array(array, value, begin, end):
    if end > begin:
        array[begin:end] = [value] * (end - begin)


if __name__ == '__main__':
    from time import clock
    t0 = clock()
    test_string = 'a'
    for string in open('/usr/share/dict/words'):
        abbrev = test_string
        test_string = string
        if len(abbrev) > len(string):
            string, abbrev = abbrev, string
        score(string, abbrev)
    print 'Benchmark: %ss' % (clock() - t0)
