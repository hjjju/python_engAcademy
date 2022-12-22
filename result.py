



# parsed = parser.from_file(txt_path)
# print(type(parsed))
# pp(parsed)
# f = open(txt_path,'r',encoding='UTF-8')

# while 1:
#     line = f.readline();
#     if not line : 
#      break

#     print(line)

# 한줄씩 출력
# lines = f.readlines()
# for i in lines:
#     print(lines)

# 리스트형식으로 가져옴
# lines = f.readlines()
# print(lines)

# 읽어와서 문자열로 반환
# rd = f.read()
# print(rd)

# lines = f.readlines()

from tika import parser
from pprint import pprint as pp
import re

text_file_path = "400_3.txt" 
new_text_content = ''
target_word1 = 'ㅁㅁ'
new_word = ''

with open(text_file_path,'r',encoding='utf-8') as f:
     ## 기존 텍스트파일에 대한 내용을 모두 읽는다.
    lines = f.readlines()
    for i, l in enumerate(lines):
        # new_string = l.strip().replace(target_word1,new_word)
        new_string =  l.strip().replace(target_word1,'')
        new_string = re.sub("[ㄱ-ㅎ]|口*|□□",'',new_string)
        if new_string:
            new_text_content += new_string + '\n'
        else:
            new_text_content += '\n'
                
with open(text_file_path,'w',encoding='utf-8') as f:
    f.write(new_text_content)

