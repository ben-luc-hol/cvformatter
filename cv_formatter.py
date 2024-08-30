from anthropic import Anthropic
import os
import json

class ResumeFormatter:
    def __init__(self):
        self.import_contents()

    def import_contents(self):
        edufiles = os.listdir('experience/education')
        jobfiles = os.listdir('experience/work')

        for file in edufiles:
          #load education descriptions into list of descriptions
         #self.education

        for file in jobfiles:
        #load job descriptions into a list of descriptions
        #self.work_experience

    def


