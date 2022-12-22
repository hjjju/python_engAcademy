from tika import parser
## 특수문자 다루기
import re
# pdf경로
pdf_path = "400_2.pdf" 
# 경로읽기
parsed = parser.from_file(pdf_path)

txt = open('400_2.txt', 'w', encoding = 'utf-8')
print(parsed['content'], file = txt)
txt.close()


