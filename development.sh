#!/bin/bash
coffee --join static/js/home.js --watch --compile static/js/home.coffee&

jade -w -P view/*.jade&

echo "The development environment has ready!"
