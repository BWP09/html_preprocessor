import preprocessor

html = preprocessor.HTMLPreprocessor()

#html.process_to_files()
print(html.process_to_str("index.html"))