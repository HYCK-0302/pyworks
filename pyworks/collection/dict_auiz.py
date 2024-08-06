#  실습 1번
#Alice", "Bob", "Charlie
score = {}
print(score)
#
score['Alice'] = 85
print(score)
#
score['Bob'] = 90
print(score)
#
score['Charlie'] = 95
print(score)
#
score["David"] = '80'
print(score)
print(type(score)) # score

score['Alice'] = "88"
print(score)

score.pop('Bob')
print(score)


for key in score.keys():
    print(f'{key}: {score[key]}')









