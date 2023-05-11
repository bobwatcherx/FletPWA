from flet import *

def main(page:Page):
	page.add(
	Column([Text("hai flet edy ",size=30)])

		)
flet.app(target=main,view=WEB_BROWSER,assets_dir="assets")

# NOW FOR CHANGE SPLASH SCREEN YOU COPY logo.jpeg TO assets/icons FOLDER

# AND FOR CHANGE FAVicon YOU copy you image example logp.jpeg to asets
# and change name to favicon.png

# AND FOR FAVICON COPY you image and change name favicon.png in assets fodler

# AND NOW BUILD TO STATIC HTML
