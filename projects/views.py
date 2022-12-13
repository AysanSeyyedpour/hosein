# from django.shortcuts import render
# from django.http import HttpResponse


# projectList = [
#     {
#         'id' : '1',
#         'title' : 'gold',
#         'description': 'this is expencive'
#     },
#     {
#         'id' : '2',
#         'title' : 'silver',
#         'description': 'this one has middle price'
#     },
#     {
#         'id' : '3',
#         'title' : 'bronze',
#         'description': 'this is cheap'
#     }
# ]


# def projects(request):
#     # msg = 'hello, who are you ?'
#     # return render(request, 'projects.html', {'message': msg})
#     page = 'Projects'
#     number = 10
#     context = {'page': page, 'number': number, 'projects': projectList}
#     return render(request, 'projects.html', context)


# def project(request, pk):
#     projectObj = None
#     for i in projectList:
#         if i['id'] == pk:
#             projectObj = i
#     return render(request, 'single-project.html', {'project':projectObj})







# # javab tamrin shomare 1

# # def project(request, pk):
# #     word = str(pk)
# #     list_word = list(word.strip(" "))
# #     for i in range(len(list_word)):
# #         last_item = list_word.pop()
# #         list_word.insert(i, last_item)
        
# #     string_word = "".join(list_word)
# #     return HttpResponse('Reversed String: ' + '' +  str(string_word))


from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return render(request, 'projects.html')

def project(request, pk):
    word = str(pk)
    list_word = list(word.strip(" "))
    # for i in range(len(list_word)):
    #     last_item = list_word.pop()
    #     list_word.insert(i, last_item)
        
    # string_word = "".join(list_word)
    count_list = len(list_word)
    return HttpResponse('Reversed String: ' + '' +  str(count_list))

