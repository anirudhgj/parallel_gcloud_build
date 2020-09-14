#!/bin/bash

echo "${INPUT_ENCODED_GOOGLE_APPLICATION_CREDENTIALS}" | base64 -d > ${INPUT_GOOGLE_APPLICATION_CREDENTIALS}
/parallel_build_components.sh