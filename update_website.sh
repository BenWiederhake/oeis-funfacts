#!/bin/bash

set -ex

cd $(dirname "$0")
pwd

git pull --ff-only
pushd gh-pages
    git pull --ff-only
popd

wget -nv -O /tmp/stripped.gz 'https://oeis.org/stripped.gz'

./oeis_funfacts.py

cd gh-pages
pwd

if [ ! -r app.css ] || [ ! -r favicon.png ]
then
    echo 'Bad checkout!'
    exit 1
fi

git commit -am "Automatic update"
git push
