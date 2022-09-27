# import re
#
#
# def word_base_data_process(text):
#     # 转为小写
#     text = text.strip().lower()
#
#     # 乱码清洗
#     text = text.encode('ascii', 'ignore').decode()
#
#     # 缩写替换
#     text = re.sub(r"’re", " are", text)
#     text = re.sub(r"’ve", " have", text)
#     text = re.sub(r"’m", " am", text)
#     text = re.sub(r"’d", " would", text)
#     text = re.sub(r"’ll", " will", text)
#     text = re.sub(r"’t", " not", text)
#
#     # 数字清洗
#     text = re.sub(r"0", " zero ", text)
#     text = re.sub(r"1", " one ", text)
#     text = re.sub(r"2", " two ", text)
#     text = re.sub(r"3", " three ", text)
#     text = re.sub(r"4", " four ", text)
#     text = re.sub(r"5", " five ", text)
#     text = re.sub(r"6", " six ", text)
#     text = re.sub(r"7", " seven ", text)
#     text = re.sub(r"8", " eight ", text)
#     text = re.sub(r"9", " nine ", text)
#
#     # 符号清洗
#     text = re.sub(r"\+", "", text)
#     text = re.sub(r"'", "", text)
#     text = re.sub(r"-", "", text)
#     text = re.sub(r"/", "", text)
#     text = re.sub(r"\\", "", text)
#     text = re.sub(r"=", "", text)
#     text = re.sub(r"\^", "", text)
#     text = re.sub(r":", "", text)
#     text = re.sub(r"\.", "", text)
#     text = re.sub(r",", "", text)
#     text = re.sub(r"\?", "", text)
#     text = re.sub(r"!", "", text)
#     text = re.sub(r"\"", "", text)
#     text = re.sub(r"&", "", text)
#     text = re.sub(r"\|", "", text)
#     text = re.sub(r";", "", text)
#     text = re.sub(r"\(", "", text)
#     text = re.sub(r"\)", "", text)
#     text = re.sub(r"”", "", text)
#     text = re.sub(r"“", "", text)
#     text = re.sub(r"’", "", text)
#     text = re.sub(r"%", "", text)
#     text = re.sub(r"’s", "", text)
#
#     # 符号替换
#     text = re.sub(r"&", " and ", text)
#     text = re.sub(r"\|", " or ", text)
#     text = re.sub(r"=", " equal ", text)
#     text = re.sub(r"\$", " dollar ", text)
#
#     return text
#
#
# print("="*10+ "开始处理" + "="*10)
# train_data = open("./news.train", 'r', encoding="utf-8").read()
# # 去除非字母符号和常用缩写
# train_data = word_base_data_process(train_data)
# train_data = train_data.replace("  "," ").replace("  "," ").replace("  "," ")
# # train_data = ' '.join(train_data.split())
#
# with open("news_word.train", "w", encoding="utf-8") as f:
#     f.write(train_data)
#
# print("news_word.train 处理完毕")
#
# test_data = open("./news.test", 'r', encoding="utf-8").read()
# # 去除非字母符号和常用缩写
# test_data = word_base_data_process(test_data)
# test_data = test_data.replace("  "," ").replace("  "," ").replace("  "," ")
# # test_data = ' '.join(test_data.split())
# with open("news_word.test", "w", encoding="utf-8") as f:
#     f.write(test_data)
#
# print("news_word.test 处理完毕")
#
# train_data = open("./news.train", 'r', encoding="utf-8").read()
# # 数据清洗
# train_data = word_base_data_process(train_data)
# train_data = re.sub("(.)", r'\1 ', train_data)
# train_data = train_data.replace("  "," ").replace("  "," ").replace("  "," ")
# # train_data = ' '.join(train_data.split())
#
# with open("news_character.train", "w", encoding="utf-8") as f:
#     f.write(train_data)
#
# print("news_character.train 处理完毕")
#
# test_data = open("./news.test", 'r', encoding="utf-8").read()
# # 数据清洗
# test_data = word_base_data_process(test_data)
# test_data = re.sub("(.)", r'\1 ', test_data)
# test_data = test_data.replace("  "," ").replace("  "," ").replace("  "," ")
# # test_data = ' '.join(test_data.split())
# with open("news_character.test", "w", encoding="utf-8") as f:
#     f.write(test_data)
#
# print("news_character.test 处理完毕")
#
# data = open("./europarl-v7.en", 'r', encoding="utf-8").read()
# # 数据清洗
# data = word_base_data_process(data)
# data = re.sub("(.)", r'\1 ', data)
# data = data.replace("  "," ").replace("  "," ").replace("  "," ")
# # data = ' '.join(data.split())
# with open("europarl_character.en", "w", encoding="utf-8") as f:
#     f.write(data)
#
# print("europarl_character.en 处理完毕")
#
# data = open("./europarl-v7.en", 'r', encoding="utf-8").read()
# # 数据清洗
# data = word_base_data_process(data)
# data = data.replace("  "," ").replace("  "," ").replace("  "," ")
# # data = ' '.join(data.split())
# with open("europarl_word.en", "w", encoding="utf-8") as f:
#     f.write(data)
#
# print("europarl_word.en 处理完毕")
#
# print("="*10+ "All process finished!" + "="*10)


data1 = open("./news_word.train", 'r', encoding="utf-8").read()
data2 = open("./europarl_word.en", 'r', encoding="utf-8").read()
with open("news+europarl_word.train", "w", encoding="utf-8") as f:
    f.write(data1)
    f.write(data2)

data1 = open("./news_character.train", 'r', encoding="utf-8").read()
data2 = open("./europarl_character.en", 'r', encoding="utf-8").read()
with open("news+europarl_character.train", "w", encoding="utf-8") as f:
    f.write(data1)
    f.write(data2)

