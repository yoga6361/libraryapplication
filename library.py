import random

# Define Books list
books = [
	{	'id': '1',
		'title': 'Treasure Island',
		'price': 6000,
		'available_copies': 12,
		'category': 'adventure'
	},
	{	'id': '2',
		'title': 'The Call of the Wild',
		'price': 18000,
		'available_copies': 30,
		'category': 'adventure'
	},
	{	'id': '3',
		'title': 'Into Thin Air',
		'price': 8000,
		'available_copies': 26,
		'category': 'adventure'
	},
	{	'id': '4',
		'title': 'Death Industrial Complex',
		'price': 10000,
		'available_copies': 5,
		'category': 'action'
	},
	{	'id': '5',
		'title': 'Game of Thrones',
		'price': 12000,
		'available_copies': 15,
		'category': 'fantasy'
	},
	{	'id': '6',
		'title': 'All the Garbage of the World, Unite!',
		'price': 7000,
		'available_copies': 15,
		'category': 'action'
	},
	{	'id': '7',
		'title': 'The Lord of the Rings',
		'price': 3000,
		'available_copies': 20,
		'category': 'fantasy'
	}]

book_print_format = '{} book with ID [{}], at a price of {}, with {} copies, classifies under {} category'

# Define application options for each role
admin_permissions = {'1': 'Add a book', '2': 'Show all available books', '3': 'Show all sold books', 
					 '4': 'Show the total income', '5': 'Log out'}

user_permissions = {'1': 'Sign Up', '2': 'Log In', '3': 'Log out'}

customer_permissions = {'1': 'Search by category', '2': 'Search by title', '3': 'Books suggestion', '4': 'Buy a book', '5': 'Log out'}

# Initialize books sold list
books_sold = list()

# Initialize users list
users = [{'username': 'admin', 'email': 'admin@library.com', 'password': 'admin', 'is_admin': True}]

# Initialize current with empty string
current_user = ''

