import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud,ImageColorGenerator
'''���´���ӽ�stopwords�ļ�'''

def addstopword(filepath):
    target = r"stopwords/stopwords.txt"
    f0 = open(target, "r", encoding="UTF-8")
    stopwords = [line for line in f0.readlines()]
    print(stopwords)
    f0.close()
    with open(filepath, "r", encoding="UTF-8") as f1, open(target, "a+", encoding="UTF-8") as f0:
        i = 0
        for line in f1.readlines():
            if line in stopwords:
                pass
            else:
                f0.write(line)
                i += 1
        print(i)

def wordsplit(target,source,result):
    f = open(target, "r", encoding="UTF-8")
    stopwords = [line.strip() for line in f.readlines()]
    f.close()
    f0 = open(source, "r", encoding="UTF-8")
    f1 = open(result, "w", encoding="UTF-8")
    re_word = {}
    i = 0
    jieba.add_word("��Ľ��")
    for line in f0.readlines():
        word = jieba.cut(line.strip(), cut_all=False, HMM=True)
        for a in word:
            if a not in stopwords:
                if a in re_word:
                    re_word[a] += 1
                else:
                    re_word[a] = 1
        #i += 1
        #if i == 100: break
    re_word = sorted(re_word.items(), key=lambda d: d[1], reverse=True)
    for k in re_word:
        if len(k[0]) > 1: f1.write(" ".join(map(str, k))+'\n')
        # print(" ".join(map(str,k)),len(k[0]))
    f0.close()
    f1.close()


if __name__ == "__main__":

    target = r"stopwords/stopwords.txt"
    source = r"stopwords/test.txt"
    result = r"stopwords/result.txt"
    image = r"image/xn.jpg"

    f = open(target, "r", encoding="UTF-8")
    stopwords = [line.strip() for line in f.readlines()]
    f.close()
    f0 = open(source, "r", encoding="UTF-8")
    f1 = open(result, "w", encoding="UTF-8")
    re_word = {}
    #i = 0
    jieba.add_word("��Ľ��")
    for line in f0.readlines():
        word = jieba.cut(line.strip(), cut_all=False, HMM=True)
        for a in word:
            if a not in stopwords:
                if a in re_word:
                    re_word[a] += 1
                else:
                    re_word[a] = 1
        #i += 1
        #if i == 1000: break
    f0.close()
    f1.close()
##############��ͼ############################################
    img = np.array(Image.open(image))
    my_wordcloud = WordCloud(
        background_color='white',  # ���ñ�����ɫ
        mask=img,  # ����ͼƬ
        max_words=200,  # ���������ʾ�Ĵ���
        font_path=r'C:/Windows/Fonts/STFANGSO.ttf',
        max_font_size=100,  # �����������ֵ
        random_state=50,  # �����������״̬������������ɫ����
    ).fit_words(re_word)   #generate(word_space)
    iamge_colors = ImageColorGenerator(img)
    plt.imshow(my_wordcloud)
    plt.axis('off')
    #plt.show()
    my_wordcloud.to_file('image/xn.png')







