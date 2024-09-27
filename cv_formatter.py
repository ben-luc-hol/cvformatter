from anthropic import Anthropic
import os

class ResumeFormatter:
    """
    A class to optimally format a resume using Claude 3.5 based on detailed candidate history, experience, and qualifications.
    """
    def __init__(self):
        self.degrees = None
        self.aboutme = None
        self.jobs = None
        self.load_contents()
        self.client = Anthropic()

    @staticmethod
    def read_txt( path: str) -> str:
        with open(path, 'r') as f:
            return f.read()

    def load_contents(self):
        """
        Loads text contents from experience directory
        :return:
        """
        self.aboutme = self.read_txt('experience/aboutme.txt')
        self.degrees = [self.read_txt(f"experience/education/{degree}") for degree in os.listdir('experience/education')]
        self.jobs = [self.read_txt(f"experience/work/{job}") for job in os.listdir('experience/work')]

    def generate_prompts(self, job_description: str, additional_information=None) -> tuple[str, str]:
        """
        Generate system and user prompts for resume tailoring based on a job description.

        :param job_description: The job description to tailor the resume for
        :return: A tuple containing the system prompt and user prompt
        """
        system_prompt = (
            f"""You are an expert career advisor and resume writer. Your task is to create a tailored, ATS-friendly resume that maximizes the candidate's chances of securing an interview for the given job description.

            Key objectives:
            1. Highlight relevant skills and experiences that match the job requirements.
            2. Use industry-specific keywords from the job description naturally throughout the resume.
            3. Quantify achievements and impact where possible.
            4. Ensure the resume is concise, professional, and easy to scan.
        
            Resume format:
        
            <RESUME>
            [Full Name]
            [Email] | [Phone] | [Location (City, State)]
            [Optional: LinkedIn profile or personal website]
        
            PROFESSIONAL SUMMARY
            A brief, impactful 2-3 sentence summary highlighting key qualifications and career trajectory.
        
            WORK EXPERIENCE
            [Job Title] | [Company Name] | [Employment Period (MM/YYYY - MM/YYYY or Present)]
            • Achievement-oriented bullet point
            • Achievement-oriented bullet point
            • Achievement-oriented bullet point
        
            [Repeat for each relevant position, with more recent and relevant roles having more detail]
        
            EDUCATION
            [Degree] in [Field of Study] | [University Name] | [Graduation Year]
            • Relevant coursework, honors, or projects (if applicable and recent)
        
            SKILLS
            [List of relevant technical and soft skills, prioritizing those mentioned in the job description]
        
            [Optional sections if relevant: Projects, Certifications, Publications, Awards]
            </RESUME>
        
            Candidate information:
        
            <PERSONAL DETAILS>
            {self.aboutme}
            </PERSONAL DETAILS>
        
            <WORK EXPERIENCE>
            {chr(10).join(self.jobs)}
            </WORK EXPERIENCE>
        
            <EDUCATION>
            {chr(10).join(self.degrees)}
            </EDUCATION>
            """
        )


        user_prompt = (
            f"""Create a tailored resume for the following job description:

            <JOB DESCRIPTION>
            {job_description}
            </JOB DESCRIPTION>
        
            Instructions:
            1. Analyze the job description carefully, identifying key requirements, skills, and preferences.
            2. Create a resume that best positions the candidate for this specific role, emphasizing relevant experiences and skills.
            3. Use language and keywords from the job description naturally throughout the resume.
            4. Prioritize recent and relevant experiences, allocating more detail to these.
            5. Quantify achievements where possible (e.g., percentages, dollar amounts, team sizes).
            6. Ensure the resume fits within a standard 1-2 page format when reasonably formatted.
            7. If the candidate lacks direct experience in some areas, highlight transferable skills or adjacent experiences.
        
            Please provide the resume in the format specified in the system prompt, focusing on creating a compelling and tailored document that will maximize the candidate's chances of securing an interview.
            
            {
            [f"Additional Info:"
             f"{additional_information}" if additional_information else ""]
            }
            
            """)

        return system_prompt, user_prompt

    def call_api(self, system_prompt, user_prompt) -> str:
        """
        Method to
        :param prompts: list of prompts
        :return:
        """
        r = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=4000,
                temperature=0.38,
                system=system_prompt,
                messages=[
                    {"role": "user", "content": [
                        {"type": "text",
                         "text": user_prompt}
                        ]
                     }
                ]
            )
        output = r.content[0].text
        return output

    def generate_resume(self, job_description: str, additional_information=None) -> str:
        """
        Run function
        :param job_description:
        :return:
        """
        system_prompt, user_prompt = self.generate_prompts(job_description, additional_information)
        formatted_resume = self.call_api(system_prompt, user_prompt)
        return formatted_resume

    def generate_bio(self, purpose):
        system_prompt = (f"""
        <PERSONAL DETAILS>
            {self.aboutme}
            </PERSONAL DETAILS>
        
            <WORK EXPERIENCE>
            {chr(10).join(self.jobs)}
            </WORK EXPERIENCE>
        
            <EDUCATION>
            {chr(10).join(self.degrees)}
            </EDUCATION>
            """)
        user_prompt = f"Please generate a bio to use for {purpose}."

        bio = self.call_api(system_prompt, user_prompt)

        return bio

    # def scrape_linkedin_job_posting(self, url):
    #     """
    #     Method to fetch description from linkedin posting
    #     :param url:
    #     :return:
    #     """
    #
    # def scrape_ziprecruiter_job_posting(self, url):
    #     """
    #     Method to fetch description from linkedin posting
    #     :param url:
    #     :return:
    #     """
    #
    # def init_google_oauth(self):
    #     pass
    #
    # def format_pdf(self, json_resume):
    #     """
    #     Formats pdf file
    #     :param json_resume:
    #     :return:
    #     """