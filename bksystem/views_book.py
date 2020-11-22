from django.http import JsonResponse
from bksystem.models import books
from django.core.exceptions import ValidationError,ObjectDoesNotExist
from django.db.utils import IntegrityError
import time

#新增書目介面
def add_event(request):
    eid = request.POST.get('eid', '')  # 发布会id
    title=request.POST.get('title', '')
    author=request.POST.get('author', '')
    isbn=request.POST.get('isbn', '')
    publisher=request.POST.get('publisher', '')
    publication_year=request.POST.get('publication_year', '')
    last_modified_date=request.POST.get('last_modified_date', '')
    created_date=request.POST.get('created_date', '')
    created_at=request.POST.get('created_a', '')
    update_at=request.POST.get('update_at', '')

    if eid == '' or title == '' or author == '' or isbn == '' or publisher == '' or publication_year == '' or last_modified_date == '':
        #or created_date == '' or created_at=='' or update_at == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    result = books.objects.filter(id=eid)
    if result:
        return JsonResponse({'status': 10022, 'message': 'book id already exists'})

    result = books.objects.filter(title=title)
    if result:
        return JsonResponse({'status': 10023, 'message': 'book name already exists'})

    

    try:
        books.objects.create(id=eid, title=title, author=author, isbn=isbn, publisher=publisher, publication_year=publication_year,
                            last_modified_date=last_modified_date, created_date=created_date,created_at=created_at,update_at=update_at )
    except ValidationError:
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status': 10024, 'message': error})

    return JsonResponse({'status': 10200, 'message': 'add event success'})

# 发布会查询
def get_event_list(request):
    eid = request.GET.get("eid", "")  # 发布会id
    title = request.GET.get("title", "")  # 发布会名称

    if eid == '' and title == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})

    if eid != '':
        event = {}
        try:
            result = books.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            books['eid'] = result.id
            books['title'] = result.title
            books['author'] = result.author
            books['isbn'] = result.isbn
            books['publisher'] = result.publisher
            books['publication_year'] = result.publication_year
            books['last_modified_date']=result.last_modified_date
            books['created_date']=result. created_date
            books['created_at']=result.created_at
            books['update_at']=result.update_at

            return JsonResponse({'status': 10200, 'message': 'success', 'data': event})

    if title != '':
        datas = []
        results = books.objects.filter(title__contains=title)
        if results:
            for r in results:
                event_dict = {
                    'eid': r.id,
                    'title': r.title,
                    'author': r.author,
                    'isbn': r.isbn,
                    'publisher': r.publisher,
                    'publication_year': r.publication_year,
                    'last_modified_date': r.last_modified_date,
                    'created_date': r.created_date,
                    'created_at': r.created_at,
                    'update_at': r.update_at,
                }
                datas.append(event_dict)
            return JsonResponse({'status': 10200, 'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})

