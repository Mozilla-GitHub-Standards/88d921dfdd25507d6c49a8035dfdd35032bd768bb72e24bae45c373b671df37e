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
* Verify that the values in `.env` correspond to the target Megaphone deployment you are testing. `ENDPOINT` is the Megaphone instance being tested. `WS_ENDPOINT` should belong to an appropriate Autopush endpoint as found in the [autopush docs](https://autopush.readthedocs.io/en/latest/#autopush-endpoints). 
* Run the command `pipenv install` to create a virtual environment and install the required dependencies
* Run the command `pipenv shell` to enter the virtual environment (which populates environment variables the tests are expecting)

## Running The Tests

From inside the virtual environment, run the following command to execute the tests

`pytest -v`
