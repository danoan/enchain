#! /usr/bin/env bash

SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

INPUT_FOLDER="${SCRIPT_PATH}/input"
OUTPUT_FOLDER="${SCRIPT_PATH}/output"
mkdir -p "${OUTPUT_FOLDER}"

pushd "${SCRIPT_PATH}" >/dev/null

cat "${INPUT_FOLDER}/list.json" | python ../convert-json.py to-dict "my-list"

popd >/dev/null
