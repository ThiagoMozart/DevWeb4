#!/bin/bash
.PHONY: default
.SILENT:


default:

start:
	gunicorn --bind 0.0.0.0:8000 \
             --reload \
             --capture-output \
             warhammer.wsgi:application