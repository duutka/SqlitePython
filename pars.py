def parsFunc(dirFile):
    file = open(dirFile, 'r', encoding='utf-8').read().replace(' and ', ',').split('\n@')
    for note in file:
        dictAttr = parsAttributes(note)
        if note.startswith('Article'):
            parsArcticle(dictAttr)
        if note.startswith('Book'):
            parsBook(dictAttr)
        if note.startswith('Booklet'):
            parsBooklet(dictAttr)
        if note.startswith('Conference'):
            parsConference(dictAttr)
    return

def parsAttributes(bibTex):
    import re
    dictAttr = dict.fromkeys(
        ['Author', 'Journal', 'Pages',  'Title',  'Volume', 'Year', 'Language'])
    # Основные атрибуты
    author = re.search(r"\s*Author\s*=\s*{\s?(?P<author>\S.*\s?)}", bibTex)
    if author:
        dictAttr['Author'] = author.group('author')
    journal = re.search(r"\s*Journal\s*=\s*{\s?(?P<journal>\S.*\s?)}", bibTex)
    if journal:
        dictAttr['Journal'] = journal.group('journal')
    pages = re.search(r"\s*Pages\s*=\s*{\s?(?P<pages>\S.*\s?)}", bibTex)
    if pages:
        dictAttr['Pages'] = pages.group('pages')
    title = re.search(r"\s*Title\s*=\s*{\s?(?P<title>\S.*\s?)}", bibTex)
    if title:
        dictAttr['Title'] = title.group('title')
    volume = re.search(r"\s*Volume\s*=\s*{\s?(?P<volume>\S.*\s?)}", bibTex)
    if volume:
        dictAttr['Volume'] = volume.group('volume')
    year = re.search(r"\s*Year\s*=\s*{\s?(?P<year>\S.*\s?)}", bibTex)
    if year:
        dictAttr['Year'] = year.group('year')
    # Дополнительные атрибуты
    language = re.search(r"\s*Language\s*=\s*{\s?(?P<language>\S.*\s?)}", bibTex)
    if language is None:
        dictAttr['Language'] = 'English'
    else:
        dictAttr['Language'] = language.group('language')
    return dictAttr


def parsArcticle(dictAttr):
    file = open(r'D:\work\python\parsing.txt', 'a+', encoding='utf-8')
    if str(dictAttr['Language']).startswith('russian'):
        file.write('{0} {1} // {2}{3}. -Вып.{4}.-С{5}\n\n'.format(dictAttr.get('Author'), dictAttr.get('Title'),
                                                                  dictAttr.get('Journal'), dictAttr.get('Year'),
                                                                  dictAttr.get('Volume'), dictAttr.get('Pages')))
    else:
        file.write('{0} {1} // {2}{3}. -Vol.{4}.-P{5}.\n\n'.format(dictAttr.get('Author'), dictAttr.get('Title'),
                                                                   dictAttr.get('Journal'), dictAttr.get('Year'),
                                                                   dictAttr.get('Volume'), dictAttr.get('Pages')))
    return


def parsBook(dictAttr):
    file = open(r'D:\work\python\parsing.txt', 'a+', encoding='utf-8')
    if str(dictAttr['Language']).startswith('russian'):
        file.write('{0} {1} // {2}{3}. -С{4}\n\n'.format(dictAttr.get('Author'), dictAttr.get('Title'),
                                                                  dictAttr.get('Publisher'), dictAttr.get('Year'),
                                                                  dictAttr.get('Numpages')))
    else:
        file.write('{0} {1} // {2}{3}. -P{4}.\n\n'.format(dictAttr.get('Author'), dictAttr.get('Title'),
                                                                   dictAttr.get('Publisher'), dictAttr.get('Year'),
                                                                   dictAttr.get('Numpages')))
    return


def parsBooklet(dictAttr):
    file = open(r'D:\work\python\parsing.txt', 'a+', encoding='utf-8')
    if str(dictAttr['Language']).startswith('russian'):
        file.write('{0}:[Booklet].-{1} // {2},{3}. -{4} л.\n\n'.format(dictAttr.get('Title'), dictAttr.get('Note'),
                                                                  dictAttr.get('Journal'), dictAttr.get('Year'),
                                                                             dictAttr.get('Pages')))

    else:
        file.write('{0}:[Буклет].-{1} // {2},{3}. -{4} л.\n\n'.format(dictAttr.get('Title'), dictAttr.get('Note'),
                                                                             dictAttr.get('Journal'),
                                                                             dictAttr.get('Year'), dictAttr.get('Pages')))

    return


def parsConference(dictAttr):
    file = open(r'D:\work\python\parsing.txt', 'a+', encoding='utf-8')
    if str(dictAttr['Language']).startswith('russian'):
        file.write('{0} {1} // {2}{3}.\n\n'.format(dictAttr.get('Author'), dictAttr.get('Title'),
                                                                  dictAttr.get('Booktitle'), dictAttr.get('Year')
                                                                ))
    else:
        file.write('{0} {1} // {2}{3}.\n\n'.format(dictAttr.get('Author'), dictAttr.get('Title'),
                                                                   dictAttr.get('Booktitle'), dictAttr.get('Year')
                                                                   ))
    return


parsFunc(r'D:\work\python\biblio.bib')
