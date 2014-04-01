# -*- coding: utf-8 -*-

"""
Tarbell project configuration
"""

# Short project name
NAME = "landingpage"

# Descriptive title of project
TITLE = "Political Framing Landing Page"

# Google spreadsheet key
SPREADSHEET_KEY = "0AqfP9C6R7wKrdGF2cFRtRE1ZblBlNVlDMnFZREJUd1E"

# Exclude these files from publication
EXCLUDES = ["*.md", "requirements.txt"]

# Create JSON data at ./data.json, disabled by default
# CREATE_JSON = True

# S3 bucket configuration
S3_BUCKETS = {
    # Provide target -> s3 url pairs, such as:
    #     "mytarget": "mys3url.bucket.url/some/path"
    # then use tarbell publish mytarget to publish to it
    "production": "politicalframing-landingpage/landingpage",
}

# Default template variables
DEFAULT_CONTEXT = {
    'name': 'landingpage',
    'title': 'Political Framing Landing Page'
}