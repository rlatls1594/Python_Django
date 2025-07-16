# import os
# from django.core.wsgi import get_wsgi_application
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# application = get_wsgi_application()

# from MTV.models import Board, Question, Answer
# def data_select():
	# print(Board.objects.all())
	# print(Board.objects.count())
	
  # print(Board.objects.filter(id=1))
  # print(Board.objects.filter(id=2))
  # print(Board.objects.get(id=1))
  # print(Board.objects.get(id=2))
	
  # print(Board.objects.filter(title__contains="Test"))
  # print(Board.objects.filter(title__contains="Django"))
	
# def data_create():
# 	Board_data = Board(title="Django Project", content="Django Project Model Data Create TEST")
# 	Board_data.save()
# print(Board.objects.all())

# def data_modify():
#     Board_data = Board.objects.get(title='Django Project')
#     Board_data.title = 'Django Model TEST'
#     Board_data.save()
#     print(Board.objects.all())

# def data_delete():
#   Board_data = Board.objects.get(title='Django Model TEST')
#   Board_data.delete()
#   print(Board.objects.all())

  # Board_data = Board.objects.filter(title__contains='Django').delete()
  # print(Board.objects.all())

# def data_objects(): # *********매우 중요***********
  # Board_object = Board.objects.get(title='Board Test Write')
  # print("ID(PK):", Board_object.id)
  # print("Title:", Board_object.title)
  # print("Content:", Board_object.content)
  # print("Create_Date:", Board_object.create_date)
  # print("Modify_Date:", Board_object.modify_date)

# def R_select():
#   Q = Question.objects.get(id=1)
#   print("ID(PK):", Q.id)
#   print("Title:", Q)
#   print("Content:", Q.content)
  
#   print("Answer Count:", Q.answer_set.count())
#   print("Answer List:", Q.answer_set.all())
#   print("Answer Get:", Q.answer_set.get(content__contains='Professor'))
#   print("Answer Filter:", Q.answer_set.filter(content__contains='Soccer'))

# def R_create():
#   Q = Question.objects.get(id=1)
#   Q.answer_set.create(content='Office Worker')
#   print("Answer List:", Q.answer_set.all())

# def R_delete():
#   Q = Question.objects.get(id=1)
#   A = Answer.objects.get(content__contains='Office Worker')
#   A.delete()
#   print("Answer List:", Q.answer_set.all())

# if __name__ == '__main__':
  # data_select()
  # data_create()
  # data_modify()
  # data_delete()
  # data_object()
  # R_select()
  # R_create()
  # R_delete()