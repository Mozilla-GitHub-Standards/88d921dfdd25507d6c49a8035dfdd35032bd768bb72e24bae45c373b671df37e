# Megaphone Tests

This repository contains tests that should be run whenever the [Megaphone](https://github.com/mozilla-services/megaphone)
service gets deployed.

## Requirements

To run these tests you need to have the following:

* This repo checked out to your filesystem
* Bearer tokens for use with Megaphone (both for reading and broadcasting)
* Python 3.6.7
* [Pipenv](https://pipenv.readthedocs.io/en/latest)

## Creating Testing Environment

* Copy `.env-dist` to `.env`
* Verify that the values in `.env` correspond to the target Megaphone deployment you are testing. `ENDPOINT` is the Megaphone instance being tested. `WS_ENDPOINT` should belong to an appropriate Autopush endpoint as found in the [autopush docs](https://autopush.readthedocs.io/en/latest/#autopush-endpoints). See below for further details.  
* Run the command `pipenv install` to create a virtual environment and install the required dependencies
* Run the command `pipenv shell` to enter the virtual environment (which populates environment variables the tests are expecting)

## Populating .env

You might have been provided with credentials like the following: 

```
For dev.megaphone.nonprod.cloudops.mozgcp.net: 
	broadcasterAuth: 
		dev-testing-broadcaster=["123abc"]}'
        readerAuth: 
		dev-testing-reader=["789xyz"]}'

```
In that case, your `.env` might look like: 

```
ENDPOINT="https://dev.megaphone.nonprod.cloudops.mozgcp.net/"
WS_ENDPOINT="wss://autopush.dev.mozaws.net/"
BROADCASTER_ID="dev-testing-broadcaster"
BROADCASTER_TOKEN="123abc"
READER_ID="dev-testing-reader"
READER_TOKEN="789xyz"
```

## Running The Tests

From inside the virtual environment, run the following command to execute the tests

`pytest -v`
