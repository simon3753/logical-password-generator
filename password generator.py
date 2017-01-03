import hashlib

def ezmd5(inputstr):
  md5 = hashlib.md5()
  md5.update(inputstr.encode('utf-8'))
  return md5.hexdigest()

print(ezmd5('how to use md5 in python hashlib?'))

#md5 = hashlib.md5()
#md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
#print(md5.hexdigest())