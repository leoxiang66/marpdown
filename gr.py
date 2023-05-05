from marpdown import *
from marpdown.utils import list_to_html_ul
from marpdown import utils


implications = [
    'The choice of training data has a significant impact on the performance of the models in practice',
    'Traditional transformers like T5 may have better performance on short-input data than efficient transformers',
    'LLMs like T5 and LongT5 are capable of generating answers that may not have a close token-level match with the gold answers but still convey similar semantics'
    
]

observation_list = ["For both T5 and LongT5 models, the highest Rouge Score and BERTScores are achieved when trained on the <b>User atterance dataset with human in the loop</b>.",'For 512 tokens when trained on the same dataset, the T5 models <b>consistently outperform</b> the LongT5 models', 'LongT5 has better performance on <b>long input data</b>', 'For all configurations,  BERTScores are <b>substantially higher</b> than the Rouge Score scores']

observation1 = f'''
## Observations 

{list_to_html_ul(observation_list[:1])}

'''

observation2 = f'''
## Observations 

{list_to_html_ul(observation_list[:2])}

'''


observation3 = f'''
## Observations 

{list_to_html_ul(observation_list[:3])}

'''

observation4 = f'''
## Observations 

{list_to_html_ul(observation_list[:4])}

'''

table2 = '''

<table style="width: 150%; text-align: center; table-layout: fixed;">
<caption style="caption-side: top; text-align: center; font-weight: bold;">BERTScore results</caption>
  <colgroup>
    <col style="width: 33.33%;">
    <col style="width: 16.67%;">
    <col style="width: 16.67%;">
    <col style="width: 33.33%;">
  </colgroup>
  <tr>
    <th rowspan="2" style="text-align: left;"></th>
    <th colspan="2">Token = 512</th>
    <th>Token = 5120</th>
  </tr>
  <tr>
    <th>T5</th>
    <th>LongT5</th>
    <th>LongT5</th>
  </tr>
  <tr>
    <td style="text-align: left;">FAQ</td>
    <td>0.879</td>
    <td>0.798</td>
    <td>0.838</td>
  </tr>
  <tr>
    <td style="text-align: left;">User atterance dataset</td>
    <td>0.883</td>
    <td>0.827</td>
    <td>0.849</td>
  </tr>
  <tr>
    <td style="text-align: left;">User atterance dataset with HIL</td>
    <td><b>0.913</b></td>
    <td>0.859</td>
    <td><b>0.906</b></td>
  </tr>
</table>


'''

table1 = '''

<table style="width: 150%; text-align: center; table-layout: fixed;">
<caption style="caption-side: top; text-align: center; font-weight: bold;">Rouge Score results</caption>
  <colgroup>
    <col style="width: 33.33%;">
    <col style="width: 16.67%;">
    <col style="width: 16.67%;">
    <col style="width: 33.33%;">
  </colgroup>
  <tr>
    <th rowspan="2" style="text-align: left;"></th>
    <th colspan="2">Token = 512</th>
    <th>Token = 5120</th>
  </tr>
  <tr>
    <th>T5</th>
    <th>LongT5</th>
    <th>LongT5</th>
  </tr>
  <tr>
    <td style="text-align: left;">FAQ</td>
    <td>0.568</td>
    <td>0.331</td>
    <td>0.410</td>
  </tr>
  <tr>
    <td style="text-align: left;">User atterance dataset</td>
    <td>0.581</td>
    <td>0.409</td>
    <td>0.432</td>
  </tr>
  <tr>
    <td style="text-align: left;">User atterance dataset with HIL</td>
    <td><b>0.677</b></td>
    <td>0.506</td>
    <td><b>0.601</b></td>
  </tr>
</table>






'''

# '''



