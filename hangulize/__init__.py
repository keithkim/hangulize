# -*- coding: utf-8 -*-
"""
hangulize
~~~~~~~~~

Korean Alphabet Transcription.
"""
import sys
import re
import unicodedata
from hangulize.hangul import *


encoding = getattr(sys.stdout, 'encoding', 'utf-8')


class Phoneme(object):
    """This abstract class wraps a Hangul letter."""

    def __init__(self, letter):
        self.letter = letter

    def __repr__(self):
        return "<%s '%s'>" % (type(self).__name__,
                              self.letter.encode(encoding))


class Choseong(Phoneme):
    """A initial consonant in Hangul.

        >>> Choseong(G)
        <Choseung 'ㄱ'>
    """
    pass

class Jungseong(Phoneme):
    """A vowel in Hangul.

        >>> Jungseong(A)
        <Jungseong 'ㅏ'>
    """
    pass

class Jongseong(Phoneme):
    """A final consonant in Hangul.

        >>> Jongseong(G)
        <Jongseong 'ㄱ'>
    """
    pass

class Impurity(Phoneme):
    """An impurity letter will be kept."""
    pass


class Notation(object):
    """Describes loanword orthography.

    :param *rule: the ordered key-value list
    """

    def __init__(self, *rule):
        self.rule = list(rule)

    def items(self, lang=None):
        """Yields each notation rules as regex."""
        for pattern, val in self.rule:
            yield self.regexify(pattern, lang), val

    @property
    def chars(self):
        """The humane characters from the notation keys."""
        chest = []
        for pattern, _ in self.rule:
            pattern = re.sub(r'[\{\}\@\[\]\^\$]', '', pattern)
            for c in pattern:
                chest.append(c)
        return set(chest)

    def regexify(self, pattern, lang=None):
        """Compiles a regular expression from the notation pattern."""
        regex = pattern
        if lang:
            vowels = ''.join([re.escape(v) for v in lang.vowels])
            regex = re.sub('@', vowels, regex)
        regex = re.sub('^{([^}]+?)}', r'(?<=[\1])', regex)
        regex = re.sub('{([^}]+?)}$', r'(?=[\1])', regex)
        return re.compile(regex)


class Language(object):
    """Wraps a foreign language. The language should have a :class:`Notation`
    instance.

        >>> class Extraterrestrial(Language):
        ...     notation = Notation(
        ...         (u'ㅹ', (Choseong(BB), Jungseong(U), Jongseong(NG))),
        ...         (u'㉠', (Choseong(G),)),
        ...         (u'ㅣ', (Jungseong(I),)),
        ...         (u'ㅋ', (Choseong(K), Jungseong(I), Jongseong(G)))
        ...     )
        ...
        >>> ext = Extraterrestrial()
        >>> print ext.hangulize(u'ㅹ㉠ㅣㅋㅋㅋ')
        뿡기킥킥킥

    :param logger: the logger object in the logging module
    """

    vowels = ()
    notation = None

    def __init__(self, logger=None):
        if not isinstance(self.notation, Notation):
            raise NotImplementedError("notation has to be defined")
        self.logger = logger

    @property
    def chars_pattern(self):
        """The regex pattern which is matched the valid characters."""
        return ''.join(re.escape(c) for c in self.notation.chars)

    def split(self, string):
        """Splits words from the string. Each words have only valid characters.
        """
        pattern = '[^%s]+' % self.chars_pattern
        return re.split(pattern, string)

    def transcribe(self, word):
        """Returns :class:`Phoneme` instance list from the word."""
        length = len(word)
        phonemes = [None] * length
        for pattern, val in self.notation.items(self):
            if isinstance(val, tuple):
                for match in pattern.finditer(word):
                    start, end = match.span()
                    phonemes[start] = val
                    del phonemes[start + 1:end]
                val = ' '
            elif not val:
                val = ''
            prev_word, prev_length = word, length
            word = pattern.sub(val, word)
            length = len(word)
            if length > prev_length:
                phonemes += [None] * (length - prev_length)
            if self.logger and word != prev_word:
                self.logger.info("-> '%s'" % word)
        return filter(None, phonemes)

    def normalize(self, string):
        """Before transcribing, normalizes the string. You could specify the
        different normalization for the language with overriding this method.
        """
        return string

    def hangulize(self, string):
        """Hangulizes the string.

            >>> from hangulize.langs.ja import Japanese
            >>> ja = Japanese()
            >>> ja.hangulize(u'あかちゃん')
            아카찬
        """
        def stringify(syllable):
            if isinstance(syllable[0], Impurity):
                return syllable[0].letter
            else:
                return join(syllable)
        string = self.normalize(string)
        if self.logger:
            self.logger.info("-> '%s'" % string)
        hangulized = []
        for word in self.split(string):
            phonemes = self.transcribe(word)
            if not phonemes:
                continue
            syllables = complete_syllables(reduce(list.__add__,
                                                  map(list, phonemes)))
            result = [stringify(syl) for syl in syllables]
            hangulized.append(''.join(result))
        return ' '.join(hangulized)


