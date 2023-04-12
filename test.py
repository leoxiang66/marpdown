if __name__ == '__main__':
    from marpdown import PPT, BaseSlide,TOCSlide,TimelineSlide

    bgimage = './images/content.png'
    motivations = [
        ("Research trends are important",'By researching trends, we can stay ahead of the curve and ensure that our work is always <b>cutting-edge</b>.'),
        ("Challenges in identifying research trends", '''<ul>
  <li><b>Lack of standardization</b>: Research data is often presented in different formats and with different terminologies, making it difficult to compare and analyze.</li>
  <li><b>Information overload</b>: With the sheer volume of research being produced every day, it can be difficult to know where to start looking for trends.</li>
  <li><b>Noise in the data</b>: Not all research is equally important or reliable, and it can be difficult to filter out the irrelevant or low-quality studies.</li>
  <li><b>Changing landscape</b>: Research trends can shift rapidly in response to new discoveries and technologies, making it difficult to keep up with the latest developments.</li>
</ul>'''),
        ("The need for an automated framework", 'Automated literature search and analysis based on <b>machine learning</b> can save time and resources while ensuring accuracy.'),
        ("tl4", 'desc1'),
    ]
    ppt = PPT(footer='**fml** - Lehrstuhl für Fördertechnik Materialfluss Logistik | TUM School of Engineering and Design | Technische Universität München', paginate=True, backgroundImage=bgimage)
    toc_ = ['Motivation', "Introduction", "Framework Design", "Evaluation & Results", "Limitations & Future Work"]
    ppt.addSlides([
        BaseSlide(backgroundImage='images/cover.png', content=""),
        TOCSlide(title='Table of Contents', toc=toc_),
        TOCSlide(title='Table of Contents', toc=toc_,focus=0),
        TimelineSlide(title='Motivation', timelines=motivations[0:1]),
        TimelineSlide(title='Motivation', timelines=motivations[0:2]),
        TimelineSlide(title='Motivation', timelines=motivations[0:3]),
        TOCSlide(title='Table of Contents', toc=toc_, focus=1),
        TOCSlide(title='Table of Contents', toc=toc_, focus=2),
        TOCSlide(title='Table of Contents', toc=toc_, focus=3),
        TOCSlide(title='Table of Contents', toc=toc_, focus=4),
    ])

    ppt.store('tmp.md')
