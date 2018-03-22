markup = """
<!doctype html>
<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1>{heading}</h1>
    </body>
</html>
"""
markup = markup.format('My Page Title', heading='My Page heading')

print(markup)