# -*- coding: utf-8 -*-
from hangulize import *


class German(Language):
    """For transcribing German."""
    
    vowels = u'aeiouäöüyAOU'
    cons = u'bcdfghjklmnpqrstvwxzß'
    notation = Notation(
        (u'ä',            'A'),
        (u'ö',            'O'),
        (u'ü',            'y'),
        ('{a|A|e}ue',     'au.e'),
        ('ae',            'A'),
        ('oe',            'O'),
        ('ue',            'y'),
        ('berg$',         'bErk'),
        ('burg$',         'burk'),
        ('bundes',        'bundeS'),
        ('x',             'ks'),
        ('b$',            'p'),
        ('d$',            't'),
        ('sch',           'Z'),
        ('{a|o|u}ch',     'X'),
        ('ch',            'x'),
        ('{@}g$',         'x'),
        ('{@}h{<cons>}',  None),
        ('{@}h$',         None),
        ('rr',            'r'),
        ('ll',            'l'),
        ('er$',           'U'),
        ('{@}r$',         'U'),
        ('eu',            'oi'),
        ('Au',            'oi'),
        ('ie',            'i'),
        ('ei',            'ai'),
        ('nn',            'n'),
        ('mm',            'm'),
        ('tt',            't'),
        ('pp',            'p'),
        ('aa',            'a'),
        ('ee',            'e'),
        ('ph',            'f'),
        ('pf',            'f'),
        ('th',            't'),
        ('kh',            'k'),
        ('dt',            't'),
        ('ck',            'k'),
        ('c{A|e|i|y}',    'C'),
        ('c',             'k'),
        ('C',             'c'),
        ('tz',            'z'),
        ('ng{@|l}',       'Ng'),
        ('ng',            'N'),
        ('ss',            'S'),
        (u'ß',            'S'),
        ('{@}st',         'St'),
        ('ts',            'c'),
        ('s$',            'S'),
        ('s{<cons>}',     'Z'),
        ('tZ',            'T'),
        ('Z{@}',          'Sj'),
        ('Z$',            'Sju'),
        ('Z{<cons>}',     'Sju'),
        ('T{@}',          'cj'),
        ('T$',            'cj'),
        ('T{<cons>}',     'cj'),
        ('x{<cons>}',     'xi'),
        ('x$',            'xi'),
        ('^U$',           (Jungseong(E),Jungseong(EO))),
        ('{^(<cons>)}U$', (Jungseong(E),Jungseong(EO))),
        ('X',             (Choseong(H),)), # achlaut
        ('x',             (Choseong(H),)), # ichlaut
        ('b',             (Choseong(B),)),
        ('c',             (Choseong(C),)),
        ('d',             (Choseong(D),)),
        ('f',             (Choseong(P),)),
        ('g',             (Choseong(G),)),
        ('k',             (Choseong(K),)),
        ('{@}l{@}',       (Jongseong(L), Choseong(L))),
        ('^l',            (Choseong(L),)),
        ('l{@}',          (Jongseong(L), Choseong(L))),
        ('l',             (Jongseong(L),)),
        ('m{@}',          (Choseong(M),)),
        ('m',             (Jongseong(M),)),
        ('n{@}',          (Choseong(N),)),
        ('n',             (Jongseong(N),)),
        ('N',             (Jongseong(NG),)),
        ('h',             (Choseong(H),)),
        ('p',             (Choseong(P),)),
        ('r',             (Choseong(L),)),
        ('s',             (Choseong(J),)),
        ('S',             (Choseong(S),)),
        ('t',             (Choseong(T),)),
        ('v',             (Choseong(P),)),
        ('w',             (Choseong(B),)),
        ('z',             (Choseong(C),)),
        ('ja',            (Jungseong(YA),)),
        ('je',            (Jungseong(YE),)),
        ('ji',            (Jungseong(I),)),
        ('jo',            (Jungseong(YO),)),
        ('ju',            (Jungseong(YU),)),
        ('jy',            (Jungseong(WI),)),
        ('jO',            (Jungseong(OE),)),
        ('jA',            (Jungseong(YE),)),
        ('jU',            (Jungseong(YEO),)),
        ('U',             (Jungseong(EO),)),
        ('a',             (Jungseong(A),)),
        ('e',             (Jungseong(E),)),
        ('E',             (Jungseong(E),)),
        ('i',             (Jungseong(I),)),
        ('o',             (Jungseong(O),)),
        ('u',             (Jungseong(U),)),
        ('A',             (Jungseong(E),)),
        ('O',             (Jungseong(OE),)),
        ('y',             (Jungseong(WI),)),
        ('j',             (Jungseong(I),)),
    )

    def normalize(self, string):
        def normalize_only_unsafe(string):
            map = {u'Ä': u'ä', u'Ö': u'ö', u'Ü': u'ü'}
            safe = map.keys() + map.values() + [u'ß']
            for c in string:
                if c not in safe:
                    yield normalize_roman(c)
                elif c in map:
                    yield map[c]
                else:
                    yield c
        return ''.join(normalize_only_unsafe(string))


de = German