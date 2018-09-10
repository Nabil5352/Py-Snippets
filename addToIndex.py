# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []

def add_to_index(index,keyword,url):
    if len(index) > 0:
        counter = 0
        urlFound = False
        for i in index:
            if i[counter] == keyword:
                for j in i[counter+1]:
                    if j == url:
                        urlFound = True
                        break
                    
                if not urlFound:
                    i[counter+1].append(url)
                    
                urlFound = False
                break
            else:
                index.append([keyword,[url]])
    else:
        index.append([keyword,[url]])


def add_page_to_index(index,url,content):
    contents = content.split()
    for i in contents:
        add_to_index(index, i, url)


#Test Cases for add_to_index
# add_to_index(index,'udacity','http://udacity.com')
# add_to_index(index,'computing','http://acm.org')
# add_to_index(index,'udacity','http://npr.org')
# print index
#>>> [['udacity', ['http://udacity.com', 'http://npr.org']],['computing', ['http://acm.org']]]

#Test Cases for add_page_to_index
add_page_to_index(index,'fake.text',"This is a test")
print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]