while True:	
	# Display all availabe options
	print('\nChoose an option')
	for op in user_permissions:
		print(op + ' ====> ' + user_permissions[op])
	print()

	# Read the option 
	opt = input('Option: ')
	print()

	# Read the reuired sign up info
	if opt == '1':
		print('Please Enter the Following Information')
		username = input('Username: ')
		email = input('Email: ')
		password = input('Password: ')
		print()

		# Add the user to the users list
		users.append({'username': username, 'email': email, 'password': password, 'is_admin': False})

	# Read the reuired log in info
	elif opt == '2':
		users_names = list()
		for u in users:
			users_names.append(u['username'])

		username = input('Username: ')

		# Test if the users list contains the username
		if username not in users_names:
			print(f'{username} is not registered\n\n')
			print()
			continue

		# Extract actual password for requested username
		for u in users:
			if username == u['username']:
				actual_pass = u['password']
				user_info = u
		
		password = input('Password: ')

		# Test if the password is correct 
		if actual_pass != password:
			print(f'Wrong Password')
			print()
			continue

		print(f'Successfully signed in as {username}')

		current_user = username

		# Test if the user is admin
		if user_info['is_admin']:
			while True:
				# Display the current user
				if current_user != '':
					print(f'{"-" * 15} The current user is {current_user} {"-" * 15}')

				# Display admin options
				print('\nChoose	an option')
				for op in admin_permissions:
					print(op + ' ====> ' + admin_permissions[op])
				print()

				# Read the option
				opt = input('Option: ')
				print()

				if opt == '1':
					# Read the reuired book info
					title = input('Enter the book title: ')
					id_ = input('Enter the book id: ')
					category = input('Enter the book category: ')
					available_copies = int(input('Enter the number of copies: '))
					price = int(input('Enter the book price: '))

					# Add the book to the books dictionary
					books.append({'title': title, 'id': id_,'price': price, 'available_copies': available_copies, 'category': category})

					print(f'{book_print_format.format(title, id_, price, available_copies, category)}, has been added successfully\n')

				elif opt == '2':
					# Show all available books
					print(f"{'-' * 25} The available books are {'-' * 25}")
					for b in books:
						print(f'{book_print_format.format(b["title"], b["id"], b["price"], b["available_copies"], b["category"])}\n')

					print()

				elif opt == '3':
					# Print books names from books_sold list
					from pprint import pprint
					pprint(books_sold)
					print(f"{'-' * 25} The sold books are {'-' * 25}")
					for b in books_sold:
						print(f'{b["title"]} book with {b["sold_copies"]} sold copies at a price of {b["price"]} for each')

				elif opt == '4':
					# Calculate the total income from books_sold list
					total_income = 0

					for b in books_sold:
						total_income = total_income + (b['price'] * b['sold_copies'])

					print(f"The total income of the sold books is: {total_income}")

				elif opt == '5':
					current_user = ''
					break

		# If the user is a customer
		else:
			while True:
				# Display the current user
				if current_user != '':
					print(f'{"-" * 15} The current User is {current_user} {"-" * 15}')

				# Display all availabe options
				print('\nChoose an option')
				for op in customer_permissions:
					print(op + ' ====> ' + customer_permissions[op])
				print()

				# Read the option
				opt = input('Option: ')
				print()

				if opt == '1':
					# Show all available bookes for specific category
					category = input('Enter category: ')
					availabe_books = list()
					for b in books:
						if b['category'] == category:
							availabe_books.append(b)

					if len(availabe_books) > 0:
						print(f'Availabe books for {category} are:\n')
						for b in availabe_books:
							print(f'{book_print_format.format(b["title"], b["id"], b["price"], b["available_copies"], b["category"])}\n')

					else:
						print('You are welcome to our library, but there are no books available for the required category right now\n')

				elif opt == '2':
					# Search by title
					title = input('Enter a book title: ')
					found = None

					for b in books:
						if title.lower() == b["title"].lower():
							found = b
							break

					if found is not None:
						print(f'{book_print_format.format(found["title"], found["id"], found["price"], found["available_copies"], found["category"])} has been found')
						continue

					print('You are welcome to our library, but the required book  is not available right now\n')

				elif opt == '3':
					# Search by category
					category = input('Enter a category: ')
					availabe_books = list()
					for b in books:
						if b['category'] == category:
							availabe_books.append(b)

					if len(availabe_books) > 0:
						suggested = random.choice(availabe_books)
						print(f'We suggest the {book_print_format.format(suggested["title"], suggested["id"], suggested["price"], suggested["available_copies"], suggested["category"])}\n\n')

					else:
						print('You are welcome to our library, but there are no books available for the required category right now\n')

				elif opt == '4':
					# Sell a book
					print('The availabe books are:\n')
					for b in books:
						print(f'{book_print_format.format(b["title"], b["id"], b["price"], b["available_copies"], b["category"])}\n')

					found = None
					id_ = input('Enter a book id: ')

					# Search by ID
					for b in books:
						if id_ == b["id"]:
							found = b
							break

					# Test if there is available copy
					if found is not None:
						if found['available_copies'] == 0:
							print('You are welcome to our library, but the required book  is not available right now\n')
							continue

						# Test if the book already added to the books_sold  list
						sold_found = None
						for b in books_sold:
							if found['id'] == b["id"]:
								sold_found = b
								break

						# Update available_copies by 1
						if sold_found is not None:
							sold_found['sold_copies']+= 1

						# Add the book to the books_sold list if it's not found
						else:
							sold_found = found.copy()
							sold_found['sold_copies'] = 1
							books_sold.append(sold_found)

						found['available_copies']-= 1
						print(f'{book_print_format.format(found["title"], found["id"], found["price"], found["available_copies"], found["category"])} has been sold to {current_user}\n')

				elif opt == '5':
					current_user = ''
					break

	elif opt == '3':
		break
