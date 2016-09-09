#!/bin/bash
if ! which $1 > /dev/null; then
      sudo apt-get install $1 -y
fi
