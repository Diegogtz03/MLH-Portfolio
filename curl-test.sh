#!/bin/bash

# Test POST
TEST_VALUE=$RANDOM
curl -s --request POST http://127.0.0.1:5000/api/timeline_post -d 'name=test&email=test@testing.com&content='$TEST_VALUE'' > /dev/null

# Test if POST worked
RESULT=$(curl -s http://127.0.0.1:5000/api/timeline_post | jq '.timeline_posts | .[] | select( .name == "test" and .email == "test@testing.com" and .content == "'$TEST_VALUE'" )')

if [ $(wc -l <<< "$RESULT") -gt 1 ]; then
  echo "Test passed"

  #Delete test timeline post
  curl -s --request DELETE http://127.0.0.1:5000/api/timeline_post -d 'id='$(echo $RESULT | jq '.id')'' > /dev/null

  echo "Test deleted from database"
else
  echo "Test failed"
fi