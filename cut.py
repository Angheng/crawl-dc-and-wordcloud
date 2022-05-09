import crawl_web
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import webbrowser


def get_tags(text, ntags=120, multiplier=10):
    raw = ' '.join(x['title'] for x in text)
    nouns = okt.nouns(raw)
    counter = Counter(nouns)
    result = counter.most_common(ntags)

    for i in range(len(result) - 1, -1, -1):
        print(result[i][0])
        if len(result[i][0]) == 1 and result[i][0]:
            result.pop(i)

    return result


def draw_cloud(tags, filename):
    wc = WordCloud(width=1024, height=768, font_path='fonts/NanumSquareRoundEB.ttf',
                   background_color='white', max_font_size=400, prefer_horizontal=0.999)
    cloud = wc.generate_from_frequencies(dict(tags))
    cloud.to_file(filename)

    webbrowser.open(filename)


if __name__ == '__main__':
    cr = crawl_web.Crawl()
    cr.set_url(input('> inset url : '))
    okt = Okt()

    test = cr.crawl_pageBase(int(input('> How many pages : ')))
    file_name = input('> output file name')

    tags = get_tags(test)

    draw_cloud(tags, file_name + '.png')
