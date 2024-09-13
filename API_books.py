from packages.google_books_api_wrapper.api import GoogleBooksAPI

client = GoogleBooksAPI()

def get_all_books_API():
	book_list = []
	search_terms = ["Fiction", "Science", "History", "Technology", "Art", "Literature"]

	for type in search_terms:
		try:
			books = client.get_books_by_subject(type)
			for i in books:
				book_list.append(i)	
		except:
			raise Exception('API books Error')

	return book_list	

def get_books_by_category_API(category):
	try:
		return client.get_books_by_subject(category)	
	except:
		raise Exception('search by Category API error')
	
def get_book_by_isbn(isbn):
	try:
		if len(isbn) == 10:
			client.get_book_by_isbn10()
		elif len(isbn == 13):
			client.get_book_by_isbn13()
		else:
			raise Exception('ISBN incorrect')
	except:
		raise Exception('search by ISBN exception')

def get_book_by_title_API(title):
	try:
		return client.get_book_by_title(title)
	except:
		raise Exception('Search by title exception')
	
def get_books_by_author_API(author):
	try:
		return client.get_books_by_author()
	except:
		raise Exception('Search by author exception')

def get_books_by_publisher(publisher):
	try:
		return client.get_books_by_publisher()
	except:
		raise Exception('Search by author exception')

def search_book_API(
		search_term: str = "", 
		isbn: str = None, 
		title: str = None, 
		author: str = None,
    publisher: str = None,
    subject: str = None):
	try:
		return client.search_book(search_term,isbn,title,author,publisher,subject)
	except:
		raise Exception('Search book exception')

# isbn_10 = '0000000000'
# isbn_13 = '9780000000002'
# authors = ['Eça De Queiroz'] #list
# description = 'Além de ser um dos melhores escritores europeus, Eça de Queiroz escreveu durante os anos em que serviu como cônsul na França, algumas das crônicas mais atraentes da história do jornalismo. Ecos de Paris, reúne escritos regularmente enviados pelo autor, para o jornal brasileiro Gazeta de Notícias, onde também colaboravam Machado de Assis, Oliveira Martins e Ramalho Ortigão, entre outros.'
# id = 'wlssEAAAQBAJ'
# large_thumbail = 'http://books.google.com/books/content?id=wlssEAAAQBAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api'
# page_count = 204
# published_date = '2021-05-05'
# publisher = 'Clube de Autores'
# large_thumbail = 'http://books.google.com/books/content?id=wlssEAAAQBAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'
# subjects = ['Fiction'] #list
# subtitle = None
# title = 'Ecos De Paris'