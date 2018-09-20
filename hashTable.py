def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable, key)

    if len(bucket) > 0:
        found = False
        for item in bucket:
            if item[0] == key:
                item[1] = value
                found = True
                break
                
        if not found:
            bucket.append([key, value])
            found = False
    else:
        bucket.append([key, value])
        
    return htable 
    
    
def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]

def hash_string(keyword,buckets):
    total = 0
    for k in keyword:
         total += ord(k)
    
    return total%buckets

def make_hashtable(nbuckets):
    table = []
    
    for i in range(nbuckets):
        table.append([])
        
    return table

table = make_hashtable(5)
hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)
hashtable_add(table,'Rochelle', 4)
hashtable_add(table,'Zoe', 14)
print table
#>>> [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]], 
#>>> [['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

