P20N: Programmer Abbreviation
====

Usage:

    > python p20n.py word_1 [word_2 [... word_n]]

Examples:

    > python p20n.py internationalization globalization localization personalization multilingualization
    internationalization    i18n
    globalization           g11n
    localization            l10n
    personalization         p13n
    multilingualization     m17n

    > python p20n.py _ u uv uvw uvwx uvwxy
    _
    u        u
    uv       u0v
    uvw      u1w
    uvwx     u2x
    uvwxy    u3y

    > python p20n.py programmer_abbreviation
    programmer_abbreviation    p20n
