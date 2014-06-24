Igor CLI
========

A CLI providing IPMI control for OSU-OSL machines. Serves as a wrapper
making HTTP requests to the [Igor REST API](https://github.com/emaadmanzoor/igor-rest-api).

## Quickstart

```
git clone https://github.com/emaadmanzoor/igor-cli
cd igor-cli
virtualenv env
source env/bin/activate
pip install --editable .
igor
```

## Configuration

The Igor API server needs to be provided either via the command-line
`--igor-server` option, or in the `~/.igorrc` file.
Here is a sample `~/.igorrc` file:

```
[igor]
igor_server = localhost:5000
```

## Documentation

The best way to get the most current documentation is via the CLI itself:
`igor --help`
