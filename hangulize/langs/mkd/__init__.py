# -*- coding: utf-8 -*-
from hangulize import *


class Macedonian(Language):
    """For transcribing Macedonian."""

    __iso639__ = {1: 'mk', 2: 'mac', 3: 'mkd'}
    __tmp__ = ',;'

    vowels = u'аеиоу'
    cs = u'бвгдѓжзѕклљмнњпрстќфхцчџш'
    vl = u'кпстќфхцчш'
    notation = Notation([
        (u'град', u'град-'),
        (u'ѓураѓ', u'џураџ'),
        (u'срѓан', u'срџан'),
        (u'бб', u'б'),
        (u'вв', u'в'),
        (u'вф', u'ф'),
        (u'гг', u'г'),
        (u'дд', u'д'),
        (u'дж', u'џ'),
        (u'дц', u'ц'),
        (u'дч', u'ч'),
        (u'жж', u'ж'),
        (u'зз', u'з'),
        (u'зс', u'с'),
        (u'кк', u'к'),
        (u'лл', u'л'),
        (u'{@}мм{@}', u'м,м'),
        (u'мм', u'м'),
        (u'{@}нн{@}', u'н,н'),
        (u'нн', u'н'),
        (u'пп', u'п'),
        (u'рр', u'р'),
        (u'сс', u'с'),
        (u'тт', u'т'),
        (u'тц', u'ц'),
        (u'тч', u'ч'),
        (u'фф', u'ф'),
        (u'хх', u'х'),
        (u'цц', u'ц'),
        (u'чч', u'ч'),
        (u'шш', u'ш'),
        (u'шч', u'ш'),
        (u'{ѓ|ж|з|ѕ|ќ|ц|ч|џ|ш}ј{@}', None),
        (u'иј{<cs>}', u'и'),
        (u'иј$', u'и'),
        (u'дз$', u'ѕ'),
        (u'дз{<cs>}$', u'ѕ'),
        (u'дс$', u'ц'),
        (u'дс{<cs>}', u'ц'),
        (u'тс', u'ц'),
        (u'дз', u'з'),
        (u'тз', u'з'),
        (u'нкт', u'Nт'),
        (u'б{<vl>}', u'п'),
        (u'б$', u'п'),
        (u'в{<vl>}', u'ф'),
        (u'в$', u'ф'),
        (u'г{<vl>}', u'к'),
        (u'г$', u'к'),
        (u'д{<vl>}', u'т'),
        (u'д$', u'т'),
        (u'ж{<vl>}', u'ш'),
        (u'ж$', u'ш'),
        (u'з{<vl>}', u'с'),
        (u'з$', u'с'),
        (u'ѕ{<vl>}', u'ц'),
        (u'ѕ$', u'ц'),
        (u'џ{<vl>}', u'ч'),
        (u'џ$', u'ч'),
        (u'ѓ{<vl>}', u'ќ'),
        (u'ѓ$', u'ќ'),
        (u'б{<vl>}', u'п'),
        (u'в{<vl>}', u'ф'),
        (u'г{<vl>}', u'к'),
        (u'д{<vl>}', u'т'),
        (u'ж{<vl>}', u'ш'),
        (u'з{<vl>}', u'с'),
        (u'ѕ{<vl>}', u'ц'),
        (u'џ{<vl>}', u'ч'),
        (u'ѓ{<vl>}', u'ќ'),
        (u'{@}к{<vl>}', u'к,'),
        (u'{@}п{<vl>}', u'п,'),
        (u'{<cs>}ј{@}', u'и'),
        (u'ѓ{а|о|у}', u'гј'),
        (u'ѓ{е|и}', u'г'),
        (u'ѓ', u'ѕи'),
        (u'ќ{а|о|у}', u'кј'),
        (u'ќ{е|и}', u'к'),
        (u'ќ', u'ци'),
        (u'љ{а|о|у}', u'лј'),
        (u'љ', u'л'),
        (u'њ{а|о|у}', u'нј'),
        (u'њ', u'н'),
        (u'ж{@}', u'з'),
        (u'ж', u'зу'),
        (u'ч{@}', u'ц'),
        (u'ч', u'чи'),
        (u'џ{@}', u'ѕ'),
        (u'џ', u'ѕи'),
        (u'ш{@}', u'сј'),
        (u'ш$', u'си'),
        (u'ш', u'сју'),
        (u'^л', u'л;'),
        (u'^м', u'м;'),
        (u'^н', u'н;'),
        (u'л$', u'л,'),
        (u'м$', u'м,'),
        (u'н$', u'н,'),
        (u'л{@|ј|м,|н,|N}', u'л;'),
        (u'м{@}', u'м;'),
        (u'н{@|ј}', u'н;'),
        (u'л', u'л,'),
        (u'м', u'м,'),
        (u'н', u'н,'),
        (u',,', u','),
        (u',;', None),
        (u',л,', u'л,'),
        (u',м,', u'м,'),
        (u',н,', u'н,'),
        (u'л{м;|н;}', u'л,'),
        (u';|-', None),
        (u'б', Choseong(B)),
        (u'в', Choseong(B)),
        (u'г', Choseong(G)),
        (u'д', Choseong(D)),
        (u'ж', Choseong(J)),
        (u'з', Choseong(J)),
        (u'ѕ', Choseong(J)),
        (u'ж', Choseong(J)),
        (u'к,', Jongseong(G)),
        (u'к', Choseong(K)),
        (u'^л', Choseong(L)),
        (u'{,}л', Choseong(L)),
        (u'л,', Jongseong(L)),
        (u'л', Jongseong(L), Choseong(L)),
        (u'м,', Jongseong(M)),
        (u'м', Choseong(M)),
        (u'н,', Jongseong(N)),
        (u'н', Choseong(N)),
        (u'N', Jongseong(NG)),
        (u'п,', Jongseong(B)),
        (u'п', Choseong(P)),
        (u'р', Choseong(L)),
        (u'с', Choseong(S)),
        (u'т', Choseong(T)),
        (u'ф', Choseong(P)),
        (u'х', Choseong(H)),
        (u'ц', Choseong(C)),
        (u'ч', Choseong(C)),
        (u'ја', Jungseong(YA)),
        (u'је', Jungseong(YE)),
        (u'ји', Jungseong(I)),
        (u'јо', Jungseong(YO)),
        (u'ју', Jungseong(YU)),
        (u'ј', Jungseong(I)),
        (u'а', Jungseong(A)),
        (u'е', Jungseong(E)),
        (u'и', Jungseong(I)),
        (u'о', Jungseong(O)),
        (u'у', Jungseong(U))
    ])

    def normalize(self, string):
        return normalize_roman(string, {
            u'А': u'а', u'Б': u'б', u'В': u'в', u'Г': u'г', u'Д': u'д',
            u'Ѓ': u'ѓ', u'Е': u'е', u'Ж': u'ж', u'З': u'з', u'Ѕ': u'ѕ',
            u'И': u'и', u'Ј': u'ј', u'К': u'к', u'Л': u'л', u'Љ': u'љ',
            u'М': u'м', u'Н': u'н', u'Њ': u'њ', u'О': u'о', u'П': u'п',
            u'Р': u'р', u'С': u'с', u'Т': u'т', u'Ќ': u'ќ', u'У': u'у',
            u'Ф': u'ф', u'Х': u'х', u'Ц': u'ц', u'Ч': u'ч', u'Џ': u'џ',
            u'Ш': u'ш'
            })


__lang__ = Macedonian