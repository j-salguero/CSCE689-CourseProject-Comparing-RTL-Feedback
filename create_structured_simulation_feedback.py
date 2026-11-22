from pathlib import Path

def read_feedback(file_path):

        """Need to be able to read original simulation feedback, in the form of a text file"""

        # since reading a txt file, use "utf-8" encoding

        with open(file_path, "r", encoding = "utf-8") as feedback_file:

                raw_feedback = feedback_file.read()

        return raw_feedback

def extract_raw_feedback(raw_feedback):
	"""Extract the most important information/lines from the raw simulation feedback"""
	
	# i only care about extracting specific information from the raw feedback files
	important_feedback_keywords = ["FAIL", "Time", "Signal", "Expected", "Actual", "Error"]
	extracted_lines_of_feedback = []

	# i need to loop through each line of the feedback and just look for/extract the information I care about
	for line_i in raw_feedback.splitlines():
		# lower case everything so I don't run into any issues with missed info due to capitalization
		for keyword_i in important_feedback_keywords:
			if keyword_i.lower() in line_i.lower():
				# if loop makes it this far, I just need to save the full line
				# remove any white space from each line
				extracted_lines_of_feedback.append(line_i.strip())

				# once i find this specific keyword during one loop, break 
				# so that I can continue looking through the rest of the list of keywords rather than wasting time
				# and don't want to add the same keyword more than once
				break

	# after I finish looking through everything, return the important extracted lines
	return extracted_lines_of_feedback

def format_raw_feedback(extracted_lines_of_feedback):
	"""Use the list of extracted lines of feedback and format them as bullet points"""
	
	# I can save all of this as a long string
	# start with a clear header
	bullet_point_structured_feedback = "Structured Simulation Feedback: \n"
	
	# loop through the given list of extracted_lines_of_feedback
	# add each as an individual bullet point
	for extracted_line_i in extracted_lines_of_feedback:
		
		# add bullet in front of each line
		bullet_point_structured_feedback += "-" + extracted_line_i + "\n"

	# return the long concat string as the bullet point list
	return bullet_point_structured_feedback
