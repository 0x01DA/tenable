import re
import json

def raw_input():
  #return 'Black|+++,Bellhomes LLC.,["age":39, "user_name":"Reid Jolley", "Group":"Black"],+++,Greek Ideas,["age":63, "user_name":"Lucius Chadwell", "Group":"Green"],["age":63, "user_name":"Cary Rizzuto", "Group":"Black"],["age":28, "user_name":"Shoshana Bickett", "Group":"Yellow"],["age":69, "user_name":"Madeleine Swallow", "Group":"Green"],["age":41, "user_name":"Buddy Etter", "Group":"Black"],+++,God fire,["age":26, "user_name":"Carlene Caulder", "Group":"Green"],["age":43, "user_name":"Napoleon Peay", "Group":"Purple"],["age":44, "user_name":"Noemi Constant", "Group":"Green"]'
  return 'Black|+++Weekly times,["age":26, "user_name":"Denna Soucie", "Group":"Black"],["age":49, "user_name":"Cassey Tercero", "Group":"Red"],["age":46, "user_name":"Glenn Feist", "Group":"Black"],["age":34, "user_name":"Rubie Chapell", "Group":"Purple"],["age":56, "user_name":"Lamont Trautman", "Group":"Red"],["age":59, "user_name":"Denis Woodson", "Group":"Red"],+++,Criminal Finders,["age":44, "user_name":"Rikki Mara", "Group":"Black"],["age":34, "user_name":"Pearly Gomes", "Group":"Red"],["age":31, "user_name":"Ceola Mckendree", "Group":"Red"],+++,IEEF,["age":26, "user_name":"Dena Diener", "Group":"Red"],["age":19, "user_name":"Kasey Sweetland", "Group":"Green"],["age":68, "user_name":"Roderick Grunwald", "Group":"Red"],["age":33, "user_name":"Divina Wetherell", "Group":"Green"],["age":67, "user_name":"Roxie Smathers", "Group":"Purple"],+++,Yours Truly Notary,["age":66, "user_name":"Drew Pursley", "Group":"Purple"],["age":51, "user_name":"Cristopher Beams", "Group":"Green"],["age":59, "user_name":"Augustine Deleeuw", "Group":"Red"],["age":67, "user_name":"Buddy Etter", "Group":"Purple"],["age":32, "user_name":"Kasey Sweetland", "Group":"Green"],+++,Mom Flowers,["age":40, "user_name":"Conception Ruggerio", "Group":"Green"],+++,Green Planet,["age":68, "user_name":"Madelene Brigmond", "Group":"Black"],["age":42, "user_name":"Harriett Nemitz", "Group":"Green"],["age":18, "user_name":"Merrie Likes", "Group":"Black"],["age":54, "user_name":"Yetta Reidy", "Group":"Purple"],["age":19, "user_name":"Augustine Deleeuw", "Group":"Green"],["age":51, "user_name":"Ulysses Brindle", "Group":"Green"],+++,Mowers and Movers,["age":43, "user_name":"Lamont Trautman", "Group":"Black"],["age":40, "user_name":"Aida Lesher", "Group":"Yellow"],["age":30, "user_name":"Augustine Deleeuw", "Group":"Red"],["age":50, "user_name":"Shanice Tyus", "Group":"Yellow"],+++,Brian Trust,["age":42, "user_name":"Yuko Farthing", "Group":"Black"],["age":40, "user_name":"Shirly Blackston", "Group":"Purple"],+++,Data Hounds,["age":29, "user_name":"Preston Aguirre", "Group":"Red"],["age":29, "user_name":"Harriett Nemitz", "Group":"Yellow"],["age":69, "user_name":"Preston Aguirre", "Group":"Yellow"],+++,Glasseye,["age":50, "user_name":"Karen Motta", "Group":"Purple"],["age":41, "user_name":"Lamont Trautman", "Group":"Black"],["age":47, "user_name":"Madelene Litten", "Group":"Black"],+++,SMOK Inc.,["age":36, "user_name":"Carlene Caulder", "Group":"Red"],["age":62, "user_name":"Denna Soucie", "Group":"Yellow"],["age":58, "user_name":"Noah Antilla", "Group":"Red"],["age":40, "user_name":"Katina Weglarz", "Group":"Black"],["age":35, "user_name":"Octavia Dymond", "Group":"Red"],+++,Bellhomes LLC.,["age":39, "user_name":"Reid Jolley", "Group":"Black"],+++,Greek Ideas,["age":63, "user_name":"Lucius Chadwell", "Group":"Green"],["age":63, "user_name":"Cary Rizzuto", "Group":"Black"],["age":28, "user_name":"Shoshana Bickett", "Group":"Yellow"],["age":69, "user_name":"Madeleine Swallow", "Group":"Green"],["age":41, "user_name":"Buddy Etter", "Group":"Black"],+++,God fire,["age":26, "user_name":"Carlene Caulder", "Group":"Green"],["age":43, "user_name":"Napoleon Peay", "Group":"Purple"],["age":44, "user_name":"Noemi Constant", "Group":"Green"],["age":41, "user_name":"Alesia Dimuzio", "Group":"Black"],["age":35, "user_name":"Laverna Poteet", "Group":"Red"],["age":28, "user_name":"Drew Pursley", "Group":"Yellow"],+++,Boxes 4 Cash,["age":48, "user_name":"Aaron Fasano", "Group":"Purple"],["age":64, "user_name":"Octavia Dymond", "Group":"Yellow"],+++,Safe Systems,["age":35, "user_name":"Valeria Almanza", "Group":"Yellow"],+++,Open,["age":24, "user_name":"Maire Fleischman", "Group":"Red"],["age":52, "user_name":"Deneen Hartzog", "Group":"Red"],["age":68, "user_name":"Long Brasch", "Group":"Black"],["age":44, "user_name":"Leonore Laurent", "Group":"Purple"],["age":69, "user_name":"Tam Chagnon", "Group":"Yellow"],["age":59, "user_name":"Drew Pursley", "Group":"Purple"],+++,Fredricks Realestate,["age":56, "user_name":"Dawne Mickley", "Group":"Yellow"],+++,Teen Speak,["age":24, "user_name":"Leonore Laurent", "Group":"Red"],["age":19, "user_name":"Pearly Gomes", "Group":"Purple"],["age":36, "user_name":"Aaron Fasano", "Group":"Green"],["age":18, "user_name":"Talisha Heckstall", "Group":"Green"],+++,SharkTanked,["age":21, "user_name":"Leeanna Yamashita", "Group":"Red"],["age":23, "user_name":"Lucius Chadwell", "Group":"Green"],+++,Poker Online,["age":37, "user_name":"Stacee Sliva", "Group":"Purple"],["age":26, "user_name":"Noemi Constant", "Group":"Green"],+++,Iron Horse Grill,["age":21, "user_name":"Katina Weglarz", "Group":"Red"],+++,Purple,["age":34, "user_name":"Shoshana Bickett", "Group":"Red"],["age":47, "user_name":"Katie Coster", "Group":"Purple"],["age":45, "user_name":"Dorene Kamen", "Group":"Purple"]'

'''
:param blob: blob of data to parse through (string)
:param group_name: A single Group name ("Green", "Red", or "Yellow",etc...)

:return: A list of all user names that are part of a given Group
'''
def ParseNamesByGroup(blob, group_name):
  p = False
  result = []
  x = re.split(r',?[\+]*,?[\w+\s\.]*,\[', blob)
  # return x
  for group in x:
    for e in group.split(", "):
      if "Group" in e:
        if group_name in e:
          result.append(user)
      if "user_name" in e:
        t = e.split(":")[1]
        user = t[1:len(t)-1]
  
  return result
   
data = raw_input()
group_name = data.split('|')[0]
blob = data.split('|')[1]
result_names_list = ParseNamesByGroup(blob, group_name)
print(json.dumps(result_names_list))

