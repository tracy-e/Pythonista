# coding: utf-8
import appex
from markdown2 import markdown
import ui
import sys

TEMPLATE = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<title>Preview</title>
<style type="text/css">
body {
	font-family: Inconsolata, Avenir, helvetica;
	font-size: 14px;
	margin: 10px;
}
pre {
	background-color: #f8f8f8;
}
code {
	background-color: #f8f8f8;
	border-radius: 2px;
	margin: 0, 2px;
	font-size: 0.95em;
}
</style>
</head>
<body>{{CONTENT}}</body>
</html>
'''

def main():
	if appex.is_running_extension():
		path = appex.get_file_path()
	else:
		path = sys.argv[1]

	with open(path, 'r', encoding='utf-8') as f:
		text = f.read()
		if not text:
			print('No input text found. Use this script from the share sheet in an app like Notes.')
			return
		converted = markdown(text)
		html = TEMPLATE.replace('{{CONTENT}}', converted)
		webview = ui.WebView(name='Markdown Preview')
		webview.load_html(html)
		webview.present()

if __name__ == '__main__':
	main()
