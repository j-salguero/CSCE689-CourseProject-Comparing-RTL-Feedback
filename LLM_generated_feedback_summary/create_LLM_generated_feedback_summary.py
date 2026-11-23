def read_LLM_summary_prompt(LLM_written_prompt):
	"""Read and save the provided LLM-generated feedback summary prompt"""
	
	# open txt file and save into variable
	with open(LLM_written_prompt, "r", encoding = "utf-8") as LLM_prompt_file:
		
		# this should read in the entire file at once
		LLM_prompt = LLM_prompt_file.read()

	# return the full written prompt as a string
	return LLM_prompt

def add_raw_feedback_to_LLM_prompt(LLM_prompt, raw_feedback):
	"""After reading in the LLM prompt, need to add the raw_feedback at the end of the prompt
	   so all of the information can be fed to the LLM at once"""
	
	# raw_feedback input should already be saved as a string
	# just need to concat the raw_feedback to LLM_prompt
	LLM_prompt_plus_raw_feedback = LLM_prompt + raw_feedback

	# return the full written prompt as a string
	return LLM_prompt_plus_raw_feedback