# | **ID** | **Model** | **Training Dataset**                                   | **Max Tokens** | **Rouge Score** | **BERTScore**  |
# |-------|-----------|--------------------------------------------------------|----------------|----------|-------|
# | 1     | T5        | FAQ                              | 512            | 0.568     | 0.879  |
# | 2     | T5        | User atterance dataset            | 512            | 0.581     | 0.883  |
# | 3     | T5        | User atterance dataset with human in the loop     | 512            | **0.677** | **0.913**|
# | 4     | LongT5    | FAQ                              | 512            | 0.331     | 0.798  |
# | 5     | LongT5    | User atterance dataset            | 512            | 0.609     | 0.827  |
# | 6     | LongT5    | User atterance dataset with human in the loop     | 512            | 0.506     | 0.859  |

# '''

# table2 = '''


# | **ID** | **Model** | **Training Dataset**                                   | **Max Tokens** | **Rouge Score** | **BERTScore**  |
# |-------|-----------|--------------------------------------------------------|----------------|----------|-------|
# | 7     | LongT5    | FAQ                              | 5120           | 0.610     | 0.838  |
# | 8     | LongT5    | User atterance dataset            | 5120           | 0.632     | 0.849  |
# | 9     | LongT5    | User atterance dataset with human in the loop     | 5120           | **0.601** | **0.906**|
# '''

gr_final = PPT(
    footer="230508 Tao Xiang Guided Research Final Presentation",
    paginate=True,
    backgroundImage='''./content.png'''
)

TOC = ['Motivation', "Introduction", "Methodology", "Evaluation & Results", "Conclusion & Future Work"]


gr_final.addSlides(BaseSlide(backgroundImage='''./cover.png'''))

