#!/bin/bash
input="credentials";
while read -r line; do
  data=($line);
  if [ $# -gt 0 ]; then
    if [[ ${data} != *${1}* ]]; then
      continue
    fi
  fi
  echo ${data[0]};
  ret=$(curl -s -H "X-Api-Key:${data[1]}" "https://${data[0]}/api/job");
  echo $ret | jq -r '.state';
  echo "$(echo $ret | jq -r '.progress.completion')%";
  left=$(echo $ret | jq -r '.progress.printTimeLeft');
  echo "$(echo "scale=2 ; $left / 60" | bc) minutes left.";
  echo;
done < $input;
