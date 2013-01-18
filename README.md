# bottle-haml

An extension for using [Haml templates](http://haml.info/) in your [Bottle](http://bottlepy.org) applications.

## Installation

`bottle-haml` is available via PIP:

    pip install bottle-haml

## Usage

Once installed, use is simple. Simply import the helper method `haml_template` as follows:

    from bottlehaml import haml_template

From there, usage is exactly the same as Bottle's built-in `template` method except it will search for files with the extension `.haml` and parse them as Haml.

## Haml reference

`bottle-haml` uses the [PyHaml](https://github.com/mikeboers/PyHAML) module to parse Haml into the Mako templates that Bottle uses. For a reference of the Haml syntax supported please see the PyHaml project's GitHub page.

Copyright (c) 2013 [WireLoad Inc.](http://www.wireload.com/)