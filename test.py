import preprocessor, sys

prepro = preprocessor.HTMLPreprocessor(pretty=True)

prepro.process_html(levels = int(sys.argv[1]))