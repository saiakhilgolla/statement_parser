# Improvements:
add another module / script to keep the list of categories independent. These are the functionalities required:
	1. Add new categories to the list.
	2. Add subcategories to the list.
	3. If chatgpt guesses something incorrectly, teach chatgpt to remember the correct category set manually
		a. categorization in to micellaneous
		b. wrong categorization
enrich banking info:
1. infer bank and account info from csv name.
2. a method to find all these details for RBC statements


steps:
1. Add month,year info to csv tables.
2. Infer category for each txn using chatgpt.py