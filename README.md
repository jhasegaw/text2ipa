# text2ipa

This is a tool to convert text files to IPA.  It currently only does a very simple English version.

## Installation:

```
python setup.py install
```

## Usage:

Command-line usage:

```
t2ipa <language> <inputfile> <outputfile>

<language> should be a capitalized language name, or a lowercase ISO 639-3 code.
<inputfile> is the name of the text file you want to convert.
<outputfile> is the output filename; if omitted, output is printed to stdout.
```

Usage in python:

```python
>>> import text2ipa
>>> converter=text2ipa.Converter('English')
>>> output=converter.convert('this is a test')
>>> print(output)
θɪs ɪs ə tɛst
```