def normalize_roman(string):
    """Removes diacritics from the string and converts to lowercase.

        >>> normalize_roman(u'E\xe8\xe9') # Eèé
        u'eee'
    """
    return ''.join((c for c in unicodedata.normalize('NFD', string) \
                      if unicodedata.category(c) != 'Mn')).lower()


def complete_syllable(syllable):
    """Inserts the default jungseong or jongseong if it is not exists.

        >>> complete_syllable((Jungseong(YO),))
        (u'\u315b', u'\u3161', u'')
        >>> print join(_)
        요
    """
    syllable = list(syllable)
    components = [type(ph) for ph in syllable]
    if Choseong not in components:
        syllable.insert(0, Choseong(NG))
    if Jungseong not in components:
        syllable.insert(1, Jungseong(EU))
    if Jongseong not in components:
        syllable.insert(2, Jungseong(Null))
    return tuple((ph.letter for ph in syllable))


def complete_syllables(phonemes):
    """Separates each syllables and completes every syllable."""
    components, syllable = [Choseong, Jungseong, Jongseong, Impurity], []
    if phonemes:
        for ph in phonemes:
            comp = type(ph)
            new_syllable = syllable and components.index(comp) <= \
                           components.index(type(syllable[-1]))
            if new_syllable:
                yield complete_syllable(syllable)
                syllable = []
            syllable.append(ph)
        yield complete_syllable(syllable)


def split_phonemes(word):
    """Returns the splitted phonemes from the word.

        >>> split_phonemes(u'안녕') #doctest: +NORMALIZE_WHITESPACE
        (<Choseong 'ㅇ'>, <Jungseong 'ㅏ'>, <Jongseong 'ㄴ'>,
         <Choseong 'ㄴ'>, <Jungseong 'ㅕ'>, <Jongseong 'ㅇ'>)
    """
    result = []
    for c in word:
        c = split(c)
        result.append(Choseong(c[0]))
        result.append(Jungseong(c[1]))
        if c[2] is not Null:
            result.append(Jongseong(c[2]))
    return tuple(result)


def join_phonemes(phonemes):
    """Returns the word from the splitted phonemes.

        >>> print join_phonemes((Jungseong(A), Jongseong(N),
        ...                      Choseong(N), Jungseong(YEO), Jongseong(NG)))
        안녕
    """
    syllables = complete_syllables(phonemes)
    chars = (join(syl) for syl in syllables)
    return reduce(unicode.__add__, chars)


def hangulize(string, locale='it', lang=None, logger=None):
    """Hangulizes the string with the given locale or lang.

        >>> print hangulize(u'gloria', 'it')
        글로리아

    :param string: the loanword
    :param locale: the locale code. if ``lang`` is not given, it is required
    :param lang: the :class:`Language` instance
    :param logger: if the logger instance is given, reports result by each
                   steps
    """
    if not lang:
        module = __import__('%s.langs.%s' % (__name__, locale))
        lang = getattr(getattr(module.langs, locale), locale)(logger=logger)
    return lang.hangulize(string)
