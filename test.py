if __name__ == '__main__':
    from marpdown import PPT, BaseSlide,TOCSlide,TimelineSlide

    bgimage = 'https://img.kaiheila.cn/assets/2022-01/HgiRGpe3aR2zk1fs.jpeg'
    timelines = [
        ("tl1",'desc1'),
        ("tl2", 'desc1'),
        ("tl3", 'desc1'),
        ("tl4", 'desc1'),
    ]
    ppt = PPT(footer='123', paginate=True)
    ppt.addSlides([
        BaseSlide(backgroundImage=bgimage, content="# Hello World"),
        BaseSlide(backgroundImage=bgimage, content="# Hello World\n\n- fuck you\n- hello?"),
        TOCSlide(title='TOC', toc=['Motivation', "Introduction", "Methods"]),
        TOCSlide(title='TOC', toc=['Motivation', "Introduction", "Methods"],focus=0),
        TimelineSlide(title='ts1',timelines= timelines[0:1]),
        TimelineSlide(title='ts1', timelines=timelines[0:2]),
        TimelineSlide(title='ts1', timelines=timelines[0:3]),
        TimelineSlide(title='ts1', timelines=timelines[0:4])])

    ppt.store('tmp.md')
