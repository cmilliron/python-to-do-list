import webbrowser

base_url = "https://www.google.com/search?q="
search_term = "+".join(input('Enter a search term: ').split(" "))

print(base_url+search_term)


webbrowser.open(base_url+search_term)
