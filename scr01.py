from bs4 import BeautifulSoup

with open(r'C:\Users\ASUS\Project_Example\.vscode\sample.html', 'r') as html_file:

    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())