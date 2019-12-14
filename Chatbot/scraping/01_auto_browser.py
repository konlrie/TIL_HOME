import webbrowser

artists = ['아이유', '방탄소년단', '에일리']
for artist in artists:
    webbrowser.open('https://search.naver.com/search.naver?query=' + artist)