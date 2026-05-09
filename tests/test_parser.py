from parsers.resume_parser import parse_resume

def test_resume_parser():

    result = parse_resume("tests/sample_resume.pdf")

    assert len(result) > 0