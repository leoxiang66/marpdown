from marpdown import *
from marpdown.utils import list_to_html_ul

gr_final = PPT(
    footer="230508 Tao Xiang Guided Research Final Presentation",
    paginate=True,
    backgroundImage='''./content.png'''
)

TOC = ['Motivation', "Introduction", "Methodology", "Evaluation & Results", "Limitation & Future Work"]


gr_final.addSlides(BaseSlide(backgroundImage='''./cover.png'''))

# Motivation
motivations = [
    ("Large Volume of HR Inquiries", list_to_html_ul([
        "Human Resource departments handle numerous tasks and queries from employees on a daily basis",
        "More than 330.000 HR tickets per year in SAP SE"
        ]),
     ),
    ("Labor Reduction and Efficiency", "Effective QA system can substantially alleviate the workload of HR staff by handling a higher volume of employee inquiries."),
    
    ("Advancements in NLP",list_to_html_ul([
        "The rapid progress in natural language processing (NLP) technologies offers opportunities to develop more sophisticated and accurate HR chatbots",'Leveraging state-of-the-art NLP techniques allows for better understanding of user intents and improved response generation, resulting in a more seamless and effective user experience'
    ]))
    
]

gr_final.addSlides(TOCSlide("Outline", toc=TOC))           
gr_final.addSlides(TOCSlide("Outline", toc=TOC, focus=0))
for i in range(len(motivations)):
    gr_final.addSlides(TimelineSlide("Motivation",timelines=motivations[:i+1]))

# Introduction
gr_final.addSlides(TOCSlide("Outline",toc=TOC,focus=1))
gr_final.addSlides(BaseSlide(content='''

# Introduction

## QA Chatbots in HR Domain

In the HR domain, QA chatbots are designed to assist employees by answering their questions and providing support on various topics, such as benefits, policies, and onboarding. 
   

'''))

gr_final.addSlides(CardSlide(title="Introduction",text='''
## QA Chatbots in HR Domain

In the HR domain, QA chatbots are designed to assist employees by answering their questions and providing support on various topics, such as benefits, policies, and onboarding. ''' ,cards=[('Traditional QA',['manually designed intents and predefined responses','Handle commonly asked questions effectively', 'Limited in understanding complex or ambiguous queries', 'Not easily scalable due to manual effort required']),
              ('Generative QA', [
                  'Leverage advancements in NLP for improved accuracy and user experience',
                  'Automatically understand user intents and find answers in context','Can handle a wider range of questions, including complex and ambiguous queries','More scalable and cost-effective solution for handling high volume of HR inquiries'])                                                                                                                                                                               ]))

gr_final.addSlides(BaseSlide(content='''
# Introduction

## Generative QA: An example


<center>
<img src = "./gqa.png" width = 80%>
</center>


'''))

gr_final.store('tmp.md')