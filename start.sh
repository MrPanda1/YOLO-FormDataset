#!/bin/bash

x=1

while [ $x -le 20 ]
do
	python3 flow \
		--model cfg/yolo-forms.cfg \
		--train \
		--annotation data/annotations/train/ \
		--dataset data/images/ \
		--load -1 \
		--gpu 0.5 \
		--trainer sgd

	echo "Crashed $x times"
	x=$(( $x + 1 ))
done