# Motivation
motivations = [
    ("Large Volume of HR Inquiries", list_to_html_ul([
        "Human Resource departments handle numerous tasks and queries from employees on a daily basis",
        "More than 330.000 HR tickets per year in SAP SE"
        ]),
     ),
    ("Labor Reduction and Efficiency", list_to_html_ul(["Effective QA system can substantially alleviate the workload of HR staff by handling a higher volume of employee inquiries.","Employees can receive instant responses without waiting."])),
    
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
<img src = "./gqa.png" width = 65%>
</center>


'''))

gr_final.addSlides(BoxlineSlide(title='''Research Questions''',
                    boxlines=[
                        "How to effectively address the issue of lengthy input (context) in generative QA systems?",
                        "Which analytical scores would be ideal to evaluate the performance of the models?",
                        "How to accurately assess the performance of generative QA models in real-world scenarios?"
                        
                        ]),
                   
                   )

# Methodlogy
gr_final.addSlides(TOCSlide(title="Outline",toc=TOC,focus=2))
gr_final.addSlides(BaseSlide(content=f'''
# Methodology - Datasets


**Domain experts internally prepared two datasets:**

## Dataset 1

![](https://i.imgur.com/EkRnz3l.png)

- Contains (question, context, answer) tuples
- The questions are very standardized and highly structured

---

# Methodology - Datasets

## Dataset 1 Example

<table>
  <tr>
    <th>Question</th>
    <th>Context</th>
    <th>Answer</th>
  </tr>
  <tr>
    <td>What local benefits can I claim during Long-Term Leave?</td>
    <td>Q: How can I request Unpaid Leave?/ How can I apply for Unpaid Leave?/I would like to understand the application process for Unpaid Leave.&lt;/strong&gt;&lt;/p&gt;&lt;p&gt;A:&nbsp; To apply for Unpaid Leave, please ...</td>
    <td>You are only eligible for Flexible Benefits in Success Map.</td>
  </tr>
</table>





---

# Methodology - Datasets

**Domain experts internally prepared two datasets:**

## Dataset 2

![](https://i.imgur.com/QeCKt6O.png)

- Contains (question, context, answer) tuples
- The questions are from real users (improved randomness)
- A question matching model is applied to retrieve the most similar question in Dataset 1
    - 60% accuracy
- For wrong retrievals: domain experts annotate correct questions

---
# Methodology - Datasets

## Dataset 2 Example

<table>
  <tr>
    <th>User Question</th>
    <th>Matched Question</th>
    <th>Context</th>
    <th>Answer</th>
  </tr>
  <tr>
    <td>insurance id card</td>
    <td>Where can I get my Aetna ID card</td>
    <td>The Aetna Medical Plan name is Aetna Choice POS II and the Group Number is 12345 (includes Fieldglass EEs) followed by your company code...</td>
    <td>You will receive an Aetna ID card for yourself, which may list up to three dependents. If you have more than three dependents, you will receive an additional card showing those dependents (note that dependents info should be complete in their BenefitFocus profile for either SSN/DOB for Aetna to recognize the dependent and be included)...</td>
  </tr>
</table>


---

# Methodology - Datasets

### Token count distributions of Dataset 1 & 2

<div style="display: flex; justify-content: space-between;">
  <img src="nt1.png" style="width: 45%;">
  <img src="nt2.png" style="width: 45%;">
</div>







---

# Methodology - Data Preprocessing

After several preprocessing steps:
- remove invalid samples (NaN, numeric)
- discard irrelevant metadata


'''))
                   
gr_final.addSlides(CardSlide(title="Methodology - Data Preprocessing",text='''After several preprocessing steps:
- remove invalid samples (NaN, numeric)
- discard irrelevant metadata

**We create 3 datasets to simulate different data environments:**

''', cards=[
    ("FAQ (N≈48k)",['derived from Dataset 1', "standard questions", 'represents a controlled enviroment for model training']),
    ("User atterance dataset  (N≈89k)",['combining Dataset 1 and 2','<b>excluding</b> the manual corrections made by do-main experts','represents a more realistic environment with inaccuracies']),
    ("User atterance dataset with human in the loop (N≈89k)",['combining Dataset 1 and 2','<b>Manual annotated contexts and answers</b> are used for wrong samples','represents a more realistic environment enhanced by domain experts']),
    
    
],card_width=270))

# **We simulate 3 data environments:**

# 1. FAQ (N≈48k)
#     - derived from Dataset 1
#     - contains only **standardized** and **highly structured** (question, context, answer) tuples
#     - represents a controlled enviroment for model training
    
# ---

# # Methodology - Data Preprocessing

# After several preprocessing steps:
# - remove invalid samples (NaN, numeric)
# - discard irrelevant metadata

# **We simulate 3 data environments:**

# 1. FAQ (N≈48k)
#     - derived from Dataset 1
#     - contains only **standardized** and **highly structured** (question, context, answer) tuples
#     - represents a controlled enviroment for model training
# 2. User atterance dataset  (N≈89k)
#     - combining Dataset 1 and 2
#     - **excluding** the manual corrections made by do-main experts
#         - some samples have mismatched contexts and answers
#     - represents a more realistic environment with inaccuracies

# ---

# # Methodology - Data Preprocessing

# After several preprocessing steps:
# - remove invalid samples (NaN, numeric)
# - discard irrelevant metadata

# **We simulate 3 data environments:**

# 1. FAQ (N≈48k)
#     - derived from Dataset 1
#     - contains only **standardized** and **highly structured** (question, context, answer) tuples
#     - represents a controlled enviroment for model training
# 2. User atterance dataset  (N≈89k)
#     - combining Dataset 1 and 2
#     - **excluding** the manual corrections made by do-main experts
#         - some samples have mismatched contexts and answers
#     - represents a more realistic environment with inaccuracies
# 3. User atterance dataset with human in the loop (N≈89k)
#     - combining Dataset 1 and 2
#     - **Manual annotated contexts and answers** are used for wrong samples
#     - represents a more realistic environment enhanced by domain experts
    
# ---

# # Methodology - Data Preprocessing

# After several preprocessing steps:
# - remove invalid samples (NaN, numeric)
# - discard irrelevant metadata

# **We simulate 3 data environments:**

# 1. FAQ (N≈48k)
#     - derived from Dataset 1
#     - contains only **standardized** and **highly structured** (question, context, answer) tuples
#     - represents a controlled enviroment for model training
# 2. User atterance dataset  (N≈89k)
#     - combining Dataset 1 and 2
#     - **excluding** the manual corrections made by do-main experts
#         - some samples have mismatched contexts and answers
#     - represents a more realistic environment with inaccuracies
# 3. User atterance dataset with human in the loop (N≈89k)
#     - combining Dataset 1 and 2
#     - **Manual annotated contexts and answers** are used for wrong samples
#     - represents a more realistic environment enhanced by domain experts
    



# {utils.red_text("We aim to explore the impact of different training data environments on the models' performance")}

# '''
# ))


gr_final.addSlides(BaseSlide(content='''
                             
# Methodology - RQ1

### How to effectively address the issue of lengthy input (context) in generative QA systems?


---

# Methodology - RQ1

### How to effectively address the issue of lengthy input (context) in generative QA systems?

#### We investigate the use of <font color = "red">efficient Transformers</font>

                             '''))


gr_final.addSlides(CardSlide(title= '''Methodology - RQ1''',text='''

### How to effectively address the issue of lengthy input (context) in generative QA systems?
           

#### We investigate the use of <font color = "red">efficient Transformers</font>



''', cards=[('Efficient Transformers',[
    'variant of Transformer models that aim to improve limitations of traditional Transformer models',
    'Enhanced computational and memory efficiency for handling lengthy inputs',
    'Examples: LongT5'
    ])]))


gr_final.addSlides(CardSlide(title='''Methodology - RQ1''',text='''
                   


#### Due to limited training resources, in this project we choose **LongT5** model and **T5** model for experiments.

                   ''',cards=[
                       ('''LongT5''', [utils.code('google/long-t5-local-base'),'''

$O(l)$
''','Up to 16,384 tokens',"296M trainable parameter"]),
                       
                       ("T5",[
                           utils.code("t5-base"),
                        utils.inline_math("O(l^2)") ,
                        'Up to 512 tokens',
                        '220M trainable parameters'
                           
                       ])
                       
                       
                   ]))


gr_final.addSlides(BaseSlide(content='''

# Methodology - RQ2



### Which analytical scores would be ideal to evaluate the performance of the models?



'''))

gr_final.addSlides(CardSlide(title='Methodology - RQ2',text='''
                             






### Which analytical scores would be ideal to evaluate the performance of the models?
                             ''',cards=[
                                 
                                 ('Rouge Score',['comparing the overlap of n-grams', 'lexical similarity']),
                                 ('BERTScore',['cosine similarities between the contextual embeddings', 'semantic similarity'])
                                 
                                 
                             ]))

gr_final.addSlides(BaseSlide(content='''
                             
# Methodology - RQ3

### How to accurately assess the performance of generative QA models in real-world scenarios?

---

# Methodology - RQ3

### How to accurately assess the performance of generative QA models in real-world scenarios?


<br>
<br>

**We build a “Real User Question Only” dataset (N≈4k) for evaluation**
- This dataset comprises only real user questions with correct context and answer pairs.
- It was constructed by filtering the test set of the “User atterance dataset with human in the loop” dataset to include only the real user question

                             '''))



# Evaluation & Results
gr_final.addSlides(TOCSlide(title='Outline', toc=TOC, focus=3))

gr_final.addSlides(BaseSlide(content=f'''
                   
# Evaluation & Results          

**We have a total of 9 configurations in our experiments:**


| **ID** | **Model**  | **Training Dataset**                                  | **Max Tokens** |
|-------|--------|---------------------------------------------------|-----------------|
| 1     | T5     | FAQ                  | 512             |
| 2     | T5     | User atterance dataset  | 512             |
| 3     | T5     | User atterance dataset with human in the loop | 512       |
| 4     | LongT5 | FAQ                  | 512             |
| 5     | LongT5 | User atterance dataset  | 512             |
| 6     | LongT5 | User atterance dataset with human in the loop | 512       |
| 7     | LongT5 | FAQ                 | 5120            |
| 8     | LongT5 | User atterance dataset  | 5120            |
| 9     | LongT5 | User atterance dataset with human in the loop | 5120      |



---

# Evaluation & Results          

**We have a total of 9 configurations in our experiments:**

| **ID** | **Model**  | **Training Dataset**                                  | **Max Tokens** |
|-------|--------|---------------------------------------------------|-----------------|
| 1     | T5     | FAQ                  | 512             |
| 2     | T5     | User atterance dataset  | 512             |
| 3     | T5     | User atterance dataset with human in the loop | 512       |
| 4     | LongT5 | FAQ                  | 512             |
| 5     | LongT5 | User atterance dataset  | 512             |
| 6     | LongT5 | User atterance dataset with human in the loop | 512       |
| 7     | LongT5 | FAQ                 | 5120            |
| 8     | LongT5 | User atterance dataset  | 5120            |
| 9     | LongT5 | User atterance dataset with human in the loop | 5120      |

- Comparing the performance of T5 and LongT5 models trained on the three different datasets
- Assessing the influence of varying input lengths on the quality of the generated answers

---

# Evaluation & Results       

**We have a total of 9 configurations in our experiments:**   

| **ID** | **Model**  | **Training Dataset**                                  | **Max Tokens** |
|-------|--------|---------------------------------------------------|-----------------|
| 1     | T5     | FAQ                  | 512             |
| 2     | T5     | User atterance dataset  | 512             |
| 3     | T5     | User atterance dataset with human in the loop | 512       |
| 4     | LongT5 | FAQ                  | 512             |
| 5     | LongT5 | User atterance dataset  | 512             |
| 6     | LongT5 | User atterance dataset with human in the loop | 512       |
| 7     | LongT5 | FAQ                 | 5120            |
| 8     | LongT5 | User atterance dataset  | 5120            |
| 9     | LongT5 | User atterance dataset with human in the loop | 5120      |

- Comparing the performance of T5 and LongT5 models trained on the three different datasets
- Assessing the influence of varying input lengths on the quality of the generated answers

{utils.red_text("For each configuration, we choose the model checkpoint with the highest BERTScore score on the validation set, obtained at a specific training epoch")}
{utils.red_text("Then evaluate them on the Real User Question Only dataset.")}
                             
---                             
                             
# Evaluation & Results


{utils.two_columns(width1=0.48,width2=0.48,column1=table1,column2=table2)}


---

# Evaluation & Results

{utils.two_columns(width1=0.48,width2=0.48,column1=table1,column2=table2)}

<br>

{observation1}



---

# Evaluation & Results

{utils.two_columns(width1=0.48,width2=0.48,column1=table1,column2=table2)}

<br>

{observation2}

---

# Evaluation & Results
{utils.two_columns(width1=0.48,width2=0.48,column1=table1,column2=table2)}

<br>

{observation3}   

---

# Evaluation & Results

{utils.two_columns(width1=0.48,width2=0.48,column1=table1,column2=table2)}
<br>

{observation4}                         
                             '''))

for i in range(len(implications)):
    gr_final.addSlides(BoxlineSlide(title='Implications', boxlines=implications[:i+1]))


# conclusion
gr_final.addSlides(TOCSlide(title='Outline',toc=TOC,focus=4))
gr_final.addSlides(BaseSlide(content='''
                             

# Conclusion & Future Work

### Conclusion

- Developed a generative QA chatbot tailored for HR domain
- Investigated T5 and LongT5 language models
- Impact of different training data distributions and input lengths
- Best performance: Real user questions with human intervention
- T5: Better for short inputs, LongT5: Promising for longer inputs

### Future Work

- Employ more models for comparison
- Collect more realistic datasets for training and evaluation
- Use a broader range of evaluation metrics
- Model selection based on input length (T5 for short inputs, LongT5 for longer inputs)                             
                             '''))



gr_final.addSlides(BaseSlide(content='''
                             
# Acknowledgement

We would like to express our sincere gratitude to SAP SE for their invaluable assistance and support throughout this project. Their generous provision of resources, including computational resources and datasets, has been instrumental in the successful completion of our work.

                             '''))

gr_final.addSlides(ThanksSlide())

gr_final.store('tmp.md')