from anthropic import Anthropic
import os
import json

class ResumeFormatter:
    """
    A class to optimally format a resume using Claude 3.5 based on detailed candidate history
    and a specific job description.
    """
    def __init__(self):
        self.load_contents()
        self.client = Anthropic()

    @staticmethod
    def open_txt( path: str) -> str:
        with open(path, 'r') as f:
            return f.read()

    def load_contents(self):
        """
        Loads text contents from experience directory
        :return:
        """
        self.aboutme = self.open_txt('experience/aboutme.txt')
        edufiles = os.listdir('experience/education')
        jobfiles = os.listdir('experience/work')

        for file in edufiles:
            #load education descriptions into list of descriptions
            #self.education = [list of strings detailing degrees]

        for file in jobfiles:
            #load job descriptions into a list of descriptions
            #self.work_experience = [list of

    def call_api(self, prompts: list) -> dict:
        """
        Method to
        :param prompts: list of prompts
        :return:
        """
        pass

    def generate_prompts(self, job_description: str) -> list:
        """
        Method to generate text prompts to the API based on a job description
        :return:
        """
        pass

    def format_resume(self, job_description: str) -> dict:
        """
        Run function
        :param job_description:
        :return:
        """
        prompts = self.generate_prompts(job_description)
        formatted_resume = self.call_api(prompts)
        return formatted_resume


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