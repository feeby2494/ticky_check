#!/bin/bash

./ticky_check.py

if test -n "error_message.csv";
  then echo "Parsing Error Messages";
  ./csv_to_html.py error_message.csv /var/www/html/error_messages.html
fi

if test -n "user_statistics.csv";
  then echo "Parsing User Stats";
  ./csv_to_html.py user_statistics.csv /var/www/html/user_stats.html
fi
# same thing:

# if [ -n "$PATH" ]; then echo "Your path is not empty!"; fi
