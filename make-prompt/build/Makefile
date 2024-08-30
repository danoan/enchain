venv_folder := /home/daniel/Projects/Git/enchain/.venv
llm_assistant_folder := "/home/daniel/Projects/Git/llm-assistant"
correct_prompt := "/home/daniel/Dropbox/Journals/prompt-collection/docs/Languages/Correct Text/config.toml"
alternative_expression_prompt := "/home/daniel/Dropbox/Journals/prompt-collection/docs/Languages/Alternative Expressions/config.toml"

base_dir := $(dir $(firstword $(MAKEFILE_LIST)))

corrected.json:
	. $(venv_folder)/bin/activate  
	echo '{"language": "portuguese", "style":"same", "message":"Oje vou amossar com a Sailon."}' | \
	llm-assistant custom $(correct_prompt) | \
	jq ".[0]" | jq '{"corrected":.}' > $@

alternative.json: corrected.json 
	. $(venv_folder)/bin/activate && \
		cat $< | jq '{"language":"portuguese","message":.corrected}' | llm-assistant custom $(alternative_expression_prompt)
