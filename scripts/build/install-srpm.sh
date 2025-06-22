#!/bin/bash

for p in `find ./ -name '*.rpm' | sort -k1 -n`
do
	rpm -ivh $p
done

