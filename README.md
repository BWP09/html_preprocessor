# HTML Preprocessor

This is a simple HTML preprocessor written in Python.
This allows you to use basic html "components".

## Usage

### EXAMPLE USAGE ABOVE IN `preprocessor` DIRECTORY

Make the following directory structure:
(The `preprocessor` directory name can be changed)

```
preprocessor.py
preprocessor
|-shared
|-templates
```

### Components

The `shared` directory is where you put your components.
Components *can* be use within other components.

Ex: `sh:[navbar]`, will be replaced by the contents of `navbar.*`

### Templates

The `templates` directory is where you put your main HTML files.