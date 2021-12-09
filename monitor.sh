#!/bin/bash
input="credentials";

negates=();
while getopts ":n:" opt; do
  case $opt in
    n) negates+=("$OPTARG");;
  esac
done
shift $((OPTIND -1));

skip=0;
while read -r line; do
  data=($line);
  if [ -z $data ]; then
    continue;
  fi
  for neg in "${negates[@]}"; do
    if [[ ${data[0]} =~ .*$neg.* ]]; then
      skip=1;
      break;
    fi
  done
  if [ $skip -eq 1 ]; then
    skip=0;
    continue;
  fi
  echo ${data[0]};
  ret=$(curl -s -H "X-Api-Key:${data[1]}" "https://${data[0]}/api/job");
  echo $ret | jq -r '.state';
  echo "$(echo $ret | jq -r '.progress.completion')%";
  left=$(echo $ret | jq -r '.progress.printTimeLeft');
  echo "$(echo "scale=2 ; $left / 60" | bc) minutes left.";
  echo;
done < $input;
