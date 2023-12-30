# HTML Preprocessor

This is a simple HTML preprocessor written in Python.
This allows you to use basic html "components".

## Usage

Make the following directory structure:
(The `preprocessor` directory name can be changed)

```
preprocessor.py
preprocessor
|-shared
|-templates
```

The `shared` directory is where you put you components.
File name is how you use them, omitting the extension.
Components *can* be use within other components.

Ex: `sh:[navbar]`, will be replaced by the contents of `navbar.*`

The `templates` directory is where your main HTML files are.