"""
Return the number of times that the string "code" appears anywhere in the given 
string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""
def count_code(str):

  codeList = list(str)
  count = 0
  i = 0
  
  while i < len(codeList):
    if i + 3 < len(codeList) and codeList[i] == 'c' \
    and codeList[i + 1] == 'o' and codeList[i + 3] == 'e':
      count += 1
      i += 4
      
    else:
      i += 1
      
  return count