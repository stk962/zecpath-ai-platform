from parsers.resume_parser import parse_resume

resume_path = 'data/resumes/sample_resume.pdf'

cleaned_text = parse_resume(resume_path)

output_path = "data/cleaned/cleaned_resume.txt"

with open(output_path, "w", encoding="utf-8") as file:
    file.write(cleaned_text)

print("Resume processed successfully")