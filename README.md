# standoff-2-API
API for standoff 2
# how to use
```python
standoff.account('id') #will return the name and link to the avatar
standoff.avatar('url') #will create in the same directory "gg.webp" with the image of the avatar if there is no avatar, then the file cannot be opened
```
# example
```python
import standoff
pr = standoff.account(42073869)
print(pr)
#output
#('kexswt_', 'https://avatars-19e92.kxcdn.com/48c416cd-3fdc-47fe-b302-bcac3f78dd00')
standoff.avatar(pr[1])
#and create gg.webp
```
# have an avatar
![alt text](good.webp "")
# no avatar
![alt text](bad.webp "")
