#!/bin/sh

for day in day_*.py; do
  echo ${day/%.py/};
  python3 $day;
  echo;
done

