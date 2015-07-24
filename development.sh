#!/bin/bash
coffee --join js/home.js --watch --compile js/home.coffee&

jade -w -P *.jade&

echo "The development environment has ready!"
