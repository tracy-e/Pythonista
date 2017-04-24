# coding: utf-8

import appex
from markdown2 import markdown_path
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
	-webkit-text-size-adjust: 100%;
    text-size-adjust: 100%;
    color: #333;
    font-family: Inconsolata, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
    font-size: 14px;
    word-wrap: break-word;
}
.codehilite {
	padding: 5px;
	background-color: #f8f8f8;
	overflow: scroll;
}
.codehilite code {
	color: #444444;
	border: none;
}
blockquote {
	background-color: #f8f8f8;
	border-left: 8px solid #eeeeee;
	margin: 0;
	padding: 5px 5px 5px 12px;
	color: #666666;
}
code {
	margin: 0 2px;
	color: #e96900;
	padding: 1px;
	border-radius: 3px;
	font-family: Consolas, "Liberation Mono", Menlo, Courier, monospace;
    font-size: 10px;
	background-color: #f8f8f8;
}
p {
	line-height: 120%;
}
a {
	color: #4078c0;
    text-decoration: none;
    background-color: transparent;
}
table {
    border-collapse: collapse;
    border-spacing: 0;
}
td, th {
    padding: 0;
}
ul, ol {
    padding: 0;
    margin-top: 0;
    margin-bottom: 0;
}
hr {
    height: 0;
    margin: 15px 0;
    overflow: hidden;
    background: transparent;
    border: 0;
    border-bottom: 1px solid #ddd;
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
	
	md = markdown_path(path, extras = ['fenced-code-blocks'])
	html = TEMPLATE.replace('{{CONTENT}}', md)
	webview = ui.WebView(name='预览')
	webview.load_html(html)
	webview.present()
	
if __name__ == '__main__':
	main()
