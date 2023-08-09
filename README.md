## Engineering Professional Development Tracker
[![GitHub forks](https://img.shields.io/github/forks/microtechno9000/engineering-pd-tracker)](https://github.com/microtechno9000/engineering-pd-tracker/network)
[![GitHub stars](https://img.shields.io/github/stars/microtechno9000/engineering-pd-tracker)](https://github.com/microtechno9000/engineering-pd-tracker/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/microtechno9000/engineering-pd-tracker)](https://github.com/microtechno9000/engineering-pd-tracker/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/microtechno9000/engineering-pd-tracker)](https://github.com/microtechno9000/engineering-pd-tracker/pulls)
[![GitHub contributors](https://img.shields.io/github/contributors/microtechno9000/engineering-pd-tracker)](https://github.com/microtechno9000/engineering-pd-tracker/graphs/contributors)
[![GitHub last commit](https://img.shields.io/github/last-commit/microtechno9000/engineering-pd-tracker?)](https://github.com/microtechno9000/engineering-pd-tracker/commits/v2_devel)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django)](https://github.com/microtechno9000/engineering-pd-tracker)

The Engineering Professional Development Tracker (EPDTracker) is an easy-to-use web application for tracking proffesional development hours to maintain compliance to or for Engineers Australia Charted Engineering.
EPDTracker is designed to minimise the overhead in tracking courses, books, YouTube videos, Podcasts or any other media, keeping the focus on the training not on record keeping.
As the tool develops, additional features will be added automatically import training from various sources. At present the tracker reports on manually entered data.

## Features

### Current Features

- **Track Professional Development Hours:** EPDTracker provides a user-friendly interface to log and monitor professional development activities. Engineers can record seminars, workshops, training programs, and other relevant activities.

- **Record and Track Valid Hours:** The application keeps a detailed record of development hours and calculates the validity based on the expiration periods of certifications and requirements for maintaining Chartered Engineering Professional status.

### Comming to a tracker near you

- **Auto Fill training data:** Auto fill training data specific training organisations or types, saving time

- **Auto import from YouTube:** From YouTube history, select and add watched videos into the training records

- **Auto import from Podcast:** Based on an RSS feed, auto import podcasts once listened

- **Docker Image:** Docker image to make it all so much simpler to run

## Usage

Requires python and flask to run, follow the installation instructions below.


## Requirements

- Ubuntu Server 20.04 or Ubuntu Desktop 20.04 onwards
- Python
- Python requirements detailed within the requirements file


## Install

Install steps in here
1. Clone the gitHub repo

`cd /opt`

`sudo mkdir epdtracker`

<u>Note: </u> depending on the /opt ownership setup, the 'epdtracker' folder will need to be changed to the current user and group.

`git clone https://github.com/microtechno9000/engineering-pd-tracker.git epdtracker`

2. Install requirements

`sudo pip3 install -r requirements.txt `

3. Run EPDTracker

`python3 tracker.py`
