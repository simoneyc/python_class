# -*- coding: utf-8 -*-

s = 'Twinkle, twinkle, little star! \
How I wonder what you are, Up above the world so high, \
    Like a diamond in the sky. When the blazing sun is gone, \
        When he nothing shines upon, Then you show your little light, \
            Twinkle, twinkle all the night. '

s = s.replace('!', '').replace(',', '').replace('.', '').replace('?', '').lower()
words = s.split()

# 字典
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)





