## Blog App Django-Rest-Framework

**Yuklab Olish**
```
git clone https://github.com/fazliddinbaxtiyorov/Blog_app_DRF.git

```
**Foydalanish**
```
 pip install -r requirements.txt
```
**Dasturni Ishlatish**
  * Dasturni pasdagi komandani terminal bilan ishga tushuring: 
```
python manage.py runserver
```


**Dasturni Boshqarish**

- 'GET/' :  http://127.0.0.1:8000/api/ - Barcha bloglarni ko'rish uchun
- 'Post/' :   http://127.0.0.1:8000/api/new - yangi blog yaratish
- 'GET/' :  http://127.0.0.1:8000/api/id - bloglarni id bo'yicha ko'rish
- 'Delete/' :   http://127.0.0.1:8000/api/id/delete - bloglarni id bo'yicha o'chirish
- 'Put/Patch' * http://127.0.0.1:8000/api/id/update - bloglarni id bo'yicha yangilash
- 'GET/' :  http://127.0.0.1:8000/api/<username> - userga tegishli barcha bloglarni ko'rish
- 'GET/' :  http://127.0.0.1:8000/api/sort/<str:field>  - berilgan postlarni tartiblash
